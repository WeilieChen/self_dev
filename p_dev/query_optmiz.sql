select c.customer_name, sum(t.amount)
from customer c, transactions t
where c.customer_id = t.customer_id
group by c.customer_name

--rewrite to 

SELECT 
    c.customer_name, 
    SUM(t.amount) AS total_amount
FROM 
    customer c
JOIN 
    transactions t ON c.customer_id = t.customer_id
GROUP BY 
    c.customer_name;


--- trying to 
EXPLAIN SELECT 
    c.customer_name, 
    SUM(t.amount) AS total_amount
FROM 
    customer c
JOIN 
    transactions t ON c.customer_id = t.customer_id
GROUP BY 
    c.customer_name;


CREATE INDEX idx_customer_id ON customer(customer_id);
CREATE INDEX idx_transaction_customer_id ON transactions(customer_id);