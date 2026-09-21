---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-21'
tags:
- wiki/paper
---

# LucaCell: a sequence-centric foundation model for cross-species single-cell analysis

## 기본 정보

- Citation key: `sunLucaCellSequenceCentric2026`
- Item type: preprint
- Authors: Yan Sun; Yong He; Minsi Ren; Yanhui Wang; Penghao Xu; Yong Hou; Yu Kang; Tingjun Hou; Jieping Ye; Huanming Yang; Zheng Wang
- DOI: 10.64898/2026.09.08.750024
- URL: [Link](https://doi.org/10.64898/2026.09.08.750024)
- Source/date: bioRxiv v1, posted 2026-09-14

## 1. 한 줄 요약

LucaCell은 고정 gene ID 대신 pretrained mRNA sequence embedding과 discretized expression을 사용해 8,500만 human·mouse cell에서 학습하고 species·modality·microbe·virus 조건으로 전이를 확장한다.

## 2. 왜 중요한가

Gene vocabulary mismatch를 sequence representation으로 완화해 human, mouse, lemur의 cell-type annotation과 human ATAC, microbial read, influenza viral-load task까지 하나의 encoder로 다룬다. 다만 매우 이질적인 task의 성능이 transcriptomic cell-state generalization을 동일하게 뜻하지 않으므로 task별 baseline과 ablation이 중요하다.

## 3. 내 연구에 연결할 점

Kidney transplant에서 donor-specific exonic variant, viral infection과 cross-species validation을 cell embedding에 연결할 가능성이 있다. Rejection 분석에서는 HLA·IFN signal 보존, species/domain shift와 fixed-vocabulary model 대비 추가 이득을 donor-level split으로 확인해야 한다.

## 4. Bibliography

Sun, Yan, Yong He, Minsi Ren, Yanhui Wang, Penghao Xu, Yong Hou, Yu Kang, et al. "LucaCell: a sequence-centric foundation model for cross-species single-cell analysis." _bioRxiv_, 2026. [https://doi.org/10.64898/2026.09.08.750024](https://doi.org/10.64898/2026.09.08.750024).
