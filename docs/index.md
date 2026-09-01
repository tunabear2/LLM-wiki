---
type: index
status: reference
rag_priority: low
updated: '2026-09-01'
tags:
- wiki/index
---

<section class="kb-home-hero">
  <span class="kb-home-eyebrow">Personal research knowledge base</span>
  <h1>LLM Bio Wiki</h1>
  <p class="kb-home-hero__lead">
    LLM과 bioinformatics를 연결해 읽고, 실험하고, 다시 찾기 위한 연구 Wiki입니다.
    Single-cell foundation model부터 transcriptomics 분석과 신장 이식 연구 기록까지 한곳에 축적합니다.
  </p>
  <div class="kb-home-hero__links">
    <a href="research-questions/">Research questions →</a>
    <a href="papers/">Browse papers →</a>
    <a href="papers/single-cell-foundation-models/">Single-cell FM map →</a>
  </div>
</section>

<section class="kb-home-section" markdown>

<span class="kb-section-label">Knowledge map</span>

## 주요 주제

<p class="kb-home-section__intro">Obsidian의 연결성, ReadTheDocs의 탐색성, 논문 사이트의 밀도를 결합한 네 개의 축입니다.</p>

<div class="kb-topic-grid">
  <section class="kb-topic">
  <h3>LLM &amp; Foundation Models</h3>
  <ul>
    <li><a href="llm/overview/">LLM 기본 개념</a></li>
    <li><a href="llm/transformer/">Transformer</a></li>
    <li><a href="llm/attention/">Attention</a></li>
    <li><a href="llm/tokenizer/">Tokenizer</a></li>
    <li><a href="llm/fine-tuning/">Fine-tuning</a></li>
    <li><a href="code/rag/">RAG</a></li>
  </ul>
  </section>

  <section class="kb-topic">
  <h3>Single-cell AI</h3>
  <ul>
    <li><a href="bio-ai/scgpt/">scGPT</a></li>
    <li><a href="bio-ai/geneformer/">Geneformer</a></li>
    <li><a href="bio-ai/single-cell-llm/">Single-cell LLM</a></li>
    <li><a href="papers/single-cell-foundation-models/">Single-cell foundation models</a></li>
    <li><a href="reports/scgpt-prognosis-progress-2026-06-16/">scGPT prognosis progress</a></li>
  </ul>
  </section>

  <section class="kb-topic">
  <h3>Genomics</h3>
  <ul>
    <li><a href="bio-ai/transcriptomics/">Transcriptomics preprocessing</a></li>
    <li><a href="papers/bulk-rna-seq/">Bulk RNA-seq</a></li>
    <li><a href="papers/scrna-seq/">scRNA-seq</a></li>
    <li><a href="papers/microarray-analysis/">Microarray</a></li>
    <li><a href="papers/dna-seq-analysis/">DNA-seq / variant analysis</a></li>
    <li><a href="papers/gwas-analysis/">GWAS</a></li>
  </ul>
  </section>

  <section class="kb-topic">
  <h3>My Research</h3>
  <ul>
    <li><a href="research-questions/">Research questions</a></li>
    <li><a href="reports/kidney-transplant-rejection-classification-summary/">Kidney transplant rejection</a></li>
    <li><a href="reports/microarray-to-scrna-prognosis-adapter/">Microarray-to-scRNA adapter</a></li>
    <li><a href="reports/transplant-prognosis-model-notes/">Transplant prognosis notes</a></li>
    <li><a href="articles/">Article / report scraps</a></li>
  </ul>
  </section>
</div>
</section>

<section class="kb-home-section" markdown>

<span class="kb-section-label">Recently updated</span>

## 최신 정리

<p class="kb-home-section__intro">최근 읽은 논문과 진행 중인 연구 흐름에서 다시 볼 가치가 높은 문서입니다.</p>

<div class="kb-article-list">
  <a class="kb-article-card" href="papers/shoeibiLockedEvaluationSurfaces2026/">
    <span class="kb-card__category">Evaluation</span>
    <span class="kb-card__title">Locked Evaluation of Geneformer Transfer</span>
    <span class="kb-card__description">CRISPRi perturbation 예측의 cross-screen transfer failure와 sampling-depth confounding을 검증.</span>
    <time class="kb-card__date" datetime="2026-08-28">2026.08.28</time>
  </a>

  <a class="kb-article-card" href="papers/xiaoLearningInterpretableTumor2026/">
    <span class="kb-card__category">Spatial FM</span>
    <span class="kb-card__title">GITIII-scale Cell State–Niche Modeling</span>
    <span class="kb-card__description">Paired scRNA·spatial data로 cell state–niche와 ligand–receptor mechanism을 학습하는 모델.</span>
    <time class="kb-card__date" datetime="2026-08-26">2026.08.26</time>
  </a>

  <a class="kb-article-card" href="papers/kobayashiGeneformerGuidedMultiomics2026/">
    <span class="kb-card__category">Geneformer</span>
    <span class="kb-card__title">Geneformer-guided Multiomics</span>
    <span class="kb-card__description">Geneformer 후보를 multiomics와 functional screen으로 검증해 Pbx1 regulatory hub를 규명.</span>
    <time class="kb-card__date" datetime="2026-08-21">2026.08.21</time>
  </a>

  <a class="kb-article-card" href="papers/birkMultiScaleModeling2026/">
    <span class="kb-card__category">Kidney Spatial AI</span>
    <span class="kb-card__title">TERRA Multi-scale Tissue Modeling</span>
    <span class="kb-card__description">Gene·cell·neighborhood embedding과 kidney in silico perturbation을 연결한 spatial foundation model.</span>
    <time class="kb-card__date" datetime="2026-08-04">2026.08.04</time>
  </a>
</div>
</section>

<section class="kb-home-section" markdown>

<span class="kb-section-label">Working principles</span>

## 정리 원칙

<div class="kb-principles">
  <div class="kb-principle">
    <strong>Concept first</strong>
    <span>핵심 개념과 중요성을 먼저 쓰고 세부 수식과 구현으로 내려갑니다.</span>
  </div>
  <div class="kb-principle">
    <strong>Evidence linked</strong>
    <span>논문, 코드, 실험 기록을 연결해 주장과 근거를 함께 보존합니다.</span>
  </div>
  <div class="kb-principle">
    <strong>Research reusable</strong>
    <span>신장 이식·transcriptomics 연구에 다시 적용할 아이디어를 남깁니다.</span>
  </div>
</div>
</section>
