GROUP BY
====
- 카테고리를 기준으로 데이터를 조사하는 것

 1. 카테고리로 정한 열은 연속적이지 않다 - 고유한 그룹을 갖는다
 2. 숫자형일 수 있다!! 무조건 문자형 아님!

- pandas는 groupby()는 "lazy" groupby object 이라고 불릴만큼 집계 함수 call이 오기 전까지 기다리고 있다.

## method call

### 다양한 메서드 예시
```
mean(): Compute mean of groups
sum(): Compute sum of group values
size(): Compute group sizes
count(): Compute count of group
std(): Standard deviation of groups
var(): Compute variance of groups
sem(): Standard error of the mean of groups
describe(): Generates descriptive statistics
first(): Compute first of group values
last(): Compute last of group values
nth() : Take nth value, or a subset if n is a list
min(): Compute min of group values
max(): Compute max of group values
```
```
df.groupby['column_A'].count()
```
column_A는 이제 열의 이름이 아니라, index의 이름이 된다!

```
df.groupby('model_year').count()['mpg']
```
model_year 열로 그룹화되고, 열 mpg에 해당하는 값만 count

```
df.groupby(['column_A', 'column_B']).sum()
```
1개 이상의 열을 그룹화하기 - column_A 먼저 그룹화 후 column_B로 그룹화 한 값들의 합계

### groupby 후 index, columns
```
avg_year = df.groupby('column_A').mean()
```
```
avg_year.index
# Int64Index([70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], dtype='int64', name='column_A')
```
그룹화한 칼럼의 index값을 보여줌(그룹화 한 컬럼이 index가 됨!)

```
column_A.columns
# Index(['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'origin'], dtype='object')
```
해당 index의 columns를 보여줌

```
avg_year['mpg']
=
df.groupby('column_A').mean()['mpg']
```

### multi columns의 index
```
df.groupby(['column_A','column_B']).mean().index
# MultiIndex([(70, 4),
            (70, 6),
            (70, 8),
            (71, 4),
            (71, 6),
            (71, 8),
            (72, 3),
            (72, 4),
            (72, 8),
            (73, 3),
            (73, 4),
            (73, 6),],names=['column_A','column_B'])
```
```
year_cyl.index.names
# FrozenList(['column_A','column_B'])
```
groupby 한 다중 열의 리스트가 나옴

```
year_cyl.index.levels
# FrozenList([[70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [3, 4, 5, 6, 8]])
```
다차원 리스트 형태로 출력됨:column_A, column_B의 값이 출력되지만 서로 연관성은 없음!!!

### Grab Based on Outside Index
- 첫번째 조건으로 모으기
```
year_cyl.loc[70]
```
70에 해당되는 값의 데이터프레임을 출력함

```
year_cyl.loc[[70, 82]]
```
70과 82 다중값에 해당하는 데이터프레임을 출력함

### Grab a Single Row
```
year_cyl.loc[(70, 4)]
```
컬럼 A = 70, 컬럼 B = 4 에 해당하는 값을 출력함

### .xs() : (cross-section)
multiindex 중 특정 레벨에서 데이터를 선택하고 싶을 때 사용

```
year_cyl.xs(key=4,level='column_B')
```
column_B의 인덱스 값 중 4에 해당하는 값의 모음
- key는 1개만 가능!!
- 가시적으로는 이게 조건에 해당하는 값을 모아둔 데이터라고 생각할 수 없다 : 변수명을 four_colB 등으로 가시적으로 보이게 하는 것이 팁!

```

```

#### 다중 키를 사용하고 싶을 경우

```
df[df['colB'].isin([6,8])]
```
colB의 값이 6,8인 데이터를 미리 필터링
```
df[df['colB'].isin([6,8])].groupby(['colA', colB']).sum()
```
해당 데이터를 colA, colB 열로 groupby 적용

### swap levels
```
year_cyl.swaplevel()
```
그룹화한 index의 순서가 바뀜! 
- ex) a->b b->a

### sort multi level index
```
year_cyl.sort_index(level='colA', ascending = False)
```
분류할 때는 가장 바깥 level부터 해야함! 안그러면 그룹화된 값이 분산될 수 있음


### agg()
카테고리당 원하는 집계 함수로 커스터마이즈 할 수 있음!
- 함수명은 기존 bulit in 메서드와 동일해야 함!
```
df.agg(['median', 'mean'])
```
```
df.agg(['std', 'sum'])['colA']
```
colA에 대한 std, sum 값

```
df.agg({'colA' : ['max', 'mean'], 'colB' : ['mean', 'std']})
```
딕셔너리 형태로 key- value로 나눠서 집계함수 적용
- NaN 값이 뜨는 경우는 해당 열에 집계함수가 명시되지 않을 때
```
