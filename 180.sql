/*
Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');
*/

/* I do not remember but this might be a model solution... */

select distinct(Logs.Num) as ConsecutiveNums
from Logs inner join
(select logs1.Id as id1, logs2.id as id2, logs1.Num as Num from
    Logs as logs1 inner join Logs as logs2 on logs1.Id = logs2.Id - 1
    where logs1.Num = logs2.Num) as doubles
on Logs.Id = doubles.id1 + 2
where doubles.Num = Logs.Num;