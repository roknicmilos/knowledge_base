# Mocking, patching, monkey patching

## Mocking

Replacing a real dependency with a fake object so you can control behavior and inspect interactions.
Reasons: return fake data, avoid hitting DBs/APIs, verify something was called.

```python
from unittest.mock import Mock

api = Mock()
api.get_user.return_value = {"id": 1}

assert api.get_user() == {"id": 1}
api.get_user.assert_called_once()
```

Test doubles: **mocks** (verify interactions), **stubs** (predefined responses), **fakes** (lightweight working
implementations), **spies** (record calls). "Mocking" is often used loosely for all of them.

## Patching

Temporarily replacing something *at runtime* (a function, class, imported dependency) – usually with a mock.

```python
from unittest.mock import patch

with patch("payments.requests.post") as mock_post:
    mock_post.return_value.status_code = 200
    charge_card()
    mock_post.assert_called_once()
```

**Key rule: patch where it is looked up, not where it is defined.**

```python
# service.py
from requests import post
def send():
    post(...)

patch("service.post")      # correct
patch("requests.post")     # usually wrong – service already holds its own reference
```

Tips: `patch.object(Class, "method")`; `autospec=True` makes the mock respect the real signature; patches are undone
when the
`with` block / decorated test ends.

```python
@patch("service.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.json.return_value = {"ok": True}
```

## Monkey patching

Ad-hoc runtime mutation by assigning directly – powerful, sometimes useful, often risky in production code.

```python
import requests
requests.get = fake_get                      # replaced globally, never restored
SomeClass.new_method = lambda self: "hello"
```

In tests, use pytest's `monkeypatch` fixture (auto-undone) rather than raw assignment.

## Summary

- mock = the fake thing
- patch = how you swap it in
- monkey patch = manual/dynamic patching, often global and unrestored

```python
with patch("module.clock.now", return_value=fixed_time):   # good: scoped, restored
    ...
module.clock.now = lambda: fixed_time                      # questionable: same effect, no cleanup
```
