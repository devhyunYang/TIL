원하는 위치의 값 추출 가능 - 파이썬 리스트와 비슷
```
arr[8] # 인덱스 위치
arr[1:5] # 범위
```

### Broadcasting
리스트와 Numpy의 차이점!
- 리스트에서 새로운 값을 넣으려면 size와 shape을 맞춰야 한다
- can broadcast a single value across a larger set of values
```
arr = np.arange(0,11)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```
```
arr[0:5] = 100 # 리스트에서는 할 수 없다
# array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])
```

numpy는 기존 배열에 영향을 준다!!!
```
arr = np.arange(0,11)
slice_or_arr = arr[0:6] # arr의 0~5번째까지의 값을 추출
slice_or_arr[:] = 99 # slice_of_arr의 모든 값을 99로 변경함

arr
# array([99, 99, 99, 99, 99,  5,  6,  7,  8,  9, 10]) 
```
기존 배열에 영향을 주지 않으려면 꼭 copy를 해야함!
```
arr_copy = arr.copy()
```

### 2차원 배열 Indexing
가독성을 위해 arr_2d[row,col] 사용을 권장함!!
```
arr_2d[row][col] or arr_2d[row,col]
```

```
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

arr_2d[0] # array([ 5, 10, 15])
arr_2d[0][1] # 10
arr_2d[0,1] # 10
```

```
arr_2d[:2]
# array([[ 5, 10, 15],
       [20, 25, 30]])

arr_2d[:2,1:]
# array([[10, 15],
       [25, 30]])
```
0, 1번째 행 + 1, 2번째 열

### 조건부 선택
```
arr = np.arange(1,11)
bool_arr = arr>4
# array([False, False, False, False,  True,  True,  True,  True,  True, True])

arr[bool_arr] ✅ True인 인덱스 위치의 값만 반환!
# array([ 5,  6,  7,  8,  9, 10])
```

위의 단계가 아래처럼 사용된다
- 배열 안에서 조건 실행 > 조건부 선택 필터로 통과
```
arr[arr>4]
# array([ 5,  6,  7,  8,  9, 10])
```
