# Metaclasses

A metaclass is the **"class of a class"**: classes create instances, metaclasses create classes. They let you control
class
creation and behavior – powerful, advanced, and rarely needed in everyday code.

## Key concepts

- Everything is an object, including classes; a class is an instance of its metaclass. The default metaclass is `type`.
- `type` can be used two ways: `type(obj)` returns the type; `type(name, bases, dict)` creates a class dynamically.

```python
MyClass = type('MyClass', (object,), {'x': 10, 'y': 20})
obj = MyClass()
print(obj.x, obj.y)   # 10 20
```

## Custom metaclass

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)

class MyClass(metaclass=Meta):
    x = 10
    y = 20
# Creating class MyClass
# Initializing class MyClass
```

## Use cases

- Enforce patterns/constraints at class level (API design)
- ORMs – map class attributes to database columns
- Dynamic class creation based on configuration
- Singleton

### Example: singleton metaclass

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

print(SingletonClass() is SingletonClass())  # True
```

> Prefer simpler tools when they suffice: `__init_subclass__`, class decorators, or just a module-level instance for a
> singleton.
