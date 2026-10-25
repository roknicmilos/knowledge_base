# Layered (horizontal) vs vertical-slice design

Two ways to organize code. (Not to be confused with horizontal/vertical *scaling* – see [scaling](scaling.md).)

| Aspect                 | Layered / horizontal                     | Vertical slices / by feature           |
|------------------------|------------------------------------------|----------------------------------------|
| Grouping               | By technical layer (UI, logic, data)     | By business domain or feature          |
| Reusability            | High within a layer                      | Limited to the slice                   |
| Separation of concerns | Clear for technical concerns             | Clear for business concerns            |
| Coupling               | Tight between layers                     | Loose between slices                   |
| Scalability            | Hard to scale individual layers          | Easier to scale individual features    |
| Development            | Changes cut across layers (coordination) | Teams can own a slice end to end       |
| Example                | Traditional monolithic apps              | Microservices, feature-based monoliths |

**Use layered when:** small/medium app, technical separation matters more than business alignment, reusable components,
simple business logic. **Use vertical slices when:** large complex apps with well-defined domains, feature-oriented
delivery, microservices (each service is a vertical containing all the layers it needs).

**In practice combine them:** horizontal layers for common technical concerns (authentication, logging) and vertical
slices for business features (user management, product catalog).
