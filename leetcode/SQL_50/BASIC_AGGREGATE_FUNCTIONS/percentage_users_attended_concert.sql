-- Table: Users

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | user_name   | varchar |
-- +-------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- Each row of this table contains the name and the id of a user.
 

-- Table: Register

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | contest_id  | int     |
-- | user_id     | int     |
-- +-------------+---------+
-- (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table contains the id of a user and the contest they registered into.
 

-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

-- The result format is in the following example.

WITH count_of_users AS (
    SELECT COUNT(DISTINCT user_id) AS usr_cnt
    FROM Users
)

SELECT r.contest_id, 
       ROUND(COUNT(r.user_id) * 100.0 / COALESCE(cu.usr_cnt, 1), 2) AS percentage
FROM Register r
JOIN count_of_users cu ON 1=1
LEFT JOIN Users u ON r.user_id = u.user_id
GROUP BY r.contest_id, cu.usr_cnt
ORDER BY percentage DESC, r.contest_id ASC;
