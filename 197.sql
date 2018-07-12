/*
Create table If Not Exists Weather (Id int, RecordDate date, Temperature int)
Truncate table Weather
insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10')
insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25')
insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20')
insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30')
*/

# Write your MySQL query statement below
# Write your MySQL query statement below
select w2.Id from Weather w1, Weather w2 where w1.Temperature < w2.Temperature and w1.RecordDate = w2.RecordDate - Interval 1 Day;