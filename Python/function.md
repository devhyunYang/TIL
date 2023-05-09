## 함수
- 코드를 재사용할 수 있고, 구조를 파악할 수 있다.

```
# 1️⃣ 함수 정의
def open_account(): 
  print("새로운 계좌가 생성되었습니다.")

# 2️⃣ 함수 호출 
open_account() 
```

### 함수의 구성

```
def deposit(balance, money):
  print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
  return balance + money
 
 deposit(balance, 1000)
```

- def : 함수를 선언하는 키워드
- deposit : 함수의 이름
- return : 함수의 종료, 결과를 반환
- balance, money : 파라미터, 받는 값
- balance, 1000 : 아규먼트, 전달되는 값
- deposit(balance, 1000) : 함수의 호출


### 기본 값
```
def profile(name, age = 17, main_lang = "파이썬"):
  print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("죠지")
# 이름 : 죠지지	나이: 17	주 사용 언어 : 파이썬
```

### 키워드 값 : 순서 상관 없음
```
def profile(name, age, main_lang):
  print(name, age, main_lang)

profile(name = "미자", age = 20, main_lang = "파이썬")
profile(age= 20, name = "귀자", main_lang = "자바")

# 미자 20 파이썬
# 귀자 20 자바
```

### 가변인자 : 서로 다른 개수의 값을 넣을 때 사용
- 인자 앞에 * 붙이기
```
def profile(name, age, *language): 
  print("이름 : {0}\t나이: {1}\t".format(name, age), end = " ")
  for lang in language:
    print(lang, end = " ")
  print()

profile("기현", 30, "Java", "python", "C+", "C++", "C#", "JavaScript")
profile("태호", 25, "Kotiln", "Swift")
```

### 함수내 주석 표시하기
```
def deposit(balance, money):
  '''
  이 함수는 입출금을 계산합니다.
  잔액과 입금액을 표시합니다.
  '''
  print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
  return balance + money

```

1️⃣ __doc__ 사용
```
print(deposit.__doc__)

# 이 함수는 입출금을 계산합니다.
  잔액과 입금액을 표시합니다.
```

2️⃣ help 사용
```
help(deposit)

Help on function deposit in module __main__:

# deposit(balance, money)
    이 함수는 입출금을 계산합니다.
    잔액과 입금액을 표시합니다.
```
