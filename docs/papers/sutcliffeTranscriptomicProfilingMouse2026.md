---
type: paper
status: reference
rag_priority: medium
updated: '2026-09-09'
tags:
- wiki/paper
---

# Transcriptomic profiling of mouse mammary tumors enables prognostic and predictive biomarker discovery for human breast cancer

## 기본 정보

- Citation key: sutcliffeTranscriptomicProfilingMouse2026
- Item type: journalArticle
- Authors: Matthew D. Sutcliffe; Kevin R. Mott; Tulay Yilmaz-Swenson; Brooke M. Felsheim; Alexander V. Lobanov; Anna R. Michmerhuizen; Patrick D. Rädler; Denis O. Okumu; Xiaping He; Adam D. Pfefferle; Stephanie Dance-Barnes; Christian Brueffer; Lao H. Saal; Michael P. East; Daniel P. Hollern; Timothy C. Elston; Gary L. Johnson; Charles M. Perou
- Journal: Cancer Research
- DOI: 10.1158/0008-5472.CAN-26-0855
- PMID: 42599213
- URL: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42599213/); [DOI](https://doi.org/10.1158/0008-5472.CAN-26-0855)
- Source/date: published and indexed 2026-08-14
- 주 카테고리: Cancer Transcriptomics / Clinical Prediction
- 교차 카테고리: Bulk RNA-seq; Microarray

## 1. 한 줄 요약

면역정상 mouse mammary tumor의 baseline·치료 후 transcriptome에서 만든 생물학 모듈을 여러 human breast-cancer cohort에 이전해 생존과 면역치료 반응을 검증한 연구다.

## 2. 연구 질문

다양한 면역정상 마우스 유방암 모델의 전사체가 인간 유방암의 예후 및 치료반응 biomarker를 발견하는 실험 플랫폼으로 전이될 수 있는가?

## 3. 데이터와 방법

26개 mouse mammary tumor model의 baseline 및 치료 7일째 bulk RNA-seq를 894개 biology module로 요약하고 Elastic Net 중심의 예측 모델을 만들었다. 인간 검증에는 SCAN-B 6,329건, UNC-337, NKI-295, CALGB 40603과 면역관문억제제 cohort를 포함했다.

## 4. 핵심 결과

Baseline survival model과 특히 day-7 면역관문억제제 반응 model은 여러 인간 cohort로 전이됐다. 반면 마우스에서 만든 화학요법 예측기는 인간 자료에서 재현되지 않아, preclinical-to-clinical transfer가 치료 유형에 따라 달라진다는 음성 결과도 제시했다.

## 5. 한계

모델 단위 중앙값이 개체 간 변이를 축소할 수 있고 ER-positive 모델이 부족하다. 면역치료와 화학요법을 실제 임상처럼 병용하지 않았으며 화학요법 signature는 인간에서 전이되지 않았다. 암·마우스에서 얻은 모듈을 다른 질환에 직접 적용할 근거는 없다.

## 6. 재현 또는 활용 포인트

- Mouse RNA-seq: GEO GSE223630, GSE124821, GSE304115
- 분석 코드: [perou-lab/mouse-mammary-tumor-modeling](https://github.com/perou-lab/mouse-mammary-tumor-modeling)
- 모듈 코드: [perou-lab/Breast-Cancer-Modules](https://github.com/perou-lab/Breast-Cancer-Modules)
- 치료 전·후 signature와 외부 cohort validation을 분리하고 실패한 치료 축도 함께 보고한 설계를 참고할 수 있다.

## 7. Transcriptomics·신장이식 연구와의 연결

신장이식에서는 동물 거부반응 모델의 treatment-response module을 인간 biopsy cohort에 이전할 때 같은 다기관·다플랫폼 외부검증 틀을 쓸 수 있다. 암의 성공 signature 자체가 아니라 모듈 구축과 전이 실패를 판별하는 절차가 핵심이다.

## 8. 관련 키워드

- Cancer transcriptomics
- Clinical prediction
- Treatment response
- Bulk RNA-seq
- External validation
- Cross-species transfer

## 9. Bibliography

Sutcliffe, Matthew D., et al. “Transcriptomic Profiling of Mouse Mammary Tumors Enables Prognostic and Predictive Biomarker Discovery for Human Breast Cancer.” Cancer Research, 2026. [https://doi.org/10.1158/0008-5472.CAN-26-0855](https://doi.org/10.1158/0008-5472.CAN-26-0855).
