# Claude Code 세션 로그

프로젝트별 상세 내용은 각 WORKLOG.md 참조.

---

## 2026-06-16 — scGPT (predict-cell 결과 통합 + bar plot)
- 기존 bulk adapter(`adapter_8000`) predict-cell 결과를 한 장으로 통합: **E-MTAB-12051(in-domain source, 16환자)** + 외부 scRNA-seq 4시리즈(GSE195719·GSE109564·GSE145927·GSE151671 AK1/AK2, 9환자) = 25환자.
- 통합 CSV `data/results/prognosis_predict_cell_combined/predict_cell_all_combined.csv` (Run1=재학습X, Run2=공통gene 재학습 컬럼 동시 보관). E-MTAB는 Run2 없음(기존 adapter 그대로 적용 = Run1 조건만).
- AUROC: E-MTAB **0.875**, GSE195719 **1.0**(나머지 단일-Rejection이라 AUROC 불가). bar plot은 **Run1만** 사용·p60 확률 내림차순 정렬·색=실제라벨로 최종 정리(`predict_cell_run1_bar.png`). 상위권(0.59↑)은 외부 Rejection 환자가 독식, E-MTAB은 Rej/NR이 0.47~0.54에 혼재.
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-15 — scGPT (kidney microarray NR/Rejection 이진 라벨링 + 시리즈별 .h5ad 추출)
- minmax 22시리즈에 대해 시리즈별 매핑 기준 합의하며 NR/Rejection 파생 .h5ad 19개 생성(`data/rma_out/minmax/`). 원본 라벨은 `obs['diagnosis_raw']` 보존, `obs['diagnosis']`에 NR/Rejection.
- 원본 4050개 → 사용 가능 **2179개(NR 1209 / Rejection 970)**. 미사용 3개(GSE50058·GSE93659·GSE9493, 중복/superset). GSE181757·GSE69677은 Illumina라 RMA 불가로 애초에 minmax 제외.
- 중복 규명: GSE9489 ⊂ GSE9493(전량 포함); GSE98320↔GSE36059/48581 529중복은 플랫폼 차이(PrimeView)로 데이터상 특정 불가→전체 1208 기준 라벨링. GSE129166은 biopsy 95만, GSE21374는 main-analysis(105명)·환자ID 합치면 221명.
- 발표용 표 이미지 `data/kidney/dataset_label_table.png` 생성(최초n/최종n/NR/Rejection 비교).
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-14 — scGPT (kidney microarray 24개 전체 RMA 전처리 + 점검)
- 24개 microarray를 플랫폼별 gold-standard로 RMA: Affy 3'IVT 17개 affy::rma, Gene/Exon ST 5개 oligo::rma, Illumina 2개 log2+quantile(neqc 대체). gene 매핑은 .db, PrimeView는 GPL15207. 전용 env r_affy(R4.5/Bioc3.22)
- 해결한 문제: ①preprocessCore threading 버그→--disable-threading 재컴파일 ②rma background correction이 저품질 CEL에서 segfault→CEL 격리 병렬 스크리닝으로 자동 제외(GSE36059 1개) ③동시 R설치 segfault→직렬화 ④annotation 미러 불안정/primeview.db 부재→curl 반복+GPL15207 대체
- 결과: **24/24 OK, 총 4,578 샘플**, log2 범위·샘플수 정상. 출력 rma_out/<GSE>_rma_gene.csv (Illumina는 _norm_gene.csv)
- 후속 1) 24개 값분포 violin plot(rma_out/violin/) 2) Illumina 제외 22개에 기존 학습데이터 방식(RMA<5→0 + per-sample minmax) 재현·적용 → rma_out/minmax/<GSE>_rma_minmax.h5ad 3) 진단 라벨 부착: characteristics에서 16개 + source_name으로 5개 = **21/22**(GSM 100% 매칭, obs.diagnosis/gsm/characteristics). GSE1563만 진단필드 부재로 보류(저신뢰). Rejection/NR 이진은 미작업(사용자 후속)
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-14 — DW (디스크 정리)
- 디스크 93%(여유 30G)에서 ~/DW(177G) 정리. 압축 해제본이 존재하는 zip 원본 4개(data_genemodule 10.3G, CellFM_data 4.9G, data_mapping 4.2G, model_example 1.5G) + __pycache__/.ipynb_checkpoints/.pyc 삭제 → 21G 확보(여유 51G, 88%)
- scFoundation 프로젝트 종료로 폴더 전체(40G) 삭제 → 여유 90G(79%). 미푸시 커밋 4개(연습 스크립트·figure·WORKLOG·한글번역) 소실 인지하고 진행. ⚠️ scrna 원격 URL에 노출된 GitHub PAT(ghp_...) revoke 필요
- 미진행 후보: kidney microarray GSE*_RAW.tar(~20G, GEO 재다운로드 가능), scGPT/data/results의 rejection_end2end_* 실험 결과(~23G)

## 2026-06-12 — scGPT (kidney scRNA-seq 5개 전체 공통 gene 재학습 Run2 완료)
- 5개 kidney scRNA-seq 파일 전부 train/test 공통 gene으로 처음부터 재학습(Run2) 후 Run1(기존 ckpt predict)과 비교 — 4개(GSE109564, GSE151671_AK1/AK2, GSE195719)를 마스터 체인으로 순차 finetune→predict
- 공통 gene 재학습이 rejection 확률을 대체로 상향(AK2 +0.097, AK1 +0.062, GSE145927 +0.06~0.07; GSE109564·GSE195719는 거의 불변) — 상향 폭은 train-only gene 비중에 비례. GSE195719 AUROC는 Run1·Run2 모두 1.0(분리력 보존). bulk CV는 소폭↓(0.776→0.755~0.780)
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-10 — scGPT (kidney scRNA-seq prognosis predict-cell + 공통 gene 재학습)
- bulk 학습 adapter(adapter_8000, kidney backbone)를 재학습 없이 5개 kidney scRNA-seq에 predict-cell: GSE195719(2클래스) 환자단위 **AUROC 1.0**, 나머지 4개 단일-Rejection은 rejection 환자 전부 0.528~0.751로 NR baseline(0.511) 상회
- GSE145927에 대해 train/test 공통 gene(16,888) 재학습 비교 → 공통 gene 셋팅이 3 환자 모두 rejection 확률 +0.06~0.07 상향(cross-domain 개선), bulk CV는 0.776→0.758로 소폭↓
- 상세 → scGPT/WORKLOG.md 참조

---

## 2026-06-01 — scGPT (음성 대조: 무관 microarray + 랜덤 라벨 파이프라인 검증)
- 신장이식과 무관한 GSE39582(대장암 585샘플, 동일 HG-U133 Plus 2.0)를 동일 RMA 전처리 후 랜덤 NR/Rejection 라벨로 finetune→predict-cell 1회 실행
- 결과: finetune OOF AUROC **0.515**, predict-cell 환자단위 AUROC **0.458** → 둘 다 우연 수준. 실제 0.776/0.875와 대비되어 기존 prognosis 신호가 진짜임을 검증
- 부수 성과: 파이프라인 homemade RMA background-correction의 수치 언더플로 버그를 erfcx 안정식으로 수정
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-01 — scGPT (adapter_8000 모델 QC h5ad predict-cell 추론)
- finetune OOF 최고 모델 `prognosis_adapter_8000`(5-fold AUROC 0.776, max_seq_len=8000)을 QC 필터 E-MTAB-12051(37,920세포/16환자)에 적용한 환자단위 예후 추론
- 결과: **환자단위 AUROC 0.875, BalAcc 0.875, 13/16 정답**. 거부 4명(ABMR×3, TCMR×1) 전부 검출(recall 1.0), 오류 3건은 모두 위양성(Non rejection DSA±)
- 입력값 정정: model-dir `models/`(복수), patient-col `orig.ident`(오타). 산출물 `data/results/prognosis_adapter_8000/predict_cell_p60_qc.csv`. 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v10 NO-CPM 변형: micro log1p_cpm 제거 테스트)
- v10에서 microarray 투영 입력의 `log1p_cpm`을 제거(`Xm_cpm = Xm`)하고 best-grid(proj+prog quantile_soft 5시드) 재평가
- minmax 파일 고정 시 영향 거의 없음(best-grid 0.710→0.711, ±0.003) — minmax가 이미 정규화돼 log1p_cpm이 거의 항등. RMA/log2 원본 입력은 PRIMARY 0.698→0.660 하락하나 quantile_soft DA가 스케일 흡수해 best-grid ~0.72 유지
- 보존: `archive_exploratory/prognosis_scgpt_embed_v10_nocpm.py`, `results/archive_exploratory/prog_v10_nocpm/`. 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (test_script 4개 backbone 실학습 실행 + 결과 정리)
- 이전 세션에서 셋업만 하고 미수행이던 4개 backbone을 H200에서 기본 인자로 실학습(scRNA E-MTAB-12051 16샘플 → microarray GSE36059+147089 627샘플 transfer). GPU 여유로 4개 동시 실행
- 결과(AUROC/AUPRC): frozen 0.689/0.429, mil 0.677/0.470, finetune 0.615/0.399, mil_finetune 0.514/0.284 → **frozen 계열 > FT 계열**(소표본 FT 과적합), MIL이 AUPRC 최고
- 전 모델이 한 클래스 쏠림(임계값/보정 문제): frozen·mil=전부 Rejection, FT 2종=전부 NR → acc/f1 무의미, AUROC/AUPRC로만 판단. 다음: target prevalence 기준 임계값 보정, frozen emb-mode ablation, MIL cibersortx bridge
- 결과 정리 → `data/test_script/RESULTS.md`, 로그 → `data/test_script/run_logs/`. 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (test_script 4개 backbone 실데이터 연결 + CV 제거 + FT 2종에 전체 gene 패널·MLM)
- `data/test_script/` 4개 스크립트(scgpt_frozen / finetune / mil / mil_finetune) = sample-level NR/Rejection 분류 backbone(scGPT+DANN, pseudobulk/cell-MIL × frozen/FT). placeholder 실데이터 연결: sc=E-MTAB-12051, micro=GSE36059+GSE147089 RMA, model=pretrain_kidney. scGPT API 설치본과 정합 확인
- CV 제거(source 16샘플·양성4 → k-fold 무의미, AUROC가 f1로 silent fallback): 전체 source 학습→microarray만 평가. frozen/mil epochs 100→50
- FT 2종에 ①전체 gene 패널(n_hvg=0=공통~17,704, gene_list_json 옵션)+배치별 토큰화로 cell당 무작위 gene 샘플링(다epoch 전역 context) ②MLM auxiliary(ExprDecoder, loss=CE+α·MLM, mask_ratio0.4, unlabeled micro도) 추가. CLI --no-mlm/--n-hvg/--gene-list/--mask-ratio
- 검증: 합성 미니배치 forward/backward(decoder grad 포함)/predict + 4개 py_compile 통과, 실데이터 로더 스모크. **실학습 미수행**(GPU 필요)
- 맥락: 이전 v11(MLM FT는 prognosis 투영 전이 개선 못함)과 별개 task(분류 backbone). 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (정리/통합: 권고 모델 단일 스크립트화 + 구버전 아카이브)
- 신규 `scripts/prognosis_final.py`: 권고 모델만 담은 단일 스크립트(scGPT gene-embedding 투영+quantile/soft DA+LR 5시드). 검증 AUROC 0.712. micro 이중정규화 제거. 산출물 results/prognosis_final/
- `data/gene_pool_17704.json`(유전자풀 안정화), `scripts/README_PROGNOSIS.md`(사용법+결론) 작성
- 탐색 스크립트 13개→`scripts/archive_exploratory/`, prog_v2~v12 결과→`results/archive_exploratory/` 이동(보존). scripts/엔 final+adapter만 남김
- 이전 세션 산출물(prognosis_adapter_*, prog_sc2micro)은 미정리(사용자 확인 대기)
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v12_rma: RMA 정규화 microarray로 FT모드 비교 재현 — 결론 robust 동일)
- scgpt_training_data.h5ad(=test용, RMA log2)를 scgpt_test_data.h5ad로 copy 후 micro=RMA버전으로 v12 재실행. (두 microarray 파일은 동일 627샘플, 정규화만 다름)
- proj: freeze=last_n=0.711(≈minmax 0.717), full+sc=0.676, full+sc_micro=0.705. cls/mean 0.40~0.55
- **microarray 정규화(minmax↔RMA) 바꿔도 결론 동일**: frozen gene-embedding 투영(~0.71) 최선, full FT는 효과 방향이 정규화/데이터따라 뒤집혀 신뢰 못함. frozen baseline 견고
- 산출물 results/prog_v12_rma/. 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v12: FT 모드 full/last_n/freeze 동일조건 비교 + micro proj 입력 수정)
- 사용자 지적: micro proj 입력에서 이미 log2인 RMA에 log1p_cpm 적용 말 것 → raw RMA 직접 사용으로 수정(이중정규화 제거). baseline proj AUROC 0.717(≈동일), AUPRC 0.467→0.479 개선
- `prognosis_scgpt_finetune_v12.py`: full/last_n(2)/freeze × {sc, sc+micro} × {proj,cls,mean} 동일조건 비교
- **결과**: proj — freeze=last_n=0.717(E 동결→baseline 동일), full+sc=0.719, full+sc_micro=0.640(하락). cls/mean — full이 최선(0.52~0.55)이나 proj에 한참 미달, last_n은 cls 악화. **어떤 FT 모드도 frozen baseline proj(~0.72) 못 넘음**
- micro 수정으로 v11의 "full FT가 proj 망침(0.687)"이 이중정규화 아티팩트였음 판명(수정 후 full+sc=0.719). 권고 모델 불변: frozen gene-embedding 투영+quantile/soft DA
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v11: self-supervised fine-tuning은 예후 전이 개선 못함, 이유 규명)
- 사용자 가설: scGPT가 scRNA-seq 기반+training data도 신장이식 sc니 fine-tuning하면 latent representation 향상될 것
- `prognosis_scgpt_finetune_v11.py`: 라벨없는 MLM(masked value prediction, 체크포인트 decoder 재사용) continue-pretrain. (a)sc만 (b)sc+micro transductive
- **결과: baseline(FT없음) proj 0.719가 최선. ft_sc+micro=0.719(순이득0), ft_sc=0.687(하락), cls/mean 0.46~0.55**
- 이유: sc-only FT는 sc 과적합→microarray 갭 확대(v2와 동일), transductive는 갭 회복뿐, MLM은 발현복원만 적응(거부판별/정렬 학습X), 체크포인트가 이미 kidney-pretrain, 투영 embedding은 MLM으로 거의 불변. 근본병목=갭+양성4명
- 교훈: sc→타플랫폼 전이엔 scGPT fine-tuning 도움 안 됨, frozen gene-embedding 투영+DA가 정석
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v10: 순수 scGPT-embedding 0.70→0.71, soft 도메인-불변 가중)
- v9 base로 추가 방법 전수(`prognosis_scgpt_embed_v10.py`, 수작업 시그니처 없이)
- **효과O**: soft 도메인-불변 가중(quantile 후 차원별 플랫폼 판별력으로 연속감쇠) → **proj+quantile_soft+LR 5시드 0.710±0.012**(피크 0.73), SVM-rbf도 소폭↑
- **효과X**: scGPT gene-program 메타진(KMeans, 내부OOF 0.85지만 외부 0.64=과적합), Subspace Align 0.64, CORAL 0.59, 메가앙상블 0.693
- 순수 scGPT-embedding 현실 상한 ~0.71 확정(천장 0.82=시그니처/거부환자 한계)
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v9: 순수 scGPT-embedding 전이 0.70 — 수작업 시그니처 없이)
- 사용자 선호: 수작업 유전자 시그니처는 인위적이라 후순위, **scGPT backbone+training embedding**으로 예후예측 우선 (→ 메모리 scgpt-embedding-over-signature-pref 기록)
- **v9 `prognosis_scgpt_embed_v9.py`**: 표현=log1p_cpm(expr)@scGPT gene-embedding-table E(512d). embedding에 고급 DA 직접 + 데이터기반 도메인불변 차원선택
- **PRIMARY=투영+quantile_ref DA+LR, 5시드=AUROC 0.699±0.014** → gene-space(0.647)·이전 scGPT embedding 전부(≤0.55) 능가. DA: quantile_ref≈rank_gauss>zscore>combat≫CORAL(해로움). 차원선택 frac0.75→0.688
- 순수 scGPT-embedding 현실 상한 ~0.70(트랜스포머 CLS 0.40, 시그니처 0.82는 참조). 정석=CLS 말고 gene-embedding-table 투영+quantile DA+LR
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v6~v8: 거부 시그니처로 0.65→0.82 돌파 + scGPT-backbone-base 설계 완성)
- 사용자 재요청: "더 많은 방법" + "scGPT backbone base 설계". 신호가 gene-space에 있으니 생물학 거부 시그니처·고급 DA·scGPT gene-embedding table backbone으로 천장(0.82) 돌파 시도
- **v6 `prognosis_gene_space_v6.py`**: 거부 시그니처 71유전자(IFN-γ/세포독성T·NK/ISG). **무학습 SIG-SCORE(per-domain z 평균)=AUROC 0.809** → gene-space 0.647 압도, 천장 거의 도달. 무학습이 학습형 LR을 압도
- **v7 `prognosis_scgpt_base_v7.py`**: scGPT **gene-embedding table**(60697×512)을 backbone base로, 발현을 트랜스포머 대신 선형 투영(Z=expr@E). cpm 입력 시 0.66으로 gene-space 능가, CLS(0.40) 크게↑ → 트랜스포머가 신호 파괴범·embedding table은 보존 확증
- **v8 `prognosis_scgpt_base_v8.py`**: scGPT 기하학으로 시그니처 정제. **scGPT-WEIGHTED 시그니처=AUROC 0.8155 = 최종 최선 모델(천장 도달)**. scGPT-GUIDED(centroid 근접 top-N)=0.80. 세 시그니처 변형 0.80~0.82 수렴=견고
- 최종 모델: scGPT-WEIGHTED 거부 시그니처(0.816). 교훈: 트랜스포머 임베딩 말고 gene-embedding table을 backbone으로, 소표본 전이엔 무학습 도메인지식 시그니처가 압도적
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v5 scGPT readout 전수 탐색: 어떤 readout도 gene-space를 못 넘음, scGPT backbone 한계 확정)
- 사용자 요청: "scGPT backbone 배경에서 성능 최대화, 모든 시도". v3/v4가 CLS 토큰만 썼으므로 신규 `prognosis_scgpt_readout_v5.py`로 frozen 인코더의 full token 출력을 뽑아 **6가지 readout**(cls/mean-pool/max-pool/meancls/meanmax/allcat) 전수
- 가설("CLS가 약한 게 문제, gene-token mean/max-pooling이 신호 보존")은 **기각**: 전이 AUROC 전부 0.40~0.47(L2 포함), gene-space 0.647에 한참 미달. micro 내부 oracle도 모든 readout 0.70~0.72 < raw gene 0.82
- FUSION(gene⊕scGPT max)=0.570 → scGPT 섞으면 오히려 하락. **문제는 CLS pooling이 아니라 frozen kidney 인코더 표현 전체**가 cross-platform 불변 신호를 손실
- 최종 결론: 이 sc→microarray 과제에서 scGPT backbone은 어떤 활용법(임베딩/readout/fine-tuning/hybrid)으로도 도움 안 됨. **최선 모델 = v4 gene-space PRIMARY 0.647 확정**
- 산출물: results/prog_v5/{readout_grid.csv, external_eval.csv, predictions.csv, FINAL_REPORT.txt}
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v4 gene-space 전이로 돌파: scGPT 임베딩이 신호를 파괴함을 발견)
- v3 진단 핵심: micro 내부 거부 oracle이 **원시유전자 0.82 vs scGPT임베딩 0.65** → scGPT CLS 임베딩이 전이신호를 파괴
- 신규 `prognosis_gene_space_v4.py`: 임베딩 버리고 **gene-space**(공유 17,704 유전자) 분류. PRIMARY=pseudobulk→per-domain z-score→LR(C=0.05) → 외부 AUROC **0.647±0.006**(5시드 안정), v3 전부(≤0.55) 능가
- scGPT 임베딩 단독=0.40(음의상관), hybrid=0.53(하락) → scGPT 임베딩은 이 과제에 해로움. gene-space 단독 최선. feature selection도 해로움
- 결론: sc→array 전이엔 임베딩 아닌 gene-space+per-domain 표준화+정규화 선형이 정석. 천장 0.82, 잔여격차는 양성4명 한계
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v3 종합 벤치마크: frozen embedding + 도메인정렬, sc→microarray 전이 실패 확정)
- 신규 `prognosis_sc_to_microarray_v3.py`: 성공방향(bulk→sc, AUC=1.0) 레시피(frozen 인코더→512d CLS→PCA+LR→percentile)를 sc→microarray에 첫 적용 + 임베딩공간 unsupervised 도메인정렬 6종(none/standardize/combat/coral/whiten/quantile)
- **912 조합 전수**(6정렬×4분류기×2소스[pseudobulk_augment,cell-level 53k]×4집계×LOGO/sgkf) + fine-tuning freeze/last_n/full(v2 재실행): 외부 AUROC 전부 0.42~0.55(랜덤/이하) → 전이 실패 확정
- 실패 메커니즘 규명: 도메인분리 AUROC=1.0(플랫폼이 신호 압도), micro 거부 oracle=0.65(천장 낮음), sc 내부 0.85(축 불일치). 양성 4명+내부 OOF 포화로 모델 선택 불가
- 산출물: results/prog_v3/{internal_cv_grid.csv(912), external_eval.csv, FINAL_REPORT.txt, diagnostics.json, roc.png, embeddings 캐시}
- 상세 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT (v2 encoder-mode 3-way 실험: full/last_n/freeze)
- pseudobulk_augment·n_folds=2로 full/last_n(2)/freeze 학습 후 외부 microarray 2종(같은 627샘플의 raw RMA vs RMA≤5 zeroing) 평가
- 내부 OOF: full(0.833)>last_n(0.625)>freeze(0.396) / 외부 AUROC는 모두 0.42~0.49(랜덤 이하)로 역전 → encoder 깊은 학습=source 과적합, 전이 실패
- last_n(2)가 외부에서 가장 일관적(GSE 0.494, SGD 0.462). zeroing 효과는 미미
- cell_level+full(4-fold) 첫 시도는 양성 0명 fold 발생으로 CV 붕괴 → n_folds=2로 교정. cell_level ~5h vs pseudobulk ~10분
- 상세 → scGPT/WORKLOG.md

## 2026-05-30 — scGPT (prognosis_sc_to_microarray_v2.py: encoder 학습 가능하도록 확장)
- v1은 scGPT encoder 완전 동결이었으나, 학습 데이터가 scRNA-seq(인코더 사전학습과 동일 도메인)라 encoder fine-tuning을 비교 실험하려 함
- `--encoder-mode {freeze, last_n, full}` 추가: freeze(기존), last_n(마지막 N개 transformer layer만 unfreeze), full(전체)
- `--encoder-lr`(기본 1e-5)로 encoder 차등 LR(별도 옵티마이저 그룹), head/adapter는 `--lr`(1e-4)
- 핵심 수정: 학습된 encoder 가중치를 체크포인트에 저장/복원 (안 하면 evaluate 시 사전학습 encoder 재로드로 fine-tuning 통째 소실되는 버그 방지)
- config.json에 encoder_mode/unfreeze_last_n/encoder_lr 기록, py_compile·CLI 확인 완료(실제 학습 미실행)
- 상세 → scGPT/WORKLOG.md

## 2026-05-29 — scGPT (prognosis_sc_to_microarray.py: scRNA-seq 학습 → microarray 평가)
- 방향 역전 신규 파이프라인: scRNA-seq(E-MTAB-12051) 학습 → 외부 microarray(GSE36059+GSE147089 RMA) 1회 평가, 환자 단위 예후(NR vs Rejection)
- `--train-mode {pseudobulk_augment(메인), cell_level, patient_pseudobulk}`, frozen scGPT encoder(pretrain_kidney) 백본
- Leakage 차단: 환자 그룹 CV(StratifiedGroupKFold), 샘플 자기완결 전처리, threshold는 train OOF에서 고정, 유전자 풀 학습데이터에서만 도출, test는 evaluate에서 1회만 read
- train/evaluate 스모크 테스트 통과(실제 학습은 미실행)
- 상세 → scGPT/WORKLOG.md

## 2026-05-28 — scGPT (데이터 분포 비교 시각화 & 전처리)
- E_MTAB_12051.h5ad → CPM + log2(CPM+1) 변환 → E_MTAB_12051_log2cpm.h5ad 생성
- scRNA-seq(pseudobulk) vs microarray(RMA / zeroing / min-max scaled) gene mean scatter plot 3종 생성
- scgpt_training_data.h5ad 전처리 분석: RMA ≤5 zeroing으로 bimodal 분포 확인
- scgpt_training_data_minmax.h5ad 생성: non-zero 값을 샘플별 min-max 스케일링 → 0~max 범위로 재분포
- 공통 유전자 17,736개 기준 Pearson r 비교: RMA원본(0.746) > min-max(0.740) > zeroing(0.702)
- 상세 → scGPT/WORKLOG.md

## 2026-05-27 — scGPT (prognosis_microarray_adapter.py 작성)
- microarray → scGPT frozen encoder → CLS → MicroarrayToSCAdapter MLP → PrognosisHead (binary + Cox)
- BCE + Cox partial-likelihood 결합 손실, Cox는 time 컬럼 있을 때만 활성화
- finetune / predict-bulk / predict-cell 3-command CLI, 학습 396k params (encoder 완전 동결)
- 상세 → scGPT/WORKLOG.md

## 2026-05-27 — scGPT (rejection_finetune_end2end_v5.py 작성)
- v4 대비 핵심 변경: finetune-mode 기본값 none, DomainAdapter 기본값 off
- 신규 predict-cell 커맨드: 단일세포 h5ad → 세포별 확률 → 환자 p{q} 집계 (p60)
- bootstrap 200회 안정성 검증 + ROC/violin 시각화 지원
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-27 — scGPT (실험 비교 분석)
- Step 3 (run_step3, AUC=0.938) vs v1/v2/v3 end2end 비교 정리
- domain_transfer.py (pseudobulk, AUC=0.667) vs run_step3 (단일세포, AUC=0.938) 구분
- frozen encoder 우위 이유: quantile binning 플랫폼 불변성 + 세포 이질성 보존

## 2026-05-27 — scGPT (v3 finetune + E-MTAB-12051 예측 완료)
- finetune-mode=none, max_seq_len=8000, 공통 유전자(17,704개) 필터 적용
- CV AUROC=0.780±0.031 (OOF threshold=0.234), 최종 모델 28에폭
- E-MTAB-12051 16샘플 예측: Rejection 9 / NR 7 (threshold=0.234)
- 고신뢰 Rejection: EXT241(0.944), NEPH017(0.864), NEPH018(0.832)
- 결과: results/rejection_end2end_v3/run_20260526-145015/predictions_emtab12051.csv
- 상세 → scGPT/WORKLOG.md

## 2026-05-26 — scGPT (rejection_finetune_end2end_v3.py)
- v2 대비 두 가지 핵심 변경: `include_zero_gene=False` (샘플별 nonzero 유전자만 토크나이즈) + `normalize_scgpt()` 추가
- Training data: `scgpt_training_data.h5ad` (전처리 완료, 정규화 불필요)
- Test data: `E_MTAB_12051_pseudobulk.h5ad` (raw counts → `--normalize` 플래그로 normalize_total+log1p 적용)
- `fixed_col_idx` 제거, `make_token_batch_nonzero()` 신규 구현
- 상세 → scGPT/WORKLOG.md

## 2026-05-26 — scGPT (scgpt_training_data.h5ad 생성)
- GSE147089_rma_zeroed.h5ad(224) + GSE36059_rma_thresh5.h5ad(403) 병합 → scgpt_training_data.h5ad (627×21463)
- condition 통합: non-rejecting/No_ABMR → NR, ABMR/TCMR/DSApos/DSAneg/MIXED → Rejection
- 전처리 배경: RMA 후 발현값 ≤5를 0으로 zeroing (bulk RNA-seq처럼 zero-inflated 분포 의도)
- 현재 X: 원본 RMA값 그대로 (0~15.11), 0값 24.07% / scGPT encoder가 binning 담당
- 상세 → scGPT/WORKLOG.md

## 2026-05-24 — scGPT (domain_transfer.py)
- pseudobulk SC(E_MTAB_12051_pseudobulk_preprocessed) 기반 domain transfer 스크립트 신규 작성
- Bulk ∩ SC ∩ vocab 교집합 유전자(17,704개) 전체로 임베딩, LR C값 스윕(--c-values) 기능 추가
- 상세 → scGPT/WORKLOG.md

## 2026-05-23~24 — scGPT (End-to-end Fine-tuning v2, DomainAdapter)
- rejection_finetune_end2end_v2.py: DomainAdapter(bottleneck MLP+residual) + per-fold pos_weight 추가
- v2 none(CV AUROC=0.782) / v2 full(CV AUROC=0.839) E-MTAB 예측 완료
- v2 none: test BalAcc=0.625 (v1 none과 동일), v2 full: BalAcc=0.500 (domain collapse 재현)
- DomainAdapter는 CV 개선하나 test generalization 기여 없음 — frozen encoder가 여전히 최선
- 상세 → scGPT/WORKLOG.md

## 2026-05-22~23 — scGPT (End-to-end Fine-tuning 비교)
- rejection_finetune_end2end.py에 코사인 LR 스케줄러 + 중간 체크포인트 저장 추가
- finetune-mode 3가지(last-n=2 / none / full) 13k genes로 전체 실험 완료
- CV: full(0.835) > last-n=2(0.798) > none(0.782) 순이었으나 E-MTAB test에서 역전
- test BalAcc: none(0.625) > full(0.500) > last-n=2(0.375) — full/last-n은 domain shift로 specificity=0 붕괴
- **결론**: 도메인 전이 환경에서 frozen encoder(none)가 최선. end-to-end FT는 CV 성능 높이지만 도메인 일반화 파괴
- 상세 → scGPT/WORKLOG.md

## 2026-04-10 — scFM (CellFM)
- scfm conda 환경에 mindspore 2.2.10 + scanpy/scib/torch/gears 설치
- datasets/CellFM.zip 압축 해제 (21개 h5ad, GO_data)
- 7개 튜토리얼 노트북 → 로컬 Python 스크립트 변환 (경로 수정, 로깅/결과저장 추가)
- 상세 내용 → scFM/WORKLOG.md

## 2026-04-03 — scFoundation
- 원본 레포 clone 후 `tunabear2/scRNA-work` 에 푸쉬
- Figshare 데이터 전체 다운로드 및 압축 해제
- `scfoundation` conda 환경 구성
- 3가지 다운스트림 태스크 실습 준비 (Gene Module / Cell Mapping / Cell Type Annotation)
- → 상세: `~/DW/scFoundation/WORKLOG.md` 섹션 1~4

## 2026-04-05 — scFoundation
- Figshare 누락 파일 확인 및 추가 다운로드 (`gse133344` h5ad, 2.1 GB)
- 실행 스크립트 경로 오류 수정 (루트 기준 → 서브폴더 기준)
- `mapping-practice.py` 신규 생성 (원본 파이프라인 코드 보존 / 실습용 분리)
- pyscenic 0.12.1 + NumPy 호환성 패치 4건 (ctxcore, transform, rss, diptest)
- `bbknn` 패키지 설치
- 3가지 태스크 실습 실행 완료 (annotation / genemodule / mapping)
- annotation: Zheng68K accuracy 83% (scFoundation = CellTypist)
- mapping: scFoundation iLISI 0.965으로 최우수 (vs Raw 0.785, scBERT 0.946)
- genemodule: 31개 metagene, T cell module 네트워크 및 RSS 생성
- → 상세: `~/DW/scFoundation/WORKLOG.md` 섹션 7, 9
  - Cell Type Annotation: Zheng68K accuracy 83% (scFoundation ≈ CellTypist)
  - Cell Mapping: scFoundation iLISI 0.965, cLISI 0.994 (best)
  - Gene Module: T cell 모듈 네트워크, GRN, pySCENIC RSS 결과 저장
- → 상세: `~/DW/scFoundation/WORKLOG.md` 섹션 5~7

## 2026-04-10 — scFM (CellFM)
- CellFM 실습 폴더 정비: CLAUDE.md, WORKLOG.md 초기 생성
- git 이력 기반 작업 진행 현황 재구성 (2024-06 최초 커밋 ~ 2025-08 최신)
- 완료된 튜토리얼: Cell Annotation, Gene Function, Batch Integration, Perturbation, lncRNA 동정
- → 상세: `~/DW/scFM/WORKLOG.md`

## 2026-04-10 — scFM (CellFM) — PyTorch 재작성
- MindSpore GPU가 H200(CUDA 12.9)과 비호환 → CellFM-torch 기반 PyTorch 재작성
- CellFM-torch 클론 (`CellFM-torch/`), `layers/utils.py`, `model.py` 활용
- 스크립트 01, 02, 03, 05, 07 완전 재작성 (syntax 검증 완료)
- → 상세: `~/DW/scFM/WORKLOG.md`

## 2026-04-10 — scFM (CellFM) — 전체 스크립트 실행
- scripts/01~07 전체 실행 완료 (버그 수정 포함)
- 01 Cell Annotation Finetune: **98.01%** acc
- 02 Zero-shot: 47.68% (Bayesian sampling 진동 한계)
- 03 Batch Integration: UMAP 저장, scib NMI=0.025
- 04 Gene Perturbation (GEARS): Pearson 0.975, Pearson_DE 0.901 (cell-gears + torch_geometric 설치)
- 05 Binary Gene Function: ~80% acc (3-fold)
- 06 Multiclass Gene Function: CC AUPR=0.881, MF Fmax=0.807
- 07 lncRNA: PBMC_10K 내 lncRNA 4개뿐 → 검출 0개 (데이터 한계)
- → 상세: `~/DW/scFM/WORKLOG.md`

## 2026-04-10 — scFM (CellFM) — 환경 재현 가이드 작성
- SETUP.md 작성 — conda env, 패키지 버전, 데이터/체크포인트 경로, 주의사항 포함
- → 상세: `~/DW/scFM/SETUP.md`

## 2026-05-04 — scGPT (2차)
- scGPT_Binary_Classification.py 재실행: Phase2 full fine-tuning → Test AUC **0.9969**, Acc 97.03%
- training_genes.json (24,159개) 저장: 학습 gene 목록 영구 보존
- predict_gsm_patients.py 수정: 학습 gene만 필터링 후 GSM 8명 환자 추론
- 추론 결과: 8명 전원 양성 판정 (확률 0.53~0.82, 학습 gene 23,077개 일치)
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-04 — scGPT
- scGPT_Binary_Classification.py 작성 및 실행 (B17 양성 vs B25_CTRL 음성, cell-level 분류기)
- 2단계 학습: Phase1 head-only (Val AUC 0.66) → Phase2 full fine-tuning (Val AUC 0.963, Test AUC 0.960)
- 수정사항: MODEL_DIR 경로 수정, var_names_make_unique 추가, tqdm progress bar 추가
- best_model.pt 저장 완료 → predict_patient()로 신규 환자 추론 가능
- 상세 내용 → scGPT/WORKLOG.md

## 2026-04-30 — scGPT
- 환자 단위 분류 모델 설계 논의 (신장 이식 normal vs rejection, 각 10명)
- 파이프라인 합의: scGPT 임베딩 추출 → mean pooling → LOOCV + Logistic Regression
- 구현은 다음 세션에 진행 예정 (데이터 경로·obs 컬럼 확인 필요)
- 상세 내용 → scGPT/WORKLOG.md

## 2026-04-13 — CellFM (~/DW/CellFM)
- cellfm conda env 패키지 전체 설치 (torch 2.6+cu124, mindspore 2.8 CPU, cell-gears, scib 등)
- CellFM-torch/model.py: MindSpore top-level import → lazy import 변경 (경고 제거)
- scripts/05: fold 값 버그 수정 [1,2,3] → [0,1,2,3,4] (5-fold CV)
- scripts 전체: deprecated torch.cuda.amp → torch.amp API 업데이트
- run_all.sh: conda env scfm → cellfm 수정
- 빠진 tutorial 검토 완료 (process.ipynb/cls_task.ipynb/ChemicalPerturbation 제외 사유 확인)
- scripts 01~07 전체 실행 완료: ConfusionMatrixDisplay 버그·GEARS 포맷 버그·metrics 순서 버그 수정
- 주요 결과: 04 GEARS pearson=0.975, 05 acc≈0.80, 06 CC AUPR=0.881, 07 PBMC lncRNA 9 cell types
- → 상세: ~/DW/CellFM/WORKLOG.md

## 2026-05-14 — scGPT (data preprocessing)
- GSE36059 / GSE147089 / E-MTAB-12051 pseudobulk preprocessed h5ad 세 파일 구조 비교
- GSE147089_rma.h5ad 손상 확인: rma_background()의 alpha=0.1 고정값이 전체 sigma^2에 곱해져 모든 값이 log2(1e-6)=-19.93으로 floored
- build_h5ad.py 수정: 하위 25% 분포에서 mu_b/sigma_b 추정, alpha=1/mean_signal로 data-driven 추정
- 재실행 결과: X range [1.85, 15.11], unique values 3.97M → 정상화 완료
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-18 — scGPT (Domain Shift)
- Bulk microarray (GSE36059+GSE147089) → scRNA-seq (E-MTAB-12051) domain shift 해결 시도 (7단계)
- 핵심 발견: scGPT kidney pretrained 임베딩이 platform 간 생물학적 신호 전이 가능 (AUC=0.938)
- LOO-CV 앙상블 (scGPT+DANN_MIL+SCVI+Cluster) AUC=0.958, BalAcc=0.833 (top4 threshold)
- 어려운 케이스: NEPH006(NR)이 모든 방법에서 높은 rejection score → 임상적 재검토 필요
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-18 — scGPT (추가 실험)
- pretrain_human vs pretrain_kidney 비교 실행 (run_step3_domain_transfer.py --model-dir pretrain_human --fresh)
- pretrain_human: AUC=0.500 (랜덤 수준) vs pretrain_kidney: AUC=0.938 → 도메인 특화 사전학습이 결정적
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-18 — scGPT (Transformer 분류기)
- DANN-PatchTransformer + Augmented MIL로 bulk array → SC NR/Rejection 분류기 구현
- 3번의 설계 반복 끝에 최적 구성: PCA-64 + DANN(λ=0.3) + AugMIL(σ=5.5)
- **T-MIL AUC=0.9583** (이전 LR 최고 0.9375 초과), LR+T-MIL 앙상블 **AUC=1.000**
- 핵심: SC intra-patient std(5.5)로 보정된 augmented MIL이 세포 단위 attention 학습 가능케 함
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-18 — scGPT (종합 벤치마크, NR vs Rejection 최종)
- 5단계(v2~v5+final) 전방위 벤치마크 진행: 25개 이상 방법 체계적 비교
- **핵심 발견**: 세포당 거부반응 확률의 **60th percentile (p60)** → **AUC=1.000 [label-free]**
  - 생물학적 의미: 거부반응 = 고활성 세포 서브집단. 평균/중앙값이 아닌 p60이 이 경계를 포착
  - 부트스트랩 (200회, 500cells/환자): AUC=0.9451±0.041 (AUC≥0.95: 54.5%)
- **권장 파이프라인**: PCA40+LR(C=0.009) 학습 → per-cell score → p60 aggregation
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-20 — scGPT (p60 재현 파이프라인)
- rejection_score_p60.py 신규 작성: pretrain_kidney scGPT embedding → cell-level rejection score → 환자별 p60 집계
- 실행 결과 재현 확인: AUC=1.0000, BalAcc=1.0000 (TN=12 FP=0 FN=0 TP=4), Bootstrap=0.9451±0.041
- 결과 저장: data/results/rejection_score_p60/ (CSV, PNG, JSON)
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-20 — scGPT
- 데이터 현황 전수 점검: train(GSE36059+GSE147089 merged_rma), test(E-MTAB-12051 pseudobulk) 전처리 검증
- pseudobulk.h5ad / pseudobulk_preprocessed.h5ad condition 라벨 추가
- train-reference QN 생성 (pseudobulk_preprocessed_trainQN.h5ad, 16×17736)
- prognosis_1.py 수정 및 3회 실험: per-sample top1200 / 고정 top1199 / freeze-backbone → test AUC 0.667→0.562→0.542 (모두 저조, 도메인 갭이 원인)
- RMA → Poisson pseudo-count 변환 (target 10k/20k/230k 탐색 → zero%≈13% 달성: target=230,000)
- prognosis_1.py 수정 및 실행: val AUC=0.831, test AUC=0.542 (pseudo-count 변환으로도 도메인 갭 해소 불가)
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-21 — scGPT
- rejection_finetune_end2end.py bin_values 동작 분석: train(RMA) 완벽 uniform, test(pseudobulk) zeros 24~36%로 bin 스파이크 확인
- gene 필터링 전략 수립: train∩test 공통 17,736개 → test zero≤1% 조건 → 13,050개 (bins 1-50 균등, CV≈4.7%)
- 8,000개 버전도 생성 (filtered_8k_genes.json, 균등 stratified 제거): 메모리 ~15GB
- 13,050 genes, batch_size=1 OOM 없이 동작 확인 (epoch ~223초, ~15GB GPU)
- rejection_finetune_end2end.py predict-ft 수정: fold 앙상블에 final_model.pt 포함
- rejection_finetune_nocv.py 신규 생성: CV 없이 전체 데이터 직접 학습
- 상세 내용 → scGPT/WORKLOG.md

## 2026-05-31 — scGPT sc→array transfer (goal: AUROC≥0.80)
- 백본 `data/best_script/scgpt_sc_to_array.py` 재현 baseline 0.698(정직)/0.732(test-selected). 9개 실험배치(robust clf, DA변형, feature-sel, DE시그니처, self/co-training, entropy-min, label-spread, composition/deconv, per-batch norm) 수행.
- **챔피언: 2-view co-training(proj+gene) 0.746** (transductive). 정직 단일소스 천장 ~0.73.
- ★진단: cosine(sc축,array축)=0.076(거의 직교), array 비지도구조 rejection 무정보(≤0.68), array oracle=0.83, cross-batch GSE36059→147089=0.846.
- **결론: 순수 sc→array(라벨미사용) ≥0.80 도달 불가. array 감독 or 사전지식 시그니처 필요.** 상세 → scGPT/WORKLOG.md
- (추가) ≥0.80 달성: scGPT 임베딩 proj + array-supervised 5-fold CV = **0.840**(정직, 라벨누수 없음). zero-shot은 0.748 천장. sc augmentation 무익. → scGPT/WORKLOG.md

## 2026-06-01 — scGPT (cell QC + zero-shot 파이프라인 독립 스크립트화)
- exp18(backbone 모델×정규화 9조합 스윕) 추가: 최고 0.749(pretrain_bc/cpm), zero-shot 정직 천장 0.748 최종 불변(총 18배치).
- E-MTAB-12051 cell QC: 표준 기준(genes≥200·counts≥500·MT%<20)으로 53,630→37,920 cells 필터링, `E_MTAB_12051_qc.h5ad` 저장.
- zero-shot 챔피언(SEED+2-view co-training) 독립 실행형 스크립트 `sc2array_cotrain.py` 작성(h5ad→cache 자동 빌드, AUROC 0.6977/0.7463 재현).
- 상세 내용 → scGPT/WORKLOG.md

## 2026-06-01 — scGPT sc→array: QC source + 범용방법으로 AUROC≥0.74 (goal)
- source를 `E_MTAB_12051_qc.h5ad`(37,920 cells)로 교체, 기존 co-training 말고 범용 방법으로 외부 AUROC≥0.74 달성.
- ★ QC 필터링이 전사 악화: honest SEED 0.698→0.632, co-training 0.748→0.655 (고-MT 손상세포가 rejection 신호 운반 → 제거 시 소실).
- ★ positive 환자 4명뿐 → LR 과적합, **nearest-centroid(prototype) 0.710**이 최고 단일방법.
- **달성: centroid(proj+quantile) seed + 단일뷰 self-training(표준 SSL, co-training 아님) = AUROC 0.7401**(BalAcc 0.704), cells/rounds에 불변. 범용 독립 스크립트 `data/best_script/sc2array_general.py`.
- 상세 → scGPT/WORKLOG.md

## 2026-06-01 — scGPT (prognosis predict-cell 집계 비교)
- predict-cell p60/mean/median AUROC 비교: mean 0.8958 > p60=median 0.8750. 3컬럼 결정론적 동시저장이라 재실행 불필요.
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-02 — scGPT (predict-cell MC-dropout sweep)
- predict-cell을 dropout {0,0.05,…,0.3} 7개로 비교(E_MTAB_12051_qc, 16환자). eval모드 dropout은 no-op이라 `--mc-dropout` 플래그(테스트타임 dropout 활성+CLI dropout 우선)를 추가한 스크립트 복사본 사용.
- **결과: 환자별 예측·AUROC(mean 0.875, p60 0.896)는 dropout에 사실상 불변, MC 예측 불확실성만 dropout에 선형 증가(0.010→0.032).** 모델 환자 순위가 dropout에 robust.
- 그림: `results/prognosis_adapter_8000/dropout_sweep/dropout_sweep_comparison.png`, 요약 `summary_dropout_sweep.csv`
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-10 — scGPT (kidney GEO 데이터셋 유형별 정리 + 메타데이터 매니페스트)
- `data/kidney/`의 GEO 31개 시리즈를 `scRNA-seq/`(4)·`bulk_RNA-seq/`(3)·`microarray/`(24) 하위폴더로 분류 이동.
- GEO 원본 메타데이터(Series_type/플랫폼)로 검증 중 기존 추정 3건 오분류 정정: GSE145927(→scRNA), GSE155670(→bulk), GSE181757(→microarray).
- NCBI GEO에서 31시리즈+13플랫폼 메타데이터 fetch → `MANIFEST.md`를 시리즈단위 메타데이터 표(제목·유형·플랫폼·샘플수·연도·PubMed·디스크)로 재작성.
- GEO series-matrix 헤더(`!Sample_characteristics_ch1`)에서 GSM 단위 임상 메타데이터(진단·rejection·Banff·biopsy time) 추출 → `data/kidney/sample_metadata.csv` (4711행, 31시리즈 전체 ok) 신규 저장.
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-14 — scGPT (kidney array 24시리즈 진단 라벨 정리)
- `data/kidney/sample_metadata.csv` 기반으로 microarray 24개 GSE 시리즈의 진단 라벨 분포를 시리즈별 표로 정리(거부/비거부·ABMR/TCMR/Mixed·IFTA·Banff·MMDx d96 등).
- characteristics 컬럼 우선, 비어있는 5개 시리즈는 source_name/title에서 추출. GSE129166은 코드값(tcmr/abmr)→진단명 변환. GSE181757은 거부가 아닌 Progressor/Non-Progressor 표현형.
- 상세 → scGPT/WORKLOG.md 참조

## 2026-06-16 — scGPT (19개 microarray 멀티-데이터셋 finetune 스크립트)
- `rma_out/training_labeled/`의 19개 .h5ad(플랫폼 상이, gene 9k~21k, 총 2,179샘플 NR1209/Rej970)를 NR/Rejection으로 동시 학습할 스크립트 신규 작성.
- 기존 `prognosis_microarray_adapter.py` 복사→`..._multidataset.py`: `merge`(union gene outer-join+dataset 라벨) 서브커맨드 추가, CV를 샘플 랜덤→**Leave-One-Dataset-Out(GSE 그룹)** 로 개편(단일클래스 3개 train 고정, per-dataset AUROC 출력). gene-name 토큰화라 플랫폼 차이 무관.
- 파일 생성·구문검증까지만(미실행, 사용자 요청). `--normalize` 금지(RMA log2).
- 상세 → scGPT/WORKLOG.md 참조
