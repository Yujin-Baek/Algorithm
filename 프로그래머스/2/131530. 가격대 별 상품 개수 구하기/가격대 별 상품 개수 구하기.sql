select (price div 10000)*10000 as price_group, count(*)
from product
group by price div 10000
order by price