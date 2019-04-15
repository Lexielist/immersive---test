create database customer;
use customer;

/*check number of all company*/
select count(*) from customerinfo;
/*check number of distinct company*/
select count(distinct company) from customerinfo;

create table uniqcompany select distinct company from customerinfo;
select count(*) from uniqcompany;

select uniqcompany.company,customerinfo.Title from uniqcompany
left join customerinfo on uniqcompany.company=customerinfo.company;

/* why is the above table has 300 rows? Should it be 267 rows, because the uniqcompany has 267 rows
what is the name of this table? */

select uniqcompany.company,customerinfo.City from uniqcompany
left join customerinfo on uniqcompany.company=customerinfo.company;

/*
ALTER TABLE 'dbtest2' ADD COLUMN 'column1' INT NOT NULL;

INSERT INTO 'dbtest2' ('column1')
  SELECT 'dbtest1'.'column1'
  FROM 'dbtest1';
  
  
SELECT Customerinfo.FirstName, customerinfo.LastName
FROM Customerinfo
LEFT JOIN uniqcompany ON customerinfo.company = uniqcompany.company;
*

CREATE TABLE uniq1 AS
    SELECT Title, FirstName, LastName
    FROM customerinfo
    WHERE customerinfo.company = uniqcompany.company;

/*  
alter table uniqcompany add column Zip int not null;

insert into uniqcompany (Zip)
select ZipCode
from customerinfo;
  
/*
Select customerinfo.company
from customerinfo
Inner join uniqcompany ON customerinfo.company = uniqcompany.company;
*/
/*
Select customerinfo.Title
from customerinfo
Inner join uniqcompany ON customerinfo.company = uniqcompany.company 
*/





 
