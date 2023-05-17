# enumerate

- 파이썬 내장 함수
- 순회 가능(리스트, 튜플, 문자열)한 객체를 입력받아 인덱스와 함께 반환

```
enumerate(iterable, start=0)
```
기본값 0

### 예시 1: 인덱스와 요소 출력하기
```
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 출력 결과:
# 0 apple
# 1 banana
# 2 cherry
```

### 예시 2: 특정 인덱스부터 반복하기
```
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# 출력 결과:
# 1 apple
# 2 banana
# 3 cherry
```

### 예시 3: enumerate 객체를 리스트로 변환하기
```
enumerate_list = list(enumerate(fruits))
print(enumerate_list)

# 출력 결과: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```
