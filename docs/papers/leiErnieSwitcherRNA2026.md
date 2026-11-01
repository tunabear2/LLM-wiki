---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-01'
tags:
- wiki/paper
---

# Ernie-Switcher: RNA Foundation Model-Guided Design of Programmable RNA Devices

## 기본 정보

- Citation key: `leiErnieSwitcherRNA2026`
- Item type: journal article
- Authors: Xin Lei; Runting Li; Yuzhong Liu; Jiesheng Huang; Yicheng Yang; Ruyuan Li; Shimin Liu; Pengxia Wang; Huaiguang Jiang; Wei Xiong
- Source: Bioinformatics, online 2026-10-26
- Original: [DOI: 10.1093/bioinformatics/btag774](https://doi.org/10.1093/bioinformatics/btag774); [PMID: 42929764](https://pubmed.ncbi.nlm.nih.gov/42929764/); [code](https://github.com/zhutiblah/Ernie-Switcher); [Zenodo](https://doi.org/10.5281/zenodo.21859277)
- 주 카테고리: `Bio AI`

## 1. 한 줄 요약

Ernie-Switcher는 RNAErnie representation, landscape navigability, biophysical constraint를 결합해 toehold switch를 최적화하고 E. coli에서 최대 35배 ON/OFF ratio를 실험적으로 확인했다.

## 2. 연구 질문

RNA foundation model이 학습한 sequence–phenotype representation으로 방대한 비선형 sequence–structure–function 공간을 탐색해 작동 가능한 programmable RNA device를 설계할 수 있는가?

## 3. 데이터와 방법

RNAErnie에서 얻은 sequence–phenotype representation으로 후보를 생성·필터링하고, threshold navigability로 최적화 가능성을 분석했다. Biophysical constraint로 탐색 경로를 plausible RNA 영역에 제한했으며 RNA toehold switch를 대상으로 계산 설계 후 E. coli에서 발현을 검증했다.

## 4. 핵심 결과

- RNA landscape의 threshold navigability lower bound는 86.4%였다.
- 최적화한 toehold switch는 E. coli에서 최대 35배 ON/OFF expression ratio를 보였다.
- Code, pretrained model, Zenodo archive와 web design platform을 공개했다.

## 5. 한계

실험 검증은 한 종류의 RNA device와 E. coli에 집중되어 있다. 다른 RNA 구조·세포 환경·전달 조건에서의 안정성과 off-target effect, 장기 기능은 확인되지 않았다.

## 6. 재현 또는 활용 포인트

RNAErnie checkpoint, navigability 정의, biophysical constraint와 후보 filtering 순서를 고정한다. In-silico score뿐 아니라 동일 host의 ON/OFF ratio와 sequence-diversity를 함께 재현한다.

## 7. Transcriptomics·신장이식 연구와의 연결

Rejection-associated RNA를 감지하는 synthetic sensor나 reporter 설계의 장기 후보가 될 수 있다. 환자 transcriptome 예측 모델은 아니며 면역세포·신장 조직 환경에서 직접 검증되지 않았다.

## 8. 관련 키워드

- Bio AI
- RNA foundation model
- RNA engineering
- sequence design

## 9. Bibliography

Lei, Xin, et al. “Ernie-Switcher: RNA Foundation Model-Guided Design of Programmable RNA Devices in a Navigable Landscape.” _Bioinformatics_, 2026. [https://doi.org/10.1093/bioinformatics/btag774](https://doi.org/10.1093/bioinformatics/btag774).
