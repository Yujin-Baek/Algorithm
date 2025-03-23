select i.id, n.fish_name, i.length
from fish_info as i
join
(select fish_type, max(length) as max_len
from fish_info
group by fish_type) as m on i.length = m.max_len and i.fish_type = m.fish_type
join fish_name_info as n on i.fish_type = n.fish_type
