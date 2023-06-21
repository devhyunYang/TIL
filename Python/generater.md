# Generator
순회가능한 객체를 만든다
- iterator(값을 차례대로 반환하는 객체)를 생성
- 값을 생성하고 반환하는 동적 방식으로 동작 - 큰 데이터 집합 처리, 연속적인 값 생성시 유리
- 실행중인 상태를 기억
- yield 키워드를 사용해야 함(yield를 만나면 함수를 멈춘다)
- 메모리는 현재값만 가지고 있다(메모리의 효율성 높임)

```
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# 제너레이터 객체 생성
generator = count_up_to(5)

# 제너레이터 객체 사용
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(next(generator))  # 4
print(next(generator))  # 5
```

## iter(), next()
-__iter__()와 __next__() 메서드를 구현

### iter()
제너레이터를 이터레이터로 변환한다
- 제너레이터는 iter()과 next() 메서드를 가지고 있다. 하지만 제너레이터 객체가 아닌 다른 객체를 이터레이터로 변환할 때 iter() 함수를 사용할 수 있다.
- iter()는 객체의 __iter__() 메서드를 호출하여 객체 반환
```
def number_generator():
    yield 1
    yield 2
    yield 3

numbers = number_generator()
iterator = iter(numbers)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
```
numbers라는 제너레이터 객체를 iter를 통해 이터레이터로 변환 > next() 사용

### next()
제너레이터 객체의 다음 값을 가져온다.
```
def number_generator():
    yield 1
    yield 2
    yield 3

numbers = number_generator()
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
```

### 제너레이터 컴프리핸션
```
gen1 = (i for i in range(100)) # 이론적으로 무한대수를 range자리에 입력하더라도 메모리를 잡아먹지 않습니다.
print(type(gen1) # <class 'generator'>
```

```
gen1 = [i for i in range(100)]  # 10만큼 메모리를 잡아먹습니다.
print(type(gen1) # <class 'list'>
```
