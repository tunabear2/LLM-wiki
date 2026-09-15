---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-15'
tags:
- wiki/paper
---

# DNT: Diploid Genomic Foundation Model

## 기본 정보

- Citation key: `leibDNTDiploidGenomic2026`
- Item type: bioRxiv preprint
- Authors: Guy Leib; Tal Zinger; Dan Ofer; Raizy Kellerman; Omri Nayshool; Dan Dominissini; Ariel Larey; Jeremy Levy; Yury Nahshan; Elay Dahan; Amit Bleiweiss; Nicole Bussola; Simon Lee; Shane O'Connell; Dung Hoang; Marissa Wirth; Noam D. Beckmann; Alexander W. Charney; Yoli Shavit; Nati Daniel; Gideon Rechavi
- DOI: 10.64898/2026.09.05.749576
- URL: [bioRxiv](https://doi.org/10.64898/2026.09.05.749576)
- Source/date: bioRxiv v1, posted 2026-09-11
- 주 카테고리: Bio AI
- 교차 카테고리: DNA-seq / Variant Analysis

## 1. 한 줄 요약

DNT는 두 homolog의 SNV와 짧은 indel, zygosity 및 상대적 phase를 하나의 입력 서열로 표현해 genomic language model이 diploid genotype을 직접 학습하도록 만든 foundation model이다.

## 2. 연구 질문

Haplotype을 따로 encoding한 뒤 downstream에서 합치는 대신, paired genotype과 cis/trans 관계를 단일 sequence 안에 보존하면 compound-heterozygous variant의 상대적 phase를 더 잘 구분할 수 있는가?

## 3. 데이터와 방법

Reference-aligned diploid encoding을 만들어 SNV와 짧은 insertion/deletion을 표현하고, phased genotype을 단일 서열로 변환하는 unphased tokenizer와 phase-retaining tokenizer를 제안했다. Nucleotide Transformer v3 backbone의 8M·100M parameter 모델을 계속 학습했으며, contextual representation에 phase 정보를 남기기 위한 auxiliary Contrastive Phase Loss를 평가했다. 검증에는 9,460개 예제로 구성한 새 compound-heterozygous benchmark를 사용했다.

## 4. 핵심 결과

입력에서 상대적 phase를 구분하지 못한 모델은 chance 수준에 머물렀다. Diploid representation을 사용한 모델은 vocabulary-adapted control의 AUROC 0.506보다 높은 0.649를 기록해, paired genotype 정보를 genomic language model이 이용할 수 있음을 보였다.

## 5. 한계

저자들은 이를 보편적인 variant prediction 성능 향상이 아니라 diploid genotype 정보를 모델에 제공하는 방법으로 한정한다. Benchmark가 구성된 compound-heterozygous 예제이므로, 자연적으로 관측되고 정확히 phasing된 임상 cohort에서 검증해야 한다. SNV와 짧은 indel 이외의 structural variant나 복잡한 haplotype에 대한 성능도 초록에서 확인되지 않는다.

## 6. 재현 또는 활용 포인트

- Haplotype-blind, vocabulary-adapted, phase-retaining input을 같은 backbone과 split에서 비교한다.
- Contrastive Phase Loss 유무와 8M·100M model size를 분리해 ablation한다.
- 가족 trio 또는 long-read phasing이 있는 독립 cohort에서 cis/trans 판별과 calibration을 평가한다.
- Reference build, variant normalization, genotype phasing 방법을 함께 고정해야 한다.
- 코드: [scrcdnai-max/DNT-Diploid-Genomic-Foundation-Model](https://github.com/scrcdnai-max/DNT-Diploid-Genomic-Foundation-Model)

## 7. Transcriptomics·신장이식 연구와의 연결

Transcriptomics와의 직접 연결은 약하지만, donor–recipient genotype에서 allele dosage와 cis/trans 관계를 보존해 면역·약물대사 관련 variant를 우선순위화하는 데 활용할 수 있다. HLA처럼 복잡하고 다형성이 높은 구간이나 임상 이식 cohort에 적용하기 전에는 정확한 phasing, ancestry representation과 별도 benchmark가 필요하다.

## 8. 관련 키워드

- Bio AI
- DNA-seq / Variant Analysis
- Genomic foundation model
- Diploid encoding
- Variant phasing
- Compound heterozygosity

## 9. Bibliography

Leib, G., T. Zinger, D. Ofer, et al. “DNT: Diploid Genomic Foundation Model.” bioRxiv, 2026. [https://doi.org/10.64898/2026.09.05.749576](https://doi.org/10.64898/2026.09.05.749576).
