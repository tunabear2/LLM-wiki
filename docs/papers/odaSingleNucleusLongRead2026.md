---
type: paper
status: reference
rag_priority: medium
updated: '2026-11-16'
tags:
- wiki/paper
---

# Single-nucleus long-read RNA sequencing reveals isoform shifts in acute kidney injury

## 기본 정보

- Citation key: `odaSingleNucleusLongRead2026`
- Item type: preprint
- Authors: Yasuhiro Oda; Megan L. Noonan; Eryn E. Dixon; Haojia Wu; Benjamin D. Humphreys
- Source: bioRxiv v1, posted 2026-11-11 (not peer reviewed)
- Original: [DOI 10.64898/2026.11.10.765759](https://doi.org/10.64898/2026.11.10.765759)
- 주 카테고리: `Transcriptomics / Platform`

## 1. 한 줄 요약

Mouse kidney의 single-cell·single-nucleus long-read RNA-seq를 비교하고 ischemia–reperfusion injury 뒤 proximal-tubule isoform usage shift를 gene-level 변화와 함께 포착했다.

## 2. 연구 질문

Frozen-tissue 친화적인 single-nucleus long-read RNA-seq가 short-read gene expression이 놓치는 kidney injury의 cell-type-specific isoform 변화를 검출할 수 있는가?

## 3. 데이터와 방법

건강한 성체 수컷 C57BL/6J mouse 3마리에서 single-cell·single-nucleus long-read library를 만들고, 양측 renal ischemia–reperfusion injury mouse 3마리에서 single-nucleus long-read RNA-seq를 수행했다. 총 13억 read, sample별 median read length 757–884 bases를 분석했다.

## 4. 핵심 결과

- Nucleus library는 intronic read가 많아 isoform-assigned read 비율은 낮았지만 distinct isoform과 expression diversity는 더 많이 검출했다.
- Injury 뒤 proximal tubule에서 oxidative-phosphorylation gene의 expression 감소와 isoform-composition shift가 함께 나타났다.
- Fut9과 Prrc2b에서 두드러진 injury-associated isoform usage shift를 보고했다.

## 5. 한계

Healthy 3마리와 injury 3마리의 수컷 mouse study로 표본이 작고 human allograft나 rejection을 포함하지 않는다. Nucleus의 intronic read와 cell/nucleus protocol 차이가 isoform 검출에 미치는 영향을 더 큰 cohort에서 확인해야 한다.

## 6. 재현 또는 활용 포인트

Cell/nucleus isolation, long-read chemistry, read length, full-length criterion, isoform annotation과 novel-isoform filter를 기록한다. 동일 sample의 short-read·bulk long-read·RT-PCR로 주요 isoform과 differential usage를 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

냉동 kidney biopsy에서 proximal-tubule injury와 rejection 관련 isoform 변화를 세포 유형별로 찾는 데 직접적인 설계 참고가 된다. Human allograft에서는 ischemic injury와 alloimmune rejection을 분리한 cohort와 독립 검증이 필요하다.

## 8. 관련 키워드

- single-nucleus RNA-seq
- long-read transcriptomics
- isoform usage
- acute kidney injury

## 9. Bibliography

Oda, Yasuhiro, et al. “Single-nucleus long-read RNA sequencing reveals isoform usage shifts in mouse acute kidney injury.” _bioRxiv_, 2026. [https://doi.org/10.64898/2026.11.10.765759](https://doi.org/10.64898/2026.11.10.765759).
