---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-24'
tags:
- wiki/paper
---

# Integrating Unsupervised Clustering with Transformer-Based Models for De Novo Cell Population Identification

## 기본 정보

- Citation key: `guoIntegratingUnsupervisedClustering2026`
- Item type: preprint
- Authors: Y. Guo; G. Duan; G. Xu; C. Liu; J. Chang; Y. Han; X. Li; S. Gao
- DOI: 10.64898/2026.11.12.766182
- URL: [Link](https://doi.org/10.64898/2026.11.12.766182)
- Source/date: bioRxiv v1, posted 2026-11-16

## 1. 한 줄 요약

Fine-tuned Geneformer-V1 classifier의 class-probability matrix를 다시 clustering해 training label에 없던 de novo cell population을 찾는 SCPM 기반 방법이다.

## 2. 왜 중요한가

Closed-set classifier의 softmax output을 unsupervised clustering input으로 재사용해 colorectal-cancer stem-cell 후보와 marker를 제안했다. Foundation model을 annotation 자동화뿐 아니라 unknown-population discovery에 연결하지만 검증은 한 공개 암 dataset 중심이다.

## 3. 내 연구에 연결할 점

기존 reference에 없는 rejection-associated state를 찾는 데 참고할 수 있다. 다만 softmax geometry가 fine-tuning label과 batch를 재현할 수 있으므로 donor·center holdout, raw-expression clustering, marker replication을 함께 요구해야 한다.

## 4. Bibliography

Guo, Y., G. Duan, G. Xu, C. Liu, J. Chang, Y. Han, X. Li, and S. Gao. "Integrating Unsupervised Clustering with Transformer-Based Models for De Novo Cell Population Identification." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.12.766182](https://doi.org/10.64898/2026.11.12.766182).
