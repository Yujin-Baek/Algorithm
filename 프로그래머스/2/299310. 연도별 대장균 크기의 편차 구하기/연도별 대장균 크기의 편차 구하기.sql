select year(e.DIFFERENTIATION_DATE) as year, (s.max_size - e.size_of_colony) as year_dev, e.id
from ecoli_data as e
join (select year(DIFFERENTIATION_DATE) as year, max(size_of_colony) as max_size from ecoli_data group by year) as s on  year(e.DIFFERENTIATION_DATE) = s.year
order by year(e.DIFFERENTIATION_DATE), (s.max_size - e.size_of_colony)