---
type: paper
status: reference
rag_priority: medium
updated: '2026-08-10'
tags:
- wiki/paper
---

# CellDuality: Unlocking Biological Reasoning in LLMs with Self-Supervised RLVR

## 기본 정보

- Citation key: `chenCellDualityUnlocking2026`
- Item type: conferencePaper
- Authors: Yuhang Chen; Zhen Tan; Ruichen Zhang; Mufan Qiu; Tianlong Chen
- PMID: 42559559
- URL: [Link](https://pubmed.ncbi.nlm.nih.gov/42559559/)
- Source/date: PubMed / ICLR 2026, indexed 2026-08-06

## 1. 한 줄 요약

CellDuality는 단일세포 biological outcome을 예측하는 forward task와 초기 perturbation을 복원하는 inverse task의 일관성을 self-supervised reward로 삼아 LLM의 single-cell reasoning을 강화한다.

## 2. 왜 중요한가

별도의 ground-truth verification label 없이 complementary task duality로 RLVR 신호를 만든다. 특히 out-of-distribution perturbation prediction에서 일반 fine-tuning보다 나은 성능을 보고해, transcriptomic prediction과 자연어 설명을 잇는 biological reasoning model의 가능성을 보여준다.

## 3. 내 연구에 연결할 점

면역억제제, cytokine, ischemia-reperfusion 조건의 rejection response를 forward/inverse consistency로 점검하는 실험 설계에 참고할 수 있다. 생성된 설명은 scFM embedding이나 DEG/pathway 결과와 대조하되, causal mechanism으로 해석하기 전 독립 perturbation과 외부 cohort 검증이 필요하다.

## 4. Bibliography

Chen, Yuhang, Zhen Tan, Ruichen Zhang, Mufan Qiu, and Tianlong Chen. "CellDuality: Unlocking Biological Reasoning in LLMs with Self-Supervised RLVR." _International Conference on Learning Representations_, 2026. [https://pubmed.ncbi.nlm.nih.gov/42559559/](https://pubmed.ncbi.nlm.nih.gov/42559559/).
