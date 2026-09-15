---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# OmniTCR: a foundation model unifying T cell receptor recognition prediction and conditional sequence generation

## 기본 정보

- Citation key: `zengOmniTCRFoundationModel2026`
- Item type: bioRxiv preprint
- Authors: Feiran Zeng; Duanyu Feng; Dandan Song; Li Ding; Zhenlin Tan; Qian Lei; Wenqiang Lei; An-Yuan Guo
- DOI: 10.64898/2026.09.10.750588
- URL: [bioRxiv](https://doi.org/10.64898/2026.09.10.750588)
- Source/date: bioRxiv v1, posted 2026-09-13
- 주 카테고리: Bio AI

## 1. 한 줄 요약

OmniTCR는 대규모 human immune-sequence corpus에서 TCR chain, peptide와 MHC를 함께 autoregressive 학습해 recognition prediction과 조건부 TCR 생성을 하나의 모델로 통합한다.

## 2. 연구 질문

방대한 단일 TCR sequence와 상대적으로 작은 TCR–peptide–MHC association 자료를 공동 학습하면, 별도로 개발되던 antigen recognition 예측과 receptor generation을 동시에 개선할 수 있는가?

## 3. 데이터와 방법

3억 2,800만 개로 formatting한 human immune-sequence record에서 113M-parameter autoregressive foundation model을 pretrain했다. Sequence-type token과 complementary component ordering을 사용해 개별 TCR chain부터 부분 또는 완전한 TCR–peptide–MHC association까지 같은 모델에 넣었다. Unseen epitope recognition, TCR–pMHC interaction, cancer와 healthy repertoire 분류, 조건부 sequence recovery를 내부 및 외부 benchmark에서 평가하고 일부 생성 후보는 구조 모델링으로 점검했다.

## 4. 핵심 결과

Unseen epitope에서 peptide–TCRβ recognition AUPRC 0.7009와 TCR–pMHC interaction AUPRC 0.8235를 기록해 가장 강한 비교 모델보다 각각 0.3396과 0.3451 높았다. 11개 독립 pan-cancer cohort의 cancer–healthy repertoire 분류에서는 평균 AUROC 0.9436을 보고했다. 내부·외부 generation benchmark에서도 가장 높은 sequence recovery를 보였고, 선택한 pMHC-conditioned CDR3β 후보의 구조적 개연성을 제시했다.

## 5. 한계

아직 peer review 전인 preprint이며, 생성 receptor 후보는 구조 모델링으로만 지지돼 실제 결합과 T-cell 기능을 입증하는 wet-lab 검증이 필요하다. 학습 자료와 평가가 human immune sequence 및 cancer cohort 중심이고, transplant alloantigen이나 면역억제 환경에서의 성능은 보고되지 않았다. 높은 repertoire 분류 성능이 cohort·assay 차이에 영향을 받지 않았는지도 별도 확인이 필요하다.

## 6. 재현 또는 활용 포인트

- Epitope뿐 아니라 patient와 cohort를 겹치지 않게 분리해 recognition generalization을 평가한다.
- TCR chain 구성, peptide, HLA allele별 성능과 calibration을 따로 보고한다.
- 생성 후보는 구조 점수에 그치지 않고 binding assay와 세포 기능 assay로 검증한다.
- Repertoire 분류에서는 sequencing depth, clonality와 batch를 통제한 단순 baseline을 함께 둔다.
- 공개 checkpoint: [loveCloud/OmniTCR](https://huggingface.co/loveCloud/OmniTCR)

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 biopsy 또는 혈액의 scRNA/TCR-seq에서 확장된 clonotype의 항원 인식 가능성을 우선순위화하고, rejection-associated T-cell state와 receptor specificity를 연결할 후보 모델이다. 다만 donor HLA·alloantigen 조합, 면역억제제 노출과 transplant-specific repertoire shift를 포함한 외부 cohort 및 기능 검증 없이는 기전으로 해석할 수 없다.

## 8. 관련 키워드

- Bio AI
- T-cell receptor
- Immune repertoire
- Autoregressive foundation model
- TCR–peptide–MHC recognition
- Conditional sequence generation

## 9. Bibliography

Zeng, F., D. Feng, D. Song, et al. “OmniTCR: A Foundation Model Unifying T Cell Receptor Recognition Prediction and Conditional Sequence Generation.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.10.750588](https://doi.org/10.64898/2026.09.10.750588).
