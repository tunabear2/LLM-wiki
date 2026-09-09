---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Benchmarking copy number alteration inference methods for spatial transcriptomics

## 기본 정보

- Citation key: hanBenchmarkingCopyNumberSpatial2026
- Item type: journalArticle
- Authors: Shi Han; Zhixi Xiong; Ying Zhou; Can Yang
- Journal: Nature Communications
- DOI: 10.1038/s41467-026-77500-5
- URL: [Publisher](https://www.nature.com/articles/s41467-026-77500-5)
- Source/date: published 2026-09-05
- 주 카테고리: Transcriptomics / Platform
- 교차 카테고리: Cancer Transcriptomics / Clinical Prediction; DNA-seq / Variant Analysis

## 1. 한 줄 요약

6개 암종·4개 spatial transcriptomics 플랫폼의 69개 절편에서 9개 copy-number inference 방법을 네 가지 실제 과제로 평가한 benchmark다.

## 2. 연구 질문

Spatial transcriptome에서 간접 추정한 CNA가 어떤 데이터·과제에서 genomic truth와 일치하며, tumor 분류와 공간 subclone 복원에 어떤 방법을 선택해야 하는가?

## 3. 데이터와 방법

CalicoST, CopyKAT, InferCNV, Clonalscope, Numbat, XClone, SCEVAN, STARCH, SlideCNA를 69개 tissue section에서 비교했다. 57개 section은 matched WGS·WES truth를 갖고 있으며 tumor classification, section 내부 subclone, organ-scale evolution과 CNA fidelity를 평가했다. CosMx, Xenium, Visium HD FFPE, Stereo-seq와 Slide-DNA-seq도 포함했다.

## 4. 핵심 결과

모든 task와 platform에서 일관되게 우승한 방법은 없었다. Reference spot, allelic information, spatial resolution과 분석 목표에 따라 성능 순위가 달라졌고, 저자들은 task-specific·data-aware selection guide를 제시했다.

## 5. 한계

자료가 암 조직에 집중되어 있고 transcriptome 기반 CNA는 직접 DNA 측정이 아니다. 모든 69개 section에 matched genomic truth가 있는 것은 아니며 platform sparsity, tumor purity와 normal reference 선택이 결과를 좌우한다. Early-access article이라 최종 편집본에서 세부가 바뀔 수 있다.

## 6. 재현 또는 활용 포인트

- 통합 benchmark: [YangLabHKUST/ST-CNABench](https://github.com/YangLabHKUST/ST-CNABench)
- Conda, Docker, Apptainer 환경과 preparation–run–evaluation workflow를 제공한다.
- 도구 선택 전에 matched DNA truth 보유 여부, normal reference, allele count와 공간 해상도를 표로 고정한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 거부반응과 직접적 CNA 연관성은 낮지만, spatial biopsy에서 비정상 clone이나 post-transplant malignancy를 조사할 때 expression-derived CNA를 DNA validation으로 확인해야 한다는 기준을 준다. Benchmark 설계 자체는 spatial method 선택에 재사용할 수 있다.

## 8. 관련 키워드

- Transcriptomics / Platform
- Spatial transcriptomics
- Copy-number alteration
- Cancer
- Cross-platform benchmark
- Spatial genomics

## 9. Bibliography

Han, Shi, Zhixi Xiong, Ying Zhou, and Can Yang. “Benchmarking Copy Number Alteration Inference Methods for Spatial Transcriptomics.” Nature Communications 17 (2026). [https://doi.org/10.1038/s41467-026-77500-5](https://doi.org/10.1038/s41467-026-77500-5).
