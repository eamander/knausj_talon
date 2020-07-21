mode: user.sql
and code.language: sql
-
select from:
	insert("SELECT ")
	key(enter)
	edit.indent_more()
	key(enter)
	edit.indent_less()
	insert("FROM")
	key(escape)
	edit.up()	
star: "*"
from: insert("FROM ")
select star from: insert("SELECT * FROM ")
where: "WHERE "
order by: "ORDER BY "
descending: " DESC"
ascending: " ASC"
dot i d: ".id"
is not null: " IS NOT NULL"
is null: " IS NULL"
inner join:
    insert("INNER JOIN  ON ")
    key(left)
    key(left)
    key(left)
    key(left)