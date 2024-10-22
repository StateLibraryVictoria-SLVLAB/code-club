# Introduction to SQL

## SQL (Structured Query Language)

SQL stands for **S**tructured **Q**uery **L**anguage, and is the programming language implemented by a database management system (DBMS) used for managing and querying data held in a relational database. SQL has been an ANSI (American National Standards Institute) standard since 1986 and each different DBMS has its own implementation of this standard. These different implementations have varying adherence to the standard, so in practice SQL code of any complexity is not typically transferrable between different DBMS systems without some modification. However, because of the standard, skills learned in one DBMS system are largely applicable to another.

Please note: the examples in this introduction use the [SQLite](https://www.sqlite.org/) engine.

The roots of SQL trace back to the work of Edgar F. Codd, a British computer scientist who introduced the relational model for databases in the 1970s. His groundbreaking work, ["A Relational Model of Data for Large Shared Data Banks"](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf), laid the foundation for how data is stored and retrieved in relational database systems, revolutionizing the field and giving rise to SQL as the standard language for relational database management.



SQL enables users to interact with data using commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, providing a flexible and intuitive way to manage and analyze data efficiently.

SQL has 2 major components:

- A **Data Definition Language (DDL)** for defining the database structure.

- A **Data Manipulation Language (DML)** for retrieving and updating data.

## Data Definition Language (DDL)

### DDL - CREATE command
`CREATE TABLE` creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.

For example:

```sql
CREATE TABLE <table_name>
  (<column1> <data type> [<constraint>] [<check>],
  (<column1> <data type> [<constraint>] [<check>],
  ...
  PRIMARY KEY (<unique_field>),
  [FOREIGN KEY (<foreign_field>) REFERENCES <associated_table> <foreign_field>)]
  );
```
Example of a University database with two tables : Department & Employee

#### Table: `employee`
| employee_id | first_name | last_name | department_id | salary | hire_date  |
|-------------|------------|-----------|---------------|--------|------------|
| 1           | John       | Smith     | 1             | 60000  | 2020-01-15 |
| 2           | Jane       | Doe       | 2             | 70000  | 2019-06-23 |
| 3           | Alice      | Johnson   | 1             | 75000  | 2021-04-01 |
| 4           | Bob        | Lee       | 3             | 55000  | 2018-10-10 |
| 5           | Eve        | Taylor    | 2             | 72000  | 2020-11-03 |

#### Table: `department`
| department_id | department_name |
|---------------|-----------------|
| 1             | IT              |
| 2             | HR              |
| 3             | Marketing       |

#### Create Table Specification:

```sql
CREATE TABLE department (
    department_id INTEGER,
    department_name TEXT NOT NULL,
  PRIMARY KEY (department_id)
);
```

```sql
CREATE TABLE employee (
    employee_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER,
    salary REAL,
    hire_date DATE NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (department_id) REFERENCES department (department_id)
);
```
#### PRIMARY KEY
A **Primary Key** is a column (or a set of columns) in a table that uniquely identifies each record in that table. The values in this column must be unique, and they cannot contain NULL values. A primary key ensures that no duplicate records exist in the table and is used to enforce the entity integrity of the table.

#### FOREIGN KEY
A **Foreign Key** is a column (or a set of columns) in a table that creates a relationship between two tables. It points to/references the primary key in another table and ensures referential integrity by restricting invalid data that doesn’t exist in the referenced table.

## Data Manipulation Language (DML)

- `SELECT`: to query data in the database.
- `INSERT`: to insert data into a table.
- `UPDATE`: to update data in a table.
- `DELETE`: to delete data from a table.

### Basic `SELECT` Queries
The following SQL statement selects all the columns from the "employee" table:
```sql
SELECT *
FROM employee;
```

Select the first_name and last_name only of each employee.
```sql
SELECT first_name, last_name
FROM employee;
```

### `WHERE` Clause
The SQL `WHERE` clause is used to filter records in a database query. It defines conditions (or predicates) that must be met for rows to be included in the result set. Only the rows that satisfy the conditions specified in the `WHERE` clause will be returned by the query.

Example: Retrieve all employees from the HR department.
```sql
SELECT first_name, last_name
FROM employee
WHERE department_id = 2;
```

A **predicate** is the condition or expression in the WHERE clause that evaluates to either **TRUE**, **FALSE**, or **NULL**. It’s the logic used to determine which rows to include. A predicate can be a comparison, a range check, pattern matching, or even a combination of multiple conditions.

### Types of Predicates:
1. **Comparison Predicate**: Compares values.
   ```sql
   WHERE salary > 50000;
   ```

2. **Range Predicate**: Uses `BETWEEN` to specify a range.
   ```sql
   WHERE hire_date BETWEEN '2020-01-01' AND '2022-01-01';
   ```

3. **Set Membership Predicate**: Uses `IN` to check for values within a set.
   ```sql
   WHERE department IN ('Sales', 'Marketing');
   ```

4. **Pattern Matching Predicate**: Uses `LIKE` for matching patterns (e.g., with `%` as a wildcard).
   ```sql
   WHERE last_name LIKE 'J%';
   ```

5. **Logical Predicates**: Combines multiple conditions using logical operators like `AND`, `OR`, and `NOT`.
   ```sql
   WHERE department_id = 2
   AND salary > 50000;
   ```

- `=` equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to
- `<>` not equal to



### SELECT `DISTINCT` : Duplicate Removal
SQL does not remove duplicates unless explictly asked to do so (removal of duplicates is computionally expensive).
`DISTINCT` is used to remove duplicates from a result set.
```sql
SELECT DISTINCT department_id
FROM employee;
```

### Sorting Output from Queries
SQL is not sorted by default.
Use `ORDER BY` statement to sort output.
The default is to order by ascending output. Use `desc` for descending output.
```sql
SELECT employee_id, last_name
FROM employee
ORDER BY last_name;
```

You can also use the column position in the `ORDER BY` clause.
e.g. ORDER BY 2 desc;

### `GROUP BY` and Aggregation
Example: No grouping
`COUNT (*)` returns the number of rows.
```sql
SELECT count(*)
FROM employee;
```

Example: Find the total salary paid to employees in each department.
```sql
SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id;
```

To restrict a `GROUP BY`, use `HAVING`, because a `WHERE` clause only applies to single rows.
```sql
SELECT department_id, COUNT(*)
FROM employee
GROUP BY department_id
HAVING COUNT(*) > 2
ORDER BY department_id;
```

### SQL Aggregate Functions
`COUNT`: Returns the number of rows, which meet the specified condition.
```sql
SELECT COUNT(*) AS high_sal
FROM employee
WHERE salary > 50000;
```

`SUM`: Returns the sum of values in a specified column (numeric).
```sql
SELECT SUM(salary)
FROM employee
WHERE department_id = 3;
```

`MIN`: returns the minimum value in a specified column.

`MAX`: returns the maximum value in a specified column.

`AVG`: returns the average of the values in a specified column.
```sql
SELECT MIN(salary) AS min_sal,
       MAX(salary) AS max_sal,
       AVG(salary) AS avg_sal
FROM employee;
```

### Subqueries or Nested Queries
A complete SQL statement embedded within another SELECT statement.
The result of the inner SELECT statement is used in the outer statement to determine the contents of the final result.

- Subquery with equality
```sql
SELECT first_name, last_name
FROM employee
WHERE department_id = (SELECT department_id
                           FROM department
                           WHERE department_name = 'IT');
```
- Nested Subquery (use of `IN`)
```sql
SELECT first_name, last_name
FROM employee
WHERE department_id IN
 (SELECT department_id
  FROM department
  WHERE department_name = 'Marketing');
```

### Multi-table Queries (`JOIN`)
Joins are used to combine data from multiple tables, based on a related column between them.
#### Simple Join (`INNER`)
e.g. Retrieve the names of employees along with their department names.
```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employee e
JOIN department d ON e.department_id = d.department_id;
```
A prefix which represents the table name is used in front of each attribute. This is recommended to avoid ambiguity.

You must include a `JOIN` clause for every link between 2 tables.
If you have `N` tables in the `FROM` clause, you should have (`N-1`) join clauses.


### Outer Join
- **`LEFT JOIN`**: retains rows of the first (left) table that are unmatched with rows from the second (right) table.
- **`RIGHT JOIN`**: retains rows of the second (right) table that are unmatched with rows from the first (left) table.
- **`FULL OUTER JOIN`**: retains rows that are unmatched in both tables.

In all of the above outer joins, the displayed unmatched columns are filled with NULLS.


![INNER JOIN](https://www.w3schools.com/sql/img_inner_join.png)  |  ![LEFT JOIN](https://www.w3schools.com/sql/img_left_join.png) |  ![RIGHT JOIN](https://www.w3schools.com/sql/img_right_join.png) |  ![FULL OUTER JOIN](https://www.w3schools.com/sql/img_full_outer_join.png)

Source: https://www.w3schools.com/sql/sql_join.asp

### Modify Commands

#### `INSERT`
```sql
INSERT INTO <table_name>
VALUES (column1 value, column2 value, ...);
```
e.g. Insert a new employee into the Employees table.
```sql
INSERT INTO employee
VALUES (6, 'Charlie', 'Green', 1, 65000, '2022-07-20');
```

#### `UPDATE`
```sql
UPDATE <table_name>
SET <column_name> = <new_value>
WHERE <search_condition>;
```

e.g. Update the salary of an employee.
```sql
UPDATE employee
SET salary = 80000
WHERE employee_id = 1;
```

#### `DELETE`
```sql
DELETE FROM <table_name>
WHERE <search_condition>;
```

- Can delete multiple records if search condition returns more than 1 row
- If search condition is omitted, all table records are deleted.

e.g. Remove an employee from the table.
```sql
DELETE FROM employee
WHERE employee_id = 3;
```


## Further Learning Resources
[W3 Schools SQL Tutorial](https://www.w3schools.com/sql/)

[Codecademy SQL](https://www.codecademy.com/learn/learn-sql)


