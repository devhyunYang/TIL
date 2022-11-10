Join (관계형 데이터베이스의 핵심 구조)
===
관계형 데이터베이스의 행들을 논리에 따라 연결할 수 있는 문법  

서로 다른 테이블에서 각각의 공통값 이용해 조합  

두 테이블을 조인할 때, 사용한 열의 이름이 동일할 경우 ON 대신 USING 사용

```
SELECT *
FROM customers AS C
JOIN orders AS O
ON C.customerNumber = O.customerNumber
✔️ ON : JOIN의 기준

SELECT *
FROM customers AS C
JOIN orders AS O
USING (customerNumber);

✔️ USING 다음 (괄호)는 생략 가능하다는 의미!
```

**JOIN의 기본 구조**

```
1️⃣ 2개 테이블

SELECT 컬럼명
FROM 테이블명 AS A // 테이블 별칭 사용하면 편하게 이용 가능
JOIN 테이블명 AS B
ON A.id = B.id

2️⃣ 3개 이상 테이블

SELECT 컬럼명
FROM 테이블명 AS A
JOIN 테이블명 AS B
ON A.id = B.id
JOIN 테이블명 AS C
ON A.id = C.id
```

WHERE과 비교연산자 사용가능
- JOIN과 ON을 훨씬 많이 사용한다
- 되도록 JOIN문 사용 권장
```
SELECT 컬럼명
FROM 테이블명 AS A, 테이블명 AS B
WHERE A.id = B.id
```

INNER JOIN의 경우 테이블의 순서를 바꾸어도 결과는 같음
```
FROM member.customer AS C
JOIN member.bookstore AS B
ON C.id = B.member_id;

❗같다

FROM member.bookstore AS B
JOIN member.customer AS C
ON C.id = B.member_id;
```

각 테이블에 동일한 칼럼명을 가진 칼럼들이 존재할 가능성이 있어 **테이블명.칼럼** 으로 어떤 테이블에서 사용하는지 명시
```
SELECT B.name
  ,C.name
  ,B.status
FROM bookstore AS B
JOIN customer AS C
ON C.id = B.member_id;
```

> 어느 부분의 데이터를 가져올 것인가에 따라 JOIN의 종류가 달라짐!
- 공통된 부분(교집합) **INNER JOIN**
- 왼쪽 테이블 기준 **LEFT.JOIN**
- 오른쪽 테이블 기준 **RIGHT JOIN**

🔹LEFT JOIN과 RIGHT JOIN은 순서가 중요하다  

🔹LEFT JOIN과 INNER JOIN 많이 씀!
