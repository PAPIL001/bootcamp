### 1. What are transactions?

Database transactions allow you to combine several operations into a single work unit.  Consider it a pledge that either all changes will occur or none will.  Thus, the transaction can be "rolled back" to prevent incomplete modifications and maintain data consistency in the event that something goes wrong throughout the process.

### 2. What are ACID properties?

ACID stands for Atomicity, Consistency, Isolation, and Durability

Atomicity: Every action taken during a transaction is handled as a single item.  The transaction as a whole fails if one fails.
 Consistency: Following the transaction, the database begins and ends in a legitimate state.  It guarantees adherence to regulations.
 Isolation: Transactions are isolated from one another, thus until a transaction is finished, it won't have an impact on another.
 Durability: Even in the event of a system failure, changes made during a transaction are irreversible once they are committed.

### 3. Suppose you do not have transactions. Is that system useful? Why?

In the absence of transactions, chaos may ensue.  Assume that when we are updating two tables, one of them succeeds while the other does not.  We are now left with contradictory evidence.  Therefore, a transaction-free system is less dependable and may result in corrupted data.  For the majority of use scenarios, it isn't optimal.

### 4. What properties does your file system have?

File systems have properties even though they are not databases.  They don't have ACID attributes or transactions, but they do have basic store and retrieval capabilities.  They don't have features like isolation or atomicity as databases do, but they might have durability (data persists after a reboot) and consistency (files aren't left in random states after crashes).

### 5. Suppose you do not have "A" in ACID? What happens? When is it ok? Give me a scenario where it is ok.

We risk having partially finished operations if we lose Atomicity, which could lead to inconsistent data.  Sometimes, though, it's OK.  Atomicity may be less important, for instance, if we're doing a straightforward operation where partial updates don't impact overall data integrity (such as refreshing a single counter).

### 6. Without C in ACID properties

Data may become invalid or break integrity requirements if it is inconsistent (e.g., attempting to put a string where a number is required).  It's essential for the majority of systems, although it might not be as important for basic logging systems that don't enforce complicated rules.

### 7. Without I in ACID properties

Transactions could disrupt one another in the absence of isolation, producing inconsistent outcomes or race circumstances.  Isolation may not be as crucial in a system that only permits one transaction to operate at a time (such as a single-user application).  However, in multi-user settings, order must be maintained.
### 8. Without D 

Without durability, there could be a chance of data loss in the event of a system crash.  Although it's generally a terrible idea in any system that depends on information preservation, we might be able to get by without durability in situations when data is not mission-critical (such as caching non-essential data).