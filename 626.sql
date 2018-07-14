/*
Create table If Not Exists seat(id int, student varchar(255));
Truncate table seat;
insert into seat (id, student) values ('1', 'Abbot');
insert into seat (id, student) values ('2', 'Doris');
insert into seat (id, student) values ('3', 'Emerson');
insert into seat (id, student) values ('4', 'Green');
insert into seat (id, student) values ('5', 'Jeames');

*/

/* This is a model solution everyone can see */

/* NOTE: "^" operator
"^" is an XOR operation in MySQL.
(example)
>SELECT 0 ^ 1;
+-------+
| 0 ^ 1 |
+-------+
|     1 |
+-------+

> SELECT 1 ^ 1;
+-------+
| 1 ^ 1 |
+-------+
|     0 |
+-------+

>SELECT 2 ^ 1;
+-------+
| 2 ^ 1 |
+-------+
|     3 |
+-------+

>SELECT 3 ^ 1;
+-------+
| 3 ^ 1 |
+-------+
|     2 |
+-------+

*/

/* COALESCE function
Returns the first non-NULL value in the list, or NULL if there are no non-NULL values. 

https://dev.mysql.com/doc/refman/5.7/en/comparison-operators.html#function_coalesce
*/


SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;