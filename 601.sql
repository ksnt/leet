/*
Create table If Not Exists stadium (id int, date DATE NULL, people int);
Truncate table stadium;
insert into stadium (id, date, people) values ('1', '2017-01-01', '10');
insert into stadium (id, date, people) values ('2', '2017-01-02', '109');
insert into stadium (id, date, people) values ('3', '2017-01-03', '150');
insert into stadium (id, date, people) values ('4', '2017-01-04', '99');
insert into stadium (id, date, people) values ('5', '2017-01-05', '145');
insert into stadium (id, date, people) values ('6', '2017-01-06', '1455');
insert into stadium (id, date, people) values ('7', '2017-01-07', '199');
insert into stadium (id, date, people) values ('8', '2017-01-08', '188');
*/

/* I might not understand this approach to the problem... */

# Write your MySQL query statement below
SELECT DISTINCT s1.id, s1.date, s1.people from stadium s1 join stadium s2 join stadium s3 on ( ((s2.id = s1.id - 1) and (s3.id-2=s2.id)) or ((s2.id - 1 = s1.id) and (s3.id-2 = s1.id)) or ((s2.id = s1.id - 2) and (s3.id - 1) =(s2.id)) ) WHERE s1.people>=100 and s2.people>=100 and s3.people>=100 order by s1.id