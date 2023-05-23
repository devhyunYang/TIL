# 산술연산

### len()
첫 번째 차원의 원소(행) 수! 
```
n = len(matrix) # 행의 개수
m = len(matrix[0]) # 열의 개수

return n, m       # 여러 개의 결과 값을 반환하면 튜플로 반환된다.
```

### 넘파이 이용하면 차원을 풀거나 낮추거나 할 필요없이 효율적으로 계산 가능
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sum = a + b

min = a - b

mul = a * b

div = a / b

print(sum) # [5 7 9]
print(min) # [-3 -3 -3]
print(mul) # [ 4 10 18]
print(div) # [0.25 0.4  0.5 ]
```
### 지수함수
```
np.exp()
```

### 로그함수
- 자연로그
```
np.log()
```
- 밑이 2인 로그
```
np.log2()
```
### sin/ cos/ tan
```
sin_ = np.sin(d)

cos_ = np.cos(d)

tan_ = np.tan(d)
```
