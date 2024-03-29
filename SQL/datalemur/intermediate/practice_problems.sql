-- Imagine you are a Data Analyst working at CVS Pharmacy, and you had access to pharmacy sales data.
-- Output the total number of drugs manufactured by Pfizer, and output the total sales for all the Pfizer drugs.


SELECT COUNT(*), SUM(total_sales)
FROM pharmacy_sales
WHERE manufacturer = 'Pfizer'

-- Write a SQL query using AVG to find the average open price for Google stock (which has a stock ticker symbol of 'GOOG').

SELECT AVG(open)
FROM stock_prices
WHERE ticker = 'GOOG'

-- Use SQL's MIN command in this practice exercise, to find the lowest Microsoft stock (MSFT) ever opened at.

SELECT MIN(open)
FROM stock_prices
WHERE ticker = 'MSFT'

-- Use SQL's MAX command in this practice exercise, to find the highest Netflix stock (NFLX) ever opened at.

SELECT MAX(open)
FROM stock_prices
WHERE ticker = 'NFLX'

-- For every FAANG stock in the stock_prices dataset, write a SQL query to find the lowest price each stock ever opened at? 
-- Be sure to also order your results by price, in descending order.

SELECT ticker, MIN(open)
FROM stock_prices
GROUP BY ticker
ORDER BY MIN(open) DESC

-- This SQL GROUP BY exercise uses real data from a LinkedIn SQL Interview question which is a bit too hard to tackle right now,
-- so we'll solve an easier variant of the interview question.

-- Suppose you are given a table of candidates and their skills. How many candidates possess each of the different skills? 
-- Sort your answers based on the count of candidates, from highest to lowest.

SELECT skill, COUNT(*)
FROM candidates
GROUP BY skill
ORDER BY COUNT(*) DESC

-- Use SQL's HAVING & MIN commands to find all FAANG stocks whose open share price was always greater than $100.
SELECT ticker, MIN(open) as min 
FROM stock_prices
GROUP BY ticker
HAVING MIN(open) > 100

-- Given a table of candidates and their technical skills, list the candidate IDs of candidates who have more than 2 technical skills.

SELECT candidate_id 
FROM candidates
GROUP BY candidate_id
HAVING COUNT(*) > 2



-- Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. 
-- You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.

-- Write a query to list the candidates who possess all of the required skills for the job. Sort the output by candidate ID in ascending order.

SELECT candidate_id
FROM candidates
WHERE skill in ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY 

-- Assume you're given the tables containing completed trade orders and user details in a Robinhood trading system.

-- Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. 
-- Output the city name and the corresponding number of completed trade orders.

SELECT city, COUNT(order_id) as total_orders 
FROM trades 
INNER JOIN users 
  ON trades.user_id = users.user_id
WHERE trades.status = 'Completed'
GROUP BY city
ORDER BY total_orders DESC
LIMIT 3


-- Assume you're given a table containing data on Amazon customers and their spending on products in different category. 
-- Write a query using COUNT DISTINCT to identify the number of unique products within each product category.

SELECT category, COUNT(DISTINCT product)
FROM product_spend
GROUP BY category

-- CVS Health is trying to better understand its pharmacy sales, and how well different products are selling. 
-- Each drug can only be produced by one manufacturer.

-- Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits. 
-- Display the result from the highest to the lowest total profit.

SELECT drug, total_sales - cogs as total_profit
FROM pharmacy_sales
ORDER BY units_sold DESC
LIMIT 3


-- Write a query to identify the manufacturers associated with the drugs that resulted in losses for CVS Health and calculate 
-- the total amount of losses incurred.

-- Output the manufacturer's name, the number of drugs associated with losses, and the total losses in absolute value. 
-- Display the results sorted in descending order with the highest losses displayed at the top.

SELECT manufacturer, COUNT(drug) AS drug_count, ABS(SUM(total_sales - cogs)) AS total_losses
FROM pharmacy_sales
WHERE (total_sales - cogs) <= 0
GROUP BY manufacturer
ORDER BY total_losses DESC

-- Your team at JPMorgan Chase is preparing to launch a new credit card, and to gain some insights, you're analyzing how many credit cards were issued each month.
-- Write a query that outputs the name of each credit card and the difference in the number of issued cards between the month with 
-- the highest issuance cards and the lowest issuance. Arrange the results based on the largest disparity.

SELECT card_name, MAX(issued_amount) - MIN(issued_amount)
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY MAX(issued_amount) - MIN(issued_amount) DESC

-- Display the stocks which had "big-mover months", and how many of those months they had. Order your results from the stocks with the most, to least, "big-mover months".
-- A "big-mover month" is when a stock closes up or down by greater than 10% compared to the price it opened at.
-- For example, when COVID hit and e-commerce became the new normal, Amazon stock in April 2020 had a big-mover month 
-- because the price shot up from $96.65 per share at open to $123.70 at close – a 28% increase!

SELECT ticker, COUNT(ticker) as counter
FROM stock_prices
WHERE (open - close) / open >= .1 OR (open - close) / open <= -.1
GROUP BY ticker
ORDER BY counter DESC


-- Imagine you are a Data Analyst working at CVS Pharmacy, and you had access to pharmacy sales data.
-- For all Merck drugs, output the drug name, and the unit cost for each drug, rounded up to the nearest dollar. Order it from cheapest to most expensive drug.
-- Hint: Unit cost is defined as the total sales divided by the units sold.

SELECT drug, CEIL((total_sales / units_sold)) AS unit_cost 
FROM pharmacy_sales
WHERE manufacturer = 'Merck'
ORDER BY unit_cost;

-- Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query to determine which parts have begun the assembly process but are not yet finished.
-- Assumptions:
-- parts_assembly table contains all parts currently in production, each at varying stages of the assembly process.
-- An unfinished part is one that lacks a finish_date.
-- This question is straightforward, so let's approach it with simplicity in both thinking and solution.
-- Effective April 11th 2023, the problem statement and assumptions were updated to enhance clarity.

SELECT part, assembly_step
FROM parts_assembly
WHERE finish_date IS NULL;


-- Delve into the Marvel Avengers dataset and write a query to categorize the superheroes based on their average likes as follows:
-- Super Likes: Superheroes with an average likes count greater than or equal to 15,000.
-- Good Likes: Superheroes with an average likes count between 5,000 and 14,999 (inclusive).
-- Low Likes: Superheroes with an average likes count less than 5,000.
-- Display the superhero's character name, platform, average likes, and the corresponding likes category.

SELECT
  actor, 
  character, 
  platform, 
  avg_likes,
  CASE 
    WHEN avg_likes >= 15000 THEN 'Super Likes'
    WHEN avg_likes BETWEEN 5000 AND 14999 THEN 'Good Likes'
    ELSE 'Low Likes'
  END AS like_rating
FROM marvel_avengers 
ORDER BY avg_likes DESC;


-- This is the same question as problem #3 in the SQL Chapter of Ace the Data Science Interview!
-- Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.
-- Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. 
-- Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

SELECT 
    SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
    SUM(CASE WHEN device_type IN ('phone', 'tablet') THEN 1 ELSE 0 END) AS mobile_views
FROM viewership;

-- Assume you're given the tables containing info about Robinhood users, and the stock trades they placed.
-- Use a JOIN to output all the information from the trades table joined to the users table.

SELECT * 
FROM trades t INNER JOIN users u
  ON t.user_id = u.user_id;


-- Assume you're given the tables containing completed trade orders and user details in a Robinhood trading system.
-- Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. 
-- Output the city name and the corresponding number of completed trade orders.

SELECT 
  city, 
  COUNT(*)
FROM trades t INNER JOIN users u
  ON t.user_id = u.user_id
WHERE status = 'Completed'
GROUP BY city 
ORDER BY COUNT(*) DESC
LIMIT 3;

-- Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").

-- Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs.

SELECT p.page_id
FROM pages p LEFT JOIN page_likes pl
  ON p.page_id = pl.page_id
WHERE pl.liked_date IS NULL
ORDER BY p.page_id;


-- Given a table of Facebook posts, for each user who posted at least twice in 2021, write a query to find the number of days between each user’s 
-- first post of the year and last post of the year in the year 2021. Output the user and number of the days between each user's first and last post.

SELECT 
    user_id,
    MAX(post_date::DATE) - MIN(post_date::DATE) AS days_between
FROM 
    posts
WHERE 
    EXTRACT(YEAR FROM post_date) = 2021
GROUP BY 
    user_id
HAVING 
    COUNT(*) >= 2;

-- Assume you're given tables with information about TikTok user sign-ups and confirmations through email and text. 
-- New users on TikTok sign up using their email addresses, and upon sign-up, each user receives a text message confirmation to activate their account.

-- Write a query to display the user IDs of those who did not confirm their sign-up on the first day, but confirmed on the second day.

-- Definition:

-- action_date refers to the date when users activated their accounts and confirmed their sign-up through text messages.

SELECT user_id
FROM emails e INNER JOIN texts t 
  ON e.email_id = t.email_id
WHERE t.action_date = e.signup_date + INTERVAL '1 day'
AND signup_action = 'Confirmed'