-- Inner Join
SELECT emp.FirstName, ord.Amount
FROM HR.Employee AS emp 
INNER JOIN Sales.SalesOrder AS ord
    ON emp.EmployeeID = ord.EmployeeID; 

-- Joins that specify multiple matching columns are called composite joins. 

/* INNER JOIN keyword selects all rows from both tables as long as there is a match between the columns. */

SELECT p.ProductID, m.Name AS Model, p.Name AS Product
FROM Production.Product AS p
INNER JOIN Production.ProductModel AS m
    ON p.ProductModelID = m.ProductModelID
ORDER BY p.ProductID;


SELECT od.SalesOrderID, m.Name AS Model, p.Name AS ProductName, od.OrderQty
FROM Production.Product AS p
INNER JOIN Production.ProductModel AS m
    ON p.ProductModelID = m.ProductModelID
INNER JOIN Sales.SalesOrderDetail AS od
    ON p.ProductID = od.ProductID
ORDER BY od.SalesOrderID;

-- Outer Join 
-- With an OUTER JOIN, you can choose to display all the rows that have matching rows between the tables, plus all the rows that don’t have a match in the other table. 
-- Left Join 

/* Outer joins are expressed using the keywords LEFT, RIGHT, or FULL preceding OUTER JOIN. The purpose of the keyword is to indicate which table 
(on which side of the keyword JOIN) should be preserved and have all its rows displayed; match, or no match. */ 

SELECT emp.FirstName, ord.Amount
FROM HR.Employee AS emp
LEFT JOIN Sales.SalesOrder AS ord
    ON emp.EmployeeID = ord.EmployeeID;

-- Cross Joins 

/* When writing queries with CROSS JOIN, consider the following guidelines:

There is no matching of rows performed, and so no ON clause is used. (It is an error to use an ON clause with CROSS JOIN.)
To use ANSI SQL-92 syntax, separate the input table names with the CROSS JOIN operator.
The following query is an example of using CROSS JOIN to create all combinations of employees and products: */ 

SELECT emp.FirstName, prd.Name
FROM HR.Employee AS emp
CROSS JOIN Production.Product AS prd;

-- A cross join is simply a Cartesian product of the two tables. Using ANSI SQL-89 syntax, you can create a cross join by just leaving off the filter that connects the two tables. 

-- Self Joins

/* So far, the joins we've used have involved different tables. There may be scenarios in which you need to retrieve and compare rows from a table with other rows from the same table. */ 

