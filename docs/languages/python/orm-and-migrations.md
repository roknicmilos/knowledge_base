# ORMs and migrations (Python)

## ORMs

- **SQLAlchemy** – the most popular and mature ORM (ORM + Core for raw SQL). Version 2.0 has first-class async support
  (`AsyncSession`) and typed models (`Mapped[...]`). **SQLModel** (SQLAlchemy + Pydantic) is popular with FastAPI.
- **Django ORM** – bundled with Django. It can technically be used outside Django, but needs manual setup and is tightly
  integrated with the ecosystem – usually only chosen with Django.
- **Tortoise ORM** – async-first, Django-like API, Pydantic integration; smaller community.

|                      | SQLAlchemy                                  | Django ORM                                                                    | Tortoise ORM                       |
|----------------------|---------------------------------------------|-------------------------------------------------------------------------------|------------------------------------|
| Framework dependency | Agnostic                                    | Django-specific                                                               | Agnostic                           |
| Async                | Yes (2.0 `AsyncSession`; partial since 1.4) | Native async query API since 4.1 (runs sync driver in threads under the hood) | Fully async                        |
| DB support           | Wide (PostgreSQL, MySQL, SQLite, Oracle, …) | PostgreSQL, MySQL, SQLite, Oracle                                             | PostgreSQL, MySQL, SQLite, MariaDB |
| Learning curve       | Moderate (more boilerplate)                 | Easy (inside Django)                                                          | Easy                               |
| Flexibility          | High                                        | Moderate                                                                      | Moderate                           |
| Migrations           | **Alembic** (separate package)              | Built in (`makemigrations`, `migrate`)                                        | **Aerich** (separate)              |
| Community            | Large, mature                               | Very large                                                                    | Smaller, growing                   |
| FastAPI integration  | Excellent (manual setup)                    | Not designed for it                                                           | Good                               |
| Type safety          | Good with 2.0 typing                        | None native                                                                   | Pydantic integration               |
| Best for             | Complex, flexible projects                  | Rapid development with Django                                                 | Async-first apps                   |

## Migration tools

Most are tied to an ORM:

- Alembic → SQLAlchemy
- Django migrations → Django ORM (bundled)
- Aerich → Tortoise ORM

They are installed separately (except Django's) – so you can leave them out when you don't need migrations.

**You may not need migrations when:** one-time setup with no schema changes; throwaway prototypes; you don't control the
schema (pre-existing DB); small personal projects; read-only/reporting systems.

**ORM-independent tools** work with raw SQL/scripts: Flyway, Liquibase, dbmate, Atlas, yoyo-migrations.
(`simple-db-migrate`, mentioned in the original notes, is no longer maintained.)
