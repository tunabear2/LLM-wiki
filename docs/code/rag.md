# RAG

## 핵심 요약

RAG(Retrieval-Augmented Generation)는 LLM이 답변하기 전에 외부 문서에서 관련 정보를 검색하고, 검색된 context를 함께 넣어 답변을 생성하는 방식이다.

## 왜 중요한가?

LLM parameter 안의 지식은 최신성이 떨어지거나 출처 확인이 어렵다. RAG는 논문 PDF, 실험 노트, guideline, 코드 문서처럼 내가 가진 자료를 검색해 답변의 근거로 사용할 수 있게 한다.

## 기본 구조

1. 문서를 chunk로 나눈다.
2. 각 chunk를 embedding으로 변환한다.
3. Vector database에 저장한다.
4. 질문이 들어오면 관련 chunk를 검색한다.
5. 검색된 context와 질문을 LLM에 넣어 답변한다.

## 간단한 pseudo-code

```python
question = "scGPT와 Geneformer의 차이는?"

query_embedding = embed(question)
contexts = vector_db.search(query_embedding, top_k=5)

prompt = build_prompt(question, contexts)
answer = llm.generate(prompt)
```

## 평가 포인트

- Retrieval recall: 필요한 문서를 잘 찾는가?
- Groundedness: 답변이 검색 문서에 근거하는가?
- Citation quality: 어떤 chunk에서 나온 정보인지 표시되는가?
- Freshness: 문서 업데이트가 index에 반영되는가?

## 내 연구에 적용할 아이디어

내 Zotero 논문 PDF와 `docs/papers/*.md` 노트를 index로 만들어, "kidney transplant rejection에서 single-cell foundation model을 어떻게 적용할까?" 같은 질문에 근거 있는 답을 하게 만든다.

## 관련 자료

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
