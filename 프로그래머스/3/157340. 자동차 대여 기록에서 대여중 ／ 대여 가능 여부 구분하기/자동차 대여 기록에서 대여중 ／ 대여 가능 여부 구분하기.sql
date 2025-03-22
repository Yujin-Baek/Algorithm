select car_id, case
    when exists(select 1 from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h where c.car_id = h.car_id and '2022-10-16' between start_date and end_date) then '대여중'
    else '대여 가능'
    end as availabilty
from (select distinct car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY) as c
order by car_id desc

