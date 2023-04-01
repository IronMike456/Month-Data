/* Function Category

Description

Scalar Operate on a single row, return a single value.

Logical Compare multiple values to determine a single output.

Ranking Operate on a partition (set) of rows.

Rowset Return a virtual table that can be used in a FROM clause in a T-SQL statement.

Aggregate Take one or more input values, return a single summarizing value. */ 

----- ESCALAR ---- 
/* Scalar functions return a single value and usually work on a single row of data. The number of input values they take can be zero (for example, GETDATE), one (for example, UPPER), or multiple (for example, ROUND). Because scalar functions always return a single value */ 

/*  They are most commonly used in SELECT clauses and WHERE clause predicates. They can also be used in the SET clause of an UPDATE statement. */ 

--- Escalar samples

/* At the time of writing, the SQL Server Technical Documentation listed more than 200 scalar functions that span multiple categories, including:

Configuration functions
Conversion functions
Cursor functions
Date and Time functions
Mathematical functions
Metadata functions
Security functions
String functions
System functions
System Statistical functions
Text and Image functions */ 

SELECT  SalesOrderID,
    OrderDate,
        YEAR(OrderDate) AS OrderYear,
        DATENAME(mm, OrderDate) AS OrderMonth,
        DAY(OrderDate) AS OrderDay,
        DATENAME(dw, OrderDate) AS OrderWeekDay,
        DATEDIFF(yy,OrderDate, GETDATE()) AS YearsSinceOrder
FROM Sales.SalesOrderHeader;

SELECT TaxAmt,
       ROUND(TaxAmt, 0) AS Rounded,
       FLOOR(TaxAmt) AS Floor,
       CEILING(TaxAmt) AS Ceiling,
       SQUARE(TaxAmt) AS Squared,
       SQRT(TaxAmt) AS Root,
       LOG(TaxAmt) AS Log,
       TaxAmt * RAND() AS Randomized
FROM Sales.SalesOrderHeader;

SELECT  CompanyName,
        UPPER(CompanyName) AS UpperCase,
        LOWER(CompanyName) AS LowerCase,
        LEN(CompanyName) AS Length,
        REVERSE(CompanyName) AS Reversed,
        CHARINDEX(' ', CompanyName) AS FirstSpace,
        LEFT(CompanyName, CHARINDEX(' ', CompanyName)) AS FirstWord,
        SUBSTRING(CompanyName, CHARINDEX(' ', CompanyName) + 1, LEN(CompanyName)) AS RestOfName
FROM Sales.Customer;

--- IIF 
/* The IIF function evaluates a Boolean input expression, and returns a specified value if the expression evaluates to True, and an alternative value if the expression evaluates to False.

For example, consider the following query, which evaluates the address type of a customer. If the value is "Main Office", the expression returns "Billing". For all other address type values, the expression returns "Mailing".*/ 

SELECT AddressType,
      IIF(AddressType = 'Main Office', 'Billing', 'Mailing') AS UseAddressFor
FROM Sales.CustomerAddress;

--- Choose 
/* The CHOOSE function evaluates an integer expression, and returns the corresponding value from a list based on its (1-based) ordinal position. */ 
SELECT SalesOrderID, Status,
CHOOSE(Status, 'Ordered', 'Shipped', 'Delivered') AS OrderStatus
FROM Sales.SalesOrderHeader;

--- Ranking functions 

/* Ranking functions allow you to perform calculations against a user-defined set of rows. These functions include ranking, offset, aggregate, and distribution functions. */ 

SELECT TOP 100 ProductID, Name, ListPrice,
RANK() OVER(ORDER BY ListPrice DESC) AS RankByPrice
FROM Production.Product AS p
ORDER BY RankByPrice;

-- OVER
/* You can use the OVER clause to define partitions, or groupings within the data. For example, the following query extends the previous example to calculate price-based rankings for products within each category.*/ 

SELECT c.Name AS Category, p.Name AS Product, ListPrice,
  RANK() OVER(PARTITION BY c.Name ORDER BY ListPrice DESC) AS RankByPrice
FROM Production.Product AS p
JOIN Production.ProductCategory AS c
ON p.ProductCategoryID = c.ProductcategoryID
ORDER BY Category, RankByPrice;

-- Rowset functions 
/* Rowset functions return a virtual table that can be used in the FROM clause as a data source. These functions take parameters specific to the rowset function itself. They include OPENDATASOURCE, OPENQUERY, OPENROWSET, OPENXML, and OPENJSON.

The OPENDATASOURCE, OPENQUERY, and OPENROWSET functions enable you to pass a query to a remote database server. The remote server will then return a set of result rows. For example, the following query uses OPENROWSET to get the results of a query from a SQL Server instance named SalesDB.*/ 

SELECT a.*
FROM OPENROWSET('SQLNCLI', 'Server=SalesDB;Trusted_Connection=yes;',
    'SELECT Name, ListPrice
    FROM AdventureWorks.Production.Product') AS a;

------ Aggregate functions 

/* Most of the queries we have looked at operate on a row at a time, using a WHERE clause to filter rows. Each row returned corresponds to one row in the original data set.

Many aggregate functions are provided in SQL Server. In this section, we’ll look at the most common functions such as SUM, MIN, MAX, AVG, and COUNT.*/ 

/* When working with aggregate functions, you need to consider the following points:

Aggregate functions return a single (scalar) value and can be used in SELECT statements almost anywhere a single value can be used. For example, these functions can be used in the SELECT, HAVING, and ORDER BY clauses. However, they cannot be used in the WHERE clause.
Aggregate functions ignore NULLs, except when using COUNT(*).
Aggregate functions in a SELECT list don't have a column header unless you provide an alias using AS.
Aggregate functions in a SELECT list operate on all rows passed to the SELECT operation. If there is no GROUP BY clause, all rows satisfying any filter in the WHERE clause will be summarized. You will learn more about GROUP BY in the next topic.
Unless you're using GROUP BY, you shouldn't combine aggregate functions with columns not included in functions in the same SELECT list. */ 


/* Function Name

SUM SUM(expression) Totals all the non-NULL numeric values in a column.

AVG AVG(expression) Averages all the non-NULL numeric values in a column (sum/count).

MIN MIN(expression) Returns the smallest number, earliest date/time, or first-occurring string (according to collation sort rules).

MAX MAX(expression) Returns the largest number, latest date/time, or last-occurring string (according to collation sort rules).

COUNT or COUNT_BIG COUNT(*) or COUNT(expression) With (*), counts all rows, including rows with NULL values. When a column is specified as expression, returns the count of non-NULL rows for that column. 
                                                                                                              COUNT returns an int; COUNT_BIG returns a big_int.*/ 

SELECT AVG(ListPrice) AS AveragePrice,
       MIN(ListPrice) AS MinimumPrice,
       MAX(ListPrice) AS MaximumPrice
FROM Production.Product
WHERE ProductCategoryID = 15;

/* When using aggregates in a SELECT clause, all columns referenced in the SELECT list must be used as inputs for an aggregate function, or be referenced in a GROUP BY clause.

Consider the following query, which attempts to include the ProductCategoryID field in the aggregated results: */ 

--- Distinct with aggregate 

SELECT COUNT(DISTINCT CustomerID) AS UniqueCustomers
FROM Sales.SalesOrderHeader; 

/* You should be aware of the use of DISTINCT in a SELECT clause to remove duplicate rows. When used with an aggregate function, DISTINCT removes duplicate values from the input column before computing the summary value. 
DISTINCT is useful when summarizing unique occurrences of values, such as customers in the orders table.*/ 

/* It is important to be aware of the possible presence of NULLs in your data, and of how NULL interacts with T-SQL query components, including aggregate function. There are a few considerations to be aware of:

With the exception of COUNT used with the (*) option, T-SQL aggregate functions ignore NULLs. For example, a SUM function will add only non-NULL values. NULLs don't evaluate to zero. COUNT(*) counts all rows, regardless of value or non-value in any column.
The presence of NULLs in a column may lead to inaccurate computations for AVG, which will sum only populated rows and divide that sum by the number of non-NULL rows. There may be a difference in results between AVG(<column>) and (SUM(<column>)/COUNT(*)). */ 

SELECT SUM(c2) AS sum_nonnulls, 
    COUNT(*) AS count_all_rows, 
    COUNT(c2) AS count_nonnulls, 
    AVG(c2) AS average, 
    (SUM(c2)/COUNT(*)) AS arith_average
FROM t1;

----- GROUP BY 

--- GROUP BY creates groups and places rows into each group as determined by the elements specified in the clause. 

SELECT CustomerID
FROM Sales.SalesOrderHeader
GROUP BY CustomerID;

--- The query above is equivalent to the following query: 
SELECT DISTINCT CustomerID
FROM Sales.SalesOrderHeader; 

/* So, what’s the difference between writing the query with a GROUP BY or a DISTINCT? If all you want to know is the distinct values for CustomerID,
 there is no difference. But with GROUP BY, we can add other elements to the SELECT list that are then aggregated for each group.*/ 

 SELECT CustomerID, COUNT(*) AS OrderCount
FROM Sales.SalesOrderHeader
GROUP BY CustomerID;

SELECT CustomerID, COUNT(*) AS OrderCount
FROM Sales.SalesOrderHeader
GROUP BY CustomerID
ORDER BY CustomerID;

/* A common obstacle to becoming comfortable with using GROUP BY in SELECT statements is understanding why the following type of error message occurs: 
            Msg 8120, Level 16, State 1, Line 2 Column <column_name> is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.*/

-- Sample 
SELECT CustomerID, PurchaseOrderNumber, COUNT(*) AS OrderCount
FROM Sales.SalesOrderHeader
GROUP BY CustomerID; 

/* 
Msg 8120, Level 16, State 1, Line 1
Column 'Sales.SalesOrderHeader.PurchaseOrderNumber' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause. */ 

--- Solution 
/* Here’s another way to think about it. This query returns one row for each CustomerID value. But rows for the same CustomerID can have different PurchaseOrderNumber values, so which of the values is the one that should be returned?

If you want to see orders per customer ID and per purchase order, you can add the PurchaseOrderNumber column to the GROUP BY clause, as follows: */ 

SELECT CustomerID, PurchaseOrderNumber, COUNT(*) AS OrderCount
FROM Sales.SalesOrderHeader
GROUP BY CustomerID, PurchaseOrderNumber;

-- HAVING = WHERE for groups 

SELECT CustomerID,
      COUNT(*) AS OrderCount
FROM Sales.SalesOrderHeader
GROUP BY CustomerID
HAVING COUNT(*) > 10; 

/* A HAVING clause enables you to create a search condition, conceptually similar to the predicate of a WHERE clause, which then tests each group returned by the GROUP BY clause. */ 

/* Compare HAVING to WHERE
While both HAVING and WHERE clauses filter data, remember that WHERE operates on rows returned by the FROM clause. If a GROUP BY ... HAVING section exists in your query following a WHERE clause, the WHERE clause will filter rows before GROUP BY is processed—potentially limiting the groups that can be created.

A HAVING clause is processed after GROUP BY and only operates on groups, not detail rows. To summarize:

A WHERE clause filters rows before any groups are formed
A HAVING clause filters entire groups, and usually looks at the results of an aggregation. */ 


