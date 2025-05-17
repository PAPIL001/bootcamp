# Level-Up Drills: Designing Real-World Persistence Systems

These drills challenge you to think like an experienced engineer, focusing on analyzing trade-offs, anticipating failure modes, and making design choices in real-world persistence systems.

## 1. Schema Evolution and Migrations

**Challenge:** Simulate a real-world schema change. Start with a `users` table with `id` and `name`. Later, add a `created_at` timestamp.

* Apply this schema change without losing existing data.
* Write a migration SQL script.
* Show how to apply the migration safely in production.

**Reflection:**

* What could go wrong if you applied this change directly?
* How do production systems manage zero-downtime migrations?

## 2. Model Boundary Enforcement

**Challenge:** Ensure ORM models (SQLAlchemy) and external APIs (Pydantic) are strictly separated.

* Write a feature to update a user's profile.
* Ensure controllers or the API layer never leak raw SQLAlchemy models.
* Only expose validated Pydantic models.

**Reflection:**

* Why is it risky to return raw ORM objects directly?
* What happens if the database schema evolves but external APIs do not?

## 3. Idempotent Upserts (Insert or Update)

**Challenge:** Implement an upsert that inserts a product if it doesn't exist and updates the price if it exists.

* Do this in SQLite and PostgreSQL.

**Reflection:**

* Why are idempotent writes important in distributed systems?
* What if the database doesn't support `ON CONFLICT` natively?

## 4. Versioned Data Storage

**Challenge:** Keep a history of changes to user email addresses.

* Design a table or schema to record all versions.
* Implement a query to fetch the latest or historical versions.

**Reflection:**

* When is it better to version data rather than overwrite it?

## 5. Concurrency and Race Condition Management

**Challenge:** Handle concurrent money transfers between two accounts.

* Write naive balance update code without transactions.
* Write a correct version using `SELECT FOR UPDATE` or retry logic.

**Reflection:**

* How did you break the system in step 1?
* Why is locking tricky in high-concurrency environments?

## 6. Handling Large Binary Data

**Challenge:** Store user profile images.

* Implement two designs:
    * Store images as BLOBs in the database.
    * Store file paths and save files to disk.
* Write pros and cons for each approach.

**Reflection:**

* What are the trade-offs between file system storage and database BLOBs?

## 7. Schema-First vs Code-First Modeling

**Challenge:** You receive a pre-defined SQL schema from another team.

* Write SQLAlchemy models based on this schema.
* Explain the difference between schema-first and code-first design.

**Reflection:**

* When would you prefer each approach?

## 8. Data Lifecycle Management

**Challenge:** Add soft delete to your products table.

* Add a `deleted_at` column.
* Ensure all queries ignore soft-deleted records.
* Write a cleanup script to purge records older than 30 days.

**Reflection:**

* Why do many systems use soft deletes?
* What risks exist if you forget to filter them?

## 9. Boundary Testing with Large Datasets

**Challenge:** Stress test your system.

* Generate 1 million records for your products table.
* Compare:
    * Single inserts (naive).
    * Batch inserts using transactions or raw SQL.
* Measure execution time and memory usage.
