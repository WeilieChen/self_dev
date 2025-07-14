select 
    payment_type, 
    sum(payment_amount) total_sale, 
    count(distinct customer_id)
from transactions
group by payment_type
order by payment_type desc;

select  
invited_by_customer_id,
sum(payment_amount)/sum(book_count) 
from transactions t 
join customers cs
on t.customer_id = cs.customer_id
group by invited_by_customer_id
order by sum(payment_amount)/sum(book_count) desc
limit 5
;

with 
base as (
    select 
    au.author_id, 
    max(case when au.website_url like '%.com%' then 1 else 0 end) is_dot_com,
    max(case when transaction_id is null then 1 else 0 end) is_never_madesale
    from authors  au
    left join books b
    on b.author_id = au.author_id
    left join transactions t 
    on b.book_id = t.book_id
    group by au.author_id
)
select 
    count(author_id) total_author,
    sum(is_dot_com)/ count(author_id)
    sum(is_never_madesale)/ count(author_id)
from base 
;


select 
t.customer_id, 
b.author_id,
sum(payment_amount) total_amount
from transactions t 
join books b
on t.book_id = b.book_id
group by t.customer_id, 
b.author_id
having count(distinct b.category) >=2
;


select 

t.customer_id, 
sum(payment_amount) as total_sale

from transactions t
join customers cs
on t.customer_id = cs.customer_id
where invited_by_customer_id is not null -- 
group by t.customer_id
order by sum(payment_amount) desc
limit 3
;

--- define who is the repeat customer 

with cus_trans as (
select 
distinct 
customer_id,
extract(year, transaction_date) year, 
extract(month, transaction_date) month
from transactions
),

preceding_check as (
select 
customer_id,
year current_year,
lead(year)over(partition by customer_id order by year, month) preceding_year,
month current_month,
lead(month)over(partition by customer_id order by year, month) preceding_month,

case
    when year = preceding_year and month +1 = preceding_month then 1
    when year +1 = preceding_year and month  = 12 and preceding_month =  1 then 1 
    else 0 end as is_repreat_customer

from cus_trans

)


{# 123 1999 10 1999 11  1
123 1999 11 1999 12  1
123 1999 12 2000 2   0 #}

select 
year, month
count (distinct customer_id)
from 
cus_trans ct 
join preceding_check pc 
on ct.customer_id = pc.customer_id
and ct.year = pc.current_year and ct.month = pc.current_month
where is_repreat_customer = 1
group by year, month
order by count (distinct customer_id)
limit 2;


with 
base (
select 
distinct 
    t.customer_id,
from transactions t  
join books b  
on t.book_id = b.book_id
join t.customers cs 
on t.customer_id = cs.customer_id
where  b.category <> any(split_to_array(interested_category))
)

select 
(select  count(customer_id) from base)*100 / count(customer_id)
from customers