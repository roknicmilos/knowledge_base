# Try-with-resources and AutoCloseable (Java)

**Try-with-resources** (Java 7) automatically closes resources (files, DB connections, sockets) when the `try` block
exits – successfully or with an exception. It removes the need for manual `finally` cleanup.

Requirement: the resource implements `AutoCloseable` (or its sub-interface `Closeable`).

Before:

```java
BufferedReader br = null;
try {
    br = new BufferedReader(new FileReader("file.txt"));
    System.out.println(br.readLine());
} finally {
    if (br != null) {
        br.close(); // must handle manually
    }
}
```

After:

```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    System.out.println(br.readLine());
} // br.close() called automatically
```

**Advantages:** no manual `finally`, guaranteed cleanup, multiple resources in one `try (A a = …; B b = …)`; since Java
9 an effectively-final variable can be used directly: `try (br)`.

## AutoCloseable

```java
public interface AutoCloseable {
    void close() throws Exception;
}
```

Introduced in Java 7 for automatic resource management – the counterpart of Python's [context
managers](../python/context-managers.md).

| Feature           | Description                                                                         |
|-------------------|-------------------------------------------------------------------------------------|
| Automatic cleanup | `close()` is called when the `try` block exits (success or failure)                 |
| Exception safety  | If both the `try` body and `close()` throw, the `close()` exception is *suppressed* |
| Chaining          | Multiple resources can be declared in one `try`                                     |

- Resources are closed in **reverse order** of declaration.
- Exceptions from `close()` are suppressed but accessible via `getSuppressed()`; if both the body and `close()` throw,
  the body's exception propagates.
- Custom classes can implement `AutoCloseable` to behave like Python context managers.

## Java try-with-resources vs Python `with`

|                    | Java                      | Python                           |
|--------------------|---------------------------|----------------------------------|
| Syntax             | `try (Resource r = ...)`  | `with Resource() as r:`          |
| Requirement        | implement `AutoCloseable` | implement `__enter__`/`__exit__` |
| Exception handling | Suppressed exceptions     | Full control inside `__exit__`   |
