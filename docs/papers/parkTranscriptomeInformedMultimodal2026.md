---
type: paper
status: reference
rag_priority: high
updated: '2026-10-07'
tags:
- wiki/paper
---

# Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies

## 기본 정보

- Citation key: `parkTranscriptomeInformedMultimodal2026`
- Item type: preprint
- Authors: Jungkyu Park; Dhruva Biswas; Joseph Cappadona; Cerise Tang; Ken G. Zeng; Bartosz Machura; Chuwen Liu; Paolo Tarantino; Coral Omene; Francisco J. Esteva; Rohit Bhargava; Marcin Braun; Kamila Paździerz; Jakub Czerwiński; Hanna Romańska-Knight; Albert Grinshpun; Bareket Daniel; Michele Buchinger; Frederick Howard; Piotr Wysocki; Brie Chun; Freya Schnabel; Rich Caruana; Jan Witowski; Krzysztof J. Geras
- Source: arXiv (submitted 2026-10-02; not peer reviewed)
- Original: [arXiv:2610.03693](https://arxiv.org/abs/2610.03693)
- 주 카테고리: `Cancer Transcriptomics / Clinical Prediction`

## 1. 한 줄 요약

H&E에서 transcriptome을 먼저 추정한 뒤 임상변수와 결합해 breast cancer neoadjuvant therapy의 pathological complete response(pCR)를 예측하는 2단계 모델을 제시했다.

## 2. 연구 질문

직접 transcriptome 측정이나 genomic assay가 부족한 biopsy에서도 transcriptome-informed representation이 치료반응 예측을 안정화하는가?

## 3. 데이터와 방법

1단계 MORPHEUS는 32개 암종 8,742명에서 H&E→14,773-gene expression을 학습했다. 2단계 NEO는 inferred expression과 clinical variable로 pCR을 예측했으며, 개발 5 cohorts 1,080명과 독립 평가 9 cohorts 1,412명을 사용했다.

## 4. 핵심 결과

통합 평가 AUROC는 0.79 (95% CI 0.73–0.85)였고 molecular subtype 내 responder를 구분했다. 임상변수만 쓰거나 한 단계 pathology 모델보다 transcriptome-wide inference가 나았으며, intratumor sampling과 작은 조직량에 대해 안정적이었다.

## 5. 한계

관찰적 local-treatment cohort이므로 치료 선택의 인과효과를 추정하지 않는다. 일부 baseline은 재구현 결과이고 genomic assay와 직접 비교되지 않았으며, 작은 조직 평가는 patch subsampling 시뮬레이션이다. 코드와 다수 원자료가 공개되지 않아 완전한 재현도 제한된다.

## 6. 재현 또는 활용 포인트

cohort·subtype·site를 patient-level로 분리하고 clinical-only, pathology-only, measured-transcriptome baseline을 모두 둔다. inferred expression의 calibration과 실제 assay 측정값과의 spatial agreement를 별도 검증한다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장 생검 H&E에서 rejection transcriptome을 보조적으로 추정하고, eGFR·donor type·immunosuppression과 결합하는 설계의 참고가 된다. 그러나 이식 치료반응의 인과·외부기관 일반화는 prospectively 수집한 paired histology–RNA cohort에서 다시 확인해야 한다.

## 8. 관련 키워드

- cancer transcriptomics
- histology-to-transcriptome
- neoadjuvant therapy
- pathological complete response

## 9. Bibliography

Park, Jungkyu, et al. “Transcriptome-informed Multi-modal AI for Predicting Neoadjuvant Therapy Response from Breast Cancer Biopsies.” arXiv, 2026. [https://arxiv.org/abs/2610.03693](https://arxiv.org/abs/2610.03693).
