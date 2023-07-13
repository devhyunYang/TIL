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
**arange** : 지정 범위 내 일정한 간격으로 value를 반환한다
- end point를 포함하지 않는다.
```
np.arange([start,] stop[, step,], dtype=None, *, like=None)
```
예시
```
np.arange(0,10,3)
# array([0, 3, 6, 9])
```

**zeros, ones**: 0 혹은 1로 구성된 배열 생성
```
np.zeros(shape, dtype=float, order='C', *, like=None)
np.ones(shape, dtype=None, order='C', *, like=None)
```
예시
```
np.zeros((2,5))
# array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
```
**linspace** : 특정 구간에 일정한 간격으로 된 value 리턴
- endpoint 포함
```
np.linspace(
    start,
    stop,
    num=50, # 갯수
    endpoint=True,
    retstep=False,
    dtype=None,
    axis=0,
)
```
예시
```
np.linspace(0,10,3)
# array([ 0.,  5., 10.])

len(np.linspace(0,10,3))
# 3 (넣었던 숫자 갯수가 그대로 나옴!)
```

**eye** : 원하는 행과 열로 대각행렬을 만들 수 있다
- square matrix 같은 갯수의 행과열을 가지고 대각선으로 놓여있음
```
np.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
```
예시
```
np.eye(5)
# array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```

### Random
랜덤 숫자 배열 생성

**rand** : 0과 1 사이의 값의 균일 분포로 지정한 모양과 빈도수로 나타냄
```
rand(d0, d1, ..., dn)
```
예시
```
np.random.rand(2,2)
# array([[0.96990985, 0.83244264],
       [0.21233911, 0.18182497]])
```
**randn** : 정규표준분포로부터 샘플을 반환한다
- 음수를 받을 수 있고 0에 가까운 숫자가 나올 확률이 높다
 예시
```
np.random.randn(2)
# array([-0.36633217, -1.40298731])
```
**randint** : 랜덤한 정수값 리턴
- 끝 값을 포함하지 않는다

```
randint(low, high=None, size=None, dtype=int)
```
예시
```
np.random.randint(0,101,(4,5))
# array([[45, 65, 11, 85, 61],
       [89, 25, 14, 16, 78],
       [72, 57, 59, 49, 67],
       [83,  4, 25, 33, 44]])
```

**seed** : 랜덤한 값의 세트 동일한 세트의 난수를 재생산할 수 있다
- seed() 안에 들어가는 숫자는 상관 없다! 하지만 다른 시드를 넣을 경우 서로 다른 유사 난수를 생성하게 된다!
예시
```
np.random.seed(42)
np.random.rand(4)
# array([0.37454012, 0.95071431, 0.73199394, 0.59865848])
```
### reshape
- 새로운 모양으로 재배열해준다!
예시
```
arr = np.arange(0, 25)
arr.reshape(5,5)
# 만약 arr.reshape(5,4)면 오류! 요소의 수와 같아야 한다
```

**max, min, argmax, argmin**
max, min : 배열의 최대 최소값

예시
```
ranarr.max()
```
argmax, argmin : 배열의 최대 최소값의 인덱스

예시
```
ranarr.argmax()
```

### dtype
- 배열의 데이터타입

예시
```
arr2 = np.array([1.2, 3.4, 5.6])
arr2.dtype
# dtype('int64')
```




