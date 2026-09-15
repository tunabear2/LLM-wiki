---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# Isocall enables scalable transcript identification from long-read RNA-sequencing data

## 기본 정보

- Citation key: `dolzhenkoIsocallScalableTranscript2026`
- Item type: preprint
- Authors: Egor Dolzhenko; Mathieu Schertzer; Romain Gossart; Thom Mokveld; Jonathan R. Belyeu; Andrey Varabyou; Xiao Zheng; Elizabeth Tseng; Zev Kronenberg; Mark Chaisson; Gloria M. Sheynkman; Fritz J. Sedlazeck; Yuri Z. Kurmangaliyev; Jocelyne Bruand
- DOI: 10.64898/2026.09.08.749180
- URL: [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.09.08.749180v1); [DOI](https://doi.org/10.64898/2026.09.08.749180)
- Source/date: bioRxiv v1 preprint, posted 2026-09-13; not peer reviewed
- 주 카테고리: Transcriptomics / Platform

## 1. 한 줄 요약

Isocall은 여러 PacBio long-read RNA-seq sample의 compact transcript profile을 합쳐 known·novel transcript를 deterministic joint calling하며, 206개 sample과 35억 raw read 규모에서도 낮은 메모리로 동작했다.

## 2. 연구 질문

수백 sample의 deeply sequenced long-read RNA cohort에서 기존 소규모용 transcript-identification method의 계산 한계를 넘으면서, 알려진 isoform과 새로운 isoform을 높은 정밀도로 공동 검출할 수 있는가?

## 3. 데이터와 방법

Isocall은 정렬된 PacBio full-length non-concatemer read를 sample별 compact transcript profile로 변환하고, 이를 여러 sample에 걸쳐 병합해 dataset에서 지지되는 known·novel transcript를 공동 호출한다. Relative abundance와 internal priming threshold를 포함한 개별 filter와 coarse preset을 제공한다. 정확도는 WTC11 SIRV spike-in control로 평가했고, 확장성은 Human Pangenome Reference Consortium의 206개 sample·35억 raw read로 시험했다. Genome in a Bottle sample에서는 matched SNP genotype과 splice-site polymorphism의 일치를 추가 정확도 기준으로 사용했다.

## 4. 핵심 결과

Default setting에서 세 가지 SIRV mix 각각에 대해 sample당 false-positive transcript가 0–2개였다. HPRC 자료는 parallelized pbmm2 alignment와 Isocall profile 생성 후, 전체 206개 sample을 합친 call 단계가 8 thread, peak memory 1.3 GB에서 25분 걸렸다. Matched genotype 검증에서는 polymorphic splice site 337개를 회수했으며, BTN3A1의 de novo donor site가 mutant allele의 complete isoform switch와 대응하는 사례를 제시했다.

## 5. 한계

현재 결과는 동료심사를 거치지 않은 v1 preprint이며 PacBio long-read와 full-length non-concatemer read를 전제로 한다. 25분이라는 수치는 upstream pbmm2 alignment와 sample별 profile 생성 시간을 제외한 joint-call 단계다. 초록은 false-positive와 precision을 강조하지만 transcript recall, 저발현 isoform 민감도와 다른 long-read platform의 성능은 충분히 제시하지 않는다. HPRC·GIAB 중심 검증이므로 degraded, low-input 또는 임상 질환 조직에 대한 성능도 별도 확인이 필요하다.

## 6. 재현 또는 활용 포인트

- PacBio chemistry, read-processing과 pbmm2 version, reference genome 및 transcript annotation version을 고정한다.
- Full-length non-concatemer 판정, relative-abundance와 internal-priming filter 및 preset을 결과와 함께 기록한다.
- SIRV mix별 false positive뿐 아니라 known-transcript recall과 저발현 구간 성능을 함께 계산한다.
- Sample별 profile 단계와 joint-call 단계를 나눠 wall time, memory, thread 수와 sample·read 규모를 보고한다.
- Matched genotype이 있으면 allele-specific splice site를 orthogonal accuracy check로 사용하고, 최종 도입 전 사용한 code release와 실행 환경을 고정한다.
- 코드: [PacificBiosciences/isocall](https://github.com/PacificBiosciences/isocall)

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 biopsy나 혈액의 long-read cohort에서 rejection-associated full-length isoform, novel splice junction과 donor·recipient allele-specific splicing을 공동 탐색하는 데 적합한 설계다. 다만 임상 biopsy의 낮은 RNA 양과 degradation, 면역·실질세포 혼합이 검출 한계를 바꿀 수 있으므로 spike-in, short-read junction evidence와 targeted RT-PCR을 함께 사용하고 donor 단위 hold-out cohort에서 재현해야 한다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Long-read RNA sequencing
- Transcript identification
- Isoform
- Joint calling
- PacBio
- Allele-specific splicing

## 9. Bibliography

Dolzhenko, Egor, et al. “Isocall Enables Scalable Transcript Identification from Long-read RNA-sequencing Data.” bioRxiv, version 1, 2026. [https://doi.org/10.64898/2026.09.08.749180](https://doi.org/10.64898/2026.09.08.749180). Preprint; not peer reviewed.
