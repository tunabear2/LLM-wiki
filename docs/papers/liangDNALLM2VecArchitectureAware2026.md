---
type: paper
status: reference
rag_priority: medium
updated: '2026-10-18'
tags:
- wiki/paper
---

# DNA-LLM2Vec: Architecture-Aware Task-Conditioned Adaptation of Decoder DNA Foundation Models

## 기본 정보

- Citation key: `liangDNALLM2VecArchitectureAware2026`
- Item type: bioRxiv preprint
- Authors: Yuan Liang; Ke Zhai; Yujian Gan; Siyou Li; Juexi Shao; Grant H. Watson; Massimo Poesio
- Source: bioRxiv v1, posted 2026-10-14 (not peer reviewed)
- Original: [DOI: 10.64898/2026.10.07.757259](https://doi.org/10.64898/2026.10.07.757259); [code and checkpoints](https://github.com/semi-nothing/dna-llm2vec)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

DNA-LLM2Vec는 causal DNA decoder를 bidirectional encoder로 바꾸고 masked next-token prediction과 strand/position contrastive view를 적용하되, 최적 변환이 backbone과 genomic task에 따라 다름을 보였다.

## 2. 연구 질문

긴 서열에 효율적인 decoder DNA foundation model을 upstream·downstream 문맥이 모두 필요한 genomic representation task에 재사용할 수 있는가?

## 3. 데이터와 방법

DNAGPT와 HyenaDNA에 bidirectional context 개방, masked next-token prediction, reverse-complement 및 crop-based contrastive learning을 단계적으로 적용했다. GB, NT, GUE, GUE+EPI에서 묶은 일곱 task family를 frozen linear probe로 비교하고, causal-eQTL distal variant-effect prediction과 base-pair mutagenesis로 표현을 진단했다.

## 4. 핵심 결과

- Extended-context EPI에서 crop-based positional contrastive learning이 가장 유리했고 Avg-EPI MCC는 DNAGPT 27.5%, HyenaDNA 26.7%였다.
- 짧고 국소적인 task에서는 이득 방향이 backbone과 tokenization에 따라 달라 보편적인 단일 adaptation recipe가 없었다.
- Bidirectional context와 MNTP는 특히 먼 거리 causal-eQTL effect prediction과 motif-aware contact structure를 개선했다.

## 5. 한계

Human-only DNAGPT 한 scale과 HyenaDNA 한 backbone을 사용했고 일부 control은 single seed였다. Multi-species encoder와 통제된 비교가 아니며, 작은 Virus-COVID·splice family와 sequence-level EPI 결과는 더 넓은 검증이 필요하다. 한 저자는 Recursion 직원이며 회사 지원을 받았다.

## 6. 재현 또는 활용 포인트

Code와 checkpoint, 공개 GB/GUE/NT dataset이 제공된다. 평균 score 하나 대신 task 길이, strand invariance, backbone, positive/negative transfer를 나눠 보고해야 한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor·recipient variant를 eQTL과 biopsy expression에 연결할 때 distal regulatory effect embedding 후보가 된다. 실제 이식 cohort와 phased donor–recipient genotype에서는 별도 검증이 필요하다.

## 8. 관련 키워드

- Bio AI
- DNA foundation model
- variant-effect prediction
- contrastive learning

## 9. Bibliography

Liang, Yuan, et al. “DNA-LLM2Vec: Architecture-Aware Task-Conditioned Adaptation of Decoder DNA Foundation Models.” bioRxiv, 2026. [https://doi.org/10.64898/2026.10.07.757259](https://doi.org/10.64898/2026.10.07.757259).
