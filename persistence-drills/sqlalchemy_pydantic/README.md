# SQLAlchemy and Pydantic Practice Exercises

This document outlines 10 progressive exercises designed to practice using SQLAlchemy with Pydantic, ranging from beginner to advanced levels.

## Beginner Level (Basic Setup & CRUD Operations)

These exercises cover the fundamentals of setting up SQLAlchemy models with Pydantic and performing basic CRUD (Create, Read, Update, Delete) operations.

### 1. Define a Simple SQLAlchemy Model with Pydantic

* Create a `User` model using SQLAlchemy.
* Define a corresponding `UserSchema` with Pydantic.
* Initialize an SQLite database.

### 2. Insert a New User

* Create a SQLAlchemy session.
* Validate user data with Pydantic before inserting.
* Commit the new user to the database.

### 3. Fetch Users from the Database

* Retrieve all users from the database.
* Convert database results to a list of Pydantic models.
* Display the users in a structured format.

## Intermediate Level (Filtering, Updating, and Deleting Data)

These exercises focus on more advanced data manipulation, including filtering, updating, and deleting records.

### 4. Filter Users Based on Email

* Create a function to fetch a user by email.
* Return a `UserSchema` response if the user exists.
* Handle cases where the user is not found.

### 5. Update User Email

* Implement a function to update a user's email.
* Ensure changes persist in the database.
* Return a success message if updated successfully.

### 6. Delete a User

* Write a function to remove a user from the database.
* Use SQLAlchemy's `delete()` method.
* Confirm deletion before committing.

## Advanced Level (Relationships, Async Queries, and Transactions)

These exercises explore more complex scenarios, including database relationships, asynchronous queries, and transactions.

### 7. Add a `Post` Table and Create a Relationship

* Define a new `Post` model with a foreign key to `User`.
* Establish a relationship between `User` and `Post`.
* Ensure users can have multiple posts.

### 8. Fetch a User and Their Posts

* Implement a query to get a user along with their posts.
* Convert results into nested Pydantic models.
* Return a structured JSON response.

### 9. Use Transactions for Bulk Inserts

* Implement a function to insert multiple users at once.
* Use transactions to ensure atomicity.
* Rollback on failure to prevent partial inserts.

### 10. Convert Everything to Async (Using SQLAlchemy 2.0)

* Use `asyncpg` for PostgreSQL with async SQLAlchemy.
* Modify queries to work with async sessions.
* Ensure async-safe user retrieval and insertion.
