---
type: report
status: active
rag_priority: high
updated: '2026-07-20'
tags:
- wiki/report
---

# Single-cell FM Paper Watch - 2026-06-08

작성일: 2026-06-08

이 문서는 `single-cell-fm-paper-watch` 자동화의 첫 실행 결과를 위키용으로 정리한 기록이다. 목적은 최근에 새로 published, posted, revised, indexed 된 single-cell foundation model 관련 논문을 찾아 paper note로 추가하고, 기존 문서와 중복되는 항목은 걸러내는 것이다.

## 한 줄 결론

최근 30일 범위에서 새로 볼 만한 논문 2개를 추가했다. 문서 업데이트는 완료됐고, `mkdocs build` 검증만 현재 Python 환경에 MkDocs가 설치되어 있지 않아 보류되었다.

## 검색 범위

| 항목 | 내용 |
| --- | --- |
| 실행 시각 | 2026-06-08 KST |
| 검색 기간 | 2026-05-09 - 2026-06-08 |
| 기준 | 이전 실행 기록이 없어서 30일 lookback 적용 |
| 주 검색원 | `paper_search_mcp`: arXiv, PubMed, bioRxiv, medRxiv |
| 보조 확인 | public web search |

사용한 검색어는 다음 계열을 넓게 포함했다.

- `single-cell foundation model`
- `single cell foundation model`
- `single-cell foundation models`
- `scFM`
- `scGPT`
- `Geneformer`
- `scFoundation`
- `UCE`
- `CellPLM`
- `transcriptomics foundation model`
- `single-cell transformer`
- `cell foundation model`
- `perturbation foundation model`
- `gene expression foundation model`

## 추가한 논문

| Paper | Source/date | DOI/URL | 한 줄 요약 | 연구 관련성 |
| --- | --- | --- | --- | --- |
| [TxFM: Effective Biological Representation Learning by Masking Gene Expression](../papers/kenyonDeanEffectiveBiologicalRepresentation2026.md) | arXiv, 2026-05-29 | [10.48550/arXiv.2605.31562](https://doi.org/10.48550/arXiv.2605.31562) | RNA-seq count에 맞춘 masked autoencoder와 curated corpus로 transcriptomics representation을 학습한다. | Kidney transplant rejection bulk/pseudobulk RNA-seq에서 raw expression 대비 pretrained embedding의 추가 가치를 비교하는 후보 모델이다. |
| [SIGnature: Scoring gene importance by interpreting single-cell foundation models](../papers/goldScoringGeneImportance2026.md) | PubMed / Nature Biotechnology, 2026-05-27 | [10.1038/s41587-026-03112-5](https://doi.org/10.1038/s41587-026-03112-5) | Single-cell foundation model attribution으로 gene importance를 계산해 atlas-scale disease signature를 검색한다. | Rejection-associated immune cell state에서 DEG를 넘어 context-specific regulatory gene 후보를 찾는 데 유용하다. |

## 중복 또는 제외한 항목

| 항목 | 판정 | 이유 |
| --- | --- | --- |
| HEIMDALL | 중복 | 이미 `docs/papers/`에 paper note가 있다. |
| USHER | 중복 | 이미 `docs/papers/`에 paper note가 있다. |
| EGSP / scFoundation survival prediction | 중복 | 이미 `docs/papers/`에 paper note가 있다. |
| COIN drug sensitivity inference | 중복 | 이미 `docs/papers/`에 paper note가 있다. |
| From Snapshots to Trajectories: Learning Single-Cell Gene Expression Dynamics via Conditional Flow Matching | 제외 | 여기서 `scFM`은 single-cell Flow Matching 의미라 foundation model 문맥과 다르다. |
| Applications of temporal graph learning for predicting the dynamics of biological systems | 제외 | scGPT/scFoundation을 baseline으로 비교하지만, 논문 자체는 temporal graph learning 방법이다. |
| `UCE`, `UC`, `FM` 약어 검색 결과 | 제외 | 대부분 single-cell/transcriptomics foundation model과 무관한 약어 충돌이었다. |

## 변경 파일

- [TxFM paper note](../papers/kenyonDeanEffectiveBiologicalRepresentation2026.md)
- [SIGnature paper note](../papers/goldScoringGeneImportance2026.md)
- [Paper Notes index](../papers/index.md)
- [Single-cell Foundation Models overview](../papers/single-cell-foundation-models.md)
- 이 실행 기록 문서

## 검증 상태

`mkdocs build`와 `python -m mkdocs build`를 모두 시도했지만, 현재 활성 Python 환경에 MkDocs가 없어 실패했다.

```text
No module named mkdocs
```

따라서 이번 실행의 상태는 "문서 업데이트 완료, site build 검증은 MkDocs 설치 후 재실행 필요"로 남긴다.

## 다음 실행 때 볼 것

- TxFM의 model/code/data 공개 여부와 실제 downstream benchmark 세부 내용을 확인한다.
- SIGnature가 어떤 single-cell foundation model과 attribution method를 기본으로 쓰는지 paper/PDF 기준으로 보강한다.
- `scFM` 약어는 false positive가 많으므로 다음 검색에서는 `foundation model`과 함께 묶어 우선순위를 높인다.
- `UCE`는 abbreviation collision이 많으므로 single-cell/transcriptomics 문맥이 없으면 제외한다.

