---create database
create database sales_db;
use sales_db;

---create table
create table customers (
    cust_id int primary key,
    cust_name varchar(50)
);

---insert data into table
insert into customers 
values
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Alice Johnson');

insert into customers (cust_name) values ('Ram'); 
-- Auto-incrementing cust_id will be generated for Ram
-- by using this we can add only value in cust_name column and cust_id will be generated automatically as its primary key and auto-incrementing and if we have other columns then that column value will be null because we have not provided any value for that column and if we have not set that column as not null then it will allow null value in that column but if we have set that column as not null then it will not allow null value in that column and it will throw an error if we try to insert a record without providing a value for that column.

-- Constraints: ( Alt + Z to wrap text )
Rules are applied to columns to maintain data integrity, such as NOT NULL (no empty values) and UNIQUE (no duplicate values).

-- Create a table with all availabe constraints and add records in it
create table products (
    product_id int primary key auto_increment,
    product_name varchar(50) UNIQUE, -- Unique constraint ensures that each product name is unique in the table
    price decimal(10, 2) check (price > 0), -- Check constraint ensures that the price is greater than 0
    stock int not null 
);
