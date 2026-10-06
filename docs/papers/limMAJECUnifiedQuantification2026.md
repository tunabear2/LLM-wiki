---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# MAJEC: unified gene, isoform, and locus-level transposable element quantification from RNA-seq

## 기본 정보

- Citation key: `limMAJECUnifiedQuantification2026`
- Item type: journalArticle
- Authors: Tian-Yeh Lim; Ari Firestone
- Journal: Bioinformatics (published 2026-10-05; indexed 2026-10-06)
- DOI: [10.1093/bioinformatics/btag737](https://doi.org/10.1093/bioinformatics/btag737); PMID: [42834519](https://pubmed.ncbi.nlm.nih.gov/42834519/)
- Code: [GitHub](https://github.com/calico/majec); [Zenodo](https://doi.org/10.5281/zenodo.19224157)
- 주 카테고리: `Bulk RNA-seq`

## 1. 한 줄 요약

MAJEC는 BAM에서 gene·isoform·transposable-element locus를 한 번에 추정하는 EM 정량화 방법으로 exon-overlap contamination을 줄인다.

## 2. 연구 질문

일반 gene/isoform quantification과 TE quantification을 분리할 때 생기는 multi-mapping과 exon-overlap 오류를 단일 모델에서 줄일 수 있는가?

## 3. 데이터와 방법

alignment와 splice-junction evidence를 함께 사용해 gene, isoform, TE locus에 read를 확률적으로 배분하는 EM 절차를 제시했다. synthetic/benchmark 자료와 biological vignette에서 Telescope, TEtranscripts, Salmon/RSEM 및 differential-expression 결과를 비교했다.

## 4. 핵심 결과

exon-overlap 오염률이 Telescope의 43%에서 MAJEC의 5%로 낮아졌고, TE differential expression은 TEtranscripts와 상관 0.987을 보였다. 단일 pass로 여러 annotation 수준을 산출하며 공개 PyPI·Bioconda 패키지와 실행 기록을 제공한다.

## 5. 한계

benchmark와 biological vignette의 범위가 제한적이며, 정확도는 alignment 품질·annotation·junction evidence에 의존한다. 임상 cohort에서의 differential-expression 및 low-input 성능은 별도 평가가 필요하다.

## 6. 재현 또는 활용 포인트

reference annotation과 BAM preprocessing을 고정하고 gene/isoform/TE를 같은 run에서 생성한다. spike-in 또는 orthogonal qPCR을 사용해 low-count TE와 exon-overlap artifact를 별도로 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식 biopsy bulk RNA-seq에서 반복서열·염증 유전자와 isoform signal을 한 모델로 비교할 수 있어 rejection-associated TE activation을 탐색하는 후보가 된다. 다만 면역세포 혼합과 library protocol이 결과에 미치는 영향을 deconvolution·batch 분석과 함께 관리해야 한다.

## 8. 관련 키워드

- bulk RNA-seq
- transposable element
- EM quantification
- isoform quantification

## 9. Bibliography

Lim, Tian-Yeh, and Ari Firestone. “MAJEC: Unified Gene, Isoform, and Locus-Level Transposable Element Quantification from RNA-seq.” *Bioinformatics*, 2026. [https://doi.org/10.1093/bioinformatics/btag737](https://doi.org/10.1093/bioinformatics/btag737).
