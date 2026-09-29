---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-29'
tags:
- wiki/paper
---

# Donor and recipient immune programs underlying delayed graft function in kidney transplantation revealed by temporal single-cell profiling

## 기본 정보

- Citation key: `makDonorRecipientImmune2026`
- Item type: journalArticle
- Authors: Martin L. Mak; Julia M. Murphy; Jessica A. Mathews; Shenghui Su; Ana Konvalinka; Slava Epelman; Sarah Q. Crome
- Journal: Kidney International
- DOI: 10.1016/j.kint.2026.07.035
- PMID: 42772447
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42772447/); [DOI](https://doi.org/10.1016/j.kint.2026.07.035)
- Source/date: online ahead of print 2026-09-22
- 주 카테고리: scRNA-seq
- 교차 카테고리: Transcriptomics / Platform

## 1. 한 줄 요약

생체·사체 donor kidney의 이식 전 상태와 delayed graft function이 발생한 사체이식 신장의 전후 변화를 single-cell·spatial transcriptomics로 연결해, 지속되는 donor macrophage와 새로 유입된 interferon-stimulated recipient macrophage 프로그램을 구분했다.

## 2. 연구 질문

Living donor와 deceased donor allograft의 이식 전 immune landscape는 어떻게 다르며, delayed graft function 초기에는 donor-derived resident immune cell과 recipient-derived infiltrating cell이 어떤 시간적·공간적 회로를 형성하는가?

## 3. 데이터와 방법

이식 전 living donor kidney 20개와 deceased donor kidney 6개를 scRNA-seq으로 비교하고, 별도의 deceased donor 2개는 spatial transcriptomics로 분석했다. Delayed graft function이 발생한 deceased-donor transplant recipient 8명의 matched pre/post allograft 16개 sample에는 fixed single-cell RNA profiling을 적용해 donor·recipient immune program의 시간 변화를 추적했다.

## 4. 핵심 결과

Deceased donor의 resident macrophage는 chemokine, cytokine과 antigen-presentation gene 발현이 낮고 autophagy·ubiquitination transcript가 높았으며 이식 후에도 남아 여러 parenchymal population과 상호작용할 위치에 있었다. Amphiregulin-expressing NK cell과 TIGIT·KLRC1(NKG2A)을 발현하는 CD8 T cell은 감소한 반면 KLRK1(NKG2D)과 pro-inflammatory signature를 가진 CD8 T cell은 이식 전후 모두 풍부했다. 초기 이식 후에는 CXCL10, TNFSF10, TNFSF13B, CCL8, ICAM1을 발현하는 interferon-stimulated recipient-derived macrophage가 새로 나타나 B·T-cell recruitment와 activation 후보 회로를 형성했다.

## 5. 한계

Deceased donor baseline은 6개, spatial 분석은 2개, temporal DGF cohort는 8쌍으로 작다. 시간 분석이 DGF가 발생한 deceased-donor transplant에 집중되어 living-donor 또는 deceased-donor non-DGF 대조군과 같은 방식으로 비교되지 않았다. 관찰적 transcriptomic·spatial association이므로 제안한 ligand–receptor 회로나 macrophage 기능의 인과성, 장기 graft outcome 예측력은 기능 실험과 독립 cohort에서 검증해야 한다.

## 6. 재현 또는 활용 포인트

- Pre/post sample pairing을 유지하고 donor origin 판정 방법과 신뢰도를 함께 기록한다.
- Fresh scRNA-seq과 fixed profiling의 chemistry 차이를 생물학적 시간 변화와 분리해 점검한다.
- Warm·cold ischemia time, immunosuppression, biopsy 시점, dialysis 기준과 batch를 공변량으로 남긴다.
- PubMed abstract에는 공개 accession과 분석 코드가 명시되지 않아 재사용 전 본문·보충자료의 접근 조건을 확인해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

연구 주제에 직접 해당한다. DGF를 하나의 bulk injury signature로 처리하지 않고 donor-resident macrophage의 억제·stress program과 recipient-derived interferon macrophage의 유입을 분리해 biomarker와 개입 시점을 설계할 수 있다. 향후 rejection·recovery trajectory와 연결하려면 non-DGF, TCMR, ABMR 및 장기 graft-loss cohort에서 같은 cell state를 외부 검증해야 한다.

## 8. 관련 키워드

- Kidney transplantation
- Delayed graft function
- scRNA-seq
- Spatial transcriptomics
- Donor-derived macrophage
- Recipient-derived macrophage
- Ischemia–reperfusion injury

## 9. Bibliography

Mak, Martin L., Julia M. Murphy, Jessica A. Mathews, Shenghui Su, Ana Konvalinka, Slava Epelman, and Sarah Q. Crome. “Donor and Recipient Immune Programs Underlying Delayed Graft Function in Kidney Transplantation Revealed by Temporal Single-Cell Profiling.” Kidney International, 2026. [https://doi.org/10.1016/j.kint.2026.07.035](https://doi.org/10.1016/j.kint.2026.07.035).
