# DB transactions and ACID

A transaction is a series of operations executed as a **single unit** – ensuring integrity and consistency.

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

COMMIT;   -- or ROLLBACK; to undo both updates
```

With a `CHECK (balance >= 0)` constraint on `accounts`, an overdraft makes the first `UPDATE` fail, the transaction is
aborted
and nothing is changed. When a read decides a write (check-then-update), lock the row: `SELECT … FOR UPDATE`.

## ACID

- **Atomicity** – all operations succeed, or none do.
- **Consistency** – the DB goes from one valid state to another; all constraints/triggers hold before and after,
  otherwise
  the transaction is aborted and nothing changes. Supported by atomicity, isolation, constraints/triggers, rollback.
- **Isolation** – concurrent transactions don't interfere with each other (to the degree set by the isolation level).
- **Durability** – committed changes are permanent, even after a crash.

([In-depth ACID explanation video](https://www.youtube.com/watch?v=pomxJOFVcQs&list=PLQnljOFTspQXjD0HOzN7P2tgzu7scWpl2))

## Isolation levels and read phenomena

**Read phenomena** (what can go wrong without isolation):

- **Dirty read** – reading uncommitted data of another transaction.
- **Non-repeatable read** – the same row read twice returns different data (another transaction committed a change).
- **Phantom read** – the same query returns a different set of rows (rows inserted/deleted meanwhile).
- **Lost update** – two transactions overwrite each other's change. (Also: write skew under snapshot isolation.)

**SQL standard isolation levels:**

| Level            | Dirty reads | Lost updates | Non-repeatable reads | Phantoms  | Notes / use                                                                      |
|------------------|-------------|--------------|----------------------|-----------|----------------------------------------------------------------------------------|
| Read Uncommitted | may occur   | may occur    | may occur            | may occur | Rarely used; non-critical reads                                                  |
| Read Committed   | prevented   | may occur    | may occur            | may occur | Default in PostgreSQL, Oracle, SQL Server                                        |
| Repeatable Read  | prevented   | prevented    | prevented            | may occur | Default in MySQL/InnoDB; consistent reads within a transaction                   |
| Serializable     | prevented   | prevented    | prevented            | prevented | As if transactions ran one after another; absolute integrity, lowest concurrency |

Higher level = more isolation but more overhead and less concurrency. Databases implement levels differently
(PostgreSQL:
Read Uncommitted behaves like Read Committed; its Repeatable Read is snapshot isolation and also prevents phantoms; most
use
MVCC) – check your DB's documentation.

## Durability: write-ahead logging

Changes are written to a **transaction log (WAL)** on durable storage *before* they are applied to the data files.

- **Append-only** – efficient sequential writes.
- **Persistent storage** – survives crashes.
- **Redo and undo information** – enough to redo committed transactions and undo uncommitted ones on recovery.

## Referential integrity

Relationships between tables stay consistent: a foreign-key value must match a primary-key (or unique) value in the
referenced table, or be `NULL`. This prevents **orphan rows**. Enforced with **foreign key (FK) constraints**; violating
them raises an error.

```sql
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### Referential actions (`ON DELETE` / `ON UPDATE`)

| Action        | Effect                                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `RESTRICT`    | Reject the change if referencing rows exist (checked immediately)                                                                        |
| `NO ACTION`   | Reject if integrity would be violated (checked at end of statement; can be deferred in PostgreSQL) – the default when no action is given |
| `CASCADE`     | Delete/update the referencing rows too                                                                                                   |
| `SET NULL`    | Set the referencing FK column to `NULL`                                                                                                  |
| `SET DEFAULT` | Set the referencing FK column to its default value                                                                                       |

### FK without a constraint?

Yes – a plain column works:

```sql
CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT   -- no FOREIGN KEY constraint here
);
```

The database then gives **no** integrity guarantee (orphans possible; the application must check). Sometimes chosen
deliberately (sharding, cross-database references, bulk-load performance). Note the FK still needs an index on the
referencing column for fast joins/cascades.
