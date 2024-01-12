-- 1. Your given a products table, which contains data about different 
-- Microsoft Azure cloud products. Output all the data, in all the columns.

SELECT *
FROM products

-- 2. Given the reviews table, write a query to retrieve all 3-star reviews 
-- using the SQL WHERE clause. Only display the user_id and stars columns.

SELECT user_id, stars
FROM reviews
WHERE stars = 3

-- Let's practice using AND along with WHERE to filter Amazon reviews 
-- based on all 4 of these conditions:
-- the review should have 4 or more stars
-- the review ID is less than 6000
-- the review ID is more than 2000
-- the review can't come from user 142

SELECT * 
FROM reviews
WHERE stars >= 4
AND review_id < 6000
AND review_id > 2000
AND user_id != 142

-- Let's practice using AND along with WHERE to filter Amazon reviews based 
-- on these two conditions:
-- the start count is greater than 2, and less than or equal to 4
-- the review must come from either user 123, 265, or 362

SELECT * 
FROM reviews
WHERE user_id IN (123, 265, 362)
AND stars > 2 AND stars <= 4

-- Imagine you are a Data Analyst working at CVS Pharmacy, and you had access to 
-- pharmacy sales data. Use the BETWEEN SQL command to find data on medicines:
-- which sold between 100,000 units and 105,000 units
-- AND were manufactured by either Biogen, AbbVie, or Eli Lilly
-- Output the manufacturer name, drug name, and the # of units sold.

SELECT manufacturer, drug, units_sold
FROM pharmacy_sales
WHERE units_sold BETWEEN 100000 AND 105000
AND manufacturer IN ('Biogen', 'AbbVie', 'Eli Lilly')


-- Imagine you are a Data Analyst working at CVS Pharmacy, and you had 
-- access to pharmacy sales data. Use the IN SQL command to find data on medicines:
-- which were manufactured by either Roche, Bayer, or AstraZeneca
-- and did not sell between 55,000 and 550,000 units

SELECT manufacturer, drug, units_sold
FROM pharmacy_sales
WHERE manufacturer IN ('Roche', 'Bayer', 'AstraZeneca')
AND units_sold NOT BETWEEN 55000 AND 550000

-- You have a table of 1000 customer records from a small-business based in Australia.
-- Find all customers whose first name starts with "F" and the last letter 
-- in their last name is "ck".

SELECT * 
FROM customers
WHERE customer_name LIKE 'F%ck'

-- You have a table of 1000 customer records from a small-business based in Australia.
-- Find all customers where the 2nd and 3rd letter in their name is "e".

SELECT * 
FROM customers
WHERE customer_name LIKE '_ee%'


-- You have a table of 1000 customer records from a small-business based in Australia.
-- Find all customers who are between the ages of 18 and 22 (inclusive), 
-- live in either Victoria, Tasmania, Queensland, their gender isn't "n/a", 
-- and their name starts with either 'A' or 'B'.

SELECT * 
FROM customers
WHERE age BETWEEN 18 and 22
AND state IN ('Victoria', 'Tasmania', 'Queensland')
AND gender != 'n/a/'
AND (customer_name LIKE 'A%' OR customer_name LIKE 'B%')