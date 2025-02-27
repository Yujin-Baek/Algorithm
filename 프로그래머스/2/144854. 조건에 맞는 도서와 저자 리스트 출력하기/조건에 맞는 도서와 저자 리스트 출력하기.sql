-- 코드를 입력하세요
SELECT book.book_id, author.author_name, to_char(book.published_date, 'YYYY-MM-DD')
from book
join author on book.author_id = author.author_id
where book.category like '경제'
order by published_date asc;