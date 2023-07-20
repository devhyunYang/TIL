# Methods

## .apply()
- 데이터프레임 열에 함수를 적용하고 broadcast 할 수 있음

### 단일 열
custom function
```
def last_four(num):
    return str(num)[-4:]
```
기존 int형인데 함수에서 str 형으로 변환함
```
df['새로운 열'] = df['적용희망 열'].apply(함수명)
df['last_four'] = df['CC Number'].apply(last_four)
```

### 다중 열
custom function
```
def simple(num):
    return num * 2
```
```
df['bill'].apply(simple)
```

lambda 사용
```
lambda num: num * 2
```
```
df['bill'].apply(lambda num:num*2)
```

#### 다중 값을 받는 함수
```
def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Other"
```

apply()에 2가지의 값을 넘김
- 1. lambda식, axis=1

```
df[['bill, 'tip']].apply(lamda df: quality(df['bill]', df['tip]), axis = 1)
```

#### np.vectorize
np.vectorize를 사용하면 시간과 구문을 단축 시킬 수 있다
```
np.vectorize(quality)(df['bill'], df['tip])
```
- Returns an object that acts like pyfunc, but takes arrays as input.
- is to transform functions which are not numpy-aware
- accept normal float, integer : not broadcasting to a numpy-array


## sort_values()
```
DataFrame.sort_values(by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
```
칼럼 A를 기준으로 정렬
```
df.sort_values('칼럼A')
```
내림차순
```
df.sort_values('칼럼A', ascending=False)
```
여러 열 가능
- tip 기준으로 정렬 후 size 기준으로 정렬
```
df.sort_values(['tip','size'])
```

## max,idxmax,min,idxmin
-  mean, max index location
```
df['column'].max() # 50.81
```
```
df['column'].idxmax() # 170
df.iloc[170] # 50.81 값을 가진 행 정보
```

```
df['column'].min()
```
```
df['column'].idxmin()
```

## corr()
- 열의 상관관계 : 열의 값이 얼마나 연관되어있는지!
- 숫자 열에서만 적용
- 1에 가까울수록 완벽히 연관되어있음
```
df.corr()
```

## value_counts()
- 카테고리 별 값의 갯수
- 분류형 데이터에서만 가능!
```
df['sex'].value_counts()
```

## unique(), nunique()
열이 가지는 고유값
```
df['day'].unique()
```
고유값의 갯수
```
df['day'].nunique()
```
len(df['day'].unique()) 값과 동일하다

## replace
```
df['sex'].replace('Female','F')
```
여러 개의 값을 교체할 때 : list 형태로 사용
```
df['sex'].replace(['Female', 'Male'], ['F','M'])
```

## map
dictionary 형태로 사용
- lots of items 을 변경하고 싶을 때 권장

```
mymap = {'Female' : 'F', 'Male' : 'M'}
```

```
df['sex'].map(mymap)
```

## duplicated
- False는 중복값이 없다. True는 중복값이 있다
  - 행의 모든 요소가 동일한 행이 이미 존재할경우 해당 행은 True로 반환
```
df.duplicated(subset=None, keep='first')
```
- subset : 특정 열만을 대상으로 할 수 있다. list 가능
- keep : first(위부터 검사) last(아래가 검사)

```
df.drop_duplicates()
```
중복값 제거

## between
```
Series.between(left, right, inclusive='both')
```
- left <= series <= right
- inclusive{“both”, “neither”, “left”, “right”}
  : 양 끝값 포함, 양 끝값 미포함, 왼쪽값만 포함, 오른쪽값만 포함
```
df[df['total_bill'].between(10,20,inclusive='both')]
```
df[]를 씌워서 filter로 사용

## nlargest, nsmallest
### nlargest
최대값
```
df.nlargest(2,'tip')
```
```
df.sort_values('tip', ascending = False).iloc[0:2]
```
와 동일하다

### nsmallest
최소값
```
df.nsmallest(2,'tip')
```
```
df.sort_values('tip').iloc[0:2]
```

## sample
```
df.sample(5)
```
5개의 랜덤 예시

```
df.sample(frac=0.1)
```
- 10% of rows in DF
- frac이 1을 초과할 경우 에러! : 모집단의 표본 개수보다 더 많은 표본 추출할 수 없다





