# HTTP

HTTP (HyperText Transfer Protocol) is an application-layer protocol for exchanging data between a client and a server
(client-server model: the client sends a request, the server sends back a response). Exchanged data can be HTML, XML,
JSON, plain text, media files and assets such as JS/CSS. HTTP is **stateless**.

- **Request type** is determined by the HTTP method.
- **Response type** is determined by the status code:
    - 100–199 informational
    - 200–299 success
    - 300–399 redirection
    - 400–499 client error
    - 500–599 server error
- The destination is an IP address + port (80 by default for HTTP, 443 for HTTPS).
- **Transport:** HTTP/1.1 and HTTP/2 run over **TCP**; HTTP/3 runs over **QUIC, which uses UDP**.
- **Versions:** HTTP/3 is standardized (RFC 9114) and widely supported by browsers and CDNs; HTTP/1.1 and HTTP/2 are
  still
  very common.

## Methods

| Method  | Purpose                                                | Example use case                       |
|---------|--------------------------------------------------------|----------------------------------------|
| GET     | Retrieve a representation of a resource                | Fetch a web page or data from an API   |
| POST    | Submit data to be processed                            | Submit a form, upload a file           |
| PUT     | Replace a resource with the provided data (idempotent) | Update an existing record              |
| PATCH   | Partially update a resource                            | Modify specific fields                 |
| DELETE  | Delete a resource                                      | Remove a record                        |
| HEAD    | Retrieve headers without the body                      | Check whether a resource exists        |
| OPTIONS | Describe communication options                         | Check allowed methods / CORS preflight |
| CONNECT | Establish a tunnel                                     | HTTPS through a proxy                  |
| TRACE   | Diagnostic loop-back of the request                    | Debugging request paths                |

See also: [HTTPS & TLS](https-and-tls.md), [DNS](dns.md), [CORS](cors.md), [REST](../architecture/rest-api.md).
