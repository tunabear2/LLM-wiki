---
type: worklog-chunk
status: archive
rag_priority: medium
updated: '2026-07-20'
date_range: 2026-04-30..2026-05-17
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

# scGPT prognosis worklog — 2026-05 early

> [!note] 검색용 분할본
> 원본은 [2026-06-16 scGPT prognosis worklog](../logs/2026-06-16-scgpt-prognosis-worklog.md)입니다. 결론이 충돌하면 최신 `reports/` 문서를 우선합니다.

## 완료: Binary Classification — B17 vs B25_CTRL (2026-05-04)

### 목표
A질병 양성(B17) / 음성(B25_CTRL) 판별 분류기를 cell-level scGPT fine-tuning으로 구현.

### 데이터
| 파일 | 내용 | Cell 수 |
|------|------|---------|
| `data/B17.h5ad` | 양성 환자 세포 | 10,022 |
| `data/B25_CTRL.h5ad` | 음성 환자 세포 | 5,960 |

- 공통 gene: 36,601개 → HVG 1,200개 → vocab 교집합 **934개** 사용
- label 1: B17 전체 cell, label 0: B25_CTRL 전체 cell
- train/val/test = 60/20/20% (cell 단위 stratified split)

### 모델 구조
- Backbone: `models/pretrain_bc/` (scGPT human pretrained, 12L-512d)
- Head: LayerNorm → Linear(512→256) → GELU → Dropout → Linear(256→1)
- 2단계 학습: Phase1 head-only frozen → Phase2 full fine-tuning

### 최종 결과
| 단계 | Val AUC | Val Acc |
|------|---------|---------|
| Phase1 ep05 (head-only) | 0.6605 | 62.6% |
| Phase2 ep10 (full FT) | **0.9632** | **88.3%** |
| **Test** | **0.9603** | **88.2%** |

### 저장 파일
- `data/best_model.pt` — 최고 Val AUC 체크포인트
- 신규 환자 추론: `predict_patient(model, "new.h5ad", vocab)` 호출

### 주의사항
- cell 단위 분할이므로 동일 환자 cell이 train/test에 섞임 → 실제 신규 환자 성능보다 낙관적

### 스크립트
- `data/scGPT_Binary_Classification.py`
- `data/training_log.txt` — 학습 로그 전문

---

## 완료: GSM 8명 환자 추론 (2026-05-04)

### 학습 재실행 결과
- gene 목록: 학습 시 사용한 24,159개 → `data/training_genes.json` 저장
- Test AUC: **0.9969** | Acc: **0.9703** (이전 실행 대비 대폭 향상)

### predict_gsm_patients.py 수정 내용
- `training_genes.json` 로드 후 환자 데이터에서 해당 gene만 필터링 (vocab 전체 대신)
- 환자마다 vocab gene 23,077개 일치 (training gene 24,159개의 부분집합)

### 추론 결과 (threshold=0.5)
| 환자 | Cells | 양성cell비율 | 양성확률 | 판정 |
|------|------:|----------:|-------:|------|
| R4697 | 7,525 | 73.2% | 0.7301 | 양성 |
| R587 | 11,602 | 57.6% | 0.5730 | 양성 |
| PBMC3 | 2,175 | 82.5% | 0.8247 | 양성 |
| PBMC4 | 5,705 | 80.4% | 0.7983 | 양성 |
| R3617 | 11,887 | 63.7% | 0.6258 | 양성 |
| R817 | 6,960 | 63.1% | 0.6274 | 양성 |
| R1777 | 6,950 | 53.6% | 0.5336 | 양성 |
| R3517 | 7,286 | 53.7% | 0.5344 | 양성 |

- **8명 전원 양성 판정**
- R1777, R3517은 확률 0.53대 — threshold 근접, 추가 검토 권장

### 저장 파일
- `data/training_genes.json` — 학습 gene 목록 24,159개
- `data/best_model.pt` — 최고 Val AUC 체크포인트


---

## 계획 중: Patient-level Classification (2026-04-30)

### 목표
scGPT 세포 임베딩을 환자별로 Pooling해서 신장 이식 후 **정상(normal) vs 거부반응(rejection)** 을 분류하는 환자 단위 모델 구축.

### 보유 데이터
| 파일 | 내용 |
|------|------|
| (경로 미확인) normal .h5ad | 정상 환자 10명 single-cell 데이터 합본 |
| (경로 미확인) rejection .h5ad | 거부반응 환자 10명 single-cell 데이터 합본 |

> 다음 세션 시작 시 파일 경로와 `adata.obs.columns` 확인 필요.

### 합의된 파이프라인

1. **데이터 준비**
   - 두 .h5ad 병합
   - `obs['patient_id']`, `obs['label']` 컬럼 존재 여부 확인 및 추가

2. **scGPT 세포 임베딩 추출**
   - 기존 `annotation.py` 참고
   - 결과: `adata.obsm["X_scGPT"]` — shape `(n_cells, 512)`

3. **환자별 Pooling**
   - 1차 시도: **Mean pooling** (환자당 모든 세포 임베딩 평균)
   - 결과 shape: `(20, 512)`

4. **분류기 학습**
   - CV 전략: **Leave-One-Out (LOOCV)** — 환자 단위 분리 필수
   - 1차 모델: **Logistic Regression**
   - 추가 시도: SVM, Random Forest

5. **추후 개선 옵션**
   - Cell-type-aware pooling (세포 타입별 평균 concat)
   - Attention-based pooling (MIL)
   - 배치 효과 보정 (Harmony / scVI)

### 다음 세션 할 일
- [ ] 두 .h5ad 파일 경로 확인
- [ ] `adata.obs.columns` 확인 (patient_id, label 컬럼 유무)
- [ ] 파이프라인 스크립트 작성 시작

---

## 2026-05-14 — GSE147089 RMA 재전처리

### 문제 진단
- `GSE147089_rma.h5ad` X 행렬 전체가 `-19.9316` 단일 값 (unique=1)
- 원인: `build_h5ad.py`의 `rma_background()` 함수 버그
  - `alpha = 0.1` (고정값) × `sigma²` (전체 분포 std ≈ 1419)² ≈ **201,350**
  - `a = x - mu - 201350` → 모든 probes에서 a << 0 → `np.maximum(..., 1e-6)` = 1e-6
  - `log2(1e-6) = -19.9316` 으로 전체 floored

### 수정 사항 (`GSE147089/build_h5ad.py`)
- `rma_background()` 파라미터 추정 방식 교체:
  ```python
  noise = x[x < np.percentile(x, 25)]
  mu_b = np.mean(noise)          # background mean: ~75
  sigma_b = np.std(noise)        # background std: ~9  (기존 ~1419)
  alpha = 1.0 / max(np.mean(x) - mu_b, 1.0)  # signal rate: ~0.00275
  ```
- `add_condition.py` 내용을 `build_h5ad.py`에 통합 (condition 매핑 포함)

### 결과
- Shape: (224, 21463)
- X range: [1.85, 15.11] (log2 microarray 기대값 범위)
- Unique values: 3,969,509 (정상)
- Conditions: No_ABMR=168, DSApos=30, DSAneg=26

---

## 2026-05-14 — Few-shot Transfer Learning: scGPT 기반 거부반응 예측 헤드

### 파이프라인 설계
- 파일: `data/rejection_finetune.py`
- 3-command CLI: `embed` / `train` / `predict`

### 아키텍처
```
Frozen scGPT Encoder (pretrain_kidney)
  └─ gene token + binned value → CLS embedding (512-dim)

RejectionHead
  └─ LayerNorm → Linear(512,256) → GELU → Dropout → LayerNorm → Dropout → Linear(256,1) → sigmoid
```

### 데이터 처리 (Bulk microarray 특수 처리)
- RMA 데이터는 0이 없으므로 전 유전자 발현 → 매 샘플마다 max_seq_len=1199 랜덤 서브셋 5회 평균
- normalize_total / log1p 비활성화 (이미 log2 RMA normalized)
- 클래스 불균형 (NR 449 : Rejection 178): BCE pos_weight=2.52 자동 적용

### 학습 결과 (5-fold Stratified CV)
- 학습 데이터: `GSE36059_GSE147089_merged_rma.h5ad` (627 samples)
- vocab match: 19,893 / 21,463 genes
- OOF AUROC: **0.7654**  AUPRC: 0.5501  Balanced Acc: 0.694
- Per-fold AUROC: **0.7908 ± 0.0222**
- 저장: `results/rejection_head/final_head.pt`

### 예측 사용법
```bash
python rejection_finetune.py predict \
    --adata <new_patient.h5ad> \
    --model-dir models/pretrain_kidney \
    --head-dir results/rejection_head \
    --output results/rejection_head/predictions.csv
```

---
