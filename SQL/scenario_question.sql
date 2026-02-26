Q. write a SQL query to find the movie titles that contain the word 'Boogie Nights'. Sort the result-set in ascending order by movie year. Return movie ID, movie title and movie release year.

SELECT mov_id, mov_title, mov_year
FROM movie
WHERE mov_title LIKE '%Boogie%Nights%'
ORDER BY mov_year ASC;

Q. write a SQL query to find the actors who played a role in the movie 'Annie Hall'. Return all the fields of actor table. (subquery related)

SELECT a.*
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
WHERE mc.mov_id IN (
    SELECT mov_id
    FROM movie
    WHERE mov_title = 'Annie Hall'
);

SELECT a.*
FROM actor a
JOIN movie_cast mc ON a.act_id = mc.act_id
JOIN movie m ON mc.mov_id = m.mov_id
WHERE m.mov_title = 'Annie Hall';

Q. write a SQL query that counts the number of unique salespeople.

select count(distinct salesperson_id) as unique_salespeople_count
from sales;

Q. write a SQL query to find the maximum order (purchase) amount in the range 2000 - 6000 (Begin and end values are included.) by combination of each customer and order date. Return customer id, order date and maximum purchase amount.

SELECT customer_id, order_date, MAX(purchase_amount) AS max_purchase_amount
FROM orders
group by customer_id, order_date
having MAX(purchase_amount) between 2000 and 6000
order by max_purchase_amount desc;

Q. Consecutive 3 Login Days (No Window Function) 

SELECT DISTINCT l1.user_id
FROM user_logins l1
JOIN user_logins l2 
  ON l1.user_id = l2.user_id
 AND l2.login_date = DATE_ADD(l1.login_date, INTERVAL 1 DAY)
JOIN user_logins l3
  ON l1.user_id = l3.user_id
 AND l3.login_date = DATE_ADD(l1.login_date, INTERVAL 2 DAY);

 Q. Employees with Same Salary in Same Department

 SELECT 
    e1.emp_id,
    e1.emp_name,
    e1.salary,
    e1.dept_id
FROM employees e1
JOIN employees e2
  ON e1.salary = e2.salary
 AND e1.dept_id = e2.dept_id
 AND e1.emp_id <> e2.emp_id;