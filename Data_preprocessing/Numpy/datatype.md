# 데이터타입

## 숫자형
#### 부호가 있는 정수(signed integer)
```
data = [1.1, 2, 3]
i = np.array(data, dtype=np.int32) # 데이터 타입을 int로 줬다
print(i) # [1, 2, 3]
```
#### 부호가 없는 정수(unsigned integer)
```
data2 = [-1, 2, 3]

ui = np.array(data2, dtype=np.uint32) # unit 8, 16, 32(0 ~ 4,294,967,295), 64
print(ui)
```
uint32가 처리하는 값이 0부터 라서 정해진 값 -1을 강제로 형변환 시켰으니 처리 가능범위의 가장 큰 값이 출력됨.

|uint|범위|
|------|---|
|uint8|0 ~ 255|
|uint16|0 ~ 65,535|
|uint32|0 ~ 4,294,967,295|
|uint64|0 ~ 184,467,440,737,095,551,615|

#### 실수(floating point)
```
f = np.array(data, dtype=np.float64)
print(f) # [1.1 2.  3. ] float 형으로 바꿈 2.0으로 출력됨. 0은 생략
```
#### 복소수(complex)
```
c = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex64) # 복소수 
# 실수
print(c.real) # [1. 3. 5.]
# 허수 
print(c.imag) [2. 4. 6.]
```
## 문자형
#### string_
방법 1️⃣string_()
```
data = [1, 2, 3]
s = np.string_(data)

print(s) # b'\x01\x02\x03' <- 바이트 단위
print(s.dtype) #s3 : string.이 3 단어로 이루어져있다
```
방법 2️⃣dtype='S'
```
s2_ = np.array(data, dtype='S')
```
#### unicod_
```
u = np.array(data, dtype='U') # unicode

print(u)
print(u.dtype) # <U1 : 1은 한 자리
```
## 논리형
- True(1), False(0)
- 비트 연산 사용
```
l1 = np.array([True, False, True])
l2 = np.array([False, False, False])

print(l1.dtype) # bool
print(l2.dtype)
```
and(&) : 모두 1일때 1
```
and_ = np.logical_and(l1, l2)
print(and_) # [False False False]
```
or(|) : 둘 중 하나가 1이면 1
```
or_ = np.logical_or(l1,l2)
print(or_) # [ True False  True]
```
xor(^) : 서로 하나가 1이면 1
```
xor_ = np.logical_xor(l1,l2)
print(xor_) # [ True  True  True]
```
not(~) : 0을 1로 1을 0으로 
```
not_ = np.logical_not(l1,l2)
print(not_) # [False  True False]
```
