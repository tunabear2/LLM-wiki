---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-03'
tags:
- wiki/paper
---

# Residual-stream geometry of single-cell foundation models carries incremental gene-regulatory signal across tissues

## 기본 정보

- Citation key: `kendiukhovResidualStreamGeometry2026`
- Item type: journalArticle
- Authors: Ihor Kendiukhov
- DOI: 10.1186/s12859-026-06538-5
- PMID: 42527907
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42527907/)
- Source/date: PubMed / BMC Bioinformatics, indexed 2026-07-30

## 1. 한 줄 요약

scGPT와 Geneformer residual-stream gene geometry는 expression-based GRN 위에 조직별 추가 TF–target 신호를 제공하지만, 보지 못한 TF와 target을 동시에 평가하면 이득이 거의 사라진다.

## 2. 왜 중요한가

Tabula Sapiens의 kidney, immune, lung context에서 TRRUST edge를 사용해 expression confound와 여러 null control을 분리했다. Multi-layer residual bundle은 kidney에서 가장 큰 ΔAUROC를 보였지만 절대 성능은 0.60–0.69 수준이어서, geometry는 독립적인 regulatory classifier보다 edge 재순위화용 보조 근거로 해석해야 한다.

## 3. 내 연구에 연결할 점

Kidney rejection에서 scFM geometry로 HLA/IFN/endothelial TF–target 후보를 만들 때 kidney-specific 신호가 있다는 점은 유용하다. 다만 TF와 target을 모두 hold out한 검증, degree/expression-matched negatives, GENIE3·co-expression·perturbation evidence를 함께 사용해 새로운 regulatory edge로의 일반화를 검증해야 한다.

## 4. Bibliography

Kendiukhov, Ihor. "Residual-stream geometry of single-cell foundation models carries incremental gene-regulatory signal across tissues." _BMC Bioinformatics_, 2026. [https://doi.org/10.1186/s12859-026-06538-5](https://doi.org/10.1186/s12859-026-06538-5).
