# PHP

- **Interpreted** language: source is compiled to bytecode at runtime (cached by OPcache) – not a true ahead-of-time
  compiled
  language.
- **Dynamically typed** – types are determined at runtime from values.
- **Weakly typed** – PHP converts types automatically when needed.
- **Multi-paradigm:** procedural; OOP (classes, objects, visibility, static methods, traits); functional style
  (first-class
  functions, closures, arrow functions, higher-order functions like `array_map`/`array_filter` – limited but present);
  imperative.

> **Verify/TODO:** modern PHP 8.x features (enums, readonly properties, attributes, union types, match, JIT) are not
> covered yet.

## PHP vs Python

|                 | Python                                                                                             | PHP                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Purpose         | General purpose: web (Django, Flask, FastAPI), data science, AI/ML, automation, scripting, desktop | Created for web; server-side scripting and dynamic sites; rarely used outside web          |
| Syntax          | Clean, indentation-based blocks, no braces                                                         | C-like: braces and semicolons                                                              |
| Inheritance     | Multiple inheritance                                                                               | Single inheritance; multiple interfaces; traits for code reuse                             |
| Typing          | Dynamic; optional type hints                                                                       | Dynamic; type declarations since PHP 7                                                     |
| Web development | Frameworks (Django, Flask, FastAPI); more structured for complex apps                              | Works natively with HTML (mix HTML and PHP in `.php` files); Laravel, Symfony, CodeIgniter |
| Ecosystem       | PyPI; data science, AI, automation                                                                 | Strong web ecosystem; wide shared-hosting support; CMS (WordPress, Joomla, Drupal)         |

Syntax comparison:

```python
if x > 0:
    print("Positive")
```

```php
if ($x > 0) {
    echo "Positive";
}
```

### Typing in PHP

- Type declarations are optional (as with Python hints); with different types passed PHP uses **implicit casting**.
- `declare(strict_types=1);` at the top of a file makes PHP throw `TypeError` on mismatched types – but only for
  function-call
  parameter/return checks in that file.

### Performance

Both are fast enough for most web workloads; PHP 7+ is very fast for request/response cycles and PHP 8 adds a JIT.
Differences
rarely decide the choice.

### Summary

- Python – versatile: web, AI, automation, general programming.
- PHP – web development, especially CMS and existing/legacy PHP projects.

See also [inheritance across languages](../../fundamentals/oop.md#inheritance-across-languages).
