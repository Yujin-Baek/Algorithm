select b.category, sum(s.sales) as total_sales
from book_sales as s
join book as b on s.book_id = b.book_id
WHERE s.sales_date BETWEEN '2022-01-01' AND '2022-01-31'
group by b.category
order by b.category