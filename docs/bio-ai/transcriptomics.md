# Transcriptomics Preprocessing

## 핵심 요약

Transcriptomics preprocessing은 raw count matrix를 분석 가능한 형태로 정리하는 과정이다. Single-cell RNA-seq에서는 cell/gene filtering, normalization, highly variable gene selection, scaling, dimensionality reduction, batch correction 등이 핵심이다.

## 기본 흐름

1. Raw count matrix 불러오기
2. Low-quality cell 제거
3. 낮은 detection gene 제거
4. Library size normalization
5. Log transform
6. Highly variable genes 선택
7. Scaling
8. PCA/UMAP/clustering
9. Cell type annotation

## QC 지표

- n_genes_by_counts: cell별 검출 gene 수
- total_counts: cell별 UMI/count 총합
- pct_counts_mt: mitochondrial gene 비율
- doublet score: doublet 가능성

## Scanpy 예시

```python
import scanpy as sc

adata = sc.read_h5ad("sample.h5ad")

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
```

## Foundation model 사용 시 주의점

일반적인 Scanpy preprocessing과 foundation model input preprocessing이 항상 같지는 않다. Geneformer는 rank-based input, scGPT는 gene-expression token 구조를 사용하므로 각 모델의 전처리 코드를 확인해야 한다.

## 내 연구에 적용할 아이디어

Rejection prediction에서 batch와 donor effect를 먼저 점검한다. Cell-level embedding을 patient-level feature로 사용할 때는 patient split을 지켜 data leakage를 막는다.

## 관련 자료

- [Scanpy preprocessing API](https://scanpy.readthedocs.io/en/1.11.x/api/preprocessing.html)
