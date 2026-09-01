---
type: report
status: active
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/report
---

# Transplant Prognosis Model Notes

작성일: 2026-05-26

이 문서는 장기 이식 예후 예측 모델을 만들 때, scGPT 기반 encoder를 어떻게 다루고 어떤 입력 전처리와 prediction head를 비교할지 정리한 설계 메모이다. 현재 맥락은 신장 이식 거부반응 및 graft outcome risk score 예측이다.

## 한 줄 결론

Training data와 test data 사이에 비대칭 domain shift가 있을 때는, training data가 scGPT pretraining domain인 single-cell에 가까운지 여부가 encoder fine-tuning 전략을 좌우한다.

- Training data가 single-cell이면 encoder weight를 task에 맞게 일부 또는 전체 fine-tuning하는 방향도 실험할 가치가 있다.
- Training data가 bulk, microarray, pseudobulk, clinical table처럼 single-cell이 아니면 scGPT encoder weight는 가급적 보존하고, adapter와 prediction head 중심으로 학습하는 편이 안정적일 수 있다.
- 이유는 scGPT가 single-cell data로 pretrain되었기 때문에, non-single-cell training signal로 encoder 전체를 업데이트하면 test single-cell representation이 pretrained manifold에서 벗어날 위험이 있기 때문이다.

## 2026-06-01 최종 구현

설계 메모의 권장 방향은 `prognosis_microarray_adapter.py`에서 frozen scGPT encoder + residual Microarray-to-SC adapter + prognosis head 구조로 구체화했다. 자세한 구현과 결과는 [Microarray-to-scRNA Prognosis Adapter](microarray-to-scrna-prognosis-adapter.md)에 정리했다.

최종 기본 구조:

```text
bulk microarray RMA/log2 sample
  -> nonzero gene tokenization
  -> quantile-binned expression values
  -> frozen scGPT kidney encoder
  -> CLS embedding
  -> residual adapter
  -> L2 normalization
  -> prognosis head
  -> rejection probability / patient risk score
```

핵심 결정:

- Encoder는 freeze하고 adapter/head만 학습한다.
- Adapter는 `LayerNorm -> 512 to 256 -> GELU -> Dropout -> 256 to 512 -> residual add` 구조다.
- Single-cell 적용 시 cell-level probability를 계산한 뒤 patient-level p60 score로 집계한다.
- 현재 구현은 BCE 기반 NR vs Rejection objective가 중심이며, Cox branch는 아직 survival loss로 활성화하지 않았다.
- 비교 결과 기준 Zeroed RMA + L2 normalization 설정이 OOF AUROC 0.762로 가장 좋았다.

## Domain 비대칭과 encoder 전략

| Training data | Test data | 권장 전략 | 메모 |
| --- | --- | --- | --- |
| Single-cell | Single-cell | `last-n` 또는 full fine-tuning 후보 | 낮은 learning rate, early stopping, layer-wise freeze를 같이 둔다. |
| Single-cell | Bulk/pseudobulk | Encoder fine-tuning 가능하지만 calibration 필요 | Cell-level signal이 sample-level label로 어떻게 aggregate되는지 따로 검증한다. |
| Bulk/microarray | Single-cell | Frozen encoder + adapter/head 우선 | scGPT single-cell prior를 보존하고, domain 차이는 adapter가 흡수하게 한다. |
| Mixed domain | Mixed domain | Frozen baseline -> adapter -> last-n 순서 | encoder update는 마지막 ablation으로 둔다. |

실험 순서는 보수적으로 잡는다.

1. Frozen scGPT encoder + CLS head로 baseline을 만든다.
2. Adapter 또는 small MLP head만 학습한다.
3. Training data가 single-cell이면 마지막 N개 layer부터 풀어본다.
4. Full fine-tuning은 성능보다 domain overfit 여부를 먼저 확인한다.

## 1. Data preprocessing

scGPT는 expression value를 quantile binning해서 입력하므로 platform 간 절대 scale 차이는 어느 정도 흡수한다. 하지만 quantile binning은 각 샘플의 분포 모양 자체를 동일하게 만들지는 못한다. 따라서 binning 전에 sample-wise normalization을 넣으면 domain shift를 줄이는 데 도움이 될 수 있다.

기본 아이디어:

```text
sample expression vector
  -> sample-wise standardization
  -> optional clipping
  -> scGPT quantile binning
  -> gene tokens + binned values
```

권장 ablation:

| 전처리 | 목적 | 주의점 |
| --- | --- | --- |
| 기존 scGPT quantile binning만 사용 | 현재 baseline 유지 | 분포 모양 차이는 남을 수 있다. |
| Sample-wise z-score 후 binning | 샘플별 mean=0, std=1로 맞춘 뒤 binning | 위치/스케일 차이는 줄지만 완전한 정규분포 변환은 아니다. |
| Rank-based inverse normal transform 후 binning | 샘플별 분포 모양까지 정규분포에 가깝게 맞춤 | global expression magnitude가 예후 신호인 경우 일부 제거될 수 있다. |
| Z-score + clipping 후 binning | outlier가 bin boundary를 흔드는 효과 완화 | clipping range를 validation에서 고정해야 한다. |

실무적으로는 `sample-wise z-score -> clip(-5, 5) -> quantile binning`을 첫 후보로 두고, 분포 모양을 더 강하게 맞춰야 하면 rank-based inverse normal transform을 비교한다.

## 2. Prediction head - 어떤 token을 쓸지

`CLS`만 쓰는 것이 가장 단순한 baseline이다. 모든 gene token이 self-attention을 통해 `CLS` token에 모일 수 있으므로 충분히 강한 출발점이다. 다만 장기 이식 예후 예측처럼 marker gene과 pathway 해석이 중요한 문제에서는 여러 aggregation head를 비교할 가치가 있다.

| Head | 구조 | 기대 효과 | 주의점 |
| --- | --- | --- | --- |
| `CLS` | `CLS -> MLP -> logit` | 가장 단순하고 강한 baseline | gene-level 해석은 약하다. |
| `CLS + mean pool` | `concat(CLS, mean(gene tokens)) -> MLP` | task summary와 평균 발현 신호를 함께 사용 | dimension이 2배가 되므로 regularization 필요 |
| Attention pooling | learnable query가 모든 gene token에 attention | dimension 증가 없이 명시적 token aggregation | attention score 해석은 보조 지표로만 사용 |
| Marker gene pooling | 알려진 rejection marker token만 pool | 사전지식을 직접 주입 | marker gene dropout/missing 처리 필요 |
| Pathway-level aggregation | pathway별 gene token pool -> pathway vector attention | 해석 가능성과 구조화된 prior 증가 | gene set 정의와 overlap 관리 필요 |
| Multi-token ensemble head | CLS, mean, max, attention head logit 평균 | 작은 모델 ensemble 효과 | head 수가 늘어 overfit 관리 필요 |

### Marker gene 후보

초기 marker pooling 후보:

```text
IFNG, GZMB, GZMA, CXCL9, CXCL10, CXCL11,
HLA-DRA, HLA-DRB1, FOXP3
```

이 목록은 rejection 관련 cytotoxic T/NK, interferon-gamma response, chemokine, antigen presentation, regulatory T cell signal을 보기 위한 시작점이다. 이후 Banff molecular diagnostics 및 B-HOT gene panel을 참고해 확장한다.

Banff/B-HOT 기반으로 확장할 때 우선 볼 gene group:

- IFNG-inducible genes
- NK/cytotoxic cell genes
- Endothelial activation/injury genes
- Monocyte/macrophage genes
- B cell/plasma cell genes
- Complement genes
- Chemokine/cytokine genes
- Tubular injury 및 graft injury 관련 genes

## 3. Pathway-level aggregation

Pathway head는 gene token을 직접 전부 평균내는 대신, biological prior 단위로 먼저 묶는다.

```text
gene token outputs
  -> immune pathway별 token pool
  -> pathway vectors
  -> attention pooling over pathways
  -> prognosis logit or risk score
```

후보 gene set:

- HALLMARK interferon alpha/gamma response
- HALLMARK inflammatory response
- HALLMARK allograft rejection
- KEGG antigen processing and presentation
- KEGG T cell receptor signaling
- KEGG B cell receptor signaling
- KEGG complement and coagulation cascades
- Banff/B-HOT transplant rejection panel

장점은 patient-level prediction 이후에도 어떤 pathway vector가 risk score에 기여했는지 볼 수 있다는 점이다. 단점은 gene set overlap이 많으면 pathway score가 독립적이지 않을 수 있다는 점이다.

## 4. 추천 실험 순서

1. `Frozen encoder + CLS head`를 baseline으로 둔다.
2. Binning 전 `sample-wise z-score`와 `rank-based inverse normal transform`을 비교한다.
3. Head ablation을 `CLS -> CLS+mean -> attention pooling -> marker pooling -> pathway pooling` 순서로 진행한다.
4. Training data가 single-cell인 경우 `last-n layer fine-tuning`을 추가한다.
5. Training data가 non-single-cell인 경우 encoder는 freeze하고 `DomainAdapter` 또는 `LoRA/adapter` 계열만 학습한다.
6. 최종 모델은 `CLS`, `attention`, `marker/pathway` head의 logit ensemble을 검토한다.

## 5. 해석과 validation 포인트

- Encoder를 풀어서 성능이 좋아져도 test domain에서 embedding collapse나 calibration drift가 생기는지 확인한다.
- Marker gene pooling은 성능만이 아니라 marker missing rate와 cell type composition에 민감한지 확인한다.
- Pathway aggregation은 예후 점수의 생물학적 해석에는 좋지만, 작은 cohort에서는 gene set prior가 과하게 작동할 수 있다.
- Binning 전 sample-wise normalization은 domain shift 제거에는 좋지만, 전체 발현량이나 RNA content 자체가 outcome signal인 경우에는 신호를 제거할 수 있다.
- 예후 모델에서는 AUC뿐 아니라 calibration, risk group separation, longitudinal endpoint와의 association을 같이 본다.

## 관련 문서

- [scGPT](../bio-ai/scgpt.md)
- [Kidney Transplant Rejection Classification](kidney-transplant-rejection-classification-summary.md)
- [Microarray-to-scRNA Prognosis Adapter](microarray-to-scrna-prognosis-adapter.md)
- [scGPT Rejection End-to-End v1/v2](../code/logs/2026-05-22-scgpt-rejection-end2end-v1-v2.md)

## 참고 문헌

- [scGPT Nature Methods](https://www.nature.com/articles/s41592-024-02201-0)
- [Banff 2019 Meeting Report: Molecular diagnostics in solid organ transplantation - B-HOT gene panel](https://rcastoragev2.blob.core.windows.net/3f3b95a8b63cd0621e1b33c49119c199/PMC7496585.pdf)
- [In-silico performance, validation, and modeling of the Nanostring Banff Human Organ Transplant gene panel using archival data from human kidney transplants](https://link.springer.com/article/10.1186/s12920-021-00891-5)
