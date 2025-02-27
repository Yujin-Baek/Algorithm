Select round(sum(coalesce(length, 10))/count(*), 2) as average_length
from fish_info


