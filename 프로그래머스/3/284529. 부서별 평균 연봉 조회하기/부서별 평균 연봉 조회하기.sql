select d.dept_id, d.dept_name_en, round(avg(e.sal), 0) as avg_sal
from HR_DEPARTMENT as d
join HR_EMPLOYEES as e on d.dept_id = e.dept_id
group by d.dept_id, d.dept_name_en
order by round(avg(e.sal), 0) desc