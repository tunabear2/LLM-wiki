---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-14'
tags:
- wiki/paper
---

# Independent benchmark of H&E-based gene expression prediction in skin

## 기본 정보

- Citation key: `shaikhutdinovaIndependentBenchmarkGeneExpression2026`
- Item type: preprint
- Authors: Regina Shaikhutdinova; Sabina Gansberger; Julia Staller; Namrata Singh; Inigo Oyarzun; Martin Simon; Barbara Sterniczky; Philipp Tschandl; Johannes Griss
- DOI: 10.64898/2026.09.07.749926
- URL: [Link](https://www.biorxiv.org/content/10.64898/2026.09.07.749926v1)
- Source/date: bioRxiv v1, posted 2026-09-09

## 1. 한 줄 요약

세 skin disease context와 두 Xenium panel에서 H&E-to-single-cell gene-expression 방법을 독립 비교한 결과, 대부분의 gene 예측은 거의 무신호였고 foundation image embedding의 ridge regression이 복잡한 모델과 대등하거나 더 나았다.

## 2. 왜 중요한가

16개 model configuration을 비교했지만 신뢰할 수 있는 예측은 주로 keratinocyte-associated gene에 제한되었다. Predicted expression은 immune·fibroblast 등에서 cell identity와 spatial organization을 보존하지 못해, 이미지에서 single-cell transcriptome을 복원한다는 주장에 단순 pretrained-embedding baseline과 biological-structure 검증이 필수임을 보여준다.

## 3. 내 연구에 연결할 점

Kidney transplant H&E에서 rejection expression program을 추정할 때 pathology foundation model의 높은 평균 상관만으로 임상 활용을 주장하면 안 된다. Renal external cohort에서 immune/endothelial/tubular cell identity, Banff lesion의 spatial organization, HLA·IFN program을 gene별로 검증하고 ridge baseline과 비교해야 한다.

## 4. Bibliography

Shaikhutdinova, Regina, Sabina Gansberger, Julia Staller, Namrata Singh, Inigo Oyarzun, Martin Simon, Barbara Sterniczky, Philipp Tschandl, and Johannes Griss. "Independent benchmark of H&E-based gene expression prediction in skin." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.07.749926](https://doi.org/10.64898/2026.09.07.749926).
