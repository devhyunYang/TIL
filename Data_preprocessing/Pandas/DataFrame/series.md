Pandas
===

- 다양한 형식의 데이터를 읽고 쓸 수 있음(csv, excel, sql, html ..)
- 지능적으로 데이터 수집 가능(집합 , 인덱싱, 조정 등등)
- 결측치 처리

series
----
```
pd.Series(
    data=None,
    index=None,
    dtype: 'Dtype | None' = None,
    name=None,
    copy: 'bool | None' = None,
    fastpath: 'bool' = False,
)
```
- named index와 함께 정보가 정렬되는 data structure
- formal definition : one - dimensional ndarray with axis labels
- Numpy array는 자동으로 숫자 인덱스를 가진다
- Pandas series는 지정된 라벨 인덱스를 추가한다.
- 데이터는 여전히 수치화되어있다 ! - 숫자 인덱스  + 라벨 인덱스 추가 가능

```
help.pd(Series)
```
주피터에서 Series와 관련된 설명을 볼 수 있음

### Index, Data Lists
인덱스와 데이터 값을 리스트 형태로 지정한다
```
MYIndex = ['Apple', 'Banana', 'Carrot']
MYData = [2000, 3000, 4000]
```
리스트를 시리즈로 변환할 수 있다
```
# 자동으로 숫자 인덱스를 가진다.
ser = pd.Series(data = MYData)

# 라벨 인덱스, 데이터 인덱스를 지정할 수 있다
ser = pd.Series(data = MYData, index = MYIndex)

# 순서가 올바르다면 따로 할당하지 않아도 사용 가능하다
ser = pd.Series(MYData, MYIndex)
```
인덱스를 지정하면 data를 찾기 훨씬 쉬워진다.

```
ser['Apple'] #2000
ser[0] #2000
```

### dictionary
딕셔너리 형태를 자동으로 시리즈화 할 수 있다
```
ages = {'Sam':5, 'Frank':10, 'Spike':7}
pd.Series(ages)

#
Sam       5
Frank    10
Spike     7
```

### operations
```
sales_ql.keys()
```
키 값을 불러올 수 있다.

```
sales_ql*2
```
시리즈를 브로드캐스팅하여 값을 계산할 수 있다

```
q1 + q2
#
Brazil      NaN
China     950.0
India     410.0
Japan       NaN
USA       510.0
```
서로 다른 시리즈에 해당 인덱스가 없을 경우 연산했을 때 NaN이 뜬다

```
ql.add(sales_q2, fill_value=0)
#
Brazil    100.0
China     950.0
India     410.0
Japan      80.0
USA       510.0
```
이렇게 add를 사용하여 연결해주면 해당 값도 연산처리가 가능하다
- fill_value는 시리즈에 값이 없을 경우 채우는 값
