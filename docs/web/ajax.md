# AJAX

**A**synchronous **J**avaScript **a**nd **X**ML – a technique that lets a page talk to the server in the background
and update only part of the page, without a full reload.

## Problem it solves

Before AJAX every form submit or data request reloaded the whole page. With AJAX the page sends a request, receives data
and updates just the relevant part.

## How it works

1. JavaScript sends an HTTP request.
2. The server processes it.
3. The server returns data (JSON today).
4. JavaScript updates the DOM.

```js
fetch('/api/users')
    .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);  // fetch does NOT reject on 4xx/5xx
        return response.json();
    })
    .then(data => console.log(data));
```

*Asynchronous* because the script keeps running while the request is in flight and handles the response later – the page
doesn't freeze. "XML" is historical: XML was the original format, JSON is far more common now.

## Building blocks

HTML/CSS, JavaScript, DOM manipulation, HTTP requests, and either `XMLHttpRequest` (old: `new XMLHttpRequest()`) or
`fetch()` / Axios (modern).

## Examples

Infinite scroll, search suggestions while typing, form submit without refresh, chat apps, "load more" posts.

See [CORS](cors.md) for cross-origin calls.
