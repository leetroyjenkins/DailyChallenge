USE Coding;





GO

SELECT id
, salary
, DENSE_RANK() OVER (ORDER BY salary DESC) as ROWNUM
FROM LeetCode.Employee
;

SELECT ISNULL(
    (
        SELECT salary
        FROM (
            SELECT id
            , salary
            , DENSE_RANK() OVER (ORDER BY salary DESC) as ROWNUM
            FROM Leetcode.Employee
        ) sal
        WHERE ROWNUM = 2
    )
, null) AS SecondHighestSalary 
;

SELECT category, COUNT(1) AS accounts_count
FROM (
    SELECT account_id
    , income
    , CASE 
        WHEN income < 20000 THEN 'Low Salary'
        WHEN income < 50001 THEN 'Average Salary'
        WHEN income > 50000 THEN 'High Salary'
        ELSE null
        END AS category
    FROM Leetcode.Accounts
) cnt
GROUP BY  category
;

WITH low_cte (category, accounts_count)
AS 
(
    SELECT 'Low Salary' AS category
    , count(account_id) AS accounts_count
    FROM Leetcode.Accounts
    WHERE income < 20000
)
, mid_cte (category, accounts_count)

AS
(
    SELECT 'Average Salary' AS category
    , count(account_id) AS accounts_count
    FROM Leetcode.Accounts
    WHERE income <= 50000
        and income > 20000
)
, high_cte (category, accounts_count)
AS
(
    SELECT 'High Salary' AS category
    , count(account_id) AS accounts_count
    FROM Leetcode.Accounts
    WHERE income > 50000
)

SELECT * 
FROM low_cte
UNION ALL
SELECT * 
FROM mid_cte
UNION ALL
SELECT * 
FROM high_cte
;