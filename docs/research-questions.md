# Research Questions

이 문서는 현재 연구에서 가장 중요한 질문들을 정리하고, 관련 논문/개념/실험 아이디어를 연결하기 위한 공간이다.

## Q1. Domain shift를 어떻게 해결할 것인가?

### 핵심 질문

Single-cell foundation model이나 LLM 기반 bio-AI 모델을 실제 연구 데이터에 적용할 때, pretraining 데이터와 target dataset 사이의 domain shift를 어떻게 줄일 수 있을까?

특히 다음과 같은 차이가 모델 성능에 어떤 영향을 주는지 확인해야 한다.

- 조직 또는 세포 타입 차이
- 질병 상태 차이
- 실험 플랫폼 차이
- 전처리 방식 차이
- cohort, batch, lab effect 차이

### 왜 중요한가?

Pretrained model은 대규모 데이터에서 일반적인 표현을 학습하지만, 실제 downstream task에서는 target dataset의 분포가 pretraining 데이터와 다를 수 있다. 이 경우 embedding 품질이 떨어지거나, 특정 cohort 또는 batch에 과적합된 예측이 나올 수 있다.

따라서 domain shift를 줄이거나 견고하게 만드는 전략은 모델의 실제 연구 활용 가능성을 결정하는 핵심 문제다.

### 관련 개념

- [[single-cell-llm]]
- [[single-cell-foundation-models]]
- [[geneformer]]
- [[scgpt]]
- [[fine-tuning]]
- [[transcriptomics]]

### 가능한 접근

1. Pretrained embedding을 그대로 사용하고, target task classifier만 학습한다.
2. Target dataset에서 일부 layer만 fine-tuning한다.
3. Batch correction 또는 data integration을 먼저 수행한 뒤 모델에 입력한다.
4. Domain-adversarial training으로 batch/cohort 정보를 제거한다.
5. Source domain과 target domain을 나누어 cross-domain validation을 수행한다.
6. Cell type별로 domain shift 영향을 따로 평가한다.

### 먼저 해볼 실험

1. 같은 task에서 random split과 cohort split 성능을 비교한다.
2. Pretrained embedding이 batch, platform, disease status를 얼마나 분리하는지 UMAP으로 확인한다.
3. Fine-tuning 전후 embedding space가 target domain에 맞게 이동하는지 비교한다.
4. Cell type별 성능 차이를 확인해 어떤 세포군에서 domain shift가 가장 큰지 찾는다.

### 현재 가설

Domain shift는 전체 데이터에서 균일하게 나타나지 않고, 특정 cell type이나 특정 disease state에서 더 크게 나타날 가능성이 있다. 따라서 전체 성능 지표 하나만 보는 것보다, cell type별/condition별/domain별 성능을 분해해서 보는 것이 중요하다.

### 다음에 읽을 논문

- Geneformer 관련 downstream transfer 논문
- scGPT 관련 perturbation 또는 cell annotation 논문
- Single-cell domain adaptation 또는 batch correction 관련 논문

