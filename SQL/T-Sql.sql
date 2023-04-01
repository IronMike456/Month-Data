-- Normal query 
SELECT OrderDate, COUNT(OrderID) AS Orders
FROM Sales.SalesOrder
WHERE Status = 'Shipped'
GROUP BY OrderDate 
HAVING COUNT(OrderID) > 1
ORDER BY OrderDate DESC;
-- Selecting specific 
SELECT ProductID, Name, ListPrice, StandardCost
FROM Production.Product;
-- Selecting exprewssions 
SELECT ProductID,
      Name + '(' + ProductNumber + ')',
  ListPrice - StandardCost
FROM Production.Product;

SELECT ProductID AS ID,
      Name + '(' + ProductNumber + ')' AS ProductName,
  ListPrice - StandardCost AS Markup
FROM Production.Product;

/* Compatible data type values can be implicitly converted as required. For example, suppose you can use the + operator to add an integer number to a decimal number,
 or to concatenate a fixed-length char value and a variable length varchar value. However, in some cases you may need to explicitly convert values from one data type to another 
 - for example, trying to use + to concatenate a varchar value and a decimal value will result in an error, unless you first convert the numeric value to a compatible string data type.*/ 

-- CAST AND TRY CAST

SELECT CAST(ProductID AS varchar(4)) + ': ' + Name AS ProductName -- The CAST function converts a value to a specified data type if the value is compatible with the target data type. An error will be returned if incompatible.
FROM Production.Product;
/* Note that the results of using CONVERT are the same as for CAST. The CAST function is an ANSI standard part of the SQL language that is available in most database systems, while CONVERT is a SQL Server specific function.*/

-- Convert and TRY_Convert

SELECT CONVERT(varchar(4), ProductID) + ': ' + Name AS ProductName -- CAST is the ANSI standard SQL function for converting between data types, and is used in many database systems. In Transact-SQL, you can also use the CONVERT function, as shown here:
FROM Production.Product;


-- The PARSE function is designed to convert formatted strings that represent numeric or date/time values. For example, consider the following query (which uses literal values rather than values from columns in a table):
SELECT PARSE('01/01/2021' AS date) AS DateValue,
   PARSE('$199.99' AS money) AS MoneyValue;

-- STR The STR function converts a numeric value to a varchar.
SELECT ProductID,  '$' + STR(ListPrice) AS Price
FROM Production.Product;

-- A NULL value means no value or unknown. It does not mean zero or blank, or even an empty string. 

-- T-SQL provides functions for conversion or replacement of NULL values. 

-- ISNULL   
SELECT FirstName,
      ISNULL(MiddleName, 'None') AS MiddleIfAny, -- For example, suppose the Sales.Customer table in a database includes a MiddleName column that allows NULL values. When querying this table, rather than returning NULL in the result, you may choose to return a specific value, such as "None".
      LastName
FROM Sales.Customer;

/* The ISNULL function is not ANSI standard, so you may wish to use the COALESCE function instead.
 COALESCE is a little more flexible in that it can take a variable number of arguments, each of which is an expression. 
 It will return the first expression in the list that is not NULL. */ 

 -- If there are only two arguments, COALESCE behaves like ISNULL. However, with more than two arguments, COALESCE can be used as an alternative to a multipart CASE expression using ISNULL.

-- NULLIF 

-- The NULLIF function allows you to return NULL under certain conditions. This function has useful applications in areas such as data cleansing, when you wish to replace blank or placeholder characters with NULL.
-- NULLIF takes two arguments and returns NULL if they're equivalent. If they aren't equal, NULLIF returns the first argument.

SELECT SalesOrderID,
      ProductID,
      UnitPrice,
      NULLIF(UnitPriceDiscount, 0) AS Discount
FROM Sales.SalesOrderDetail;

