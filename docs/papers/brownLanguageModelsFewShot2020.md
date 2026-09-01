---
type: paper
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/paper
---

# Language Models are Few-Shot Learners

## 기본 정보

- Citation key: `brownLanguageModelsFewShot2020`
- Item type: conferencePaper
- Authors: Tom B. Brown; Benjamin Mann; Nick Ryder; Melanie Subbiah; Jared Kaplan; Prafulla Dhariwal; et al.
- DOI: 10.48550/arXiv.2005.14165
- URL: [Link](https://arxiv.org/abs/2005.14165)
- Source/date: arXiv / NeurIPS, 2020

## 1. 한 줄 요약

GPT-3는 175B parameter autoregressive language model을 통해 gradient update 없이 prompt 안의 예시만으로 many-task few-shot learning이 가능함을 보였다.

## 2. 왜 중요한가

LLM의 핵심 사용 방식이 "fine-tune된 개별 모델"에서 "범용 모델 + 자연어 지시 + few-shot examples"로 넘어가는 전환점이다. 모델 규모, data scale, prompt design이 downstream behavior를 바꾸는 문제를 본격화했다.

## 3. 내 연구에 연결할 점

Kidney transplant 문헌 정리, phenotype coding, paper-note 초안 생성처럼 label이 적고 task가 계속 바뀌는 작업에서는 few-shot prompting이 실용적이다. 단, 생물의학 사실 검증은 retrieval과 citation 확인이 필수다.

## 4. Bibliography

Brown, Tom B., Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, et al. "Language Models are Few-Shot Learners." _NeurIPS_, 2020. [https://doi.org/10.48550/arXiv.2005.14165](https://doi.org/10.48550/arXiv.2005.14165).

