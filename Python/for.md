# 반복문 

```
for 변수명 in 순회가능한 객체:
    수행 문장
```

1. 리스트 요소 출력하기
```
fruits = ["사과", "바나나", "딸기", "오렌지"]

for fruit in fruits:
    print(fruit)
    
사과
바나나
딸기
오렌지
```

2. 숫자 범위 반복하기
```
for i in range(1, 6):
    print(i)

1
2
3
4
5
```

3. 문자열 글자 출력하기
```
message = "Hello!"

for char in message:
    print(char)

H
e
l
l
o
!
```
4. 딕셔너리 형태
```
student_scores = {"John": 85, "Emily": 92, "Tom": 78, "Sara": 95}

for name, score in student_scores.items():
    print(name, "의 점수:", score)
```
dictionary 형태의 경우 key값만 출력된다.

✔️ **value 값을 출력하고 싶은 경우**

1. 딕셔너리명[key 이름]
```
student_scores = {"John": 85, "Emily": 92, "Tom": 78, "Sara": 95}

for name in student_scores:
    print(student_scores[name])
```
2. items() 메서드를 사용
```
student_scores = {"John": 85, "Emily": 92, "Tom": 78, "Sara": 95}

for name, score in student_scores.items():
    print(name, score)
```

### for ~ else
```
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 0:
        print("0은 포함되어 있습니다.")
        break
else: # else를 for와 동일선상에 둔다면, for가 break없이 정상종료 되었는가 그렇다면!
    print("0은 포함되어 있지 않습니다.")
```

- 0을 찾으면 "0은 포함되어 있습니다."를 출력하고 반복문 종료
- 그렇지 않으면 else 문 실행되며 "0은 포함되어 있지 않습니다." 출력

else문은 반복문이 완벽히 종료되었을 때 실행되며, break를 통해 반복문이 중간에 종료되지 않았을 때 실행된다

