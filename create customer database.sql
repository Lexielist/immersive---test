create database customer;
use customer;
create table customerTable(
id integer primary key
);
drop table customertablecustomer;

/*ALTER TABLE table_name ADD column_name field_type (PRIMARY KEY auto_increment if applicable) FIRST*/
alter TABLE customerinfo ADD id INT PRIMARY KEY auto_increment first;


/*this line moves id column to the very left*/
alter table customerinfo modify id int first;


/*this line moves id column to right after 'position' column*/
alter table customerinfo modify id int after position;


/*this line drops the id column - useful if you want to redo it*/
alter table customerinfo drop column id;

select state from customerinfo;

/*count number of state*/
select count(state) from customerinfo;

/* count number of distinct state*/
select count(distinct state) from customerinfo;
/*count number of distinct company and print out in descending order*/

create table uniqTable select distinct Company from customerinfo;

select * from uniqTable




