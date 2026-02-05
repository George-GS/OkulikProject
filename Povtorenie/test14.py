SELECT * FROM users
WHERE email = 'user124@test.com'
AND created_at = '2024-03-15 10:30:00'


2
UNSERT INTO users (email, password) VALUES ('buyer@test.com', 'pass123');


3
SELECT u.name, p.name, o.quantity, o.quantity * p.price AS total_price
FROM users u JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id;

4
UPDATE users SET name = "Mike" WHERE id = 214214;
DELETE FROM user WHERE id = 214124;

5
SELECT SUM(total_amount) AS total
FROM orders
WHERE created_at BEETWEEN '2024-03-01' AND '2024-03-31'
AND status = 'completed';

6