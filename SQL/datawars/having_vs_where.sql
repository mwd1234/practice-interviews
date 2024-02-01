SELECT payment_id, rental_id
FROM payment
WHERE amount > 5.99
ORDER BY customer_id DESC
LIMIT 10

-- 

