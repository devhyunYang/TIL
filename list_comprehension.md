# list comprehension (지능형 리스트)

한 줄의 코드로 새로운 리스트를 생성하는 방법

### 1. 기본형태
```
[수행 연산 for 현재 처리 요소 in 시퀀스]
```

### 2. 조건을 추가한 경우
```
[수행 연산 for 현재 처리 요소 in 시퀀스 if 조건]
```

### 3. 예시
예시 1
```
squared_numbers = []
for num in range(1, 6):
    squared_numbers.append(num**2)
print(squared_numbers)
```

```
squared_numbers = [num**2 for num in range(1,6)]
```
예시 2
```
message = "hello"
uppercase_letters = []
for char in message:
    uppercase_letters.append(char.upper())
print(uppercase_letters)
```
```
message = "hello"
uppercase_letters = [char.upper() for char in message]
```
예시 3
```
numbers = [1, 2, 3, 4, 5]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)
```
```
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
```
