## Numpy
파이썬에서 과학, 수치 연산을 위한 라이브러리
- Creating N-dimensional arrays
- quickly broadcast functions & Built-in functions

```
import numpy as np
```
### 다차원 배열(ndarray)

숫자 하나 : 스칼라
```
s = np.array(1)
```

1차원 : 벡터(Vector)
```
1차원 배열 생성 
a = np.array([1, 2, 3, 4]) # [1 2 3 4]

배열의 차원
print(a.shape) # (4, )

배열의 열
print(a.ndim) # 1

배열의 데이터 타입
print(a.dtype) # int64

각 요소의 바이트 단위 크기
print(a.itemsize) # 8
```

2차원 : 행렬(Matrix)
```
2차원 배열 생성
b = np.array([[1, 2], [3, 4]])

print(b)
[[1 2]
 [3 4]]
```

3차원 : 텐서(Tensor)
```
3차원 배열 생성 
c = np.array([[[1,2], [3, 4]], [[5, 6], [7, 8]]])

print(c)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
  
print(c.shape)
(2, 2, 2)
```

for문을 활용한 배열
```
f = np.array([i for i in range(1, 10, 2)])
print(f) # [1 3 5 7 9]
```
1부터 9까지의 범위에서 2씩 증가하는 배열 만들기

### Built-in Method

