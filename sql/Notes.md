# SQL & MySQL

## Console
Connect to your SQL server

``` shell
$ mysql -u {username} -p -h localhost 
```

#### Show your databases
``` SQL
show databases;
```

The database `information_schema` is a special table in which mysql stores the information about our databases, tables structures, and other data that it needs to operate.

#### Select a database
``` SQL
use {database};
```

#### Show currently selected database

``` SQL
select database();
```

#### Show warnings
``` SQL
show warnings;
```

## What's a database?

A place where you can store data about anything, so you can then transform that data into information.

All the focus is about the data, the design and how you operate on the data.

SQL is relational, which means tables depend on each other. Tables are related to each other.

## Command `CREATE` 

There are two main table types:
- InnoDB
- Myisam


From the architechture point of view there are two kinds of tables: 
- Catalog
- Operation

For example in a library, the amount of users will not be updated as soon as the records of the lended books so in principle, lended books should use a Myisam type and a User table should be InnoDB given that, it might be slightly more important.


### Create database
``` SQL
CREATE DATABASE platzi_operation;

CREATE DATABASE IF NOT EXISTS platzi_operation;
```

The use of `IF NOT EXISTS` ensures that instead of an error we get a warning, which might be useful for scripts

#### Create tables

``` SQL
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    author_id INTEGER UNSIGNED,
    title VARCHAR(100) NOT NULL,
    `year` INTEGER UNSIGNED NOT NULL DEFAULT 1900,
    language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 638-1 Language',
    cover_url VARCHAR(500),
    price DOUBLE(6,2) NOT NULL DEFAULT 10.0,
    sellable TINYINT(1) DEFAULT 1,
    copies INTEGER NOT NULL DEFAULT 1,
    description TEXT
);

CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER UNISGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(3)
);
```

* `INTEGER`: The datatype 
* `PRIMARY`: Means this column will act as a primarhy key
* `AUTO_INCREMENT`: Each new record will have a new index
* `UNSIGNED`: Indicates the symbol wont be stored
* `VARCHAR({max})`: A strin` of {max} number of characters
* `NOT NULL`: This column cannot be NULL
* `DEFAULT`: Self explanatory, it assigns the value by default in case no value is specified 
* `COMMENT`: Adds a comment to the column, nobody will see it but the people looking at the database structure
* `DOUBLE({total}, {decimal})` The first number tells the database the total number of digits the number will have, the second number is the number of digits reserved for the decimal
* `TINYINT(1)`: Will be either a 1 or a 0
* `TEXT` Data type for text


We should note that in even if we delete a record, the auto increment will always be the number of the last record + 1, which means that this value cannot be interpreted as the tables cardinality (The number of rows in the table)

It's important to note that in some apps there are already more users for example than the capacity of integers in most programming languages.

> **Good practices**
> - Each table named as the plural of the sustantive it represents.
> - All names in english
> - Every table needs an ID preferrably an autoincremental integer
> - Images and pictures shouldn't be stored in the DB
> - All caps for reserved mysql words 

#### Delete a table
``` SQL
DROP TABLE authors;
```

Deletes the table, it's content and structure, and it's not unduable


#### `DESCRIBE` table

``` SQL
describe authors;
desc books;
```

> Shows a brief description of the table structure

``` SQL
show full columns from books;
```

> Gives a much more detailed look at a table

``` SQL
CREATE TABLE clients (
    client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name`VARCHAR(50) NOT NULL,
    email  VARCHAR(100) NOT NULL UNIQUE,
    birthdate DATETIME,
    gender ENUM('M', 'W', 'NB', 'NA') NOT NULL,
    active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### >> Functions and keywords
* `UNIQUE`: There cannot be two equal records in this table for this column
* `DATETIME`: A normal datetime
* `TIMESTAMP`: A unix timestamp (seconds since january 1st 1970)
* `CURRENT_TIMESTAMP`: Current timestamp of the computer
* `ON UPDATE CURRENT TIMESTAMP`: Will save computer timestamp every time the record updates 

> **Good practices**
> - Never delete a row, only deactivateit (see active column)

***Excercise***

``` SQL
CREATE TABLE transactions (
    transaction_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    transaction_type ENUM('Borrowign', 'Return', 'Sell') NOT NULL,
    client_id INTEGER UNSIGNED NOT NULL,
    book_id INTEGER UNSIGNED NOT NULL,
    finished TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Command `INSERT` 

```SQL 
INSERT INTO authors (author_id, name, nationality)
VALUES ('', 'Maria Dueñas', 'ESP')

INSERT INTO authors (name, nationality)
VALUES ('Juan Rulfo', 'MEX')

INSERT INTO authors 
VALUES ('', 'Juan Rulfo', 'MEX')
```

> If you dont specify the column list before sending the values, it will spect you to send all the values.
> Many things depend on the installation configuration

#### Send multiple insertions
``` SQL
INSERT INTO authors (name, nationality)
VALUES 
('Juan Rulfo', 'MEX'), 
('Maria Dueñas', 'ESP');
```

> **Good Practices**
> - Send in chunks of 50, then if theres an error with the network or something we only loose 50 rows of data 


## Command `ON DUPLICATE KEY` 

Will update the specified values if a record already exists for a given unique key.

```SQL
INSERT INTO `clients` VALUES (1,'Maria Dolores Gomez','Maria Dolores.95983222J@random.names','1971-06-06','F',1,'2018-04-09 16:51:30') ON DUPLICATE KEY IGNORE ALL;

INSERT INTO `clients` VALUES (1,'Maria Dolores Gomez','Maria Dolores.95983222J@random.names','1971-06-06','F',1,'2018-04-09 16:51:30') ON DUPLICATE KEY UPDATE SET active = VALUES(active)
```

### >> Functions and keywords
* `IGNORE ALL`: Ignores any error that might rise NEVER USE
* `UPDATE SET column_name = VALUES({column name})`: Will update duplicated row with the values from the column name specified

> **Good practices**
> - NEVER use the IGNORE ALL command

> ***Tip*** 
> 
> Use `\G` to present data in a far more readable way
> 
> `select * from clients where client_id = 4\G`


## Subqueries
``` SQL
INSERT INTO books (title, author, `year`)
VALUES ('Some book title',
    (SELECT author_id FROM authors 
    WHERE name = 'Some author name'
    LIMIT 1
    ), 1960
);
```

This will insert into books the data we manually entered and will go do the subquery in order to get the author_id we require. Use this functionality carefully, as powerfull as this is, it can get out of hand pretty easyly as it will require more resources

## Bash and SQL files

Let's say you have a file called `db_initial.sql` that contains all of the initial data for a database you want to populate. How do you import the instructions in the file to your database?

#### Importing a file 
``` shell
$ mysql -u root -p < db_initial.sql
```

#### Specifying the database
```shell
$ mysql -u root -p -D mydatabase < db_initial.sql
```
> ***Tip***\
> For your sql files: use a double dash at the start of a line to comment it
>``` SQL
> --DROP DATABASE IF EXISTS mydatabase;
>```


## Command `SELECT`  👑
### All hail the king

First some pretty basic queries. These are the pumpkyn latte of select
``` SQL
-- Get all the columns and rows from the table clients
SELECT * FROM clients;

-- Get specific columns and all rows from the table clients
SELECT name, email, gender FROM clients;

-- Get every column from the first 10 rows of the table clients
SELECT * FROM clients LIMIT 10;

-- Get specific columns from the rows of clients that satisfy the given criteria
SELECT name, email gender FROM clients WHERE gender = 'W';
```

The real magic and usefullness of `SELECT` comes when you think about it not as just a data fetcher but as a way to dynamically design tables that will only exist when executing the query

``` SQL
SELECT name, YEAR(NOW()) - YEAR(birthdate) FROM clients LIMIT 10
``` 

> ***Tips***
> - There are a lot of functions in SQL, if you need something very specific and you think there should be a funcion for that, there probably is.
> - The keyword `LIMIT` always goes at the end.
> - Create an alias using the keyword `AS`


## Command `INNER JOIN` 

Is basically taking two tables, make a relation between them and return the resulting data. This next query will combine the data from the tables authors and books by the author_id.

```SQL
SELECT b.book_id, a.name, b.title
FROM books as b
INNER JOIN authors as a
    ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5
```

Now we will combine multiple tables, notice that when we have the info from all these tables we can apply conditions using any of the columns from any table, also it's important to note that we don't have to join all the tables by comparing them to a column of the principal table, the join command can relate tables based on other related tables. Finally, when we do the `ON` relation, is not necessary for the related columns to have the same name, we can compare by example: `ON x.item_id = y.id_item`

```SQL
SELECT 
FROM transactions as t
JOIN books as b
    ON t.book_id = b.book_id
JOIN clients as c
    ON t.client_id = c.client_id
JOIN authors as a 
    ON b.author_id = a.author_id
```

> ***Tips***
> - Of course you can use comparators such as `>`, `<`, `<=`, etc. when creating a query 
> - `JOIN` and `INNER JOIN` are the same
> - On MySQL you can ditch the `AS` keyword entirely and just put the alias in front of the table name like so:
> ```sql
> SELECT * FROM transactions t
> ```


## Command `LEFT JOIN` 

Returns records from the main table, even when there's no matches with the joined tables, the following query will return all the authors between the id's 1 to 5, even if a given author has no books on record, where as we saw with the previous 

```SQL
SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a
LEFT JOIN books AS b
    ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id;
```

We can go one step forward by using the functions `COUNT()` and `GROUP BY`, these functions used together will let us get the ammount of books per author, because we are saying to sql to group all the results by author id and then we are using the function count to return the ammount of boot ids received

```SQL
SELECT a.author_id, a.name, a.nationality, COUNT(b.book_id)
FROM authors AS a
LEFT JOIN books AS b
    ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
GROUP BY a.author_id
ORDER BY a.author_id;
```

### >> Functions and keywords

- `YEAR()`: Returns the year from a date
- `NOW()`: Returns date and time from right now
- `LIKE '%% text to find'`: Text alikness function. The `%%` works as a wildcard
- `COUNT(*)`: Returns a count of items in a query
- `BETWEEN 1 AND 5`: Returns for a condtion between the given numbers, both inclusive, works on dates and numbers
- `WHERE {column} IN ('{value1}', '{value2}', '{valueN}')`: Returns record when column value is in any of the given options
- `ORDER BY {column_name}`: Will order the results by the given column
  - `ASC`, `DESC`: Specifies the sorting direction, by default `ASC`
- `GROUP BY {column_name}`: Will group the results by the specified columns


## All `JOINS` and how to use them.

 // WIP //
 
