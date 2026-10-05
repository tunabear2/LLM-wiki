---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-05'
tags:
- wiki/paper
---

# When Do Biological Reasoning Models Use Their Biological Inputs?

## 기본 정보

- Citation key: `fangWhenBiologicalReasoning2026`
- Item type: preprint
- Authors: Ada Fang; Nikitha Thoduguli; Lukas Fesser; Hanlin Zhang; Sham M. Kakade; Marinka Zitnik
- DOI: 10.48550/arXiv.2610.00898
- URL: [Link](https://doi.org/10.48550/arXiv.2610.00898)
- Source/date: arXiv v1, submitted 2026-10-01

## 1. 한 줄 요약

여섯 biological reasoning model의 DNA·protein·single-cell 입력을 교란해, 높은 정확도나 representation의 probe 가능성이 실제 biological input 사용을 보장하지 않음을 보인다.

## 2. 왜 중요한가

저자들은 biological input shuffle, text–representation evidence conflict, linear probe와 reasoning-trace 분석을 함께 사용한다. 일부 모델은 informative foundation embedding을 받아도 사실상 text를 따랐고, CellWhisperer와 Cell2Sentence 계열에서는 cell/gene 입력 기여가 확인돼 모델별 차이를 드러냈다.

## 3. 내 연구에 연결할 점

Rejection 설명 모델이 scFM embedding을 입력으로 받는다는 사실만으로 omics-grounded reasoning을 주장하면 안 된다. Cell embedding shuffle, 상충하는 임상 text, input ablation과 counterfactual gene program을 사용해 예측과 설명이 실제 biopsy signal에 의존하는지 감사해야 한다.

## 4. Bibliography

Fang, Ada, Nikitha Thoduguli, Lukas Fesser, Hanlin Zhang, Sham M. Kakade, and Marinka Zitnik. "When Do Biological Reasoning Models Use Their Biological Inputs?" _arXiv_, 2026. [https://doi.org/10.48550/arXiv.2610.00898](https://doi.org/10.48550/arXiv.2610.00898).
