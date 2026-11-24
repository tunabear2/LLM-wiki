---
type: paper
status: reference
rag_priority: high
updated: '2026-11-24'
tags:
- wiki/paper
---

# LeakageHunter-SCFM: Evidence-bounded dataset-lineage auditing for single-cell foundation model benchmarks

## 기본 정보

- Citation key: `zhaLeakageHunterSCFMEvidence2026`
- Item type: journal article
- Authors: Yi Zha; Da Lin; Ying Chen; Yue Liu; Yu Zhang
- DOI: 10.1016/j.jbi.2026.105128
- PMID: 43051310
- URL: [Link](https://doi.org/10.1016/j.jbi.2026.105128)
- Source/date: Journal of Biomedical Informatics, published and PubMed indexed 2026-11-18

## 1. 한 줄 요약

LeakageHunter-SCFM은 논문·repository의 accession, DOI와 URL을 정규화해 scFM benchmark의 dataset lineage와 잠재적 pretraining overlap을 evidence 수준별로 감사한다.

## 2. 왜 중요한가

Identifier overlap, review priority와 confirmed exposure를 분리하고, 직접 근거가 없는 corpus membership·성능 영향 claim에는 ceiling을 둔다. 자동 triage는 recall을 높였지만 blinded 평가의 precision과 F1은 완전하지 않아 reviewer adjudication을 유지한다.

## 3. 내 연구에 연결할 점

Public kidney atlas와 transplant cohort가 model pretraining·fine-tuning·benchmark 사이에서 중복되는지 accession 단위로 추적하는 데 적합하다. Overlap 후보 자체를 leakage 확정으로 해석하지 말고 provenance와 sample-level evidence를 남겨야 한다.

## 4. Bibliography

Zha, Yi, Da Lin, Ying Chen, Yue Liu, and Yu Zhang. "LeakageHunter-SCFM: Evidence-bounded dataset-lineage auditing for single-cell foundation model benchmarks." _Journal of Biomedical Informatics_ (2026): 105128. [https://doi.org/10.1016/j.jbi.2026.105128](https://doi.org/10.1016/j.jbi.2026.105128).
