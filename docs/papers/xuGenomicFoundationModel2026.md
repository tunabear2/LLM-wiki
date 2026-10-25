---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# A Genomic Foundation Model for Interpreting Human Genetic Diversity

## 기본 정보

- Citation key: `xuGenomicFoundationModel2026`
- Item type: bioRxiv preprint
- Authors: QinYi Xu; ZhiKun Wu; Meijing Dong; Tianpeng Bao; Wenyan Nong; Xuanzhao Huang; Hongxi Yang; Yao Zhou; Xianfu Yi; Shijie Zhang; Dandan Huang; Pak Chung Sham; Wenhao Zhou; Mulin Jun Li
- Source: bioRxiv v1, posted 2026-10-21 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.19.760276](https://doi.org/10.64898/2026.10.19.760276); [code](https://github.com/mulinlab/hEVO)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

hEVO는 8개 cohort의 phased human haplotype diversity를 사전학습 신호로 사용해 compact model에서도 기능 주석·variant 해석·인간 진화 과제를 폭넓게 개선했다.

## 2. 연구 질문

Population-scale human haplotype variation을 label 없이 학습하면 reference-sequence 중심 genomic model보다 transferable variant representation을 얻을 수 있는가?

## 3. 데이터와 방법

550,237개 sample 중 63,809명의 WGS에서 복원한 47.84억 distinct haplotype sequence로 약 1 kb context model을 학습했다. Evo 2, Nucleotide Transformer, GPN 등과 기능 주석, 임상 pathogenicity, fine-mapped causal variant, experimental regulatory effect, ancestry·selection 과제를 비교했다.

## 4. 핵심 결과

- 19개 primary comparison 중 18개에서 1위를 기록했다.
- Task-specific training 없는 allele score가 여섯 variant benchmark에서 가장 높은 성능을 보였다.
- ClinVar retrospective reclassification에서 나중에 downgrade된 pathogenic classification 식별도 개선했다.

## 5. 한계

약 1 kb context라 distal regulation과 extended haplotype을 충분히 모델링하지 못했고 SNV만 학습해 indel·복잡 SV를 제외했다. Pretraining sequence/개인과 downstream label의 간접 노출 가능성이 남고, unseen population이나 prospective clinical utility를 독립 검증한 것은 아니다. 계산비용 때문에 일부 최대 comparator checkpoint도 평가하지 못했다.

## 6. 재현 또는 활용 포인트

Code가 공개되어 있다. Cohort별 haplotype 재구성, ancestry split, exact/overlap leakage와 model-size matched baseline을 확인하고 allele score calibration을 외부 population에서 다시 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient variant를 eQTL, allele-specific expression과 biopsy program에 연결하는 sequence prior 후보다. 약 1 kb 한계 때문에 HLA/KIR·장거리 enhancer·복잡 SV는 별도 도구와 phased 분석이 필요하다.

## 8. 관련 키워드

- Bio AI
- DNA-seq / Variant Analysis
- GWAS
- genomic foundation model

## 9. Bibliography

Xu, QinYi, et al. “A Genomic Foundation Model for Interpreting Human Genetic Diversity.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.19.760276](https://doi.org/10.64898/2026.10.19.760276).
