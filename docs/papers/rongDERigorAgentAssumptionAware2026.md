---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# DE-Rigor-Agent: Assumption-Aware Differential Expression Analysis of Bulk RNA-seq

## 기본 정보

- Citation key: `rongDERigorAgentAssumptionAware2026`
- Item type: preprint
- Authors: Ziqi Rong; Changhu Wang; Chenxin Flora Jiang; Yiwen Yang; Jingyi Jessica Li
- Source: bioRxiv v1, posted 2026-11-11 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.09.765522](https://doi.org/10.64898/2026.11.09.765522)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

DE-Rigor-Agent는 bulk RNA-seq DE method를 실행하기 전에 입력·설계·분포 진단과 전문가 규칙으로 부적합한 방법을 제외하고 선택 근거를 남기는 LLM agent workflow다.

## 2. 연구 질문

LLM agent가 인기 있는 DESeq2·edgeR를 관성적으로 선택하는 대신 dataset별 통계 가정을 점검해 false-discovery inflation과 power loss를 줄일 수 있는가?

## 3. 데이터와 방법

Workflow를 input standardization, method filtering, retained-method execution의 세 단계로 나눴다. 여섯 DE method를 expert-curated criteria와 dataset diagnostic으로 평가했다. Small sample, zero inflation, outlier, pre-normalized input, confounded batch effect 등을 포함한 14개 scenario·140개 simulated dataset에서 두 general-purpose LLM agent와 비교했다.

## 4. 핵심 결과

- Method–dataset incompatibility가 FDR inflation 또는 power 감소로 이어졌다.
- 일반 LLM agent 두 종은 assumption을 보라는 prompt가 있어도 거의 모든 dataset에서 DESeq2나 edgeR를 선택했다.
- DE-Rigor-Agent의 filtering은 simulation에 넣은 incompatibility와 대체로 일치했고 random seed에 안정적이었으며 추가 계산비용은 작았다.

## 5. 한계

핵심 평가는 140개 simulation에 기반하며 실제 dataset에는 완전한 method-suitability truth가 없다. 여섯 방법 밖의 tool, 복잡한 repeated-measure design, LLM·prompt version 변화에 대한 일반화는 별도 검증이 필요하다.

## 6. 재현 또는 활용 포인트

Count matrix 여부, normalization 상태, design matrix rank, batch–phenotype confounding, sample size, zero/outlier diagnostic을 machine-readable log로 남긴다. Agent 선택과 별개로 각 방법의 FDR·power simulation 및 analyst review를 보존한다.

## 7. Transcriptomics·신장이식 연구와의 연결

소표본·batch confounding이 흔한 allograft bulk RNA-seq에서 자동 분석이 부적합한 method를 고르는 위험을 줄일 수 있다. Biopsy 반복측정과 donor/recipient covariate를 지원하는지 먼저 확인하고 수동 statistical review를 유지해야 한다.

## 8. 관련 키워드

- differential expression
- bulk RNA-seq
- LLM agent
- statistical assumptions

## 9. Bibliography

Rong, Zhiwei, et al. “DE-Rigor-Agent: An Agentic Workflow for Assumption-Aware Differential Expression Analysis of Bulk RNA-seq Data.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.09.765522](https://doi.org/10.64898/2026.11.09.765522).
