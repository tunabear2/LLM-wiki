---
type: paper
status: reference
rag_priority: high
updated: '2026-10-19'
tags:
- wiki/paper
---

# CellChain: Benchmarking Cross-Scale Evidence Use for Perturbation Reasoning

## 기본 정보

- Citation key: `xiaCellChainBenchmarkingCrossScale2026`
- Item type: preprint
- Authors: X. Xia; Y. Wang; S. Chen; L. Yu; H. Wu; W. Huang; C. Yao; Z. Gao; S. Sun
- arXiv: 2610.16346
- URL: [Link](https://arxiv.org/abs/2610.16346)
- Source/date: arXiv v1, submitted 2026-10-12

## 1. 한 줄 요약

CellChain은 provenance-aware evidence graph로 590개 perturbation case를 구성해 18개 foundation model의 gene dependency, cytokine axis와 drug sensitivity reasoning을 평가한다.

## 2. 왜 중요한가

Evidence coverage, composition과 biological assignment를 통제해 정보가 늘어도 정확도가 일관되게 개선되지 않고, matched history와 swapped history 사이에 큰 차이가 남음을 보인다. 최종 accuracy만으로 가려지는 correction과 새 오류를 decision transition으로 분해한다.

## 3. 내 연구에 연결할 점

Rejection target·drug reasoning에서 renal literature, pathway, transcriptomic evidence의 기여를 교체 실험으로 감사할 수 있다. 다만 single-cell FM 자체의 benchmark는 아니므로 expression-level prediction과 donor OOD 검증을 별도로 유지해야 한다.

## 4. Bibliography

Xia, X., et al. "CellChain: Benchmarking Cross-Scale Evidence Use for Perturbation Reasoning." _arXiv_, 2026. [https://arxiv.org/abs/2610.16346](https://arxiv.org/abs/2610.16346).
