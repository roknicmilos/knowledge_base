# Django

High-level, open-source Python web framework for building web apps quickly. Follows **MVT** (Model-View-Template), a
variation of [MVC](../../../design/mvc-and-mvvm.md); emphasizes reusability, modularity and DRY ("Don't Repeat
Yourself").

## Architecture

Primarily a **monolith** – models, views, templates are one codebase deployed as one unit. Depending on how you
structure the project it can also be a modular monolith, or be adapted to a microservices architecture.

## Django ORM

Lets you work with databases via Python instead of raw SQL.

**Pros**

- **Productivity** – abstracts SQL, less boilerplate.
- **Database agnostic** – PostgreSQL, MySQL, SQLite, Oracle with little code change (mostly the `DATABASES` setting;
  DB-specific features and raw SQL reduce portability).
- **Automatic schema migrations** (`makemigrations`/`migrate`).
- **Security** – parameterized queries prevent SQL injection.
- **Readable, maintainable** model-centric code.
- **Query optimization tools** – `select_related`, `prefetch_related`.
- **Rich query API** – filters, aggregation, annotations, joins, window functions (`Window`), subqueries.
- **Integration** with admin, forms, auth.

**Cons**

- Performance overhead vs raw SQL for complex queries/large datasets; sometimes inefficient SQL.
- Limited control over SQL / DB-specific features (fall back to raw SQL).
- Learning curve (`F()`, `Q()`, aggregation).
- **N+1** if used carelessly.
- Relational-first: NoSQL support is limited. (`django-nonrel` is abandoned; MongoDB now maintains an official Django
  backend – *verify*.)
- Complex queries (subqueries, window functions) can be more verbose than SQL.
- Debugging generated SQL can be tricky.
- Not ideal where extreme performance/fine-tuned DB access is needed (raw SQL or SQLAlchemy).

**Use when:** standard web apps of moderate complexity, rapid development and maintainability, multiple/switchable
databases, Django's migrations/admin/auth. **Avoid when:** highly complex DB-specific queries, extreme performance
optimization, NoSQL.

## N+1 problem in the Django ORM

Occurs when you access related objects (foreign key, many-to-many) in a loop without optimizing the query:

```python
def book_list(request):
    books = Book.objects.all()                  # 1 query to fetch all books
    for book in books:
        print(book.title, book.author.name)     # 1 query per book to fetch the author
    return render(request, 'books.html', {'books': books})
```

Fixes:

1. **`select_related`** – SQL JOIN, one query; for single-valued relations (foreign key, one-to-one).
   ```python
   books = Book.objects.select_related('author').all()   # 1 query with JOIN
   ```
2. **`prefetch_related`** – a separate query for the related objects, joined in Python; for multi-valued relations
   (many-to-many, reverse FK).
   ```python
   authors = Author.objects.prefetch_related('book_set').all()   # 2 queries
   for author in authors:
       print(author.name, [b.title for b in author.book_set.all()])   # no extra queries
   ```
3. **`annotate` / `aggregate`** – when you only need aggregated data:
   ```python
   authors = Author.objects.annotate(book_count=Count('book'))
   ```
4. **Raw SQL** (`raw()`, or `Subquery`/`RawSQL` expressions; `extra()` is discouraged) for complex cases:
   ```python
   books = Book.objects.raw('''
       SELECT books.*, authors.name
       FROM books INNER JOIN authors ON books.author_id = authors.id;
   ''')
   ```
5. **`values()` / `values_list()`** – fetch only the fields you need.

Profile queries with Django Debug Toolbar, or `connection.queries` (only filled when `DEBUG=True`).

|             | N+1                      | Optimized                     |
|-------------|--------------------------|-------------------------------|
| Queries     | 1 + N                    | 1 or 2                        |
| Performance | Poor (latency, overhead) | Good                          |
| Scalability | Doesn't scale            | Scales                        |
| Complexity  | Simple to write          | Needs deliberate query design |

General explanation: [N+1 problem](../../../databases/query-performance.md#n1-problem).

## Security

> **TODO:** more Django security topics (XSS escaping, clickjacking, `ALLOWED_HOSTS`, `SECURE_*` settings, password
> hashers).

### CSRF

Django protects against [CSRF](../../../security/csrf.md) via middleware and a template tag.

- **`django.middleware.csrf.CsrfViewMiddleware`** is enabled by default in `MIDDLEWARE`: it adds a CSRF token to
  responses and validates it on unsafe requests; missing/invalid token → `403 Forbidden`.
- **Forms:** every POST form needs `{% csrf_token %}`, which renders a hidden input with the token.
- **Validation:** the browser sends the token with the form data; Django compares it with the secret stored client-side
  in the `csrftoken` **cookie** (default) or, when `CSRF_USE_SESSIONS = True`, in the user's session.
- **AJAX:** read the token from the `csrftoken` cookie and send it in the `X-CSRFToken` header.

Settings:

- `CSRF_USE_SESSIONS` – store the secret in the session instead of a cookie (default `False` → cookie).
- `CSRF_COOKIE_NAME` (default `csrftoken`), `CSRF_COOKIE_AGE` (default 31449600 s = 1 year), `CSRF_COOKIE_SECURE` (HTTPS
  only), `CSRF_COOKIE_HTTPONLY` (hide from JavaScript – then the token must be read from the DOM instead of the cookie),
  `CSRF_COOKIE_SAMESITE`.
- `CSRF_TRUSTED_ORIGINS` – origins (with scheme, e.g. `https://app.example.com`) allowed for cross-origin POSTs (needed
  behind proxies/separate frontends).
