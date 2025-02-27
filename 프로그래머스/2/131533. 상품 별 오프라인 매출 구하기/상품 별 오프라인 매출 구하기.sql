SELECT product.product_code, sum(product.price * offline_sale.sales_amount) as sales
from product
join offline_sale on product.product_id = offline_sale.product_id
group by product.product_id
order by sales desc, product.product_code asc;