# SQL query performance

## SQL logical execution order

`FROM` / `JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `DISTINCT` → `ORDER BY` → `LIMIT/OFFSET`
(which is why a `SELECT` alias can't be used in `WHERE`). Video: <https://www.youtube.com/watch?v=BHwzDmr6d7s>

## Finding why a query with multiple JOINs is slow

1. **Understand the query** – purpose, tables, relationships, complexity (number of JOINs, subqueries, `GROUP BY`,
   `ORDER BY`).
2. **Check the execution plan** with `EXPLAIN` / `EXPLAIN ANALYZE`. Look for:
    - full table scans (missing index or non-selective filter),
    - nested loops (fine with an indexed inner side, slow on large unindexed sets),
    - hash/merge joins (usually good for large sets),
    - sorts (expensive on large sets),
    - the most expensive nodes (highest cost / actual time) and big gaps between estimated and actual rows (stale
      statistics →
      run `ANALYZE`).
3. **Check indexes** – columns in `JOIN`, `WHERE`, `ORDER BY`/`GROUP BY` indexed *and actually used* in the plan; don't
   over-index.
4. **Analyze data distribution** – table sizes, skewed values.
5. **Optimize JOINs** – join on indexed columns, right join type (`INNER` vs `LEFT`), remove unnecessary joins and
   accidental
   Cartesian products.
6. **Reduce rows early** – selective filters; (modern optimizers usually push predicates down themselves, so verify in
   the plan).
7. **Check subqueries** – correlated subqueries executed per row (e.g. in the `SELECT` list) are slow; rewrite as joins
   or
   window functions when the plan shows it helps.
8. **Profile** – find slow queries system-wide.

| DB         | Tools                                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| PostgreSQL | `EXPLAIN (ANALYZE, BUFFERS)`, `pg_stat_statements`, `auto_explain`, slow query log                                       |
| MySQL      | `EXPLAIN`, `EXPLAIN ANALYZE` (8.0.18+), Performance Schema / `sys` schema, slow query log (`SHOW PROFILE` is deprecated) |
| SQL Server | Execution plans, Query Store, Extended Events (SQL Server Profiler is deprecated), Database Engine Tuning Advisor        |
| Oracle     | `EXPLAIN PLAN`, SQL Trace, TKPROF                                                                                        |

Video on `EXPLAIN` in Postgres: <https://www.youtube.com/watch?v=P7EUFtjeAmI>

### EXPLAIN vs EXPLAIN ANALYZE

|                    | EXPLAIN                        | EXPLAIN ANALYZE                                                                   |
|--------------------|--------------------------------|-----------------------------------------------------------------------------------|
| Executes the query | No                             | **Yes** (can modify data if the query does – wrap in a transaction and roll back) |
| Output             | Estimated costs and row counts | Actual run times and row counts                                                   |
| Use                | Planning, optimization         | Performance analysis, debugging                                                   |

## N+1 problem

Common with ORMs. 1 query fetches N parent rows, then **N more queries** fetch each parent's children
(`SELECT * FROM users` → `SELECT * FROM orders WHERE user_id = ?` per user) → 1 + N round-trips.

Solutions:

- **Eager loading / JOIN** – fetch parents and children in one query. Careful: JOINing a to-many relation repeats the
  parent
  columns per child row.
  ```sql
  SELECT users.*, orders.*
  FROM users
  LEFT JOIN orders ON users.id = orders.user_id;
  ```
- **Batch loading** – fetch children in batches (`WHERE user_id IN (…)`), e.g. Hibernate `@BatchSize`, Django
  `prefetch_related`.
- **Caching** frequently accessed related data (e.g. in Redis).
- Fetch only the columns/aggregates you need (`COUNT` via `GROUP BY`).

Framework specifics: [Django N+1](../languages/python/frameworks/django.md#n1-problem-in-the-django-orm).
