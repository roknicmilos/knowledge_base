# MVC and MVVM

Both are **architectural (UI) patterns** that separate concerns; they are not GoF design patterns.

> **TODO:** actual design patterns (GoF: creational/structural/behavioral) with Python examples – see
> [`examples/python/design_patterns`](../../examples/python/design_patterns/README.md) (`gang_of_4/`,
> `dependency_injection/`).

## MVC – Model-View-Controller

- **Model** – data and business logic: entity classes (e.g. `Product`), persistence (e.g. `ProductRepository`), services
  (e.g. `ProductService`). Independent of the UI.
- **View** – the UI; shows data and collects input. Depends on the model for what it displays but doesn't change it
  directly (e.g. a page listing products with a filter form).
- **Controller** – mediator between model and view: handles user input, updates the model/view (e.g. a method that
  fetches products by the user's filters and hands them to the view).
- **Benefits:** separation of concerns, scalability, reusability, testability. Can get complex in large apps.
- Django's variant is MVT (Model-View-Template), see [Django](../languages/python/frameworks/django.md).

## MVVM – Model-View-ViewModel

Mostly for UI-heavy apps (desktop, mobile, some frontend frameworks).

- **Model** and **View** – as in MVC.
- **ViewModel** – mediator that holds UI state, exposes properties/commands the view **binds** to, and talks to the
  model. The view never calls the database directly.
- Flow: `View <—binds to—> ViewModel <—uses—> Model`.
- Compared with MVC it makes the view mostly declarative and easier to unit-test (no UI needed to test the ViewModel).
