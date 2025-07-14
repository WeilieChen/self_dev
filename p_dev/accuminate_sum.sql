create temp table sales (
    date date,
    sale_id int,
    amount int
)
;

insert into sales values
('2023-05-01', 1 ,100),
('2023-05-02', 1 ,200),
('2023-05-03', 1 ,300),
('2023-05-04', 1 ,400),
('2023-05-05', 1 ,500),
('2023-05-01', 2 ,150),
('2023-05-02', 2 ,160),
('2023-05-03', 2 ,1760),
('2023-05-04', 2 ,103),
('2023-05-05', 2 ,104)
;

select
    date,
    sale_id,
    amount,
    sum(amount)over (partition by sale_id order by date  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) accu_sales
from sales
group by
    date,
    sale_id,
    amount;


select
    main.date,
    main.sale_id,
    main.amount,
    sum(sc.amount) acc_count
from sales main
left join sales sc
on main.sale_id  = sc.sale_id
and main.date >= sc.date
group by     main.date,
    main.sale_id,
    main.amount
order by sale_id, date
