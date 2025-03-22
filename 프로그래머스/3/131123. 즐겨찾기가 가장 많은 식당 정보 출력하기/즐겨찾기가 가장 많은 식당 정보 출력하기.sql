select r.food_type, r.rest_id, r.rest_name, s.favorites
from rest_info as r
join
(select food_type, max(favorites) as favorites
from rest_info
group by food_type) as s
on r.favorites = s.favorites and r.food_type = s.food_type
order by food_type desc
