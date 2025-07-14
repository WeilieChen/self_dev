
/*
what is the total value of sales and the number of unique paying customers
grouped by and stored descending order by payment types?
*/
--------------------------------------------------------------------
select 
    payment_type,
    sum(payment_amount) total_sale ,
    count(distinct customer_id)
from transactions
group by payment_type
order by payment_type desc
;


/*
find the IDs of top 5 customers, ordered by the avg payment per book
make by the people they invited
*/
--------------------------------------------------------------------
select 
invited_by_customer_id, 
sum(payment_amount) / sum(book_count) avg_payment
from transactions t
join customer_id c
on t.customer_id = c.customer_id
group by invited_by_customer_id
order by sum(payment_amount) / sum(book_count) desc 
limit 5
;



/*
find the total number of authors, 
what percentage of them have a website url that contain ".com"
and what percentage never make a sales?
*/

--------------------------------------------------------------------
with 
base (
select
a.author_id, 
max(case when website_url like '%.com%' then 1 else 0 end) as is_web,
max(case when transaction_id is null then 1, else 0 end) make_sale 
from authors a 
left join books b 
on a.author_id = b.author_id
left join transactions t 
on b.book_id = t.book_id
group by a.author_id
)
select 
count(author_id) total_author,
sum(case when is_web = 1 then 1 else 0 end) / count(author_id) as %has_com,
sum(case when make_sale = 1 then 1 else 0 end)/count(author_id)  as %never_makesale
from base

--------------------------------------------------------------------

/*
find the customers who purchased from the same author with that at least two catergories
and the total sales of these books 
*/

with 
base as (
select
t.customer_id, 
b.author_id, 
b.category,
payment_amount
from customers cs
join transactions t
on cs.customer_id = t.customer_id
join books b
on t.book_id = b.book_id
)


select 
customer_id, 
sum(payment_amount) total_sale
from base
group by customer_id, author_id
having count(distinct category) >=2 


------ for finding top 3 customer who purchase books 

select *
from (
select 
customer_id, 
sum(payment_amount) total_sale
from base
group by customer_id, author_id
having count(distinct category) >=2 
)
order by total_sale desc
limit 3


--------------------------------------------------------------------

/*
rank customers by the sale by who they invited ?
*/

with base as (
    select 
    invited_by_customer_id, 
    customer_id, 
    sum(payment_amount) total_sale
    from 
        transactions t
    join customers cs
    on t.customer_id = cs.customer_id
    group by 
    invited_by_customer_id, 
    customer_id 
)

select 
customer_id,
rank() over (order by total_sale, by invited_by_customer_id) rk
from base

--------------------------------------------------------------------

/*
rank the top 3 customer by total sales value of the 
people they directly invited to the platform
*/

select 
t.customer_id 
sum(payment_amount) total_sale
from transactions t
join customers cs
on t.customer_id  = cs.customer_id
where cs.invited_by_customer_id is not null  -- which as invited by other people
group by t.customer_id
order by sum(payment_amount) desc
limit 3


--------------------------------------------------------------------

/*
for each customer, find the total number of books and total number of 
unique books they purchased
*/

select 
    t.customer_id,
    sum(book_count) total_books,
    count(distinct book_id) total_unique_books
from transactions t 
group customer_id

--------------------------------------------------------------------

/*
find top two months with unique customers who made purchases 
this month and the previous months/
*/

with 
base as (
select 
    customer_id,
    to_char(transaction_date, 'YYYY-MM') year_month,
    sum(payment_amount) sales 
from transactions
group by customer_id, to_char(transaction_date, 'YYYY-MM')
),

summary as (
select 
customer_id,
year_month,
sales as current_month,
lag(year_month) over(partition by customer_id order by year_month) previous_month,
lag(sales) over(partition by customer_id order by year_month) previous_month_sale,

(sales + lag(sales) over(partition by customer_id order by year_month)) total_2_month_sales
from base
)

select 
    customer_id,
    year_month,
    previous_month
from 
summary 
where     rank()over(partition by customer_id order by total_2_month_sales desc) <=2

--------------------------------------------------------------------

/*
find the top two months with the highest number of repreat customers, where a repeat customer is
defined as someone made a purchases in both the current month and immediately preceding month
--- rank these months based on the count of such repeat customers

*/

--- need to get the repreat customer 
with base (
select 
distinct 
customer_id, 
extract(year, transaction_date) year
extract(month, transaction_date) month
from transactions
),

repeat_customer as (
select 
distinct 
customer_id, 
year,
month current_month
lead(year) over(partition by customer order by year, month) preceding_year,
lead(month) over(partition by customer order by year, month) preceding_month,
case
    year = preceding_year and current_month+1 = preceding_month  then 1 
    year + 1 = preceding_year and current = 12 and preceding_month = 1 then 1
    else 0 end repeat_customers
from base
order by year, month
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
limit 2




--------------------------------------------------------------------

/*
find the top 3 customers ordered by the total sales value of the people they directly invited
*/

with 
base as ( 
select 
    cs.customer_id, 
    sum(payment_amount) sales
from transactions t 
join customers cs
on t.customer_id = cs.customer_id
where invited_by_customer_id is not null  -- people directly invited by other customer 
group by cs.customer_id
)

select invited_by_customer_id
from base
order by sales desc 
limit 3

--------------------------------------------------------------------

/*
find the top 3 payment types under which the most books were sold
*/

select 
sum(book_count) books_sold,
payment_type
from transactions
group by payment_type
order by sum(book_count) desc
limit 3

--------------------------------------------------------------------

/*
what is the precentage of customers have bought at least one book not in their interested category?
in PostreSQL use UNNEST() which to explode the array to row level
--- split_to_array () 

or use any() string compare in array element
*/

with
unnest_interest as (
    select
        customer_id,
        unnest(split_to_array(interested_in_categories)) interested_category
    from customers
),

customer_buy_noe_interest_books as (
select 
    t.customer, 
    max(case when interested_category is null then 1 else 0) not_in_interest
from transactions t 
left join unnest_interest ui
on t.customer_id = ui.customer_id
left join books b
on t.book_id = b.book_id
and b.category = ui.interested_category
group by t.customer
)

select 
    round((select count(customer_id) from  customer_buy_noe_interest_books where  not_in_interest =1) * 100 / 
    count(distinct customer_id)
    )
from customers


/*
what precentage of customers have never bought a book in their interest category?

*/

with 
base (
select 
distinct t.customer_id
from transactions t 
join book b 
on t.book_id = b .book_id
join customers cs 
on t.customer_id = cs.customer_id
and  b.category != any(interested_in_categories)
)

select 
round((select count(customer_id) from base) * 100 / count(distinct customer_id))

from customers


/*
find all the customer purchsae more than 3 books on the first day and last day of transaction, not only 1 day
more then 3, but in both day

*/

with 
--- customer has at least 2 days which first and last
customer_purchase_day as (
select 
customer_id, 
min(transaction_date) first_day, 
max(transaction_date) last_day
from transactions
group by customer_id
having min(transaction_date) != max(transaction_date)

)

select
t.customer_id
from transactions t 
join customer_purchase_day cd 
on t.customer_id = cd.customer_id
and (t.transaction_date = cd.first_day or t.transaction_date =cd.last_day)
group by t.customer_id
having sum(book_count) >=3 