# 1. 숫자 자료형

print(5)  # 5
print(3.1435)  # 3.1435
print(-109)  # -109

A = 507
B = 3.1435
C = 4-4j

print(type(A))  # <class 'int'> (정수형)
print(type(B))  # <class 'float'> (실수형)
print(type(C))  # <class 'complex'>

# 2. 문자 자료형

print("Hello world")  # Hello world
print('안녕하세요')  # 안녕하세요

# 2-2. 시퀀스 자료형
# 문자열, 리스트, 튜플 -> 순서가 유지되고, 정수로 인덱싱, 길이가 있다.

a = 'Happy'
b = [1, 2, 3]
c = ('a', 'b', 'c')

# 시퀀스는 복제가 가능하다

a = 'Why'
print(a * 3)  # WhyWhyWhy

c = ('a', 'b', 'c')
print(c * 3)  # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# 같은 타입의 시퀀스끼리 붙일 수 있다.

a = [1, 5]
b = [2, 4]

print(a+b)  # [1, 5, 2, 4]

# 3. Boolean 자료형
# True, False 2가지의 답만 가진다.

print(5 > 10)  # False
print(5 < 10)  # True

print(True)  # True 
print(False)  # False 

# not 사용 (부정)

print(not 5 > 10)  # True
print(not 5 < 10)  # False 

