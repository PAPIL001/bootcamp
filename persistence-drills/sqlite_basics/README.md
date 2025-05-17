# SQLite Summary and Exercises

This document summarizes the introduction to SQLite and the exercises provided. It covers SQLite's characteristics, when to use it, and practical exercises to get started.

## Introduction to Databases and SQLite

The initial section provides a brief overview of databases, recommending resources for further learning:

* **Database Introduction:** [https://philip.greenspun.com/sql/introduction.html](https://philip.greenspun.com/sql/introduction.html)
* **Database Design:** Database design for mere mortals
* **SQL:** SQL for dummies
* **Advanced SQL:** Joe Celko's books

It emphasizes a practical, programming-oriented approach to databases.

### Key Database Concepts

The document highlights essential database concepts:

* Transactions
* ACID Properties (Atomicity, Consistency, Isolation, Durability)

It also poses questions to test understanding:

* What are transactions?
* What are ACID Properties?
* What happens if you don't have transactions?
* What properties does your file system have?
* What happens if you don't have A, C, I, or D in ACID? When is it acceptable to violate these properties?

### Database Choices

The document provides guidance on choosing a database:

* **(Key, Value) store:** Use Redis for simple lookup tables.
* **Relational Database:** Use a relational database when you need a database.
    * **SQLite:** Use SQLite when the application is the only entity interacting with the database (e.g., most web apps).
    * **Postgres:** Use Postgres when multiple applications need to access the database (e.g., loading, CRUD operations, and reports), especially in a distributed environment.

## SQLite

The exercises will primarily use SQLite.

### SQLiteの特徴 (Characteristics)

* Doesn't require a server.
* The database is stored in a single file, which can be easily copied.

### Tools

* SQLite can be installed locally for testing.
* DB Browser can be used in PyCharm and VS Code.

### Installation and Testing

The following steps are provided to install and test SQLite:

1.  Open a database: `sqlite3 example.db`
2.  Create a table: `CREATE TABLE COMPANIES (company_name varchar(20), id int);`
3.  Add values: `INSERT INTO COMPANIES VALUES ("aganitha", 1);`
4.  Exit: `ctrl-D` or `.exit`
5.  Verify the database file: `file example.db`
6.  Copy the database file to a server.
7.  On the server, open the database: `sqlite3 example.db`
8.  Execute a query: `SELECT * from COMPANIES`

### Exercise

* Write a program that generates 500 insert statements for the table. Execute this SQL program using the command line and measure the execution time.
