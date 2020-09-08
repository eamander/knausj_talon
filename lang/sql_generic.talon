mode: user.sql
mode: command
and code.language: sql
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_genericactive context
action(user.code_null): "NULL"
action(user.code_is_not_null): " IS NOT NULL"
action(user.code_is_null): " IS NULL"
action(user.code_operator_assignment): " := "
action(user.code_operator_subtraction): " - "
action(user.code_operator_addition): " + "
action(user.code_operator_multiplication): " * "
action(user.code_operator_division): " / "
action(user.code_operator_greater_than): " > "
action(user.code_operator_greater_than_or_equal_to): " >= "
action(user.code_operator_less_than): " < "
action(user.code_operator_less_than_or_equal_to): " <= "
action(user.code_operator_and): " and "
action(user.code_operator_or): " or "
action(user.code_state_case):
	insert("CASE \n\tWHEN THEN \nEND")
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
group by: insert("GROUP BY ")
order by: "ORDER BY "
descending: " DESC"
ascending: " ASC"
set: 
	insert("SET @ ;")
	key(left)
	key(left)
dot i d: ".id"
is not null: " IS NOT NULL"
is null: " IS NULL"
inner join:
    insert("INNER JOIN  ON ")
    key(left)
    key(left)
    key(left)
    key(left)
like: 
	insert("like '%%'")
	key(left)
	key(left)
limit: "LIMIT "
	
