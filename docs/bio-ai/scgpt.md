# scGPT

## 핵심 요약

scGPT는 single-cell multi-omics 데이터를 위한 generative pretrained Transformer 모델이다. 대규모 single-cell 데이터에서 cell과 gene의 표현을 학습하고, annotation, perturbation prediction, batch correction, multi-omics integration 같은 downstream task에 활용하는 것을 목표로 한다.

## 왜 중요한가?

Single-cell 데이터는 tissue, batch, protocol 차이가 크고 label이 부족한 경우가 많다. scGPT 같은 foundation model은 큰 데이터에서 미리 학습한 representation을 작은 실험 데이터에 transfer할 수 있다는 점에서 유용하다.

## 입력과 표현

- Gene을 token처럼 다룬다.
- Expression value는 token의 feature 또는 embedding으로 결합된다.
- Cell 하나는 gene-expression token들의 집합 또는 sequence로 표현된다.

## 활용 task

- Cell type annotation
- Batch correction
- Perturbation response prediction
- Multi-omics integration
- Gene network 또는 marker gene 탐색 보조

## 주의점

- 모델이 학습한 gene vocabulary와 내 데이터 gene symbol이 맞아야 한다.
- Preprocessing 방식이 논문/코드와 일치해야 한다.
- 모델 예측은 biological hypothesis 생성 도구로 보고, wet/dry validation이 필요하다.

## 내 연구에 적용할 아이디어

Kidney transplant rejection scRNA-seq에서 rejection-specific immune cell state를 embedding space에서 비교한다. Stable graft와 rejection sample의 cell embedding 차이를 보고, rejection marker gene 후보를 추출한다.

장기 이식 예후 예측 모델에서는 train/test domain 비대칭에 따라 encoder를 freeze할지 fine-tuning할지 나누어 실험한다. 자세한 설계 메모는 [Transplant Prognosis Model Notes](../reports/transplant-prognosis-model-notes.md)에 정리한다.

## 관련 자료

- [scGPT Nature Methods](https://www.nature.com/articles/s41592-024-02201-0)

## 같이 읽을 Paper Notes

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../papers/cuiScGPTFoundation2024.md)
- [Bayesian Hyperparameter Optimization Improves scGPT Fine-Tuning for Single-Cell Multi-Omics Integration](../papers/tayBayesianHyperparameterOptimization2026.md)
- [Causal circuit tracing reveals distinct computational architectures in single-cell foundation models](../papers/kendiukhovCausalCircuitTracing2026.md)
- [Evaluating the learnability of single-cell large language models on multiple tasks](../papers/yanEvaluatingLearnabilitySingleCell2026.md)
