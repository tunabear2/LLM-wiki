---
type: code-note
status: reference
rag_priority: medium
updated: '2026-07-20'
tags:
- wiki/code-note
---

# PyTorch

## 핵심 요약

PyTorch는 tensor 연산, 자동 미분, neural network module, GPU 학습을 지원하는 deep learning framework이다. LLM과 single-cell foundation model 구현의 기본 도구로 자주 쓰인다.

## 기본 구성

- `torch.Tensor`: 다차원 배열
- `torch.nn`: layer와 model 정의
- `torch.autograd`: 자동 미분
- `torch.optim`: optimizer
- `Dataset` / `DataLoader`: 데이터 배치 처리

## Tensor 예시

```python
import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
w = torch.randn(2, 1, requires_grad=True)

y = x @ w
loss = y.mean()
loss.backward()

print(w.grad)
```

## 모델 예시

```python
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)
```

## 체크리스트

- Tensor shape를 항상 주석이나 print로 확인한다.
- `model.train()`과 `model.eval()`을 구분한다.
- GPU 사용 시 model과 tensor를 같은 device로 옮긴다.
- Random seed와 train/validation split을 기록한다.

## 관련 자료

- [PyTorch tutorial](https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html)
