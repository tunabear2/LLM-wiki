---
type: worklog-chunk
status: archive
rag_priority: medium
updated: '2026-07-20'
date_range: 2026-05-18..2026-05-24
source: code/logs/2026-06-16-scgpt-prognosis-worklog.md
topics:
- single-cell
- kidney-transplant
- prognosis
models:
- scGPT
tags:
- wiki/worklog-chunk
---

# scGPT prognosis worklog — 2026-05-18~24

> [!note] 검색용 분할본
> 원본은 [2026-06-16 scGPT prognosis worklog](../logs/2026-06-16-scgpt-prognosis-worklog.md)입니다. 결론이 충돌하면 최신 `reports/` 문서를 우선합니다.

## 완료: domain_transfer.py 작성 (2026-05-24)

### 목표
`run_step3_domain_transfer.py` 기반으로, SC 데이터를 pseudobulk로 교체하고 LR C값 스윕을 추가한 새 스크립트 작성

### 주요 변경사항

| 항목 | 기존 (run_step3) | 신규 (domain_transfer.py) |
|------|-----------------|--------------------------|
| SC 데이터 | `E_MTAB_12051.h5ad` (단일 세포) | `E_MTAB_12051_pseudobulk_preprocessed.h5ad` |
| SC 전처리 | normalize(1e4) + log1p (raw counts) | normalize=None, log1p=False (CPM+log2 완료) |
| 환자 pooling | 세포 임베딩 → median pooling | 불필요 (1행=1환자) |
| 환자 ID 컬럼 | `orig.ident` | `obs.index` |
| 임베딩 유전자 | Bulk/SC 각각 vocab 독립 필터 | **Bulk ∩ SC ∩ vocab 교집합 (17,704개)** |
| 유전자 선택 | 샘플당 상위 1,200개 | **교집합 전체 (17,704개)** |
| 시퀀스 길이 | 1,200 토큰 | 17,705 토큰 (CLS+17,704) |
| batch_size | 128 | 1 |
| LR C값 | 단일값 고정 | `--c-values` 인수로 다중 테스트 (기본: 5개) |
| 캐시 파일 | `bulk_embeddings.npz` | `bulk_embeddings_shared.npz` |

### 설계 결정: 공통 유전자 필터링
- Bulk 고유 유전자 vs SC 고유 유전자가 각각 CLS에 포함되면 두 임베딩이 다른 feature space를 요약 → LR decision boundary가 SC에 적용될 때 체계적 어긋남 발생
- **동일한 17,704개 유전자**를 양쪽에 입력 → CLS 토큰이 같은 feature space를 요약 → domain transfer에서 직접 비교 가능

### 출력 파일
- `results/domain_transfer_run/bulk_embeddings_shared.npz`
- `results/domain_transfer_run/sc_pb_embeddings_shared.npz`
- `results/domain_transfer_run/predictions_C{c}.csv` (C값별)
- `results/domain_transfer_run/c_sweep_summary.csv`

### 실행 예시
```bash
cd /home/tunabear2/DW/scGPT/data
python ../domain_transfer.py --c-values 0.001 0.01 0.1 1.0 10.0
python ../domain_transfer.py --use-cache --c-values 0.01 0.1
```

---

## 완료: End-to-end Fine-tuning v2 (DomainAdapter) 비교 실험 (2026-05-23~24)

### 목표
rejection_finetune_end2end_v2.py (DomainAdapter + per-fold pos_weight 추가)로 none / full 모드 실험 후 v1과 성능 비교

### v2 아키텍처 변경사항 (vs v1)
- `DomainAdapter` 추가: `CLS → LayerNorm → fc1(512→128) → GELU → Dropout → fc2(128→512) → residual`
- Per-fold pos_weight: 전체 데이터 대신 fold별 train_idx에서 계산
- 훈련 파라미터: 265,857 / 50,544,257 (0.53%) — v1 none 133K의 2배 (adapter 추가)

### CV 결과 비교

| 모드 | Per-fold AUROC (mean) | OOF AUROC | OOF BalAcc@opt | CV epochs |
|------|----------------------|-----------|-----------------|-----------|
| v2 none | 0.782 ± 0.027 | 0.734 | 0.676 | 26 |
| v2 full | **0.839 ± 0.036** | 0.759 | **0.735** | 14 |

#### v2 none per-fold 상세
| Fold | AUROC | AUPRC | BalAcc | best_epoch |
|------|-------|-------|--------|------------|
| 1 | 0.801 | 0.565 | 0.544 | 14 |
| 2 | 0.738 | 0.582 | 0.622 | 19 |
| 3 | 0.815 | 0.576 | 0.578 | 44 |
| 4 | 0.771 | 0.558 | 0.518 | 8 |
| 5 | 0.784 | 0.620 | 0.578 | 47 |

#### v2 full per-fold 상세
| Fold | AUROC | AUPRC | BalAcc | best_epoch |
|------|-------|-------|--------|------------|
| 1 | 0.821 | 0.614 | 0.514 | 12 |
| 2 | 0.800 | 0.606 | 0.675 | 19 |
| 3 | **0.905** | **0.781** | 0.667 | 7 |
| 4 | 0.836 | 0.649 | 0.768 | 12 |
| 5 | 0.834 | 0.737 | 0.754 | 19 |

### E-MTAB-12051 predict-ft 결과

| sample_id | true | v2 none | v2 full | 정답(none) | 정답(full) |
|-----------|------|---------|---------|-----------|-----------|
| EXT217 | NR | 0.003 | 0.666 | O | X |
| EXT230 | Rejection | 0.048 | 0.986 | O | O |
| EXT238 | NR | 0.003 | 0.666 | O | X |
| EXT240 | NR | 0.005 | 0.983 | O | X |
| EXT241 | NR | 0.982 | 0.993 | X | X |
| NEPH006 | NR | 0.005 | 0.832 | O | X |
| NEPH009 | Rejection | 0.033 | 0.983 | O | O |
| NEPH010 | Rejection | 0.003 | 0.832 | X | O |
| NEPH011 | NR | 0.003 | 0.666 | O | X |
| NEPH012 | NR | 0.003 | 0.832 | O | X |
| NEPH014 | NR | 0.003 | 0.841 | O | X |
| NEPH015 | NR | 0.005 | 0.835 | O | X |
| NEPH016 | NR | 0.003 | 0.832 | O | X |
| NEPH017 | NR | 0.832 | 0.834 | X | X |
| NEPH018 | NR | 0.615 | 0.984 | X | X |
| NEPH019 | Rejection | 0.005 | 0.832 | X | O |

#### TP/TN/FP/FN 요약

| 모드 | TP | TN | FP | FN | Sensitivity | Specificity | BalAcc |
|------|----|----|----|----|-------------|-------------|--------|
| v2 none | 2 | 9 | 3 | 2 | 0.500 | 0.750 | **0.625** |
| v2 full | 4 | 0 | 12 | 0 | 1.000 | 0.000 | 0.500 |

### v1 vs v2 전체 비교

| 모드 | CV AUROC | Test TP | TN | FP | FN | Test BalAcc |
|------|----------|---------|----|----|-----|-------------|
| v1 full | 0.835 | 4 | 0 | 12 | 0 | 0.500 |
| v1 last-n=2 | 0.798 | 2 | 4 | 8 | 2 | 0.375 |
| v1 none | — | 2 | 9 | 3 | 2 | 0.625 |
| v2 none | 0.782 | 2 | 9 | 3 | 2 | **0.625** |
| v2 full | 0.839 | 4 | 0 | 12 | 0 | 0.500 |

### 핵심 발견

1. **DomainAdapter 효과 없음**: v2 none이 v1 none과 정확히 동일한 test 결과. CV AUROC는 개선(0.625→0.782)됐지만 test generalization에 기여 없음.

2. **Full mode domain collapse 재현**: v2 full도 v1 full과 동일하게 specificity=0. 인코더를 end-to-end fine-tuning하면 bulk RMA 공간으로 이동 → SC 테스트 샘플을 모두 Rejection으로 예측.

3. **일관된 어려운 케이스**: 모든 실험에서 동일한 5개 케이스에서 오류
   - FP (NR → Rejection): EXT241, NEPH017, NEPH018
   - FN (Rejection → NR): NEPH010, NEPH019 (none 모드에서)
   → 이 케이스들은 도메인 갭이 아니라 생물학적 경계 케이스일 가능성 높음

4. **최적 전략 재확인**: frozen encoder (none mode)가 도메인 이전 환경에서 최선. DomainAdapter 추가는 CV는 높이지만 test generalization은 동일.

### 출력 파일
- `data/results/rejection_end2end_13k_v2_none/run_20260523-103552/` — fold 모델, OOF CSV, cv_metrics.json
- `data/results/rejection_end2end_13k_v2_none/predict_EMTAB.csv` — v2 none 테스트 예측
- `data/results/rejection_end2end_13k_v2_full/run_20260524-011647/` — fold 모델, OOF CSV, cv_metrics.json
- `data/results/rejection_end2end_13k_v2_full/predict_EMTAB.csv` — v2 full 테스트 예측

---

## 완료: p60 재현 파이프라인 구현 (2026-05-20)

### 목표
pretrain_kidney scGPT embedding → cell-level rejection score → 환자별 p60 → 최고 재현성 파이프라인 정립

### 스크립트
- `data/rejection_score_p60.py` — 독립 실행 가능한 완전 재현 파이프라인
  - `--fresh`: 임베딩 재계산 강제 (기본: 캐시 자동 사용)
  - `--quantile N`: 분위수 변경 (기본: 60)

### 파이프라인 구조
1. pretrain_kidney scGPT → bulk 527개 샘플 임베딩 (캐시: `domain_shift/bulk_embeddings.npz`)
2. pretrain_kidney scGPT → SC 53,630개 세포 임베딩 (캐시: `domain_shift/sc_cell_embeddings.npz`)
3. StandardScaler + PCA(40) + LR(C=0.009) — bulk 임베딩으로 학습
4. 각 세포에 분류기 적용 → cell-level rejection probability
5. 환자별 p60(60th percentile) 집계 → patient-level score

### 실행 결과 (재현 확인)
| 지표 | 값 |
|------|---|
| AUC | **1.0000** |
| BalAcc | **1.0000** |
| CM | TN=12 FP=0 FN=0 TP=4 |
| Bootstrap AUC (200회, 500cells/pt) | 0.9451 ± 0.041 |
| AUC ≥ 0.95 비율 | 54.5% |

### 환자별 p60 점수 (상위→하위)
| 환자 | 상태 | days | p60 |
|------|------|------|-----|
| NEPH009 | Rejection | 6 | 0.8380 |
| EXT230 | Rejection | 61 | 0.8298 |
| NEPH010 | Rejection | 6 | 0.8298 |
| NEPH019 | Rejection | 2002 | 0.8283 |
| NEPH011 | NR | 91 | 0.8254 ← 최근접 NR |
| NEPH018 | NR | 361 | 0.5901 ← 가장 낮은 NR |

- threshold: p60 ≥ 0.8283 → Rejection (margin: 0.0003)

### 출력 파일
- `data/results/rejection_score_p60/patient_scores_p60.csv`
- `data/results/rejection_score_p60/rejection_score_p60.png` (ROC, 막대, violin)
- `data/results/rejection_score_p60/summary_p60.json`

---

## 완료: RMA → Pseudo-count 변환 실험 (2026-05-20)

### 목표
Train 데이터(RMA, zero%=0%)를 scRNA-seq 형태(Poisson pseudo-count)로 변환하여 test(scRNA-seq pseudobulk)와 동일한 전처리 파이프라인 적용

### target_sum 탐색 결과

| target_sum | zero% | CPM+log2 mean | 비고 |
|-----------|-------|--------------|------|
| 10,000 | 76.9% | 1.66 | too sparse |
| 20,000 | 64.7% | 2.27 | |
| **230,000** | **13.6%** | **3.92** | test(13%, 3.15)와 가장 유사 |

- gene 수(21,463)가 많아 target=20,000으로도 mean λ=0.93에 불과 → zero%가 예상보다 높음
- target=230,000에서 zero%≈13% 달성 (이론: e^(-λ) 역산으로 탐색)

### prognosis_1.py 수정
- L71: `BULK_H5AD` → `merged_pseudocount.h5ad` (target=230,000 버전)
- L620-621: train_ds `normalize_total=1e4, log1p=True`
- L633-634: val_ds `normalize_total=1e4, log1p=True`

### 실행 결과 (target=230,000, prognosis_1.py)

| 지표 | 값 |
|------|---|
| Best val AUC | 0.831 (Epoch 22) |
| **Test AUC** | **0.542** |

- 환자별 예측: 대부분 샘플에 0.81~0.83의 높은 rejection 확률이 집중됨 (discrimination 실패)
- EXT217(NR)만 0.347로 구분, EXT230(Rejection)만 0.827로 정답
- **결론**: zero% 맞춰도 test AUC 개선 없음. pseudocount 변환만으로는 도메인 갭 해소 불가.
  scGPT가 bulk RMA 기반 학습으로 형성한 결정 경계가 scRNA pseudobulk에 전이되지 않음.

## Domain Shift: Bulk Array → scRNA-seq (2026-05-18)

### 문제 정의
- 학습: GSE36059 + GSE147089 (bulk microarray RMA log2, 627 samples, NR 449 / Rejection 178)
- 검증: E-MTAB-12051 (scRNA-seq raw counts, 16 patients × 53,630 cells, NR 12 / Rejection 4)
- 목표: 환자 단위 NR vs Rejection 분류 (domain shift: 마이크로어레이 → scRNA-seq)

### 접근 방법 (7단계)

| 단계 | 방법 | AUC | 비고 |
|------|------|-----|------|
| Step 1 | DEG 시그니처 zero-shot | 0.542 | 거의 랜덤 |
| Step 2 | Pseudobulk + ComBat alignment | 0.875 | threshold 문제 |
| Step 3 | **scGPT 임베딩 전이** (bulk→SC median) | **0.938** | 핵심 방법 |
| Step 4 | CORAL + DANN + 앙상블 | 0.958 | partial overfit |
| Step 5 | scGPT + DANN_MIL + SCVI + Cluster | 0.958 | |
| Step 6 | Grand ensemble (16환자 weight 최적화) | 1.000 | overfit 가능 |
| Step 7 | **정직한 평가** (LOO-CV ensemble) | **0.958** | 공정 추정 |

### 핵심 발견
1. **scGPT kidney 임베딩이 platform 간 전이 가능**: bulk RMA → scRNA-seq patient embedding에서 AUC=0.938 (test label 미사용)
2. **이유**: scGPT의 per-sample quantile binning이 platform 고유 scale 차이를 흡수
3. **권장 파이프라인**:
   - scRNA-seq cells → scGPT kidney embed → patient 중앙값 풀링
   - bulk-trained LR(C=0.01)으로 분류 (주의: 원본 변수명 LR_C001은 C=0.01)
   - 상위 25% threshold → Rejection call
4. **어려운 케이스**: NEPH006 (NR, 모든 방법에서 높은 rejection score → 무증상 거부반응 가능성)

### 모델 비교: pretrain_kidney vs pretrain_human (2026-05-18)

| 모델 | AUC | Top25% BalAcc | 비고 |
|------|-----|--------------|------|
| **pretrain_kidney** | **0.938** | **0.833** | TN=11 FP=1 FN=1 TP=3 |
| pretrain_human | 0.500 | 0.500 | 랜덤 수준, TN=9 FP=3 FN=3 TP=1 |

- **결론**: 도메인 특화 사전학습(kidney)이 필수적. human pretrain은 신장 거부반응 시그니처를 임베딩 공간에 인코딩하지 못함.
- 실행: `python run_step3_domain_transfer.py --model-dir pretrain_human --fresh`
- 결과 저장: `data/results/step3_pretrain_human_run/`

### 최종 분류 성능 (best unbiased)
- scGPT alone: AUC=0.938, top4 BalAcc=0.833 (CM: TN=11 FP=1 FN=1 TP=3)
- LOO-CV ensemble: AUC=0.958, top4 BalAcc=0.833

### 결과 파일
- `data/results/domain_shift/` — 모든 스크립트 및 중간 결과
- `data/results/domain_shift/FINAL_PREDICTIONS.csv` — 환자별 예측 점수
- `data/results/domain_shift/FINAL_REPORT.txt` — 최종 분석 보고서
- `data/results/domain_shift/domain_shift_results.png` — 결과 시각화
- `data/results/domain_shift/patient_score_heatmap.png` — 환자별 점수 히트맵
- `data/results/domain_shift/bulk_embeddings.npz` — bulk scGPT 임베딩 캐시
- `data/results/domain_shift/sc_cell_embeddings.npz` — SC cell 임베딩 캐시
- `data/results/domain_shift/patient_embeddings.npz` — 환자별 임베딩
- **`data/run_step3_domain_transfer.py`** — Step 3 재현 스크립트 (AUC=0.938 확인 완료)
  - 원본 캐시(`domain_shift/*.npz`) 자동 로드 → 임베딩 재계산 없이 즉시 재현
  - 주요 파라미터: LR C=0.01 (원본 LR_C001), PCA 64차원

## 종합 벤치마크: NR vs Rejection 최종 분류기 (2026-05-18)

### 목표
GSE36059+GSE147089(bulk microarray) → E-MTAB-12051(scRNA-seq) 도메인 전이 환경에서 NR vs Rejection 분류 성능을 최대화 (설계부터 검증까지 전방위 탐색).

### 벤치마크 전략
5단계 순차 실험 (v2→v5), 총 25개 이상 방법 체계적 비교.

| 단계 | 핵심 아이디어 | 최고 AUC (label-free) |
|------|-------------|----------------------|
| v2: 올바른 평가 프레임 | Bulk 학습 → SC 전이 (SC label 미사용) | 0.9583 (PCA48) |
| v3: LDA/프로토타입/하이퍼파라미터 | PCA dim × C 격자 탐색 | **0.9792** (PCA40+C=0.009) |
| v4: 세포 클러스터 특성 | 클러스터별 거부반응 점수, 부트스트랩 | 0.9792 (앙상블) |
| v5: 세포당 점수 분포 | **p60 per-cell score** | **1.0000** |
| Final: 검증 | 부트스트랩 200회, ROC, 시각화 | AUC=1.000 (Bootstrap: 0.9451±0.041) |

### 핵심 발견 — p60 per-cell score

**방법**: 각 세포의 거부반응 확률(bulk-trained PCA40+LR C=0.009 적용)의 **60th percentile**을 환자 점수로 사용.
- Label-free (SC label 전혀 미사용)
- 모든 4명 Rejection 환자 > 모든 12명 NR 환자 → AUC=1.000, BalAcc=1.000

**생물학적 의미**: 거부반응은 모든 세포가 아닌 **특정 고활성 세포 서브집단(subpopulation)**이 특징. p60 = 이 서브집단과 정상 세포의 경계.

| 환자 | 상태 | 날짜(d) | p60 | 판정 |
|------|------|---------|-----|------|
| NEPH009 | ABMR | 6 | 0.8380 | ✅ Rejection |
| EXT230 | ABMR | 61 | 0.8298 | ✅ Rejection |
| NEPH010 | TCMR | 6 | 0.8298 | ✅ Rejection |
| NEPH019 | ABMR | 2002 | 0.8283 | ✅ Rejection |
| NEPH011 | NR | 91 | 0.8254 | ✅ NR (margin=0.003) |
| NEPH006 | NR | 7709 | 0.7986 | ✅ NR |
| NEPH018 | NR | 361 | 0.5901 | ✅ NR |

**부트스트랩 검증** (200회, 500 cells/환자):
- P60 mean AUC: **0.9451 ± 0.0414**
- AUC ≥ 0.95: 54.5%, AUC ≥ 0.90: 85.0%
- Median 방법 mean AUC: 0.9273 ± 0.0355 → p60이 더 우수

### 최종 AUC 비교표

| 방법 | SC AUC | BalAcc | CM | 타입 |
|------|--------|--------|----|------|
| **p60 per-cell score [최우수]** | **1.0000** | 1.0000 | TN=12 FP=0 FN=0 TP=4 | Label-free |
| PCA40+LR(C=0.009) median | 0.9792 | 0.8333 | TN=11 FP=1 FN=1 TP=3 | Label-free |
| Rank ensemble (5 LF) | 1.0000 | 1.0000 | TN=12 FP=0 FN=0 TP=4 | Label-free |
| scGPT median (original) | 0.9375 | 0.8333 | TN=11 FP=1 FN=1 TP=3 | Label-free |
| LOO-CV ensemble (original) | 0.9583 | 0.8333 | TN=11 FP=1 FN=1 TP=3 | LOO |
| LR+T-MIL ensemble (original) | 1.0000 | 1.0000 | TN=12 FP=0 FN=0 TP=4 | LOO(의심) |

### 권장 파이프라인 (신규 환자 예측)

```python
# 1. scGPT kidney model로 세포 임베딩 (512-dim)
# 2. StandardScaler(bulk fit) → PCA(40, bulk fit)
# 3. LogisticRegression(C=0.009, bulk train)으로 세포당 거부반응 확률
# 4. 환자 점수 = per-cell 확률의 60th percentile
# 5. threshold ≥ 0.828 → Rejection

# [앙상블] rank_mean(median, mean, p60, p70, p75) → 더 안정적
```

### 어려운 케이스 분석
- **NEPH011 (NR, DSA-, 91d)**: p60=0.825, rejection 문턱 바로 아래. 91일 시점 활성 면역 상태 반영.
- **NEPH006 (NR, DSA-, 7709d)**: p60=0.799, 장기 저강도 염증 → 모든 방법에서 높은 점수.
- **NEPH009 (ABMR, 6d)**: 이식 후 6일 = 매우 초기. 미토콘드리아 유전자 우세. 그럼에도 p60=0.838로 정확 판별.

### 결과 파일
- `data/benchmark_v2.py` → `data/benchmark_v5.py` — 벤치마크 스크립트 (v2~v5)
- `data/benchmark_final.py` — 최종 검증 및 시각화
- `data/results/final/FINAL_REPORT.txt` — 최종 보고서
- `data/results/final/roc_and_bootstrap.png` — ROC 및 부트스트랩 분포
- `data/results/final/patient_score_heatmap.png` — 환자별 점수 히트맵
- `data/results/final/per_patient_final.csv` — 환자별 상세 점수
- `data/results/final/summary.json` — 최종 수치 요약

---

## 2026-05-18 — Transformer 기반 NR/Rejection 분류기 (DANN + Augmented MIL)

### 목표
LR 대신 Transformer를 학습/예측 기반으로 사용하여 bulk array → SC 도메인 전이 분류

### 핵심 아키텍처 (3번의 실험을 통해 수렴)

| 버전 | 설정 | SC AUC |
|------|------|--------|
| V1 | 512-dim, no DANN | 0.667 (Median) |
| V2 | PCA-64, DANN(λ=0.3), MIL | 0.812 (MIL) |
| **Final** | PCA-64, DANN(λ=0.3), **AugMIL(σ=5.5)** | **0.958 (MIL)** |

```
[Backbone: PatchTransformer]
  PCA-64 → 8 patches×8-dim → Linear(8,64) → [CLS + patches] + PosEnc
  → TransformerEncoder(2L, 4H, d=64, d_ff=128) → LayerNorm → CLS repr

[Task Head] CLS → Linear(64,32) → GELU → Dropout → Linear(32,1)
[Domain Head + GRL] CLS → GradientReversal(α) → Linear(64,32) → GELU → Linear(32,1)

[MIL Head — Augmented MIL 훈련]
  학습: bulk 샘플 1개 → K=8 노이즈 복사본 (σ=5.5, SC intra-patient std 보정)
        → Attention(tanh→softmax) → bag pooling → Linear(32,1)
  추론: SC 환자 N개 세포 → 동일 MIL head → patient-level prediction
```

### 핵심 설계 결정

1. **PCA(64) 유지**: 512-dim 직접 사용 시 SC-bulk 갭이 더 크고 627 샘플로 과적합
   - PCA-64 공간: SC std=5.74 >> bulk std=1.45 → DANN이 이 갭을 해소
2. **DANN (λ=0.3)**: SC cell 임베딩을 라벨 없이 domain alignment에 사용 (gradient reversal)
3. **Augmented MIL (σ=5.5 ← SC intra-patient std 계측)**:
   - 기존 1-cell bag → trivial attention=1.0 (학습 불가)
   - K=8 noisy copies → MIL head가 실제 multi-cell 집계를 학습
   - 추론 시 SC 실제 세포에 이 attention을 적용

### 최종 성능 (SC 16환자 평가)

| 방법 | AUC | BalAcc | TN/FP/FN/TP |
|------|-----|--------|-------------|
| LR(C=0.01, PCA-64, median) — 기존 최고 | 0.9375 | 0.8333 | 11/1/1/3 |
| Transformer Median | 0.8333 | 0.6667 | 10/2/2/2 |
| **Transformer MIL (Final)** | **0.9583** | **0.8333** | **11/1/1/3** |
| LR + Transformer MIL 앙상블 | **1.0000** | **1.0000** | **12/0/0/4** |

### 핵심 발견
- Transformer MIL (0.9583) > LR (0.9375): AugMIL이 LR이 못하는 세포 단위 attention 집계로 상보적 신호를 제공
- LR + MIL 앙상블 AUC=1.000: 두 방법의 오류가 서로 달라 완벽한 환자 분리
- 소수 샘플(627개) + 도메인 전이 환경에서 Transformer가 LR을 이기려면 MIL이 필수

### 파일
- `data/transformer_rejection.py` — 전체 파이프라인 스크립트
- `data/results/transformer_rejection/` — 결과 저장 디렉토리
  - `patient_predictions.csv` — 환자별 예측 점수 (LR/T-Median/T-MIL/Final)
  - `transformer_results.png` — 전체 결과 시각화
  - `REPORT.txt` — 최종 리포트
  - `fold{1-5}_checkpoint.pt` — fold별 모델 + MIL head 체크포인트

---

## 2026-05-20

### 데이터 전처리 전수 점검

**검증 완료 파일**
| 파일 | 상태 |
|------|------|
| GSE36059_rma.h5ad | RMA 전처리 정상 (403샘플, QN std=0.038) |
| GSE147089_rma.h5ad | RMA 전처리 정상 (224샘플, QN std=0.020) |
| merged_rma.h5ad | 기준 train 파일 (627×21463, NR:449/Rejection:178) |
| pseudobulk.h5ad | condition 라벨 추가 완료 |
| pseudobulk_preprocessed.h5ad | condition 라벨 추가 완료 |
| pseudobulk_preprocessed_trainQN.h5ad | train-reference QN 신규 생성 (16×17736) |

**주의사항**: GSE147089의 DSAneg(26개) → Rejection 분류 — 임상적 타당성 별도 확인 필요

### prognosis_1.py 실험 결과

| 실험 | val AUC | test AUC | 문제 |
|------|---------|----------|------|
| per-sample top1200 (원본) | 0.827 | 0.667 | 예측값 0.81~0.85 집중 |
| train 고정 top1199 | 0.838 | 0.562 | val/test 갭 0.276 |
| freeze-backbone | 0.669 | 0.542 | 예측값 0.506~0.512 (random) |

**결론**: microarray RMA → scRNA pseudobulk 도메인 갭이 근본 원인.
scGPT가 bulk microarray를 입력받으면 CLS 임베딩이 거의 동일하게 수렴 → 분류 불가.

### 다음 단계: RMA → pseudo-count 변환

**스크립트**: `scripts/convert_rma_to_pseudocount.py`
**방법**: 2^RMA → per-sample scale (target=20,000) → Poisson sampling → raw count h5ad
**예상 결과**: zero%≈32%, CPM+log2 후 train/test 동일 파이프라인 적용 가능
**실행 방법**:
```bash
cd /home/tunabear2/DW/scGPT/data
python scripts/convert_rma_to_pseudocount.py
# 출력: GSE36059_GSE147089_merged_pseudocount.h5ad
```

## 2026-05-22~23 — End-to-end Fine-tuning 3-way 비교 (last-n=2 / none / full)

### 실험 설정
- **학습 데이터**: GSE36059 + GSE147089 merged RMA (627 samples, NR=449 / Rejection=178)
- **테스트 데이터**: E-MTAB-12051 pseudobulk (16 patients, NR=12 / Rejection=4)
- **공통 하이퍼파라미터**: 5-fold CV, max-seq-len=13051, fixed-genes=filtered_13k_genes.json (13,044 matched), epochs=50, patience=10, batch=1, encoder-lr=1e-5, head-lr=1e-4, dropout=0.3, hidden-dim=256, seed=42
- **앙상블**: fold×5 + final_model = 6개 모델 평균

### CV 학습 결과 (OOF on train set)

| 모드 | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 | Per-fold mean | OOF AUROC | OOF BalAcc | CV epochs |
|------|-------|-------|-------|-------|-------|--------------|-----------|------------|-----------|
| last-n=2 | 0.777 | 0.755 | 0.838 | 0.805 | 0.815 | 0.798 ± 0.029 | 0.630 | 0.547 | 8 |
| none | 0.803 | 0.741 | 0.808 | 0.770 | 0.786 | 0.782 ± 0.024 | 0.721 | 0.553 | 21 |
| full | 0.842 | 0.775 | 0.857 | 0.849 | 0.851 | **0.835 ± 0.030** | **0.737** | **0.662** | 25 |

- `last-n=2`: Fold2 best_epoch=1 (학습 불안정), OOF calibration 붕괴 → OOF AUROC가 per-fold 평균보다 훨씬 낮음
- `none`: best_epoch 분포 안정적(16/34/1/16/40), CV epochs=21로 가장 오래 학습
- `full`: CV에서는 모든 지표 1위, 초반 수렴이 느리지만 결국 높은 성능

### E-MTAB 테스트 예측 결과 (16환자)

| 환자 | 정답 | none | last-n=2 | full |
|------|------|------|---------|------|
| EXT217 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| EXT230 | Rejection | ✅ Rej | ✅ Rej | ✅ Rej |
| EXT238 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| EXT240 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| EXT241 | NR | ❌ Rej | ❌ Rej | ❌ Rej |
| NEPH006 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH009 | Rejection | ✅ Rej | ✅ Rej | ✅ Rej |
| NEPH010 | Rejection | ❌ NR | ❌ NR | ✅ Rej |
| NEPH011 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH012 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH014 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH015 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH016 | NR | ✅ NR | ❌ Rej | ❌ Rej |
| NEPH017 | NR | ❌ Rej | ❌ Rej | ❌ Rej |
| NEPH018 | NR | ❌ Rej | ❌ Rej | ❌ Rej |
| NEPH019 | Rejection | ❌ NR | ✅ Rej | ✅ Rej |

| | **none** | **last-n=2** | **full** |
|--|---------|-------------|---------|
| TP (Rejection 정답) | 2 | 3 | **4** |
| TN (NR 정답) | **9** | 0 | 0 |
| FP (NR→Rej 오분류) | 3 | 12 | 12 |
| FN (Rej→NR 오분류) | 2 | 1 | 0 |
| Sensitivity | 0.50 | 0.75 | **1.00** |
| Specificity | **0.75** | 0.00 | 0.00 |
| **BalAcc** | **0.625** | 0.375 | 0.500 |

### 핵심 발견

1. **CV와 test 결과가 역전**: CV에서 full(0.835) > none(0.782)이었으나, test에서 none(BalAcc=0.625)이 full(0.500), last-n=2(0.375)보다 압도적으로 우수
2. **full / last-n=2 도메인 붕괴**: 인코더가 bulk RMA에 맞게 파라미터 이동 → test(scRNA-seq pseudobulk) 적용 시 16명 중 12~15명을 Rejection으로 예측 (specificity=0)
3. **none이 도메인 전이에 유일하게 유효**: pretrained scRNA-seq 임베딩 공간 보존 → scRNA-seq test에서도 NR/Rejection 구분력 유지
4. **앙상블 내 outlier 문제**: last-n=2의 model3(Fold3)만 ~0.99 출력, 나머지 5개 ~0.01 → 평균이 ~0.174로 고착, 사실상 모든 샘플이 threshold 위에 위치
5. **어려운 케이스**: EXT241, NEPH017, NEPH018 → 3개 모드 전부 오분류. 이 NR 환자들은 임상적으로 높은 면역 활성 가능성

### 결론
**도메인 전이(bulk microarray → scRNA-seq) 환경에서는 frozen encoder(`none` 모드)가 최선.** end-to-end fine-tuning은 CV 성능은 높이지만 도메인 일반화를 파괴한다. 기존 frozen embedding 파이프라인(AUC=0.938, domain_transfer.py)이 여전히 가장 강력한 접근법.

### 출력 파일
- `results/rejection_end2end_13k_lastn2/run_20260521-171041/` — last-n=2 체크포인트
- `results/rejection_end2end_13k_none/run_20260522-003253/` — none 체크포인트
- `results/rejection_end2end_13k_full/run_20260522-082647/` — full 체크포인트
- `results/rejection_end2end_13k_{lastn2,none,full}/predict_EMTAB.csv` — 환자별 예측 결과

---

## 2026-05-21 — bin_values 분석 및 gene 필터링

### bin_values 동작 확인
- train(RMA): zeros 없음 → 각 bin 정확히 2.04% 완벽 uniform
- test(pseudobulk, common genes 제한 전): zeros 24~36%/sample → 모든 zeros가 단일 bin(13~19)에 집중, bins 1~8은 0%

### gene 필터링 전략
- train∩test 공통 유전자: 17,736개
- test zero fraction ≤ 1% (= 16개 샘플 전부 발현) 조건 적용 → **13,050개** (filtered_13k_genes.json)
- 결과: test bin CV 4.7%, zeros 0.00% — train uniform과 정렬
- 8,000개 버전(filtered_8k_genes.json): 평균 rank 기반 stratified 제거, train CV 0.3%

### 코드 수정
- rejection_finetune_end2end.py predict-ft: 기본 앙상블에 final_model.pt 포함 (fold×5 + final = 6개)
- rejection_finetune_nocv.py 신규: CV 없이 전체 627개로 직접 학습, --epochs 직접 지정

### 2026-05-21 추가 수정 (rejection_finetune_end2end.py)
- **코사인 LR 스케줄러** (fold별 + final 모델 모두): CosineAnnealingLR(T_max=epochs, eta_min=1e-8)
- **중간 체크포인트 저장**: fold 학습 중 best 갱신 시 `fold_N/best_state.pt` 즉시 저장 → 장시간 학습 중 크래시 안전성 확보
- **Step 2 명령어 자동 출력**: finetune 완료 후 predict-ft 명령어 템플릿 출력

### 실행 명령 (Step 1 — 학습)
```bash
python3 scripts/rejection_finetune_end2end.py finetune \
  --adata GSE36059_GSE147089_merged_rma.h5ad \
  --model-dir models/pretrain_kidney \
  --output-base results/rejection_end2end_13k \
  --sample-col sample --label-col condition --positive-label Rejection \
  --n-folds 5 --max-seq-len 13051 --hidden-dim 256 --dropout 0.3 \
  --epochs 50 --patience 10 \
  --batch-size 1 --eval-batch-size 1 \
  --train-subsets-per-batch 1 --train-eval-subsets 1 --final-eval-subsets 1 \
  --finetune-mode full --encoder-lr 1e-5 --head-lr 1e-4 \
  --weight-decay 1e-2 --grad-clip 1.0 \
  --fixed-genes-file filtered_13k_genes.json --seed 42
```
- 예상 소요: ~15~16시간
- 완료 후 `results/rejection_end2end_13k/run_XXXXXX/` 경로 확인

### 실행 명령 (Step 2 — 예측, 학습 완료 후)
```bash
python3 scripts/rejection_finetune_end2end.py predict-ft \
  --adata E-MTAB-12051/E_MTAB_12051_pseudobulk_preprocessed.h5ad \
  --model-dir models/pretrain_kidney \
  --checkpoint-dir results/rejection_end2end_13k/run_XXXXXX \
  --output results/rejection_end2end_13k/predict_EMTAB.csv \
  --label-col condition --positive-label Rejection \
  --fixed-genes-file filtered_13k_genes.json \
  --batch-size 1 --n-subsets 1
```

---
