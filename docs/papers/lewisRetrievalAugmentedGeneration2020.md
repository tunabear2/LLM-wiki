# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## 기본 정보

- Citation key: `lewisRetrievalAugmentedGeneration2020`
- Item type: conferencePaper
- Authors: Patrick Lewis; Ethan Perez; Aleksandra Piktus; Fabio Petroni; Vladimir Karpukhin; Naman Goyal; Heinrich Kuttler; et al.
- DOI: 10.48550/arXiv.2005.11401
- URL: [Link](https://arxiv.org/abs/2005.11401)
- Source/date: arXiv / NeurIPS, 2020

## 1. 한 줄 요약

RAG는 parametric language model에 dense retrieval을 결합해, 외부 문서 근거를 가져와 knowledge-intensive generation을 수행하는 구조다.

## 2. 왜 중요한가

LLM이 모든 지식을 weight 안에 기억해야 한다는 가정에서 벗어나, 검색된 evidence와 generation을 함께 쓰는 표준 패턴을 만들었다. 최신 문헌, 사내 문서, 임상 지침처럼 계속 바뀌는 지식에 특히 중요하다.

## 3. 내 연구에 연결할 점

Transplant rejection literature QA나 paper-note 자동화에서는 PubMed/arXiv/Zotero library를 retrieval layer로 두고, 생성 결과에 DOI/PMID evidence를 붙이는 구성이 더 안전하다.

## 4. Bibliography

Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." _NeurIPS_, 2020. [https://doi.org/10.48550/arXiv.2005.11401](https://doi.org/10.48550/arXiv.2005.11401).

