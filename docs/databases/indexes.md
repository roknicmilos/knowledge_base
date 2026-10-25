# DB indexes and views

Structures that speed up data retrieval on a table, like an index in a book – the DBMS can find rows without a **full
table scan**. Conceptually a sorted list of the values of one or more columns plus a pointer to the row.

- Typically implemented as B-trees (also hash, GIN/GiST, bitmap… depending on DB).
- Built on one or more columns of a **single** table (or a materialized/indexed view) – not across tables.
- **Pros:** faster reads, efficient sorting/grouping. **Cons:** slower writes, extra storage.

## When to index

1. Columns in `WHERE` filters.
2. Columns in `JOIN` conditions.
3. Columns in `ORDER BY` / `GROUP BY`.
4. Columns with **high cardinality** (many distinct values).
5. Primary keys and unique columns – indexed automatically.

Also consider **composite indexes** (column order matters: `(a, b)` serves queries on `a` and on `a, b`, **not** on `b`
alone), **covering indexes** (contain every column the query needs) and **partial indexes**.

## When NOT to index

1. **Low cardinality** columns (boolean flags, status codes): little filtering power, the optimizer may ignore the
   index. (They can still help inside a composite or partial index.)
2. Columns **rarely used** in queries – maintenance cost outweighs the benefit.
3. **Frequently updated** columns (counters, timestamps) – every update must update the index.
4. **Large text/binary** columns (`TEXT`, `BLOB`, `VARCHAR(MAX)`) – big indexes; some DBs (MySQL) limit indexed size.
5. **Write-heavy** tables where writes far outnumber reads.
6. **Small tables** (e.g. lookup tables under ~100 rows) – a full scan is often faster.
7. Tables with frequent **bulk inserts** – consider dropping indexes before the load and recreating them after.
8. **Redundant** indexes – e.g. with a composite index on `(col1, col2)`, a separate index on `col1` is redundant.

Random values such as UUIDs are fine to index when you query by them; the issue is random **primary keys** (see
fragmentation below) – prefer time-ordered IDs (UUIDv7, ULID) or sequential integers.

## Index fragmentation

Occurs when the logical order of index entries doesn't match their physical order on disk – caused by random inserts
(random UUID keys), frequent updates and deletes. Queries then do extra work. To keep performance:

- detect fragmentation with the DB's tools,
- rebuild/reorganize fragmented indexes,
- use sequential/time-ordered keys and tune fill factors,
- monitor and maintain indexes regularly.

## Views

A **view** is a virtual table defined by a query; it doesn't store data itself.

- Behaves like a table but is defined by SQL; data is fetched dynamically from the underlying tables.
- Reusable query: define once, query like a table.
- Often read-only (simple views are updatable in many DBs).
- Security: expose only certain columns/rows.
- Types: **simple** (single table, no joins/aggregates), **complex** (joins, aggregates, subqueries), **materialized**
  (result stored physically; fast for expensive queries; needs manual/scheduled refresh).
