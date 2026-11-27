-- 1. Show first 10 passengers
SELECT *
FROM passengers
LIMIT 10;


-- 2. Count all passengers
SELECT COUNT(*)
FROM passengers;


-- 3. Show all survivors
SELECT *
FROM passengers
WHERE survived = 1;


-- 4. Count passengers by gender
SELECT
    sex,
    COUNT(*)
FROM passengers
GROUP BY sex;
