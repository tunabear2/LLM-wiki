---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-07'
tags:
- wiki/paper
---

# scProtoTransformer: Scalable reference mapping across molecules, cells, and donors

## 기본 정보

- Citation key: `tangScProtoTransformer2026`
- Item type: journalArticle
- Authors: Zhenchao Tang; Haohuai He; Shouzhi Chen; Jun Zhu; Tianxu Lv; Jiale Zhou; Jiehui Huang; Yaokun Li; Guanxing Chen; Linlin You; Calvin Yu-Chian Chen
- DOI: 10.1126/sciadv.aef0286
- PMID: 42664347
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42664347/)
- Source/date: PubMed / Science Advances, published and indexed 2026-08-28

## 1. 한 줄 요약

scProtoTransformer는 pathway prototype token과 scGPT 지식 증류를 결합해 gene·cell·donor 수준의 scalable reference mapping을 수행한다.

## 2. 왜 중요한가

약 300개 pathway prototype으로 gene expression을 압축하고 frozen foundation model embedding을 teacher로 사용해 큰 pretraining corpus의 일부만으로 representation을 학습한다. Batch robustness와 biological interpretability를 계산 효율과 함께 다룬다.

## 3. 내 연구에 연결할 점

다기관 kidney transplant biopsy를 donor-level로 mapping할 때 pathway prototype이 center/batch 차이를 줄이면서 HLA·IFN·endothelial signal을 보존하는지 검증할 수 있다. Teacher scGPT와의 중복·pretraining exposure는 별도로 감사해야 한다.

## 4. Bibliography

Tang, Zhenchao, Haohuai He, Shouzhi Chen, et al. "scProtoTransformer: Scalable reference mapping across molecules, cells, and donors." _Science Advances_ 12, no. 35 (2026): eaef0286. [https://doi.org/10.1126/sciadv.aef0286](https://doi.org/10.1126/sciadv.aef0286).
