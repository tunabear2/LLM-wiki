# Language Models are Unsupervised Multitask Learners

## 기본 정보

- Citation key: `radfordLanguageModelsUnsupervised2019`
- Item type: technicalReport
- Authors: Alec Radford; Jeffrey Wu; Rewon Child; David Luan; Dario Amodei; Ilya Sutskever
- URL: [Link](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- Source/date: OpenAI technical report, 2019

## 1. 한 줄 요약

GPT-2는 WebText로 학습한 autoregressive Transformer language model이 zero-shot task transfer를 어느 정도 수행할 수 있음을 보여준 논문이다.

## 2. 왜 중요한가

이 논문은 "언어모델을 크게 학습하면 명시적 supervised dataset 없이도 여러 NLP task를 prompt 형태로 수행할 수 있다"는 흐름을 넓혔다. 이후 GPT-3의 few-shot learning, instruction tuning, prompt engineering 논의가 이 방향 위에서 발전했다.

## 3. 내 연구에 연결할 점

Bio/medical text mining에서는 task-specific classifier만 만들기보다, 논문 abstract, gene set 설명, 임상 phenotype 설명을 prompt로 넣어 zero-shot 또는 few-shot으로 구조화하는 접근의 출발점으로 볼 수 있다.

## 4. Bibliography

Radford, Alec, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. "Language Models are Unsupervised Multitask Learners." OpenAI, 2019.

