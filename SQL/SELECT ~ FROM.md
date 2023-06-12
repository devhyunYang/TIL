
AS
----
계산식 AS 컬럼, 테이블의 별칭을 정할 수 있다.

```
SELECT id,
  retail_price,
  cost,
  retail_price - cost AS profit
FROM `thelook_ecommerce.products`;
```

LIMIT
-----
갯수를 제한한다. SQL문의 마지막 순서에 붙인다. 
```
select *
from `thelook_ecommerce.users` 
limit 5;
```

DISTINCT
--------
중복 값 제거
- 한 번만 나오면 뒤의 내용이 하나의 세트가 되어 중복 제거가 된다.

```
select distinct country
from `thelook_ecommerce.users`;
```

```
SELECT 
  DISTINCT
    category AS product_category,
    brand AS product_brand
FROM `thelook_ecommerce.products`
LIMIT 30
```