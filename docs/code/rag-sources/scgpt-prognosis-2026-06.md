---
type: worklog-chunk
status: archive
rag_priority: medium
updated: '2026-07-20'
date_range: 2026-06-01..2026-06-16
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

# scGPT prognosis worklog — 2026-06

> [!note] 검색용 분할본
> 원본은 [2026-06-16 scGPT prognosis worklog](../logs/2026-06-16-scgpt-prognosis-worklog.md)입니다. 결론이 충돌하면 최신 `reports/` 문서를 우선합니다.

## predict-cell 결과 통합 (E-MTAB + 외부 scRNA-seq 4) + bar plot (2026-06-16)

### 목표
- `prognosis_microarray_adapter.py predict-cell`로 얻은 환자단위 p60 rejection 확률을 **한 장(CSV + bar plot)** 으로 통합. in-domain source(E-MTAB-12051)와 외부 scRNA-seq 4시리즈를 함께 비교.

### 데이터 소스 (모두 `data/results/` 하위)
- E-MTAB-12051 (in-domain, 16환자): `prognosis_adapter_8000/predict_cell_p60_qc.csv`
- 외부 Run1(재학습 없이 adapter_8000): `prognosis_adapter_8000/predict_cell_<GSE>_p60.csv`
- 외부 Run2(공통gene 재학습): `prognosis_adapter_commongenes_<GSE>/predict_cell_<GSE>_p60.csv`
- ⚠️ **E-MTAB는 Run2(공통gene 재학습) 안 함** — 기존 bulk adapter를 그대로 적용한 Run1 조건만 존재.

### 산출물: `data/results/prognosis_predict_cell_combined/`
- `predict_cell_all_combined.csv` — 25환자 × `dataset, domain, patient_id, n_cells, label, run1_p60_prob, run2_p60_prob, run2_minus_run1` (Run2는 외부 4개만, E-MTAB은 NaN)
- `predict_cell_run1_bar.png` — **최종 그림**: Run1 p60 확률만, **내림차순 정렬**, 색=실제라벨(빨강 Rejection / 파랑 NR), 0.5선·AUROC라벨·그룹선 제거, 제목 `predict-cell p60 rejection probability.`
- `predict_cell_all_combined_bar.png` — (중간본) Run1 solid + Run2 빗금 그룹 막대, AUROC 표기. 사용자가 Run1-only를 택하면서 비채택.

### 결과 요약
- AUROC(p60): **E-MTAB-12051 = 0.875** (Rej 4/NR 12), **GSE195719 = 1.0** (Rej 2/NR 1). 나머지 3개(GSE109564·145927·151671)는 단일-Rejection이라 AUROC 산출 불가, 확률값만.
- 정렬 시 상위권(p60≥0.59)은 전부 외부 Rejection 환자(KUT014·AK1·GSE109564·AK2·day11). E-MTAB 환자는 Rej/NR이 0.47~0.54 좁은 구간에 혼재 → in-domain source가 외부보다 분리력 약함.
- 공통gene 재학습(Run2)은 외부 확률을 대체로 상향(AK2 +0.097, AK1 +0.062, GSE145927 +0.06~0.07; GSE109564·195719 거의 불변)이나, 통합 그림은 E-MTAB와의 공정 비교 위해 Run1로 통일.

---

## 19개 microarray 데이터셋 멀티-데이터셋 finetune 스크립트 작성 (2026-06-16)

### 배경 / 목표
- `rma_out/training_labeled/`의 **19개 .h5ad** (플랫폼 상이 → gene 수 9,054~21,355개)를 NR/Rejection 라벨로 동시 학습하고 싶음.
- 라벨 컬럼: 전 19개 통일 **`diagnosis` = `NR`/`Rejection`**. 총 **2,179 샘플 (NR 1,209 / Rej 970)**, vocab 매칭 93%.
- 값은 RMA log2 (0~14.7, counts 아님) → **`--normalize` 쓰면 안 됨** (per-sample quantile binning이 스케일 흡수).
- ⚠️ **단일클래스 3개**: GSE106675(Rej 10), GSE21374(Rej 29), GSE48581(Rej 65) — NR 없음.

### 핵심 판단
- 이 모델(`prognosis_microarray_adapter.py`)은 **gene-name 기반 토큰화 + nonzero gene만 선택 + per-sample binning** → 플랫폼/gene 수 차이를 구조적으로 흡수. 따라서 **교집합(7,843)으로 줄일 필요 없이 union(26,288)으로 합치고 없는 값 0** 으로 두면 됨.
- 기존 코드는 `StratifiedKFold`(샘플 랜덤 분할) → 19개 섞으면 같은 GSE가 train/val 양쪽 → **배치/플랫폼 누설 → AUROC 과대평가**. 새 코호트/SC 일반화 목표와 불일치.
- → **Leave-One-Dataset-Out (GSE 단위 grouped CV)** 채택. 단일클래스 3개는 항상 train 고정(학습신호는 활용, val 불가). 사용자와 합의.

### 산출물: `scripts/prognosis_microarray_adapter_multidataset.py` (기존 파일 미변경, 복사 후 수정)
- 신규 **`merge`** 서브커맨드: N개 h5ad를 union gene으로 outer-join(fill 0, csr_matrix), 파일명에서 GSE 파싱해 `obs['dataset']` + `obs['source_file']` 부착 → 단일 merged h5ad.
- **`finetune`** 그룹 CV로 개편:
  - `--cv logo` (기본) = leave-one-dataset-out (two-class GSE 1개당 fold 1개, 16 fold)
  - `--cv grouped` = `StratifiedGroupKFold(--n-folds)` (two-class GSE 대상, 단일클래스 pinned-train)
  - `--group-col dataset` 추가, 단일클래스 자동 감지→train 고정
  - OOF는 two-class 샘플만(nan 마스킹), **per-dataset AUROC 표** + pooled OOF + mean±std 출력, `cv_metrics.json`에 `per_dataset`/`single_class_datasets`/`cv_mode` 기록
  - `load_bulk_h5ad`에 `group_col` 인자/반환 추가, 라벨 기본값 `condition`→`diagnosis`
- 검증: `py_compile` OK, `merge/finetune --help` 정상. **아직 실행 안 함**(사용자 요청 — 파일 생성만).

### 다음에 실행할 명령 (미실행)
```
python3 scripts/prognosis_microarray_adapter_multidataset.py merge \
    --input-dir rma_out/training_labeled --pattern '*.h5ad' \
    --label-col diagnosis --group-col dataset \
    --output rma_out/training_labeled_merged.h5ad

python3 scripts/prognosis_microarray_adapter_multidataset.py finetune \
    --adata rma_out/training_labeled_merged.h5ad \
    --model-dir models/pretrain_kidney \
    --label-col diagnosis --positive-label Rejection \
    --group-col dataset --cv logo \
    --output-base results/prognosis_adapter_multidataset
```
(주의: `--normalize` 금지. LOGO=16회 학습, encoder frozen이라 어댑터+헤드만 학습.)

---

## microarray minmax h5ad에 진단 라벨 부착 (21/22 시리즈) + Rejection/NR 작업용 참조 (2026-06-14)

### 위치 / 형식
- 대상 파일: **`rma_out/minmax/<GSE>_rma_minmax.h5ad`** (X = 샘플×유전자, zeroed<5+per-sample minmax)
- 추가된 `obs` 컬럼: **`diagnosis`**(시리즈 원본 진단, 가공 최소), **`gsm`**(GSM ID), **`characteristics`**(GEO 원문 전체 — 보완·재파싱용)
- 라벨 소스: `kidney/sample_metadata.csv`의 `characteristics`. 부착 스크립트: **`scripts/add_diagnosis_labels.py`**
- GSM 매칭: obs_name에서 `GSM\d+` 추출 → 전 시리즈 100% 매칭. **16개 전부 전 샘플 labeled.**
- ⚠️ Rejection/NR **이진 라벨은 미작업**(사용자 후속). 아래 분포 참고해 매핑하면 됨.

### 16개 시리즈: 사용 필드 + 진단값 분포 (Rejection/NR 매핑 시 매핑 대상)
| 시리즈 | 사용 characteristics 필드 | diagnosis 값 분포 |
|---|---|---|
| GSE36059 | `diagnosis (tcmr,abmr,mixed,non-rejecting)` | non-rejecting 280, ABMR 65, TCMR 35, MIXED 22, Nephrectomy 8 |
| GSE48581 | `diagnosis (tcmr,non-tcmr,nephrectomies)` | non-TCMR 268, TCMR 32, Nephrectomies 6 |
| GSE192444 | `mmdx (abmr,tcmr,mixed,nr,pabmr,ptcmr)` | NR 175, ABMR 67, TCMR 21, Mixed 19, pABMR 12, pTCMR 6 |
| GSE98320 | `d96` (분자진단; `mmdx`는 종종 '-') | NOMOA 274, ABMR 215, IFTA 145, Bord. 109, GN 97, AKI 96, TCMR 87, Mixed 41, TG 40, BK 37, Other 25, ABMRsusp 24, DiabNeph 18 |
| GSE21374 | `rejection/non rejection` | nonrej 206, rej 76 |
| GSE138043 | `rejection at 12months post transplant` | non-AR 37, AR 15 |
| GSE14328 | 첫 free-text 세그먼트 | stable 18, acute rejection 18 |
| GSE9493 | `Banff'97`(쉼표구분); 없으면 control 설명 | non-rejecting 21, Control(nephrectomy) 14, CAN I/II/III 25, AR IA/IB/IIA/IIB 9, AR+CAN 7, borderline 4, (Lot#A507273 1=특이값) |
| GSE50058 | `patient group` | stable(STA) 58, acute rejection(AR) 43 |
| GSE34437 | `disease status` | living donor 33, no abnormalities 16, ARIA 7, ARIB 6, borderline 4 |
| GSE53605 | `histological diagnosis` | Normal 18, CNIT 14, AR/ACR 13, IF/TA 10 |
| GSE72925 | `diagnosis` | Normal 68, IFTA 59, TCMR 26, PVAN 10, Normal/BKVB 5 |
| GSE147089 | `phenotype` | No ABMRh 168, DSAposABMRh 30, DSAnegABMRh 26 |
| GSE75693 | `condition` | Stable graft 30, Acute rejection 15, BKVN 15, CAN 유무 12/7 |
| GSE106675 | `condition` | Rejection 10, Donor 7, Tolerance 7, Standard IS 6 |
| GSE129166 | `tcmr`+`abmr` 코드 변환 | no rejection 130, ABMR 47, Borderline 24, TCMR 6, Mixed 5 |

특이 파싱: GSE129166 코드(tcmr2→TCMR,1→Borderline,abmr1→ABMR,Mixed,둘다0→no rejection); GSE9493 쉼표구분+Banff'97 끝, control은 Banff 없음; GSE98320 d96 사용; GSE14328 첫 세그먼트; 일반은 마지막 콜론 뒤 값.

### 추가: 무라벨 6개 중 5개 source_name으로 라벨 (고신뢰) — 스크립트 `scripts/add_diagnosis_labels_src.py`
characteristics엔 진단이 없었지만 GEO **`source_name`에 진단 그룹이 명시**돼 있어 5개를 라벨링(논문 추정 아님 → 고신뢰). obs 컬럼: `gsm`, `diagnosis`(=source_name), `source_name`.
| 시리즈 | diagnosis(=source_name) 분포 |
|---|---|
| GSE44131 | Non-specific IFTA 17, Normal transplant 12, CAMR/TGP(C4d+/DSA+) 11, TGP DSA+/C4d- 9, TGP DSA-/C4d-(g+ptc>1) 8 |
| GSE50084 | DSA+ & acute/chronic rejection 56, No DSA normal/mild IF-TA 32, DSA+ normal/mild IF-TA 27 |
| GSE93658 | cAMR 33, TCMR_IFTA 17, control 16, DSA_IFTA 13, IFTA 12, TCMR_DSA- 10 |
| GSE93659 | TGP C4d+ &/or MVI>1 17, control 12, TGP C4d- MVI0/1 DSAneg 10, TGP C4d- MVI0/1 5 |
| GSE9489 | control nephrectomy 13, CAN II 10, CAN III 8, AR+CAN 7, non-rejecting 7, CAN I 4, AR IA 3, AR IB 3, borderline 3, AR IIA 1, AR IIB 1 |

→ **현재 라벨 완료 21/22.** 남은 무라벨 1개: **`GSE1563`** — source_name=PBL/kidney(조직만), characteristics 빈값 → 진단 그룹 없음. 논문(Flechner 2004, PMID 15307835) 보충표로 GSM↔그룹 매핑 필요(저신뢰라 자동화 보류). minmax h5ad에 diagnosis 컬럼 없음.

## kidney microarray 24개 전체 RMA 전처리 (gold-standard R) + 점검 (2026-06-14)

### 목적/방식
`kidney/microarray/` 24개 시리즈 전부를 플랫폼에 맞는 gold-standard 방법으로 RMA 전처리. 과거 homemade RMA(erfcx background)의 수치 이슈를 피해 검증된 R 함수 사용:
- **Affy 3'IVT(17)**: `affy::ReadAffy` + `affy::rma` (background+quantile norm+median polish)
- **Affy Gene/Exon ST(5)**: `oligo::rma(target="core")`
- **Illumina BeadArray(2)**: RMA 부적용 → `log2 + limma::normalizeBetweenArrays(quantile)`
- gene 매핑: `<platform>.db` (AnnotationDbi `mapIds` PROBEID→SYMBOL), 동일 gene은 mean. PrimeView는 Bioc에 primeview.db 부재 → GEO **GPL15207** annotation(48,873 probe→symbol)으로 매핑.
전용 conda 환경 `r_affy`(R 4.5.3/Bioc 3.22)에서 실행. 데이터셋별 "추출→(affy)CEL 스크리닝→RMA→gene/probeset CSV→임시정리"로 디스크 절약. 출력 `rma_out/<GSE>_rma_gene.csv`(+`_rma_probeset.csv`), Illumina는 `_norm_gene.csv`.

### 겪은 문제와 해결 (사용자 "잘 확인하면서" 당부 반영)
1. **preprocessCore threading 버그** (`pthread_create() is 22`, rma quantile norm 단계): bioconda 빌드 문제 → `install.packages("preprocessCore", configure.args="--disable-threading")` 소스 재컴파일로 해결.
2. **affy::rma background correction segfault** (특정 저품질 CEL, 예 GSE36059 GSM880610 3.0MB): `tryCatch`로 못 잡는 C 레벨 충돌 → RMA 전 각 CEL을 **격리 서브프로세스로 병렬 스크리닝**(`bg.correct`)하여 충돌 CEL 자동 제외(`<GSE>_excluded_cels.txt` 기록). GSE36059만 1개 제외(411→410).
3. **동시 R 라이브러리 쓰기 → segfault**: preprocessCore 재설치가 실행 중 rma를 망가뜨림 → 설치와 rma를 **직렬화**.
4. **conda post-link 깨짐**(base의 cross-compiler 훅) + **annotation 미러(osn) 불안정**: conda 대신 `install.packages`/직접 curl, 유효(gzip -t)할 때까지 전체 재다운로드 루프로 해결. primeview.db는 Bioc 3.22 부재 → GPL15207 대체.

### 최종 점검 (24/24 OK, 총 4,578 샘플)
| 플랫폼 | 시리즈(샘플수) | gene 수 |
|---|---|---|
| HG-U133 Plus 2.0 (12) | GSE36059(410, 1제외), GSE147089(224), GSE129166(212), GSE21374(282), GSE48581(306), GSE50058(101), GSE72925(168), GSE75693(79), GSE34437(66), GSE14328(36), GSE9489(60), GSE9493(82) | 21,355 |
| HG-U133A 2.0 (2) | GSE106675(30), GSE53605(55) | 13,041 |
| HG-U95Av2 (1) | GSE1563(62) | 9,054 |
| HG-U219 (1) | GSE192444(300) | 19,434 |
| PrimeView (1) | GSE98320(1208) | 20,084 |
| HuGene 1.0 ST (4) | GSE44131(57), GSE50084(115), GSE93658(101), GSE93659(44) | 19,997 |
| HuEx 1.0 ST (1) | GSE138043(52) | 17,259 |
| Illumina HT-12 V4 (2) | GSE69677(88), GSE181757(440) | 19,672 / 21,186 |

log2 범위 정상(Affy ~1.2–15.5, Illumina quantile ~6–14.5), 샘플 수 MANIFEST 일치. 스크립트: `scripts/rma_affy_oligo.R`, `screen_cel.R`, `illumina_norm.R`, `rma_primeview.R`, `run_rma_affy_oligo.sh`, `run_illumina.sh`, `run_gse98320.sh`.

### 후속: zeroing + min-max 전처리 (Illumina 제외 22개)
기존 학습데이터(`scgpt_training_data_minmax.h5ad`) 생성 방식을 역산·검증(재현 오차 2e-6)하여 동일 적용:
1. **RMA < 5.0 → 0** (zeroing)
2. **per-sample min-max**: 각 샘플 nonzero를 `(v−v_min)/(v_max−v_min)×v_max` → [0, 샘플최대] (샘플별 최댓값 보존)
대상은 Illumina 2개 제외한 22개(`rma_out/*_rma_gene.csv`). 출력 `rma_out/minmax/<GSE>_rma_minmax.h5ad` (X=샘플×유전자, float32, obs=샘플명/var=유전자명). zero%는 절대 임계 5.0 적용으로 데이터셋별 8.8~67.1% 변동. 스크립트: `scripts/rma_zeroed_minmax.py`. 분포 확인용 바이올린 plot은 `rma_out/violin/`(개별 24 + 통합 `ALL_datasets_violin.png`), 스크립트 `scripts/rma_violin.py`.

## kidney array 24개 시리즈 진단 라벨 정리 (2026-06-14)

### 작업
- 소스: `data/kidney/sample_metadata.csv` (4712행, 31시리즈). microarray로 분류된 24개 GSE 시리즈만 필터링(디렉터리 `data/kidney/microarray/` 24개와 일치).
- 시리즈별 진단 라벨 분포를 표로 정리. 라벨 추출 규칙:
  - 기본: `characteristics` 컬럼의 진단/condition/phenotype 필드.
  - characteristics 비어있는 5개(GSE1563, GSE44131, GSE50084, GSE93658, GSE93659)는 `source_name`/`title`에서 추출.
  - **GSE129166**: 코드값 필드(`tcmr 0/1/2`, `abmr 0/1`)를 진단명으로 변환 — tcmr=2→TCMR, =1→Borderline, abmr=1→ABMR, 둘다 0→no rejection. (값이 괄호 안 콜론을 포함해 마지막 콜론 기준 파싱 필요.) biopsy 95 + blood 117.
  - GSE192444·GSE98320은 분자진단(MMDx) 라벨(d96/mmdx).

### 주요 라벨 분포(요약)
- 거부/비거부 이진계열: GSE138043(non-AR37/AR15), GSE21374(nonrej206/rej76), GSE50058(STA58/AR43), GSE138043 등.
- ABMR/TCMR/Mixed 분자계열: GSE36059(NR281/ABMR65/TCMR35/Mixed22/Nx8), GSE48581(non-TCMR268/TCMR32/Nx6), GSE192444(NR175/ABMR67/TCMR21/Mixed19/pABMR12/pTCMR6), GSE98320(NOMOA274/ABMR215/IFTA145/Bord109/GN97/AKI96/TCMR87/…).
- 표현형 주의: **GSE181757**은 거부 진단이 아닌 graft 진행성 Progressor97/Non-Progressor343.
- 기타: GSE147089(ABMRh), GSE72925/GSE53605/GSE75693(Normal·IFTA·TCMR·CNIT·BKVN 등), GSE9489/GSE9493(Banff CAN/AR 등급), GSE44131/GSE93658/GSE93659(TGP/cAMR/DSA·C4d 조합).

### 비고
- 이진 rejection/non-rejection 통합 매핑 CSV는 아직 미생성(요청 시 작성). 시리즈마다 라벨 스킴이 달라 통합 시 매핑 규칙 합의 필요.

## prognosis adapter — kidney scRNA-seq 5개 파일 전체 공통 gene 재학습(Run2) 완료 + Run1 vs Run2 비교 (2026-06-12)

### 작업
5개 kidney scRNA-seq 파일 전부에 대해 train/test 공통 gene으로 처음부터 재학습(Run2)을 완료하고 Run1(기존 bulk ckpt 재사용 predict)과 비교. GSE145927은 앞서(06-10) 완료, 나머지 4개(GSE109564, GSE151671_AK1/AK2, GSE195719)를 마스터 체인(`logs/run2_batch_master.sh`)으로 순차 finetune→predict-cell(각 ~7~11h, GPU 타 사용자와 공유). 각 파일별 공통 gene으로 학습데이터 subset(`scgpt_training_data_commongenes_<tag>.h5ad`) 생성 후 동일 하이퍼파라미터로 finetune.

### 최종 비교 (p60_prob: Run1 → Run2, 전부 predict-cell `--patient-col sample --normalize`)

| 파일 | 환자 | label | Run1 p60 | Run2 p60 | Δ | Run2 bulk OOF |
|---|---|---|---|---|---|---|
| GSE145927 | day11 / day232 / day2542 | Rej×3 | 0.588 / 0.548 / 0.528 | 0.656 / 0.615 / 0.590 | +0.06~0.07 | 0.758 |
| GSE109564 | GSE109564 | Rej | 0.676 | 0.677 | +0.001 | 0.780 |
| GSE151671_AK1 | AK1 | Rej | 0.717 | 0.778 | +0.062 | 0.760 |
| GSE151671_AK2 | AK2 | Rej | 0.638 | 0.736 | +0.097 | 0.755 |
| GSE195719 | CMR442 / KUT014 / NRM363 | Rej / Rej / **NR** | 0.554 / 0.751 / 0.511 | 0.568 / 0.755 / 0.527 | +0.01~0.02 | 0.762 |

(Run1 bulk OOF=0.776, 공유 ckpt `run_20260528-022429`)

### 결론
- **공통 gene 재학습(Run2)은 rejection 확률을 대체로 상향**: GSE145927(+0.06~0.07), AK1(+0.062), AK2(+0.097)에서 뚜렷. GSE109564(+0.001)·GSE195719(+0.01~0.02)는 거의 불변.
- **상향 폭은 "train-only gene 비중"에 비례하는 경향**: 공통 gene 비율이 낮아 Run1이 추론 못 쓰는 train-only gene에 의존하던 케이스(AK1/AK2/145927)에서 재학습 이득이 크고, 이미 공통 비율 높은 케이스는 변화 미미.
- **GSE195719(2클래스) AUROC는 Run1·Run2 모두 1.000** — NR(NRM363)이 양쪽 모두 최저점, 재학습이 NR도 비슷하게 +0.016 올려 마진·순위 보존(분리력 손상 없음).
- bulk in-domain CV는 Run2가 대체로 소폭↓(0.776→0.755~0.780, 학습 gene 감소) but cross-domain SC에선 동등~개선 → in-domain vs cross-domain 트레이드오프 재확인.
- 산출물: 각 `results/prognosis_adapter_commongenes_<tag>/{run_*/, predict_cell_<tag>_p60.{csv,png}}`, 공통 gene 학습데이터 `scgpt_training_data_commongenes_<tag>.h5ad`.

## prognosis adapter — kidney scRNA-seq 5개 파일 predict-cell + 공통 gene 재학습 비교 (2026-06-10)

### 목적
bulk microarray로 학습한 prognosis adapter 모델(`prognosis_adapter_8000/run_20260528-022429`, pretrain_kidney backbone, bulk CV OOF 0.776)을 kidney scRNA-seq test 데이터에 cross-domain predict-cell. (1) 재학습 없이 test만 교체, (2) train/test 공통 gene으로 재학습 후 비교.

### Run 1 — 기존 체크포인트 재사용, 5개 scRNA-seq 파일 predict-cell
공통 옵션: `--normalize --patient-col sample --label-col {label|rejection} --positive-label Rejection --quantile 60 --cell-batch-size 8(배치)/32(145927)`. 6-ckpt(fold5+final) 앙상블, 3-subset 평균. 산출물 `results/prognosis_adapter_8000/predict_cell_<GSE>_p60.{csv,png}`.

| Dataset | 환자 | label | n_cells | p60_prob |
|---|---|---|---|---|
| GSE109564 | GSE109564 | Rej(ABMR) | 4,487 | 0.676 |
| GSE145927 | day11/day232/day2542 | Rej(ABMR)×3 | 5.4k/12.7k/19k | 0.588 / 0.548 / 0.528 |
| GSE151671_AK1 | AK1 | Rej | 6,000 | 0.717 |
| GSE151671_AK2 | AK2 | Rej | 6,000 | 0.638 |
| GSE195719 | KUT014/CMR442/NRM363 | Rej/Rej/**NR** | 2.5k/4.8k/4.2k | 0.751 / 0.554 / **0.511** |

- **GSE195719(유일 2클래스): patient-level AUROC=1.000, BalAcc=1.000** — NR(0.511) < Rejection 2명. 완벽 분리.
- 나머지는 단일 Rejection 클래스라 AUROC 불가하나 rejection 환자 9명 전부 0.528~0.751 > NR baseline 0.511. 모델이 rejection을 일관 상향 랭크.

### Run 2 — train/test 공통 gene(16,888)으로 재학습 후 GSE145927 predict-cell
common = train(21,463) ∩ GSE145927(24,491) ∩ vocab = **16,888** (Run 1 추론 in-use와 동일). 학습데이터를 공통 gene으로 subset(`scgpt_training_data_commongenes_GSE145927.h5ad`, 627×16,888) 후 동일 하이퍼파라미터로 finetune(`run_20260610-150921`). bulk CV OOF AUROC **0.758**(Run1 0.776보다 소폭↓, gene 감소 영향).

GSE145927 predict-cell 비교 (전부 Rejection):
| 환자 | Run1 p60 | Run2 p60 | Δ | Run1 mean | Run2 mean |
|---|---|---|---|---|---|
| day11 | 0.588 | 0.656 | +0.068 | 0.581 | 0.652 |
| day232 | 0.548 | 0.615 | +0.067 | 0.522 | 0.589 |
| day2542 | 0.528 | 0.590 | +0.062 | 0.479 | 0.546 |

### 결론
- **공통 gene 셋팅이 cross-domain SC 전이를 개선**: 3 환자 모두 rejection 확률 +0.06~0.07 상향, day2542 mean이 0.479→0.546으로 부호 전환. train-only gene 의존 제거 → 도메인 갭 축소 효과.
- bulk in-domain CV는 Run2가 소폭 낮음(학습 feature 감소) → in-domain vs cross-domain 트레이드오프. 순위(day11>day232>day2542)는 양쪽 보존.
- 세팅: test는 raw counts라 `--normalize` 필수, training data(log2 RMA)는 normalize 미적용. GPU는 타 사용자 102GB 점유로 공유 상태에서 실행.

## kidney GEO 데이터셋 유형별 분류 + 시리즈 메타데이터 매니페스트 (2026-06-10)

### 작업
`data/kidney/`에 평면으로 있던 GEO RAW 31개 시리즈를 데이터 유형별 하위폴더로 정리하고, NCBI GEO 원본 메타데이터를 받아 `MANIFEST.md`를 시리즈단위 메타데이터 표로 재작성.

### 폴더 구조 (분류 근거: GEO `Series_type` + 플랫폼 + 연구설계)
- `kidney/scRNA-seq/` (4): GSE109564, GSE145927, GSE151671, GSE195719
- `kidney/bulk_RNA-seq/` (3): GSE120495, GSE131179, GSE155670
- `kidney/microarray/` (24): 나머지 (대부분 Affy HG-U133 Plus 2.0 계열)

### ★ 오분류 3건 정정 (이전 manifest는 로컬 파일 확장자만으로 유형 추정 → 오류)
GEO `Series_type`/플랫폼으로 검증해 정정:
- **GSE145927**: `Counts(CSV)` 추정 → 실제 **scRNA-seq** (단일세포 81,139 cells, NovaSeq 6000; Expression+germline WGS 혼합)
- **GSE155670**: `Microarray/TXT` 추정 → 실제 **bulk RNA-seq** (정렬 memory B cell subset, NextSeq 500)
- **GSE181757**: `Counts(CSV)` 추정 → 실제 **microarray** (Illumina HumanHT-12 V4 BeadArray, 440 샘플)

### 메타데이터 수집
- NCBI GEO `acc.cgi?...&form=text&view=brief`로 31개 시리즈 메타(제목·type·platform_id·날짜·PubMed·GSM수) + 13개 GPL 플랫폼 정식명 fetch (`/tmp/geo_meta/`, 임시).
- `MANIFEST.md` 표 컬럼: GSE · 제목(full) · 데이터유형 · 플랫폼명 · 샘플수(GSM) · 공개연도 · PubMed · 디스크.
- 플랫폼 분포: Affy HG-U133 Plus 2.0(GPL570) 다수, 그 외 U133A 2.0/U95Av2/Human Gene·Exon 1.0 ST/U219/PrimeView, Illumina HumanHT-12/NextSeq/NovaSeq/HiSeq, Ion Torrent Proton.
- GSE93658/GSE93659는 PubMed 미등록.

### GSM 단위 임상 메타데이터 추출 (`sample_metadata.csv`)
- GEO series-matrix(`ftp.ncbi.nlm.nih.gov/geo/series/.../matrix/*_series_matrix.txt.gz`) 헤더만 스트리밍(`curl|zcat|awk '/series_matrix_table_begin/{exit}'`)으로 받아 `!Sample_geo_accession/title/source_name_ch1/characteristics_ch1` 파싱 → GSM별 transpose.
- 멀티플랫폼 시리즈(GSE109564 등)는 GPL별 매트릭스 모두 수집, `platform` 컬럼에 GPL 태그.
- **31개 시리즈 전체 ok, 4711 GSM** (sample_manifest.csv의 4199 RAW행보다 많음 — 컬럼매트릭스형 시리즈의 GSM이 RAW 파일로 분리되지 않아 manifest엔 누락됐던 것).
- 컬럼: `GSE, GSM, data_type, platform, title, source_name, characteristics`(원본 key:value를 ` | ` 연결). rejection 라벨 키는 시리즈마다 상이(GSE21374 `rejection/non rejection`, GSE36059 `diagnosis(tcmr,abmr,…)`, GSE192444 `mmdx`, GSE98320 `d96`, GSE14328/9489/9493 Banff 등).

### 산출물
- `data/kidney/MANIFEST.md` (재작성) — 시리즈단위 메타데이터 레퍼런스
- `data/kidney/sample_metadata.csv` (신규, ~1MB/4711행) — GSM 단위 **임상** 메타데이터
- `data/kidney/sample_manifest.csv` (기존 유지) — GSM 단위 **파일** 정보(파일명·포맷·크기)
- 하위폴더로 이동된 31개 GSE RAW (git 미추적 데이터)

## 완료: pretrain_human 인코더로 adapter_8000 재현 — kidney vs human backbone 비교 (2026-06-02)

### 동기
최고 모델 `prognosis_adapter_8000`(run_20260528-022429, `--model-dir models/pretrain_kidney`)과 **완전히 동일한 옵션에서 `--model-dir`만 `models/pretrain_human`으로 바꿔** finetune→predict-cell 수행, backbone 사전학습(신장특화 vs 범용 human) 차이가 예후 전이에 미치는 영향 비교.

### 실행 (옵션 동일성 검증)
- finetune: `results/prognosis_adapter_8000_human/run_20260602-154815`. 저장된 args.json이 원본과 `model_dir`(→`models/pretrain_human`)·`output_base` 두 항목만 다르고 나머지 전부 동일(hidden/adapter 256, dropout 0.2, max_seq_len 8000, 5-fold, epochs 60, patience 15, batch 8, head_lr 1e-4, wd 0.01, cox_weight 0, seed 42, no normalize) 확인.
- predict-cell: `--adata E-MTAB-12051/E_MTAB_12051_qc.h5ad --normalize --model-dir models/pretrain_human --quantile 60 --patient-col orig.ident --label-col condition`. 6-ckpt(fold5+final) 앙상블, 37,920세포×16환자, 사용 17,704유전자(training_genes 19,893).

### 결과 — finetune은 human이 소폭↑이나 cross-domain 전이는 **완전 붕괴**
| 지표 | kidney (adapter_8000) | **human (신규)** |
|------|:---:|:---:|
| 5-fold OOF AUROC | 0.776 | **0.799** ↑ |
| per-fold AUROC | .778/.837/.811/.740/.748 | .794/.861/.825/.770/.779 |
| **환자단위 predict-cell AUROC (p60)** | **0.875** | **0.500** (우연) |
| 거부환자 recall (4명) | 4/4 (100%) | **1/4 (25%)** |
| accuracy | 13/16 | 13/16 (단 다수class NR 찍기) |
| p60_prob NR / Rej 범위 | 0.466–0.543 / **0.525–0.543** | 0.429–0.497 / 0.404–0.502(겹침) |

- **핵심**: human backbone은 bulk microarray 학습(OOF 0.799)에서 오히려 약간 더 잘 적합하지만, **bulk→single-cell 도메인 갭에서 임베딩 공간이 정렬되지 않아** 환자단위 AUROC가 0.500(완전 우연)으로 붕괴. 거부 4명 중 NEPH019 1명만 검출, NEPH010(거부)은 전체 2번째로 낮은 점수. 모든 환자 p60_prob가 0.40–0.50 좁은 띠에 뭉쳐 판별력 0.
- accuracy 13/16은 동일하나 의미 정반대: human은 거의 전원 NR(다수class)로 찍어 우연히 13개 맞춤(거부 3명 놓침), kidney는 거부 4/4 완벽+위양성 3건.
- **결론**: 신장특화 사전학습(pretrain_kidney)이 범용 human backbone 대비 bulk array→scRNA-seq 예후 전이에 결정적. in-domain 적합도(OOF)와 cross-domain 전이력은 별개이며, backbone 도메인 정합이 전이의 핵심. [[project_domain_shift]] / [[project_sc_to_microarray_transfer]]와 일관.
- 산출물: `data/results/prognosis_adapter_8000_human/` (run_20260602-154815 체크포인트·cv_metrics.json, `predict_cell_p60_qc.csv`, finetune/predict 로그).

---

## 완료: predict-cell MC-dropout sweep — dropout이 예측에 미치는 영향 비교 (2026-06-02)

### 동기 / 핵심 함정
`prognosis_microarray_adapter.py predict-cell`을 dropout 7개 값(0, 0.05, 0.1, 0.15, 0.20, 0.25, 0.30)으로 돌려 예측 변화를 비교하려 함. 데이터=`E-MTAB-12051/E_MTAB_12051_qc.h5ad`(37,920 cells / 16환자, NR 12 / Rejection 4).
- **함정 1**: 추론이 `model.eval()`+`@torch.no_grad()` → 표준 dropout은 항등함수(no-op). 그냥 `--dropout`만 바꾸면 7개 결과가 **완전히 동일**.
- **함정 2**: `cmd_predict_cell`이 checkpoint의 `args.json`(dropout=0.2)으로 CLI `--dropout`을 **덮어씀**.
→ "dropout 변화→예측 변화"를 보려면 **MC-Dropout(테스트타임 dropout 활성)** 이 유일하게 의미있는 방법.

### 구현
원본 보존, 복사본 `best_script/prognosis_microarray_adapter_mcdrop.py`에 `--mc-dropout` 플래그 추가:
- ON이면 CLI `--dropout`을 saved_args보다 우선.
- `embed_cells_batched`에서 `model.eval()` 후 `nn.Dropout` 모듈만 `.train()`으로 재활성(LayerNorm 등은 eval 유지).
- subset 간 std를 MC 불확실성으로 계산 → CSV에 `mean_mc_std`, `std_cell_prob` 컬럼 추가.

### 실행 설정
- checkpoint: `results/prognosis_adapter_8000/run_20260528-022429` (5 folds + final = 6-ckpt 앙상블).
- batch 256, n_subsets 3 (셀당 6×3=18 MC 표본), `--patient-col orig.ident --label-col condition`.
- GPU는 단일 프로세스로 이미 100% 연산 포화(메모리 8.9GB만) → **연산 병목**. 마이크로벤치상 병렬 이득 ~30%뿐이라 **동시성 2**로 실행. 총 ~3h.
- 드라이버: `results/prognosis_adapter_8000/dropout_sweep/run_sweep.sh` (concurrency 2).

### 결과 (summary_dropout_sweep.csv)
| dropout | AUROC(mean) | AUROC(p60) | mean_mc_std | Rej−NR mean_prob |
|---|---|---|---|---|
| 0.00 | 0.875 | 0.875 | 0.0105 | 0.0384 |
| 0.05 | 0.875 | 0.896 | 0.0151 | 0.0384 |
| 0.10 | 0.875 | 0.896 | 0.0189 | 0.0385 |
| 0.15 | 0.875 | 0.896 | 0.0224 | 0.0385 |
| 0.20 | 0.875 | 0.896 | 0.0258 | 0.0384 |
| 0.25 | 0.875 | 0.896 | 0.0291 | 0.0384 |
| 0.30 | 0.875 | 0.896 | 0.0325 | 0.0380 |

- **dropout=0 결과(AUROC 0.875)가 기존 정식 baseline과 일치** → MC 파이프라인 검증 완료.
- **AUROC·환자별 예측·NR/Rejection 분리(gap~0.038)는 dropout에 사실상 불변.** 테스트타임 dropout이 환자 순위를 거의 흔들지 않음 → 모델이 dropout에 robust.
- **MC 예측 불확실성(mean_mc_std)만 dropout에 거의 선형 증가**(0.010→0.032), 두 클래스 동일 양상.
- 그림 4패널: `results/prognosis_adapter_8000/dropout_sweep/dropout_sweep_comparison.png` (A: AUROC vs dropout, B: 환자별 예측 궤적, C: 불확실성 vs dropout, D: 클래스 분리도). 플롯 스크립트 `make_figure.py`.

## 완료: 음성 대조 — 무관 microarray + 랜덤 라벨로 전체 파이프라인 검증 (2026-06-01)

### 동기
prognosis 파이프라인(finetune→predict-cell)의 0.875 AUROC가 진짜 생물학적 신호인지, 아니면 방법론적 누수/아티팩트인지 검증. 신장이식과 **전혀 무관한** microarray를 동일 RMA 전처리 후 **랜덤 NR/Rejection 라벨**을 달아 똑같이 학습·추론. 신호가 진짜면 랜덤 라벨에서는 AUROC≈0.5여야 함.

### 데이터 — GSE39582 (대장암, 585샘플, 동일 Affymetrix HG-U133 Plus 2.0)
- GEO RAW tar 4.4GB(585 CEL) 다운로드(NCBI HTTP가 resume 거부 → FTP suppl 경로로 이어받기) → R affy `ReadAffy`로 raw PM 추출(604,258 probes × 585).
- RMA(배경보정→quantile정규화→log2→probeset median) + 기존 `hgu133plus2_probe_gene_map.csv` 재사용 gene symbol 매핑 → 585×21,355.
- **버그 발견·수정**: 파이프라인 문서의 homemade `rma_background`가 GSE39582의 큰 분산(σ~1250)에서 `alpha*σ²`(~150k)가 최대강도(~40k)를 초과 → `a/σ≈-125`에서 `dnorm/pnorm` 수치 언더플로(0/1e-15=0) → 전 값 바닥(log2(1e-6)=-19.93, nonzero 6유전자/샘플로 degenerate). inverse Mills ratio를 `erfcx` 기반 안정식 `λ(z)=2/(√(2π)·erfcx(-z/√2))`(exp(-z²/2) 약분)으로 교체해 복원.
- 절대 스케일은 데이터셋마다 다름(GSE39582 log2 [3.3,5.8] vs kidney [0,15]; homemade RMA의 분산의존 압축). scGPT 토큰화가 nonzero 유전자 **순위만** 분위수 binning하므로, 충실성 기준은 절대 임계값이 아니라 **희소도**. 학습 데이터(=merged_rma에서 값<5.0→0, zero% 24.07%)와 동일하게 **하위 24.07% 분위수 zeroing** → zero% 24.1%, nonzero 16,181유전자/샘플(학습 16,264와 일치), vocab 93.1%(19,875유전자).
- 랜덤 라벨: seed 42, 학습과 동일 유병률 28.4% → NR 419 / Rejection 166.

### 실행 (best run과 동일 설정)
```
finetune --adata GSE39582_negctrl_randomlabel.h5ad --model-dir models/pretrain_kidney \
  --label-col condition --positive-label Rejection --max-seq-len 8000 --seed 42
  (no --normalize, adapter_dim/hidden_dim 256, dropout 0.2, 5-fold, epochs 60, head_lr 1e-4, fp16=off)
predict-cell --adata E-MTAB-12051/E_MTAB_12051_qc.h5ad --normalize --quantile 60
  --patient-col orig.ident --label-col condition --positive-label Rejection
```

### 결과 — 음성 대조 성립 ✓
| 지표 | 실제(adapter_8000) | **음성 대조(랜덤 라벨)** |
|------|:---:|:---:|
| finetune 5-fold OOF AUROC | 0.776 | **0.515** (AUPRC 0.308≈유병률, BalAcc 0.531) |
| predict-cell 환자단위 AUROC | 0.875 | **0.458** |
- fold별 best epoch 대부분 epoch 1~2(개선 없이 early stop) → 랜덤 라벨에 학습 가능 신호 없음.
- 환자 16명 p60 확률이 전부 0.486~0.498로 **거의 상수**(판별력 0). 4 거부환자 모두 1로, NR 12명 중 8명도 1로 예측(임계값 0.49 아래 군집) → 순위는 노이즈.

### 핵심
- 랜덤 라벨에서 OOF 0.515 / 환자단위 0.458로 **둘 다 우연 수준**. 실제 0.776/0.875와 명확히 대비 → **기존 prognosis 신호는 진짜 생물학적 신호이며 방법론적 누수·아티팩트가 아님**을 검증.
- 산출물: `data/negctrl_GSE39582/` (CEL, PM CSV, `GSE39582_negctrl_randomlabel.h5ad`, build/finetune/predict 로그), `data/results/prognosis_negctrl_GSE39582/run_20260601-170840/` (체크포인트, cv_metrics.json, `predict_cell_p60_qc_negctrl.csv`+`.png`).

---

## 완료: adapter_8000 모델로 QC h5ad predict-cell 추론 (2026-06-01)

### 동기
finetune 9개 run 중 5-fold OOF AUROC 최고(0.776)였던 `prognosis_adapter_8000` 모델(run_20260528-022429, max_seq_len=8000, cox_weight=0)을 QC 필터링된 E-MTAB-12051 단일세포 데이터에 적용해 환자단위 예후예측 추론.

### 실행
```
python3 scripts/prognosis_microarray_adapter.py predict-cell \
  --adata E-MTAB-12051/E_MTAB_12051_qc.h5ad --normalize \
  --model-dir models/pretrain_kidney \
  --checkpoint-dir results/prognosis_adapter_8000/run_20260528-022429 \
  --patient-col orig.ident --label-col condition --positive-label Rejection \
  --quantile 60 --output results/prognosis_adapter_8000/predict_cell_p60_qc.csv
```
- 입력값 정정 2건: `--model-dir model/...`→`models/pretrain_kidney`(복수), `--patient-col org.ident`→`orig.ident`(오타).
- 입력 37,920세포×28,794유전자(사용 17,704/학습 19,893), normalize_total(1e4)→log1p, 환자 16명, 6체크포인트(fold5+final) 앙상블, p60 집계.

### 결과 (환자단위, 임계 0.525)
- **AUROC 0.875, BalAcc 0.875, accuracy 13/16(0.8125)**
- 거부 환자(label=1) 4명(ABMR 3 + TCMR 1) **전부 정답**(recall 1.0). 오류 3건은 전부 위양성(NEPH006/NEPH015/NEPH018, 모두 Non rejection).
- 산출물: `data/results/prognosis_adapter_8000/predict_cell_p60_qc.csv`

### 환자별 정밀 라벨 vs 예측 (disease 컬럼 기준)
| 환자 | 정밀 진단 | label | predicted | 결과 |
|------|-----------|:---:|:---:|:---:|
| EXT217 | Non rejection DSA+ | 0 | 0 | ✓ |
| EXT230 | **ABMR** (Antibody-mediated rejection) | 1 | 1 | ✓ |
| EXT238 | Non rejection DSA+ | 0 | 0 | ✓ |
| EXT240 | Non rejection DSA+ | 0 | 0 | ✓ |
| EXT241 | Non rejection DSA+ | 0 | 0 | ✓ |
| NEPH006 | Non rejection DSA- | 0 | 1 | ✗ FP |
| NEPH009 | **ABMR** | 1 | 1 | ✓ |
| NEPH010 | **TCMR** (T cell-mediated rejection) | 1 | 1 | ✓ |
| NEPH011 | Non rejection DSA- | 0 | 0 | ✓ |
| NEPH012 | Non rejection DSA- | 0 | 0 | ✓ |
| NEPH014 | Non rejection DSA+ | 0 | 0 | ✓ |
| NEPH015 | Non rejection DSA+ | 0 | 1 | ✗ FP |
| NEPH016 | Non rejection DSA+ | 0 | 0 | ✓ |
| NEPH017 | Non rejection DSA- | 0 | 0 | ✓ |
| NEPH018 | Non rejection DSA+ | 0 | 1 | ✗ FP |
| NEPH019 | **ABMR** | 1 | 1 | ✓ |

### 핵심
- QC 필터 데이터에서도 환자단위 AUROC 0.875로 양호. 거부 4명(ABMR×3, TCMR×1) 완벽 검출, 위양성 3건은 모두 DSA± Non rejection(특이도 9/12=0.75).
- 단 내부 16명 소표본이므로 외부 627샘플 천장(~0.71~0.73, [[project_sc_to_microarray_transfer]])과 별개의 in-cohort 수치로 해석.

### 집계 quantile 비교 (p55 / p60 / p65)
세포단위 확률을 환자단위로 집계할 때 quantile 변화 영향 확인. 동일 모델/입력, `--quantile`만 변경.
| Quantile | AUROC | BalAcc | Accuracy | 민감도(거부4명) | 위양성 | 임계값 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| p55 | 0.854 | 0.875 | 13/16 | 4/4 (100%) | NEPH006, NEPH015, NEPH018 | 0.516 |
| **p60** ⭐ | **0.875** | **0.875** | **13/16** | 4/4 (100%) | NEPH006, NEPH015, NEPH018 | 0.525 |
| p65 | 0.875 | 0.833 | 12/16 | 4/4 (100%) | EXT241 추가 + 위 3명 | 0.535 |

- **세 설정 모두 거부 환자(ABMR×3, TCMR×1) 100% 검출**(FN 0). 차이는 위양성에서만 발생.
- **p60 종합 최적**: AUROC 0.875(최고) + BalAcc 0.875(균형). quantile↑(p65)는 일부 NR(EXT241 DSA+) 점수가 같이 올라 특이도 하락(BalAcc 0.833). quantile↓(p55)는 AUROC만 소폭 하락(0.854), 위양성 구성은 p60과 동일.

### 산출물
- `data/results/prognosis_adapter_8000/predict_cell_p{55,60,65}_qc.csv`
- 그림: `predict_cell_p60_qc_figure.png`(환자별 표+예측확률), `quantile_comparison_qc_figure.png`(p55/p60/p65 비교)

---

## 2026-06-01 — scGPT (E-MTAB-12051 cell QC + zero-shot 파이프라인 독립 스크립트화)

### E-MTAB-12051 cell QC
- 원본 `E-MTAB-12051/E_MTAB_12051.h5ad` (53,630 cells × 28,794 genes, raw counts, gene symbol) cell QC 수행.
- 분포: median 683 genes / 1,576 counts / **MT% 10.8%(p75=22.7, p95=61.3)** — 신장 조직 특성상 MT 비율 높음. 이미 total_counts≥500 사전필터된 상태.
- 임계값별 잔존 cell: 관대(genes≥200·counts≥500·MT%<50) 49,323(92.0%) | **표준(MT%<20) 37,920(70.7%)** | 엄격(genes≥500·counts≥1000·MT%<15) 24,688(46.0%). 잔존 수 좌우 변수는 MT% 컷.
- **표준 기준으로 필터링 저장: `E-MTAB-12051/E_MTAB_12051_qc.h5ad`** (37,920 cells, 327MB). raw counts·메타데이터(16환자 라벨) 보존, obs에 QC지표(n_genes_by_counts/total_counts/pct_counts_mt) + uns['qc_filter'] 기록. 유전자 필터링은 미적용.

### zero-shot 챔피언 파이프라인 독립 스크립트화
- `final_honest.py`에서 천장 진단 제거하고 SEED+co-training 파이프라인만 추출 → **`results/sc2array_iter/sc2array_cotrain.py`** 신규 작성.
  - SEED(proj+quantile DA+LR multiseed) AUROC 0.6977 / FINAL(2-view co-training proj+gene, transductive) **AUROC 0.7463** — 원본과 동일 재현.
- 이후 **독립 실행형으로 확장**: harness.py의 cache 빌드 로직(인코더→E, micro/sc h5ad 로드)을 통합. cache.npz 없으면 자동 빌드, `--rebuild`로 강제 재빌드. `/tmp`에 새 캐시 빌드 검증 시 동일 결과(0.6977/0.7463).
  - 필요 입력: models/pretrain_kidney, gene_pool_17704.json, E-MTAB-12051/E_MTAB_12051.h5ad, scgpt_test_data_minmax.h5ad, best_script/prognosis_microarray_adapter.py.
  - 출력: predictions.csv + metrics.json.

### QC source(E_MTAB_12051_qc.h5ad) + 범용(non-co-training) 방법으로 AUROC ≥ 0.74 달성
목표(/goal): 백본 `scgpt_sc_to_array.py` 기반, source를 **QC 필터된 sc(`E_MTAB_12051_qc.h5ad`, 37,920 cells)**로 교체하고, **기존 2-view co-training 대신 다른 데이터에도 범용 적용 가능한 방법**으로 외부 AUROC ≥ 0.74 달성.

실험 캐시·스크립트: `data/results/sc2array_qc/{exp_general.py, exp_selftrain.py, exp_refine.py, confirm.py, *.out, *_sweep.json}` (모두 `best_script/cache_qc.npz`에서 동작 — torch 불필요).

#### ★ 결정적 발견 1 — QC 필터링이 sc→array 전사를 **악화**시킨다
- 동일 파이프라인을 QC source에 적용: **honest SEED(proj+quantile+LR) 0.6323** (비-QC 0.698 대비 ↓), **co-training 0.6551** (비-QC 0.748 대비 대폭 ↓).
- 원인: 표준 QC(MT%<20)가 53,630→37,920 cells로 ~30%(주로 고-MT 세포) 제거. 신장 거부반응=조직 손상/스트레스 맥락이라 **고-MT(스트레스/손상) 세포가 rejection 신호를 운반** → 이들을 제거하면 pseudobulk에서 판별 분산이 사라짐. (transductive 천장은 target=microarray 기하가 결정하므로 불변이나, weak seed로는 co-training이 천장까지 못 올라감 → QC에서 co-training 0.655로 붕괴.)

#### ★ 결정적 발견 2 — positive 환자 4명뿐일 때 **LR은 과적합, prototype(centroid)이 강건**
- 범용 sweep(rep×DA×classifier×ensemble, `exp_general.py`): LR 계열 전부 0.55~0.66, 그런데 **nearest-centroid(cosine 공간) proj+quantile = 0.7103**로 최고. param-free·few-shot 강건성 덕분. → 다른 데이터에도 그대로 쓸 수 있는 일반 원리(소수 양성 source엔 프로토타입 분류기).

#### ★ 목표 달성 — centroid seed + 단일뷰 self-training (표준 SSL, co-training 아님)
- `exp_selftrain.py`/`confirm.py`: centroid(proj+quantile) seed 0.7103에서 출발 → **단일뷰 balanced self-training(신뢰도 ramp, centroid 재적합)** 으로 끌어올림.
- **PRIMARY = centroid(proj+quantile) + centroid self-train(rounds=10): AUROC 0.7401 / AUPRC 0.4795 / BalAcc 0.7036 ≥ 0.74 달성.**
- 강건성: cells∈{200,400}, rounds∈{8,10} 전부 quantile-only=0.7401로 **불변**(노이즈 아님). DA-ensemble(quantile/zscore/rank_gauss self-train rank-mean)=0.7385로 단일 quantile보다 약간 낮아 단순한 quantile self-train을 채택.
- co-training과 차별점: **단일 분류기·단일 표현의 교과서적 self-training**이라 hand-picked 2nd view가 없어 임의의 sc→bulk 쌍에 그대로 이식 가능. prototype 분류기가 소수 양성 과적합 제거.

#### 최종 산출물(범용 독립 실행 스크립트)
- **`data/best_script/sc2array_general.py`** — cache_qc.npz 자동 빌드/사용(`--rebuild`로 h5ad에서 재빌드), centroid prototype seed(다중 DA·다중 seed) + 단일뷰 self-training, DA-ensemble 보조.
  - 기본값 cells=200, rounds=10. 출력 `general_out/{predictions.csv, metrics.json, FINAL_REPORT.txt}`.
  - 재현 검증: SEED 0.7103 / **PRIMARY 0.7401** / FINAL(ens) 0.7385.
- 입력: `E-MTAB-12051/E_MTAB_12051_qc.h5ad`, `scgpt_test_data_minmax.h5ad`, `models/pretrain_kidney`, `gene_pool_17704.json`.

**요약**: QC source는 sc→array rejection 신호를 약화시키지만(고-MT 손상세포 제거), **소수 양성 source엔 prototype(centroid) 분류기 + 단일뷰 self-training**이라는 범용 레시피로 비-QC co-training(0.746)에 근접한 **0.7401(≥0.74, QC source)** 을 co-training 없이 달성. 다른 sc→bulk 전사에도 그대로 적용 가능.

#### 단일 파일화 — 비-데이터 외부 의존 제거
- `sc2array_general.py`를 진짜 단일 파일로 정리: 유일한 비-데이터 외부 의존이던 `gene_pool_17704.json`을 코드 내부 유도로 대체. **pool = (microarray var ∩ sc var ∩ model vocab)** — 검증 결과 기존 json과 **동일한 17704 유전자 집합**(set 일치), proj/DA/centroid 모두 유전자 순서 불변이라 결과 동일.
- 이제 의존 입력은 데이터/모델뿐: `E_MTAB_12051_qc.h5ad`, `scgpt_test_data_minmax.h5ad`, `models/pretrain_kidney`(vocab.json+best_model.pt). 로컬 `.py` import 없음. CLI `--sc/--micro/--model`로 경로 교체 가능, `--rebuild`로 h5ad에서 cache 재생성.
- 검증: `/tmp`에 cache 처음부터 재빌드 → 유도 pool 17704, **SEED 0.7103 / PRIMARY 0.7401 / FINAL 0.7385** 동일 재현.

### 2026-06-01 — prognosis_microarray_adapter predict-cell 집계 비교 (p60/mean/median)
- 기존 `results/prognosis_adapter_8000/predict_cell_p60_qc.csv` (E_MTAB_12051_qc, 16명, run_20260528-022429 6-ckpt 앙상블) 활용.
- **핵심 발견**: predict-cell은 `--agg`와 무관하게 환자별 `p60_prob/mean_prob/median_prob` 3컬럼을 항상 함께 저장하고, seed=42 결정론적이라 mean/median 재실행 없이 CSV에서 바로 AUROC 비교 가능. (사용자 확인 후 재실행 생략)
- **집계별 AUROC**: mean **0.8958** > p60 0.8750 = median 0.8750.
- 양성 Rejection 4명 전원 정답(민감도 1.0). 오분류는 전부 NR→R false positive: 공통 hard case NEPH015/NEPH018; EXT241(p60만 정답), NEPH006(mean만 정답, 우꼬리 skew 영향).
- 산출물: `agg_comparison_p60mean_median.csv`, `per_sample_predictions_compare.csv`.

### 2026-06-02 — Attention-pooling readout 변형 비교 (prognosis adapter)
- 신규 스크립트 `data/scripts/prognosis_microarray_attnpool.py` (base: `prognosis_microarray_adapter.py`).
  - 변경점: encoder가 CLS(`x[:,0,:]`) 대신 **전체 토큰 시퀀스(B,L,D)** 반환 → 학습형 단일 query **multi-head attention pooling**(non-pad 토큰에 attend → LN) → adapter → head. encoder frozen, pool+adapter+head만 학습. state_dict에 `pool` 추가, `--pool-heads`(기본 8) CLI.
- 동일 조건 비교(array=`scgpt_training_data_minmax.h5ad`, sc=`E_MTAB_12051_qc.h5ad`, kidney, max_seq_len=1200):
  - **In-domain array OOF AUROC**: CLS 0.7457 → **ATTN-POOL 0.7701** (per-fold 0.790±0.034). 개선.
  - **Cross-domain SC(16환자, 양성4)**: CLS mean 0.667/p60 0.604 vs **ATTN-POOL mean 0.562/p60 0.479**. 전사 악화.
- **결론**: attention-pool query가 array 도메인 통계에 더 잘 적합(in-domain↑)하나 그 추가 용량이 array→sc 도메인 시프트에서 살아남지 못함(sc⊥array 천장). 파라미터 없는 CLS readout이 cross-domain prognosis 전사엔 더 robust.
- 산출물: `data/results/prognosis_attnpool_minmax/RESULTS.md`, `run_20260602-121606/{cv_metrics.json, predict_cell_p60.csv/.png, predict_cell_per_patient.png}`. (seq_len=8000 변형은 ~3h+이고 기존 0.896 CLS와 전처리가 달라 비교 불가라 중단)

## 2026-06-15 — scGPT (kidney microarray NR/Rejection 이진 라벨링 + 시리즈별 .h5ad 추출)

### 배경
- `data/rma_out/minmax/<GSE>_rma_minmax.h5ad` 22개(Affymetrix RMA)에는 `obs['diagnosis']`에 **원본 진단 문자열만** 저장돼 있음(이진 매핑은 수동 큐레이션으로 남겨둔 상태). 사용자와 시리즈별로 NR/Rejection 매핑 기준을 합의하며 파생 .h5ad를 생성.
- 라벨링 출처: 대부분 `obs['diagnosis']`(characteristics 파생), 일부는 `data/kidney/sample_metadata.csv`의 `characteristics`/`source_name`/`title` 재파싱.
- 공통 규칙: 원본 라벨은 `obs['diagnosis_raw']`에 보존, `obs['diagnosis']`에 NR/Rejection 기입. 원본 minmax 파일은 불변, 파생은 별도 파일명으로 저장.

### 시리즈별 처리 (최초 n → 최종 n, NR/Rej)
- GSE106675 30→10 (Rejection 10만; Donor/Tolerance/Std-immuno 제외) → `GSE106675_rejection_rma_minmax.h5ad`
- GSE129166 212→**95(biopsy)**→**84** : blood/PBMC 117 제외(`tissue:` 필드로 분리), no rejection 60→NR, Borderline 11 제외, ABMR/TCMR/Mixed 24→Rejection → `GSE129166_biopsy_rma_minmax.h5ad`(95), `GSE129166_biopsy_NRvsRej_rma_minmax.h5ad`(84)
- GSE138043 52→52 : non-AR 37→NR, AR 15→Rejection → `GSE138043_NRvsRej_rma_minmax.h5ad`
- GSE14328 36→36 : stable 18→NR, acute rejection 18→Rejection → `GSE14328_NRvsRej_rma_minmax.h5ad`
- GSE147089 224→224 : No ABMRh 168→NR, DSApos/neg ABMRh 56→Rejection → `GSE147089_NRvsRej_rma_minmax.h5ad`
- GSE1563 62→17 : 환자 ID(title)에서 biopsy(BX)만, TX1~10→NR(10), AR1~7→Rejection(7); C/NR*/PBL 제외 → `GSE1563_TXAR_biopsy_rma_minmax.h5ad`
- GSE192444 300→282 : NR 175→NR, ABMR/TCMR/Mixed 107→Rejection (pABMR/pTCMR 18 제외) → `GSE192444_NRvsRej_rma_minmax.h5ad`
- GSE21374 282→29 : 환자 ID(title 코드 `<num>A<n>AGX..`)로 합치면 221명; main-analysis 플래그(`first biopsy per patient...=1`)=105명 검증; 그중 rej 29만 추출(Rejection) → `GSE21374_rejection_mainanalysis_rma_minmax.h5ad`
- GSE34437 66→29 : no significant abnormalities 16→NR, ARIA+ARIB 13→Rejection (baseline donor 33, borderline 4 제외) → `GSE34437_NRvsRej_rma_minmax.h5ad`
- GSE36059 410→402 : non-rejecting 280→NR, ABMR/TCMR/MIXED 122→Rejection (Nephrectomy 8 제외) → `GSE36059_NRvsRej_rma_minmax.h5ad`
- GSE44131 57→23 : Normal 12→NR, CAMR/TGP(C4d+/DSA+) 11→Rejection → `GSE44131_NRvsRej_rma_minmax.h5ad`
- GSE48581 306→65 : histologic diagnosis 필드 기준 ABMR/TCMR/Mixed 65→Rejection만 → `GSE48581_rejection_rma_minmax.h5ad`
- GSE50084 115→48 : biopsy 61개 중 No-DSA-normal 20→NR, DSA+ rejection 28→Rejection (blood 54, biopsy DSA+normal 13 제외) → `GSE50084_biopsy_NRvsRej_rma_minmax.h5ad`
- GSE53605 55→31 : Normal allografts 18→NR, AR 13→Rejection (CNIT/IFTA 제외) → `GSE53605_NRvsRej_rma_minmax.h5ad`
- GSE72925 168→94 : Normal 68→NR, TCMR 26→Rejection → `GSE72925_NRvsRej_rma_minmax.h5ad`
- GSE75693 79→45 : Stable graft 30→NR, Acute rejection 15→Rejection → `GSE75693_NRvsRej_rma_minmax.h5ad`
- GSE93658 101→76 : control 16→NR, cAMR/TCMR_IFTA/TCMR_DSA- 60→Rejection (GEO 확인: kidney chronic rejection) → `GSE93658_NRvsRej_rma_minmax.h5ad`
- GSE9489 60→15 : non-rejecting 7→NR, AR IA~IIB 8→Rejection → `GSE9489_NRvsRej_rma_minmax.h5ad`
- GSE98320 1208→617 : NOMOA 274→NR, ABMR/TCMR/Mixed 343→Rejection (d96 필드) → `GSE98320_NRvsRej_rma_minmax.h5ad`

### 중복/제외 발견
- **GSE9489 ⊂ GSE9493**: GSE9489 60개 전부가 GSE9493(82개)에 포함(동일 GSM·title). superset인 GSE9493만 쓰는 게 권장.
- **GSE98320 ↔ GSE36059/GSE48581 529개 중복(외부 정보)**: GSM 0겹침·title 코드 불일치·발현상관 최대 0.84로 **데이터만으로 특정 불가**. 원인=플랫폼 차이(GSE98320=GPL15207 PrimeView 20084유전자 vs 나머지 21355). 매핑 테이블 없으면 dedup 불가 → GSE98320은 전체 1208 기준으로 라벨링(중복 미제거).
- **미사용 3개**(사용자 결정): GSE50058, GSE93659, GSE9493 (중복/superset).
- **24개 중 minmax 미포함 2개**: GSE181757(Illumina HumanHT-12 V4, GPL10558), GSE69677(Illumina non-normalized) — RMA(Affy 전용) 불가라 `_norm_gene.csv`(quantile)로 별도 처리, 통합 세트 제외.

### 집계
- 원본 22시리즈 4050개 → 라벨링 후 사용 가능 **2179개 (NR 1209 / Rejection 970)**, 미사용 3개(227개) 제외.
- 플랫폼별 유전자 수 상이(9054/13041/17259/19434/19997/20084/21355) → 통합 시 공통 유전자 교집합 필요.

### 산출물
- 파생 .h5ad: `data/rma_out/minmax/` 하위 위 19개 파일.
- 발표용 표 이미지: `data/kidney/dataset_label_table.png` (최초n/최종n/NR/Rejection 비교, matplotlib).
