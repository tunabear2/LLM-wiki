# LoRA: Low-Rank Adaptation of Large Language Models

## 기본 정보

- Citation key: `huLoRALowRank2021`
- Item type: conferencePaper
- Authors: Edward J. Hu; Yelong Shen; Phillip Wallis; Zeyuan Allen-Zhu; Yuanzhi Li; Shean Wang; Lu Wang; Weizhu Chen
- DOI: 10.48550/arXiv.2106.09685
- URL: [Link](https://arxiv.org/abs/2106.09685)
- Source/date: arXiv / ICLR, 2021-2022

## 1. 한 줄 요약

LoRA는 pretrained model weight를 고정하고 low-rank trainable matrix를 주입해, full fine-tuning보다 훨씬 적은 parameter와 memory로 adaptation하는 방법이다.

## 2. 왜 중요한가

대형 모델을 여러 downstream task에 맞추는 비용을 크게 낮췄다. Adapter, prompt tuning, QLoRA 등 parameter-efficient fine-tuning 흐름의 중심에 있다.

## 3. 내 연구에 연결할 점

scGPT나 biomedical LLM을 transplant rejection task에 맞출 때, full fine-tuning 전에 LoRA류 PEFT를 baseline으로 두면 계산량과 overfitting을 줄일 수 있다.

## 4. Bibliography

Hu, Edward J., Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. "LoRA: Low-Rank Adaptation of Large Language Models." _ICLR_, 2022. [https://doi.org/10.48550/arXiv.2106.09685](https://doi.org/10.48550/arXiv.2106.09685).

