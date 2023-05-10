## 클래스

클래스는 공장, 붕어빵틀이다! 

인스턴스는 공장에서 생산되는 물건, 붕어빵! 🐠클래스로 만들어진 객체

```
class 클래스명:
    def 메소드1(self, 전달값1, 전달값2, ...):
        실행명령문1
        실행명령문2
        ...

    def 메소드2(self, 전달값1, 전달값2, ...):
        실행명령문1
        실행명령문2
        ...
```

### __init__()
------------------
- 생성자 : 클래스 객체를 생성할 때 자동 호출
- self를 제외한 생성자의 전달값의 갯수만큼 값을 줘야함.
```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

# Rectangle 클래스의 객체 생성
rect = Rectangle(5, 10)

# 너비와 높이 출력
print("너비:", rect.width)
print("높이:", rect.height)

# 면적 계산 및 출력
area = rect.calculate_area()
print("면적:", area)
```
- 생성자가 width, height < 2개의 전달값을 받고 있기 때문에
- 5, 10의 값을 넣음!

### 멤버변수 (인스턴스 변수)
-----------------
- 클래스 내 정의된 변수, 객체의 속성을 나타낸다
- 객체의 상태를 나타내거나 데이터를 저장할 때 사용된다.
- 클래스 내 self(매개변수) 키워드를 사용하여 멤버 변수에 접근할 수 있다.

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```
- self.width, self.height 는 객체의 멤버변수로 지정되어있다.
- self를 통해 접근 값을 설정하고 가져올 수 있다!

### 메소드
-------------------
- 클래스 내 정의 된 함수,
- self는 무조건 써주기!

```
class Rectangle:
    def __init__(self, width, height): 1️⃣
        self.width = width
        self.height = height
    
    def calculate_area(self): 2️⃣
        return self.width * self.height
        
rect = Rectangle(5, 10)
area = rect.calculate_area()
print("면적:", area) # 면적: 50
```

2️⃣ 메소드가 호출됨 > 1️⃣의 생성자의 전달값 가져옴

### 상속

```
class 자식클래스(상속받을 부모클래스):
```
- 클래스 간의 코드를 재사용, 계층구조 구성
- 자식클래스는 상속 받은 클래스의 속성 메서드 사용 + 새로운 속성 메서드 추가 가능

```
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("소리를 만듭니다.")

class Dog(Animal): ✔️ Animal을 상속 받았다
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        print("멍멍!")

# Dog 클래스의 객체 생성
my_dog = Dog("멍멍이")

# 상속된 메서드 호출
my_dog.sound()  # 출력: 멍멍!
```

### 다중상속
- 한 클래스가 여러 부모 클래스로부터 상속 받을 수 있다
- , 로 구분하여 여러 부모 클래스 지정 가능

```
class Shape:
    def get_area(self):
        pass

class Color:
    def get_color(self):
        pass

class Square(Shape, Color): ✔️ Shape, Color 클래스 상속 받음
    def __init__(self, side):
        super().__init__(side, side)
```

### 메소드 오버라이딩
--------------------------
- 부모 클래스 메소드를 자식 클래스에서 재정의
```
class Animal:
    def speak(self):
        print("동물이 소리를 낸다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")
        
animal = Animal()
dog = Dog()

animal.speak()  # "동물이 소리를 낸다."
dog.speak()     # "멍멍!"
```
해당 유닛에 맞춰 호출이 가능하다. 

### Pass
-----------------
- 아무것도 하지 않고 넘어간다 > 작동됨

```
def game_start():
    print("게임 시작")

def game_over():
    pass

game_start()
game_over()

# 게임 시작
```

### Super
------------
```
super().메서드(인자)
```
- 부모 클래스의 메서드를 호출하는 내장 함수
- 부모 클래스의 기능 유지 + 자식 클래스의 개별적 로직 구현

```
class Parent:
    def greet(self):
        print("부모 클래스의 인사")

class Child(Parent):
    def greet(self): 
        super().greet() ✔️ Parent 클래스의 greet 메소드 호출
        print("자식 클래스의 인사")
```

