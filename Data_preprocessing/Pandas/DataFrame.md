# DataFrame 
- 2차원 배열
- 표/테이블 형태

## 데이터프레임 만들기
1️⃣ import
```
import pandas as pd
```
2️⃣ pd.DataFrame
```
df = pd.DataFrame({'키' : '값'})
```
2️⃣ 예시
```
df = pd.DataFrame({
    '연차' : [1, 2, 3],
    '연도' : [2015, 2016, 2017],
    '매출' : [10000, 20000, 30000]
})
```
3️⃣ 인덱스 확인
```
df.index # 인덱스가 자동으로 만들어졌다(RangeIndex)
df.set_index('열이름', inplace = True) # 지정하는 열을 인덱스로 만들기
```

## Column(열, 컬럼)
```
df['열이름'] # 시리즈 형태로 접근 가능하다
```
```
df.columns # column 확인하기
```

## Data
### 데이터 조회

1️⃣ loc
```
df.loc[2016] # 행데이터의 내용을 가져옴
df.loc[2016:2017] # 여러 개의 행 데이터 값을 가져올 수 있음
df.loc[2016, '매출'] # 해당 행데이터에 해당 열 값
```
2️⃣ iloc
```
df.iloc[1] # 행데이터의 내용을 가져옴
df.iloc[2:3] # n ~ n-1 행데이터의 값
```

### 데이터 불러오기
csv 파일 불러오기
```
data = pd.read_csv('경로')
```
기초 통계 
```
data.describe()
```
위에서부터 5행 보여줌
```
data.head()
```
아래서부터 5행 보여줌
```
data.tail()
``` 
column 값, null 유무, 열 별 데이터타입 확인
```
data.info()
```

### 데이터 기초 통계
데이터 타입 변환 - astype 사용
```
data_int = data.astype({'column명' : 'int', ...})
```
통계 함수
```
data['column'].maen() # 평균
data['column'].median() # 중앙값
data['column'].std() # 표준편차
data['column'].unique() # 유일값 > numpy의 배열 객체로 리턴됨
data['column'].value_counts() # 속성값의 빈도수
```
apply() : 열 또는 행에 대해 함수 적용

### Groupby
- 데이터를 그룹별로 분할
- 1단계 split : 범주현 데이터 / 원본 데이터에서 분류하고자 하는 데이터를 나눠준다.
- 2단계 apply : 수치형 데이터 / 분류된 데이터(그룹별)에 함수 적용
- 3단계 combine : 함수 적용 / 다시 합쳐줌

<img width="150" src="https://www.w3resource.com/w3r_images/pandas-groupby-split-apply-combine.svg">

칼럼 1별로 그룹화하고, 그룹별 칼럼2의 합
- 인덱싱해서 Series 형태로 출력됨
```
data.groupby('칼럼1')['칼럼2'].sum()
```
칼럼1 그룹 > 칼럼1 그룹 중 칼럼2 그룹 > 함수 적용
- 인덱싱 안하면 DataFrame으로 출력됨
```
data.groupby(['칼럼1', '칼럼2']).mean()
```

두 식은 똑같이 적용된다
```
data.groupby(['칼럼1', '칼럼2'])['칼럼3'].mean()
data.groupby(['칼럼1', '칼럼2']).mean()['칼럼3']
```

### to_datetime
- 문자형 자료를 datetime형으로 변환 
```
pd.to_datetime
```
