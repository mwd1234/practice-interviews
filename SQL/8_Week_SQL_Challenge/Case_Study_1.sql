-- 1. What is the total amount each customer spent at the restaurant?

SELECT s.customer_id, SUM(price)
FROM dannys_diner.sales s
INNER JOIN dannys_diner.menu m ON s.product_id = m.product_id
GROUP BY s.customer_id
ORDER BY s.customer_id;

-- 2. How many days has each customer visited the restaurant?

SELECT customer_id, COUNT(DISTINCT(order_date))
FROM dannys_diner.sales s
GROUP BY s.customer_id
ORDER BY s.customer_id;

-- 3. What was the first item from the menu purchased by each customer?

SELECT DISTINCT s.customer_id, m.product_name
FROM ( 
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM dannys_diner.sales s
  GROUP BY s.customer_id
  ORDER BY s.customer_id 
) AS first_orders
INNER JOIN dannys_diner.sales AS s ON s.customer_id = first_orders.customer_id AND s.order_date = first_orders.first_order_date
INNER JOIN dannys_diner.menu AS m ON s.product_id = m.product_id
ORDER BY s.customer_id

-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?

SELECT m.product_name, COUNT(*) AS count_sold
FROM dannys_diner.sales s
INNER JOIN dannys_diner.menu m ON 
	s.product_id = m.product_id
GROUP BY m.product_name 
ORDER BY count_sold DESC
LIMIT 1

-- 5. Which item was the most popular for each customer?

WITH customer_sales AS (
    SELECT 
        customer_id,
        product_id,
        COUNT(*) AS product_count
    FROM dannys_diner.sales
    GROUP BY customer_id, product_id
),
ranked_sales AS (
    SELECT 
        customer_id,
        product_id,
        product_count,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY product_count DESC) AS rank
    FROM customer_sales
)
SELECT 
    r.customer_id,
    m.product_name AS most_popular_item,
    r.product_count
FROM 
    ranked_sales r
JOIN 
    dannys_diner.menu m ON r.product_id = m.product_id
WHERE  
    r.rank = 1
ORDER BY r.customer_id;

-- 6. Which item was purchased first by the customer after they became a member?

