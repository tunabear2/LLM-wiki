---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Why Does Post-Training Quantization Work?

## 기본 정보

- Citation key: `chenWhyPostTrainingQuantization2026`
- Item type: arXiv preprint
- Authors: Yuxiang Chen; Michael Beyer; Jun Zhu; Jianfei Chen
- arXiv: 2609.11716
- DOI: 10.48550/arXiv.2609.11716
- URL: [arXiv](https://arxiv.org/abs/2609.11716)
- Source/date: arXiv v1, submitted 2026-09-10
- 주 카테고리: LLM / Transformer

## 1. 한 줄 요약

사전학습된 LLM의 post-training quantization 오차가 층 사이에서 부분 상쇄되고 LM head가 상위 토큰을 우선 보존한다는 두 메커니즘으로, 낮은 정밀도에서도 출력이 비교적 안정적인 이유를 설명한다.

## 2. 연구 질문

각 층에서 생기는 양자화 오차가 깊이에 따라 누적될 것으로 예상되는데도, 별도의 quantization-aware training 없이 사전학습 모델이 성능을 유지하는 이유는 무엇인가?

## 3. 데이터와 방법

Full-precision과 quantized forward pass의 hidden state를 층별로 비교하고, 무작위 초기화 모델과 사전학습 모델에서 오차가 전파되는 양상을 대조했다. 이어 각 층이 새로 만드는 오차와 입력에서 물려받은 오차의 방향 관계를 정량화하고, 마지막 LM head의 기하가 토큰 logit과 확률 변화에 미치는 영향을 여러 모델과 양자화 설정에서 분석했다.

## 4. 핵심 결과

사전학습 모델에서는 한 층이 새로 만드는 오차가 입력 오차와 반대 방향을 띠어 부분적으로 상쇄됐고, 이 성질은 pretraining 중 형성됐다. 또한 LM head는 모델이 높은 순위를 부여한 토큰의 점수와 확률을 상대적으로 잘 보존했다. 두 현상이 함께 작동해 hidden-state 차이가 여러 층을 지나도 next-token output 변화가 작게 유지된다고 보고했다.

## 5. 한계

아직 peer review 전인 preprint다. 초록에는 평가한 모델군, bit-width, quantizer별 세부 결과가 제시되지 않아 모든 architecture와 quantization 방식에 일반화할 수 없다. 상위 토큰 확률 보존이 긴 생성, calibration, safety 또는 domain-specific biological model의 downstream 성능 보존을 뜻하는지도 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

- 같은 checkpoint에서 full-precision과 quantized activation을 층별로 저장해 누적 오차와 새 오차의 내적 또는 방향 관계를 비교한다.
- Pretrained model과 architecture-matched random initialization을 함께 평가해 pretraining 효과를 분리한다.
- Perplexity뿐 아니라 downstream accuracy, calibration, 긴 생성의 오류 누적을 bit-width와 quantizer별로 보고한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Genomic language model이나 single-cell foundation model을 제한된 GPU 환경에 배포할 때 PTQ를 선택하는 이론적 근거가 될 수 있다. 다만 rejection classification, cell-state annotation과 variant prioritization 성능이 실제로 유지되는지는 renal·immune external cohort에서 full-precision baseline과 직접 비교해야 한다.

## 8. 관련 키워드

- LLM / Transformer
- Post-training quantization
- Hidden-state error
- Residual error cancellation
- LM head geometry
- Efficient inference

## 9. Bibliography

Chen, Yuxiang, Michael Beyer, Jun Zhu, and Jianfei Chen. “Why Does Post-Training Quantization Work?” arXiv:2609.11716, 2026. [https://doi.org/10.48550/arXiv.2609.11716](https://doi.org/10.48550/arXiv.2609.11716).
