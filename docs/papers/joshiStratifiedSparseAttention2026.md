---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-25'
tags:
- wiki/paper
---

# Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity

## 기본 정보

- Citation key: `joshiStratifiedSparseAttention2026`
- Item type: arXiv preprint
- Authors: Sahil Joshi; Prithvi Dixit; Aryan Katiyar; Agniva Chowdhury; Joseph E. Gonzalez; Anshumali Shrivastava; Aditya Desai; Kumar Krishna Agrawal
- Source: arXiv v1, submitted 2026-10-20
- Original: [arXiv:2610.28441](https://arxiv.org/abs/2610.28441); [code](https://github.com/skylight-org/SSA-Paper-Code)
- 주 카테고리: `LLM / Transformer`

## 1. 한 줄 요약

SSA는 높은 score token은 결정적으로 보존하고 나머지는 proxy score에 비례해 표본추출·포함확률 보정하여, 극단적 sparse attention에서 dense attention의 잔여 질량을 더 잘 복원한다.

## 2. 연구 질문

Top-k retrieval의 누락과 uniform sampling의 분산을 동시에 줄여 long-context sparse attention의 정확도–속도 trade-off를 개선할 수 있는가?

## 3. 데이터와 방법

Attention budget을 deterministic heavy-hitter stratum과 importance-sampled residual stratum으로 나눴다. RULER, LongBench, LOFT, AIME에서 Llama, Qwen, Ministral 계열 다섯 model(3B–27B)을 평가하고 CUDA/Triton kernel로 decode 성능을 측정했다.

## 4. 핵심 결과

- 50배 sparsity에서 Ministral-3-8B의 RULER-HARD 정확도는 strongest practical baseline 대비 32K에서 81.8%→84.2%, 128K에서 63.8%→69.3%로 올랐다.
- 이 설정은 dense attention 성능의 94%(32K), 85%(128K)를 회복했다.
- 1M context에서 FlashInfer 대비 최대 2.96배 decode speedup을 보였고 code와 kernel을 공개했다.

## 5. 한계

이득은 proxy score 품질, heavy-hitter/sampling budget과 custom kernel 구현에 의존한다. 평가가 선택한 다섯 model과 long-context benchmark에 집중되어 실제 RAG evidence recall·hardware별 end-to-end 비용은 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Dense, top-k, uniform hybrid와 같은 총 attention budget에서 비교하고 seed별 sampling variance를 보고한다. Context length, sparsity, heavy-hitter fraction과 kernel/hardware를 함께 고정한다.

## 7. Transcriptomics·신장이식 연구와의 연결

장문 논문·임상 문서 RAG에서 context 비용을 줄일 수 있지만, 희귀 rejection phenotype이나 낮은 빈도의 결정적 문장이 residual sampling에서 안정적으로 유지되는지 evidence-recall 검사가 필요하다.

## 8. 관련 키워드

- LLM / Transformer
- sparse attention
- importance sampling
- long-context inference

## 9. Bibliography

Joshi, Sahil, et al. “Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity.” arXiv:2610.28441, 2026. [https://arxiv.org/abs/2610.28441](https://arxiv.org/abs/2610.28441).
