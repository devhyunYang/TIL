DataFrame
===
- 행과 열로 구성된 테이블이다
- **A group of Pandas Series objects that share the same index**


## 파일 디렉토리
파일 경로 : 주피터 노트북에서만 가능!
```
pwd
```
해당 디렉토리 파일 리스트 확인
```
ls
```

## 데이터 프레임에 관련된 기본 정보 확인
열정보 확인 : 열 이름 
```
df.columns

#Index(['total_bill', 'tip', 'sex'])
```

행 갯수 확인
```
len(df)
```

데이터 프레임의 인덱스 정보
```
df.index
```

데이터 프레임 첫 몇 행 + 마지막 몇 행
```
df.head(3) # 특정 행까지 지정 할 수 있음
df.tail()
```

데이터 프레임의 정보 : 항목, 칼럼, 데이터타입, null 갯수 등
```
df.info()
```

통계 관련 정보 제공
```
df.describe()
df.describe().transpose() # 행, 열 변경 
```
## selection, indexing
### columns

#### 단일 칼럼 호출
```
df['칼럼 명']
```
타입을 확인했을 때 series로 나온다.
```
type(df['칼럼 명'])
# pandas.core.series.Series
```
#### 복수 칼럼
컬럼명을 리스트로 넘겼기 때문에 괄호 2개
```
df[['칼럼 1','칼럼 2']]
```
#### 칼럼 생성하기
```
df['새로운 칼럼명'] = 100 * df['tip'] / df['total_bill']
```
기존의 칼럼명을 사용하면 새로운 내용으로 기존 칼럼이 변경된다.
```
df['price_per_person'] = df['total_bill'] / df['size']
```

#### 칼럼 삭제하기
axis = 1을 설정하지 않으면 오류가 난다.
```
df.drop('칼럼 명', axis = 1)
```
영구적으로 생성, 삭제를 희망하면 꼭 재할당해줘야한다
- inplace=True라는 메서드도 있지만 아래 방법을 권장함 
```
df = df.drop('칼럼 명', axis = 1) 
```

#### 인덱싱
기존 숫자 인덱스가 자동 제공되지만, 칼럼도 인덱스로 설정할 수 있다. 
- 고유값일 때 사용하는 것을 권장
```
df.set_index('칼럼명')
```
설정한 인덱스 리셋하기
- 재할당 해줘야 영구적으로 적용됨.
```
df = df.reset_index()
```

### rows
#### 단일 행 호출

integer based : 정수로 행 호출
```
df.iloc[0]
```

name based: 문자로 행 호출
```
df.loc['Sun2959']
```

#### 복수 행 호출
```
df.iloc[0:4]
```
```
df.loc[['Sun2959','Sun5260']]
```

#### 행 삭제
'행' 이기 때문에 axis = 0
````
df.drop('Sun2959', axis=0)
````

#### 행 삽입
복수 행을 삽입할 때 보통 pd.concat()을 사용한다. 
- _append()는 실제로 많이 사용하지 않음

```
df._append(one_row).tail()
```



