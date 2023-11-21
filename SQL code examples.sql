/* select */
SELECT column1, column2, column3
FROM table_name
WHERE condition;

/* select * */
SELECT *
FROM customers
WHERE age >= 18;

/* JOIN * */
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;

/* LEFT JOIN * */
SELECT customers.customer_name, orders.order_id
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

/* LEFT OUTER JOIN* */
SELECT customers.customer_name, orders.order_id
FROM customers
LEFT OUTER JOIN orders
ON customers.customer_id = orders.customer_id;

/* WHERE* */
SELECT name, department, salary
FROM employees
WHERE department = 'Sales' AND salary > 50000;

/* GROUP BY* */
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

/* HAVING* */
SELECT customer_id, SUM(quantity) AS total_quantity
FROM orders
GROUP BY customer_id
HAVING SUM(quantity) >= 50;


/* Window Function
Window functions in SQL are used to perform calculations on a set of rows that are related to the current row. These functions are applied to a window,
 which is a subset of rows from a table based on a specified condition or partition. Here are some examples of window functions in SQL:
ROW_NUMBER(): This function assigns a unique sequential number to each row within a partition. The syntax for the ROW_NUMBER() function is:*/

SELECT column1, column2, ..., ROW_NUMBER() OVER (ORDER BY column1) AS row_num
FROM table_name;

/* SUM* */
SELECT column1, column2, ..., SUM(column3) OVER (PARTITION BY column1) AS column3_sum
FROM table_name;

/* RANK* */
SELECT column1, column2, ..., RANK() OVER (PARTITION BY column1 ORDER BY column3 DESC) AS rank_num
FROM table_name;

/* AVG* */
SELECT column1, column2, ..., AVG(column3) OVER (PARTITION BY column1) AS column3_avg
FROM table_name;

/*UNION
In SQL, the UNION operator is used to combine the results of two or more SELECT statements into a single result set. The SELECT statements must
 have the same number of columns, and the columns must have compatible data types. Duplicate rows are automatically removed from the result set.

Here’s an example of using the UNION operator in SQL:

Suppose we have two tables named “customers” and “employees”, both with columns for “name” and “city”. We want to create a list of all people 
(both customers and employees) who live in New York City. We can use the UNION operator to combine the results of two SELECT statements, one for each table:*/

SELECT name, city
FROM customers
WHERE city = 'New York'
UNION
SELECT name, city
FROM employees
WHERE city = 'New York';

/* CREATE* */
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  phone VARCHAR(20)
);
/* INSERT* */
INSERT INTO customers (id, name, email, phone)
VALUES (1, 'John Doe', 'johndoe@example.com', '555-555-1234');

/* UPDATE* */
UPDATE students
SET major = 'Mathematics', gpa = 3.7
WHERE id = 1234;

/* DELETE* */
DELETE FROM students
WHERE id = 1234;

/* DROP* */
DROP TABLE table_name;
DROP INDEX index_name ON table_name;
DROP VIEW view_name;
DROP PROCEDURE procedure_name;

/* ALTER* */
ALTER TABLE table_name
ADD column_name data_type [constraint],
MODIFY column_name data_type [constraint],
DROP column_name,
ADD CONSTRAINT constraint_name constraint_definition,
DROP CONSTRAINT constraint_name;

/* ALTER INDEX* */
ALTER INDEX index_name
ADD column_name,
DROP column_name;

ALTER VIEW view_name
AS select_statement;