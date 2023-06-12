WHERE
====
```
SELECT *
FROM 위치
WHERE 조건;
```
- 필터(조건)에 해당하는 데이터만 가지고 올 수 있다
- 비교연산자, SQL연산자, 논리연산자 등 사용이 가능하며, 연산자끼리 결합 가능
```
SELECT *
FROM `thelook_ecommerce.users`
WHERE (age <= 40 AND country = 'Brasil') OR (age > 60 AND country = 'Korea');
```

비교연산자
- 같지 않음 (!=, <> 중 하나)

NOT
---
- 결과를 뒤집음
```
* 미국 빼고 나머지 다

select * from `thelook_ecommerce.users`
where NOT(country = 'United States');
```

BETWEEN
-------
- 사이 값(이상 이하)
````
WHERE 필드명 between a and b
````
```
WHERE age between 20 and 30
WHERE age >= 20 and age <= 30
```
```
select * from `thelook_ecommerce.users`
where NOT(country = 'United States')
```
2020-01-01 00:00:00 ~ 2020-02-01 00:00:00
- 2월 1일 데이터는 포함하지 않는다(1월달 가입자라고 생각하면 된다)

IN
--
필드 안의 값과 일치하는 값
````
select * 
from `thelook_ecommerce.products`
where brand in ('Onia', 'Hurley', 'Matix');

select * 
from `thelook_ecommerce.products`
WHERE brand = 'Onia'
OR brand = 'Hurley'
OR brand = 'Matrix';
````

LIKE
----
- 문자열 안 특정 글자가 포함이 되어있는 값
- LIKE'비교문자'
  - 대소문자를 구분하지 않는다
  
### % 
: 와일드 카드
```
SELECT *
FROM `thelook_ecommerce.products`
WHERE name LIKE '%Men%' 
AND name LIKE '%Sport%';;
```
MEN이라는 글자를 포함하는 값, 앞 뒤 어떤 문자가 있어도 상관 없다.
%의 위치에 따라 조건이 달라진다.
- MEN% : MEN으로 시작되는 값
- %MEN : MEN으로 끝나는 값

### _ 
: 글자수 제한을 포함한다, 한 _ 당 1 글자수를 뜻한다.
- Da___ : Da로 시작하는 5글자

NULL
----
값이 없는 값
- IS NULL
- IS NOT NULL


```
SELECT *
AND (cost/retail_price)*100 AS sale_price 
FROM `thelook_ecommerce.products`
WHERE NOT (brand = 'TYR')
AND name LIKE '&Suit%'
AND sale_price >= 50;

SELECT *,
  (cost/retail_price)*100 AS sale_price
FROM `thelook_ecommerce.products`
WHERE brand != 'TYR'
AND name LIKE '%Suit%'
AND (cost/retail_price)*100 >= 50;

위 별칭을 아래 조건에 사용할 수 없다 > SQL문의 작동 순서(추가 예정) 
```
