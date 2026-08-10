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
  <a class="kb-article-card" href="reports/microarray-to-scrna-prognosis-adapter/">
    <span class="kb-card__category">My Research</span>
    <span class="kb-card__title">Microarray-to-scRNA Prognosis Adapter</span>
    <span class="kb-card__description">Bulk microarray에서 학습한 예후 신호를 single-cell 환자 데이터로 연결하는 adapter 설계와 검증.</span>
    <time class="kb-card__date" datetime="2026-06-16">2026.06.16</time>
  </a>

  <a class="kb-article-card" href="reports/scgpt-worklog-summary/">
    <span class="kb-card__category">Research log</span>
    <span class="kb-card__title">scGPT Worklog Summary</span>
    <span class="kb-card__description">scGPT 기반 신장 이식 연구의 실험 흐름과 주요 의사결정을 다시 찾기 쉽게 정리한 기록.</span>
    <time class="kb-card__date" datetime="2026-06-04">2026.06.04</time>
  </a>

  <a class="kb-article-card" href="articles/2026-05-27-bulk-rnaseq-foundation-model-benchmark/">
    <span class="kb-card__category">Benchmark</span>
    <span class="kb-card__title">Bulk RNA-seq Foundation Model Benchmark</span>
    <span class="kb-card__description">Transcriptomics foundation model의 표현과 downstream 성능을 비교하기 위한 벤치마크 정리.</span>
    <time class="kb-card__date" datetime="2026-05-27">2026.05.27</time>
  </a>

  <a class="kb-article-card" href="reports/scgpt-prognosis-progress-2026-06-16/">
    <span class="kb-card__category">My Research</span>
    <span class="kb-card__title">scGPT Prognosis Progress Map</span>
    <span class="kb-card__description">신장 이식 거부반응과 예후 예측 실험의 현재 구조, 검증 결과, 다음 단계를 연결한 지도.</span>
    <time class="kb-card__date" datetime="2026-06-16">2026.06.16</time>
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
