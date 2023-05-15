## *args, **kwargs

주어진 수보다 더 많은 인수를 넣을 경우 에러가 난다!

```
def add(a, b):
    return a + b

print(add(1,2,3)) # error
```

Python 함수에서 매개변수를 유연하게 처리하는 방법
- *arg = allows you to pass multiple non-key arguments
- **kwargs = allows you to pass multiple keyword_arguments
------------------------------------------------
### 1. *args

- 함수에 임의의 수의 위치 인자를 전달

```
def add(*args):
  total = 0
  for arg in args:
    total += arg
  return total

add(1,2,3,4,5) # 15
```
args를 사용하면 여러 개의 인수를 전달할 수 있다.

인수들은 튜플로 묶인다.
```
def myfunc(*args):
    for arg in args:
        print(arg)
myfunc('Hello', 'world', 123) 
```

### 2. **kwargs
/**kwargs는 keyword arguments의 약자다.
- 딕셔너리 형태로 함수 내부로 전달된다.

```
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='Alice', age=25, city='New York')
```
dictionary 형태로 받기 때문에 각각 key와 value값이 출력된다. 

### 3.*args 와 **kwargs 같이 사용하기
```
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

my_function(1, 2, name='Alice', age=25)

1
2
name Alice
age 25
```
순서바꾸면 syntax error : args > kwargs 

```
def print_details(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details("Hello", "world", name="Alice", age=20)
# 출력:
# Hello
# world
# name: Alice
# age: 20
```
print_details 함수는 *args로 전달된 위치 인수들을 출력하고, **kwargs로 전달된 키워드 인수들을 출력한다

```
def shipping_label(*args, **kwargs): 
  for arg in args:
    print(arg, end = " ")
  print()

  if "apt" in kwargs:
    print(f"{kwargs.get('street')} {kwargs.get('apt')}") # get을 사용해서 값을 가져오기
  else:
    print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123 Fake St.",
               apt = "100",
               city = "Detroit",
               state = "NY",
               zip = "12343")
```
