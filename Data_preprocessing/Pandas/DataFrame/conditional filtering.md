- columns are Features
- Rows are instances of data

### 단일 조건
1. 비교를 실행하고 싶은 열 설정
   
```
df['Bill'] > 30
```
2. 조건에 해당하는 시리즈만 데이터 프레임으로 넘어감 -> 데이터 프레임은 True인 행만 선택
```
df[df['Bill'] > 30]
```
### multi conditions
#### & : and , 두 조건에 모두 참일경우
```
df[(df['total_bill'] > 30) & (df['sex'] == 'Male')]
```
#### | : or , 두 조건 중 하나라도 참일경우
```
df[(df['total_bill'] > 30) | (df['sex'] == 'Male')]
```
#### isin()
- 너무 많은 조건을 하나하나 연결하기 불편하다
- 리스트가 옵션에 있는지 여부에 따라 boolean 값 반환

```
options = ['Sat', 'Sun']
df['day'].isin(options)
```

데이터 프레임 형식으로 출력된다.
```
df[df['day'].isin(['Sat','Sun'])]
```
