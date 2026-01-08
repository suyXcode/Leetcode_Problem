# Write your MySQL query statement below
select 
d.name Department,
EE.name Employee,
EE.salary Salary
-- EE.ranks
 from 
 (select e.departmentId dep, e.name  , e.salary  ,DENSE_RANK() over(partition by e.departmentId order by salary desc) as ranks from Employee e ) as EE
join
 Department d on EE.dep =d.id
 where EE.ranks between 1 and 3 
