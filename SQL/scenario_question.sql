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