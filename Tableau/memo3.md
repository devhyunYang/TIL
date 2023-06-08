### 아이콘 클릭
시간이 다 동일할 경우 -> 아이콘 클릭해서 날짜로 변경

### 필드 놓기
날짜 관련 데이터 사용 : 모든 날짜의 옵션을 보고 선택 가능
- 윈도우 : 마우스 오른쪽 드래그
- 맥 : option + 마우스 왼쪽 드래그

### 달력
-
- 마크 (사각형) steps > 색상
- 레이블 > 맞춤 > 가로 왼 세로 상단
- 테두리 서식 : 행 구분선, 열 구분선 수준 올리면 테두리가 뚜렷해진다.
- 주 없애기 : 행 선반의 주 > 머리글 표시 해제


### 필터
- 워크시트에 적용 > 선택한 워크시트
![Tableau_filter](https://github.com/devhyunYang/TIL/assets/116538020/8acca87f-147a-44a1-b4c2-12c610fca406)
- 데이터 > 날짜속성 월요일 부터로!

start 우클릭 > 필드레이블 숨기기


![Tableau_ dateSetting](https://github.com/devhyunYang/TIL/assets/116538020/dcfe2e3b-75da-49db-8840-81559fd02f3f)

### 데이터 원본에서 필터 걸기
- 우측 상단 필터 > 추가 > 필드 선택 

### 분할
- 우클릭 > 변환 > 분할
- if I-G 라면 (- 기준으로 2개)
  - 지난 : I
  - 첫 : G


### 봄, 여름, 가을, 겨울
계산된 필드 만들기
```
CASE DATEPART('month', [날짜])
WHEN IN(3,4,5) THEN '봄'
WHEN IN(6,7,8) THEN '여름'
WHEN IN(9,10,11) THEN '가을'
ELSE '겨울'
END
```
기본속성 > 정렬 > 수동 정렬 : 이렇게 하면 다음 시트에도 적용된다.
- 일반 상식과 맞춰서 정렬하기

```
IF DATEPART('hour', [날짜]) < 11 THEN '오전'
ELSEIF DATEPART('hour', [날짜]) < 14 THEN '점심'
ELSEIF DATEPART('hour', [날짜]) < 18 THEN '오후'
ELSE '저녁'
END
```
IF 보다 효율적인 CASE - WHEN
```
CASE DATEPART('hour', [날짜]) 
WHEN IN(7,8,9,10) THEN '오전'
WHEN IN(11, 12, 13) THEN '점심'
WHEN IN(14, 15, 16, 17) THEN '오후'
ELSE '저녁'
```

### 공공기관 데이터
