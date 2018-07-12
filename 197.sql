# Write your MySQL query statement below
select class from (select class,count(*) as count from courses group by class DESC) as popular_class where count >= 5;