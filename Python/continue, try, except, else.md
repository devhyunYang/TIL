# continue
- 주로 반복문에서 사용
- continue가 실행되면 반복문의 남은 부분은 무시되고 다음 반복 시작
- 특정 조건을 만족하는 경우에만 원하는 동작 수행, 나머지 경우 건너뛸 수 있다.

```
# 예시 1: 홀수만 출력하기
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue  # 짝수인 경우 현재 반복 중단하고 다음 반복으로 이동
    print(num)  # 홀수인 경우에만 출력

# 출력 결과: 1
#          3
#          5
```
    
# try, except, else

```
try 실행문
except 예외 발생시 처리
else 예외 안 발생시 정상적 종료 때 실행
```
