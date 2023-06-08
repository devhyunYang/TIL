### 사이트에서 표데이터 구글 시트로 가져오기
2개의 테이블이 연결된 데이터였음
=IMPORTHTML("https://www.espn.com/soccer/table/_/league/eng.1", "table", 1)
=IMPORTHTML("https://www.espn.com/soccer/table/_/league/eng.1", "table", 2)

### 불일치 필드 병합
해마다 해당하지 않는 필드에 null 값이 있었는데, 연도끼리 합쳐줘서 하나의 필드로 병합했음

### 정규표현식 활용
1ARSArsenal
1. 숫자(순위)만 뽑기
- REGEXP_EXTRACT([column], '(\d+)')
2. 팀 약어 뽑기
- REGEXP_EXTRACT([Column],'(\D+)') : 약어를 제외한 모든 문자
- LEFT([계산1],3)
3. 팀 이름
- RIGHT([계산1],LEN([계산1])-3)
