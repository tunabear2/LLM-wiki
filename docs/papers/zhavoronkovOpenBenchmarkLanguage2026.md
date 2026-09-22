---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-22'
tags:
- wiki/paper
---

# An open benchmark and language models for AI in aging biology

## 기본 정보

- Citation key: `zhavoronkovOpenBenchmarkLanguage2026`
- Item type: journalArticle
- Authors: Alex Zhavoronkov; Vladimir Naumov; Denis Sidorenko; Alex Aliper; Vladimir Aladinskiy; Ramin Hasani; Alexander Amini; Katerina Nasto; Mathieu Reymond; Rim Shayakhmetov; Zulfat Miftakhutdinov; Vadim N. Gladyshev; Fedor Galkin
- Journal: Cell 189(19):5980–5994.e8
- DOI: 10.1016/j.cell.2026.08.026
- PMID: 42753698
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42753698/); [DOI](https://doi.org/10.1016/j.cell.2026.08.026)
- Source/date: published 2026-09-17
- 주 카테고리: Bio AI

## 1. 한 줄 요약

LongevityBench는 노화 생물학의 다섯 biodata domain, 17개 task에서 18개 frontier AI를 비교하고, 0.6B–9B 규모의 domain-adapted Longevity-LLM이 훨씬 큰 범용 모델과 경쟁할 수 있음을 보인 공개 benchmark다.

## 2. 연구 질문

범용·생물학 특화 AI가 DNA methylation, transcriptomics, proteomics, genetics와 clinical data를 실제 노화 연구 맥락에서 얼마나 일관되게 해석하며, 소형 domain model이 frontier-scale 자원을 대체할 수 있는가?

## 3. 데이터와 방법

LongevityBench는 다섯 biodata domain의 17개 task로 구성되고 6개 개발팀의 frontier AI 18개를 평가한다. 저자들은 노화 관련 domain data로 0.6B–9B parameter의 multitask Longevity-LLM 다섯 종을 fine-tune하고 같은 suite에서 비교했다. Benchmark, model weights와 agent interface인 Longevity Claw를 공개했다.

## 4. 핵심 결과

모든 task를 지배하는 단일 모델은 없었고, omics 기반 age prediction은 scale과 무관하게 가장 어려운 축이었다. 소형 Longevity-LLM들은 여러 task에서 훨씬 큰 frontier system과 동등하거나 더 높은 성능을 보였다. 결과는 범용 language model도 domain adaptation을 통해 structured-omics task에 맞출 수 있음을 보여준다.

## 5. 한계

노화 중심 suite이므로 질환·이식 outcome으로 일반화되지 않는다. Benchmark task와 fine-tuning corpus 사이의 잠재적 중복, task별 metric 선택과 independent replication을 계속 점검해야 한다. 여러 저자가 모델·benchmark를 개발한 Insilico Medicine 또는 Liquid AI의 임직원·창업자이며 상업적 이해관계가 공개돼 있다.

## 6. 재현 또는 활용 포인트

- 공개 benchmark와 checkpoint의 version, prompt, decoding 설정을 고정한다.
- Overall 평균뿐 아니라 modality·task별 점수와 실패 유형을 보고한다.
- Training-data contamination을 점검할 수 있는 시간 분리·기관 분리 holdout을 추가한다.
- Clinical-only, raw omics baseline과 domain-LLM의 순증분 가치를 평가한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Donor/recipient age, 면역노화, methylation·transcriptome·proteome·임상정보를 아우르는 이식 benchmark 설계에 직접 참고할 수 있다. 거부반응 연구에서는 age prediction 자체가 아니라 graft outcome에 대한 modality별 external validation과 calibration이 필요하다.

## 8. 관련 키워드

- Bio AI
- LongevityBench
- Language model
- Multi-omics
- Aging biology

## 9. Bibliography

Zhavoronkov, Alex, et al. “An Open Benchmark and Language Models for AI in Aging Biology.” Cell 189, no. 19 (2026): 5980–5994.e8. [https://doi.org/10.1016/j.cell.2026.08.026](https://doi.org/10.1016/j.cell.2026.08.026).
