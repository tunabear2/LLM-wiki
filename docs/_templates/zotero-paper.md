# {{ title }}

## 기본 정보

- Citation key: `{{ citekey }}`
- Item type: {% if itemType %}{{ itemType }}{% else %}확인 필요{% endif %}
- Authors: {% if creators.length > 0 %}{% for creator in creators %}{% if creator.firstName %}{{ creator.firstName }} {% endif %}{{ creator.lastName }}{% if not loop.last %}; {% endif %}{% endfor %}{% else %}확인 필요{% endif %}
- DOI: {% if DOI %}{{ DOI }}{% else %}없음 또는 확인 필요{% endif %}
- URL: {% if url %}[Link]({{ url }}){% else %}없음 또는 확인 필요{% endif %}

## Abstract

{% if abstractNote %}
{{ abstractNote }}
{% else %}
Abstract를 Zotero metadata에서 확인하거나 직접 작성한다.
{% endif %}

## 1. 한 줄 요약

{% persist "one-line-summary" %}
이 논문은 무엇을 해결하려고 했는가?
{% endpersist %}

## 2. 배경

{% persist "background" %}
기존 방법의 한계는 무엇인가?
{% endpersist %}

## 3. 핵심 아이디어

{% persist "core-idea" %}
논문의 가장 중요한 아이디어를 3문장 이내로 정리한다.
{% endpersist %}

## 4. Method

### Input

{% persist "method-input" %}
모델 또는 방법이 입력으로 받는 데이터는 무엇인가?
{% endpersist %}

### Model Architecture

{% persist "method-architecture" %}
모델 구조를 단계별로 정리한다.
{% endpersist %}

### Training Objective

{% persist "method-objective" %}
학습 목표, loss, pretraining task를 정리한다.
{% endpersist %}

### Output

{% persist "method-output" %}
모델이 최종적으로 예측하거나 생성하는 것은 무엇인가?
{% endpersist %}

## 5. Figure 정리

### Figure 1

{% persist "figure-1" %}
무엇을 보여주는 그림인가?
{% endpersist %}

### Figure 2

{% persist "figure-2" %}
핵심 결과는 무엇인가?
{% endpersist %}

## 6. 장점

{% persist "strengths" %}
- 
{% endpersist %}

## 7. 한계

{% persist "limitations" %}
- 
{% endpersist %}

## 8. 내 연구에 적용할 아이디어

{% persist "research-ideas" %}
예: kidney transplant rejection prediction, transcriptomics, single-cell foundation model 연구에 어떻게 활용할 수 있을까?
{% endpersist %}

## 9. 관련 키워드

{% persist "keywords" %}
- Transformer
- Foundation model
- Gene expression
- Fine-tuning
{% endpersist %}

## 10. Zotero PDF 하이라이트

{% persist "annotations" %}
{% set newAnnotations = annotations | filterby("date", "dateafter", lastImportDate) %}
{% if newAnnotations.length > 0 %}
### Imported: {{ importDate | format("YYYY-MM-DD HH:mm") }}

{% for annotation in newAnnotations %}
{% if annotation.annotatedText %}
> {{ annotation.annotatedText }}
{% endif %}
{% if annotation.comment %}

메모: {{ annotation.comment }}
{% endif %}
{% if annotation.page %}

Page: {{ annotation.page }}
{% endif %}

{% endfor %}
{% elif isFirstImport %}
아직 가져온 PDF highlight가 없습니다. Zotero PDF reader에서 highlight를 만든 뒤 다시 import한다.
{% endif %}
{% endpersist %}

## 11. Bibliography

{{ bibliography }}
