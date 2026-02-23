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

-- Insert command in which we select records from another table
insert into employee1 select * from Employee;

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
    stock int not null,
    created_at timestamp default current_timestamp, -- Default constraint sets the default value to the current timestamp when a new record is inserted
    purchease_date date not null,
    cust_id int,
    constraint fk_cust_id -- Naming the foreign key constraint as fk_cust_id for better readability and maintenance
        foreign key (cust_id) references customers(cust_id) -- Foreign key constraint establishes a relationship between the products table and the customers table, ensuring that the cust_id in the products table must exist in the customers table.
);

-- Alter commands of SQL
-- Add a new column to the products table
alter table products add column description varchar(255);
-- Modify the price column to allow null values
alter table products modify column price decimal(10, 2) null;
-- Drop the description column from the products table
alter table products drop column description;
-- Add a new column to the products table with a default value
alter table products add column category varchar(50) default 'General';
-- Add a new column to the products table with a check constraint
alter table products add column discount decimal(5, 2) check (discount >= 0 and discount <= 100);
-- Add a new column to the products table with a foreign key constraint
alter table products add column supplier_id int;
alter table products add constraint fk_supplier_id foreign key (supplier_id) references suppliers(supplier_id);

-- keys in SQL
-- primary key
-- foreigen key
-- crosskey
-- combine key
-- surrogate key

-- SQL processes a query in the order: 
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT.

-- SQL joins

-- inner join

SELECT * from product p join customers c on p.product_id = c.product_id;

-- Left join

SELECT * from product p left join customers c on p.product_id = c.product_id;

-- right join

SELECT * from product p right join customers c on p.product_id = c.product_id;

-- Unions in SQL -- 
Union combine the result sets of two or more SELECT queries.
It removes duplicate rows by default.

UNION ALL is faster because it does not check for duplicates.

-- DML commands in SQL

insert is already doe in above 

-- update command

update product
set name = 'kisan'
WHERE product_id = 2;


update product
set name = 'kisan'
WHERE product_id = 2 and price > 100; -- This will update the name to 'kisan' only if the product_id is 2 and the price is greater than 100.

update product
set name = 'kisan'; -- This will update the name to 'kisan' for all records in the product table, which is not recommended unless you intend to update all records.

-- Update with CASE Statement
update product
set price = case 
    when price < 50 then price * 1.1 -- Increase price by 10% if it's less than 50
    when price >= 50 and price < 100 then price * 1.05 -- Increase price by 5% if it's between 50 and 100
    else price -- Keep the price unchanged if it's 100 or more
end;

-- Reset the "Age" column to NULL for all employees.
UPDATE Employees -- Specify the table to update.
SET Age = NULL; -- Set the "Age" column to NULL for all rows.


-- delete command

delete from product
where product_id = 2; -- This will delete the record with product_id 2 from the product table.

delete from product
where price > 100; -- This will delete all records from the product table where the price is greater than 100.

delete from product; -- This will delete all records from the product table, which is not recommended unless you intend to delete all records.

-- Write a SQL query to copy data from one table into another table.

-- Insert employees from the "OldEmployees" table into the "Employees" table.
INSERT INTO Employees (EmployeeID, Name, Age, Salary) -- Specify the target columns.
SELECT EmployeeID, Name, Age, Salary FROM OldEmployees; -- Copy data from another table.


-- Trnsaformations in SQL 

-- Aggregation functions: SUM, AVG, COUNT, MAX, MIN
SELECT SUM(price) as total_price from product; -- This will calculate the total price of all products in the product table.
SELECT AVG(price) as average_price from product; -- This will calculate the average price of all products in the product table.
SELECT COUNT(*) as total_products from product; -- This will count the total number of products in the product table.
SELECT MAX(price) as max_price from product; -- This will find the maximum price of all products in the product table.
SELECT MIN(price) as min_price from product; -- This will find the minimum price of all products in the product table.

-- numeric transformations: ROUND, CEIL, FLOOR, PLUSE, MINUS, MULTIPLY, DIVIDE

SELECT ROUND(price, 2) as rounded_price from product; -- This will round the price of each product to 2 decimal places.
SELECT CEIL(price) as ceiling_price from product; -- This will round the price of each product up to the nearest integer.
SELECT FLOOR(price) as floor_price from product; -- This will round the price of each product down to the nearest integer.
SELECT price + 10 as increased_price from product; -- This will add 10 to the price of each product.
SELECT price - 5 as decreased_price from product; -- This will subtract 5 from the price of each product.
SELECT price * 2 as doubled_price from product; -- This will multiply the price of each product by 2.
SELECT price / 2 as halved_price from product; -- This will divide the price of each product by 2.
select quantity * amount as price from product; -- This will calculate the price by multiplying the quantity and amount for each product.
select price, price * discount / 100 as discount_amount from product; -- This will calculate the discount amount by multiplying the price with the discount percentage and dividing by 100 for each product.

-- DATE and time transformations: NOW, CURDATE, CURTIME, DATE_ADD, DATE_SUB
SELECT NOW() as current_datetime; -- This will return the current date and time.
SELECT CURDATE() as current_date; -- This will return the current date.
SELECT CURTIME() as current_time; -- This will return the current time.
SELECT DATE_ADD(CURDATE(), INTERVAL 7 DAY) as next_week; -- This will add 7 days to the current date and return the result as next_week.
SELECT DATE_SUB(CURDATE(), INTERVAL 7 DAY) as last_week; -- This will subtract 7 days from the current date and return the result as last_week.
SELECT DATE_ADD(CURDATE(), INTERVAL 1 MONTH) as next_month; -- This will add 1 month to the current date and return the result as next_month.
SELECT DATE_SUB(CURDATE(), INTERVAL 1 MONTH) as last_month; -- This will subtract 1 month from the current date and return the result as last_month.
SELECT DATE_ADD(CURDATE(), INTERVAL 1 YEAR) as next_year; -- This will add 1 year to the current date and return the result as next_year.
SELECT DATE_SUB(CURDATE(), INTERVAL 1 YEAR) as last_year; -- This will subtract 1 year from the current date and return the result as last_year.
select purchease_date, DATE_ADD(purchease_date, INTERVAL 30 DAY) as return_date from product; -- This will calculate the return date by adding 30 days to the purchease_date for each product.
select purchease_date, DATE_ADD(purchease_date, INTERVAL 1 YEAR) as warranty_end_date from product; -- This will calculate the warranty end date by adding 1 year to the purchease_date for each product.
select date_of_birth, year(date_of_birth) as birth_year from customers; -- This will extract the birth year from the date_of_birth for each customer.
select date_of_birth, month(date_of_birth) as birth_month from customers; -- This will extract the birth month from the date_of_birth for each customer.
select date_of_birth, day(date_of_birth) as birth_day, weekday(date_of_birth) as birth_weekday, dayname(date_of_birth) as birth_day_name from customers; -- This will extract the birth day, birth weekday, and birth day name from the date_of_birth for each customer.

-- String transformations: CONCAT, UPPER, LOWER, SUBSTRING, LENGTH
SELECT CONCAT(first_name, ' ', last_name) as full_name from customers; -- This will concatenate the first_name and last_name with a space in between to create a full_name for each customer.
SELECT UPPER(product_name) as uppercase_name from product; -- This will convert the product_name to uppercase for each product.
SELECT LOWER(product_name) as lowercase_name from product; -- This will convert the product_name to lowercase for each product.
SELECT SUBSTRING(product_name, 1, 5) as short_name from product; -- This will extract the first 5 characters from the product_name to create a short_name for each product.
SELECT LENGTH(product_name) as name_length from product; -- This will calculate the length of the product_name for each product.

-- Casting data types: CAST

SELECT CAST(price as CHAR) as price_string from product; -- This will cast the price from a numeric data type to a character string for each product.


-- Grouping data: GROUP BY
SELECT category, COUNT(*) as total_products from product
GROUP BY category; -- This will group the products by category and count the total number of products in each category.
SELECT category, AVG(price) as average_price from product
GROUP BY category; -- This will group the products by category and calculate the average price of products in each category.
SELECT category, SUM(price) as total_price from product
GROUP BY category; -- This will group the products by category and calculate the total price of products in each category.

-- Filtering grouped data: HAVING

SELECT category, COUNT(*) as total_products from product
GROUP BY category
HAVING COUNT(*) > 5; -- This will filter the grouped data to only show categories with more than 5 products.

SELECT category, AVG(price) as average_price from product
GROUP BY category
HAVING AVG(price) > 100; -- This will filter the grouped data to only show categories with an average price greater than 100.

-- Window functions: ROW_NUMBER, RANK, DENSE_RANK, NTILE

select *, sum(price) over (order by price) as running_total from product; -- This will calculate a running total of the price for each product ordered by price.
select *, avg(price) over (order by price) as average_price from product; -- This will calculate the average price for each product ordered by price.

select *, sum(price) over (partition by category order by price rows between unbounded preceding and current row) as running_total from product; -- This will calculate a running total of the price for each product partitioned by category and ordered by price.
select *, avg(price) over (partition by category order by price rows between unbounded preceding and unbounded following) as average_price from product; -- This will calculate the average price for each product partitioned by category and ordered by price.

select *, row_number() over (order by price) as row_num from product; -- This will assign a unique row number to each product ordered by price.
select *, rank() over (order by price) as price_rank from product; -- This will assign a rank to each product based on price, with ties receiving the same rank and the next rank being skipped.
select *, dense_rank() over (partition by category order by price) as dense_price_rank from product; -- This will assign a dense rank to each product based on price within each category, with ties receiving the same rank and the next rank being the next consecutive number.