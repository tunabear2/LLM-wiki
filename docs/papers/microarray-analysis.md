# Microarray Analysis Paper Notes

Microarray 분석 섹션은 probe-level intensity에서 normalized expression matrix, differential expression, batch correction, public cohort reuse까지 이어지는 흐름을 공부하기 위한 공간이다. Kidney transplant 자료에서는 오래된 public cohort가 microarray인 경우가 많으므로, bulk RNA-seq/scRNA-seq와 함께 쓰려면 platform-specific bias를 먼저 이해해야 한다.

## 핵심 질문

- Probe-level signal을 gene-level expression으로 요약할 때 어떤 background correction, normalization, summarization이 들어가는가?
- Affymetrix, Illumina, Agilent 같은 array platform과 probe annotation 차이가 downstream DEG와 classifier에 어떤 영향을 주는가?
- Batch, lab, date, platform 차이를 biological signal과 분리할 수 있는가?
- Public GEO microarray cohort를 재사용할 때 raw CEL/IDAT 파일과 processed matrix 중 무엇을 써야 하는가?
- Microarray expression을 bulk RNA-seq 또는 scRNA-seq pseudobulk와 결합할 때 scale/dynamic range 차이를 어떻게 점검할 것인가?

## 공부 순서

| Paper | 초점 | 내 연구와 연결 |
| --- | --- | --- |
| [MIAME](brazmaMIAME2001.md) | Microarray experiment reporting standard | GEO/ArrayExpress metadata와 reproducibility를 점검하는 기준 |
| [GEO](barrettGEO2002.md) | Public gene expression repository | 신장이식 public cohort를 찾고 metadata를 재구성하는 출발점 |
| [RMA](irizarryRMA2003.md) | Affymetrix probe-level background correction, quantile normalization, summarization | CEL 파일에서 comparable expression matrix를 만드는 기본 preprocessing |
| [limma](smythLimma2004.md) | Linear model과 empirical Bayes moderated statistics | Microarray DEG와 covariate-adjusted analysis의 표준 baseline |
| [ComBat](johnsonComBat2007.md) | Empirical Bayes batch-effect correction | 여러 GEO cohort 또는 platform batch를 합칠 때 기본 보정법 |
| [SAM](tusherSAM2001.md) | Permutation/FDR 기반 microarray DEG scoring | 초기 high-dimensional DEG 분석과 FDR 사고방식 이해 |
| [RNA-Seq vs Microarray in Activated T Cells](zhaoComparisonRNASeqMicroarray2014.1.16..md) | Microarray와 RNA-seq platform 차이 | Microarray-to-RNA-seq/scRNA-seq transfer에서 dynamic range와 low-expression 차이 해석 |

## 분석 체크리스트

- Raw data가 있으면 platform별 표준 preprocessing(RMA/neqc 등)을 우선 검토한다.
- Probe ID를 gene symbol로 바꿀 때 multiple probes per gene, outdated annotation, cross-hybridization을 기록한다.
- PCA/MDS에서 batch, platform, disease label, center, sample date가 어떻게 분리되는지 먼저 본다.
- DEG 분석에는 fold change, moderated statistic, adjusted P-value, effect direction을 함께 확인한다.
- RNA-seq와 결합할 때는 gene intersection, per-platform normalization, external validation을 분리해서 설계한다.
