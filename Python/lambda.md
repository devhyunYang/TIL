# lambda

익명 함수를 만들기 위한 표현식

```
lambda 함수 인자: 함수의 반환 값
```
- 인자는 쉼표로 구분, 생략 가능

```
add = lambda x, y: x + y
print(add(3, 5) # 8
```

## 1. 정렬 기준으로 활용
```
people = [
  {'name' : 'Charile', 'age' : 31},
  {'name' : 'Bob', 'age' : 25},
  {'name' : 'Julia', 'age' : 47}
]

sorted_people = sorted(people, key=lambda: x['age])
print(sorted_people)

# [{'name' : 'Bob', 'age' : 25}, {'name' : 'Charile', 'age' : 31}, {'name' : 'Julia', 'age' : 47}]
```
sprted() 함수의 'key'매개변수에 나이순으로 정렬

## 2. 조건부 표현식
```
numbers = [1, -3, 5, -7, 9]

result = list(map(lambda x: x if x > 0 else 0, numbers))
print(result) # [1, 0, 5, 0, 9]
```

## 3. 필터링하기
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4, 6, 8, 10]
```
