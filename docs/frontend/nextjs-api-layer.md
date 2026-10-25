# API layer in a Next.js (React) project

How to organize the code that calls your backend. Three approaches, in increasing structure.

## Approach 1: single API object

```js
// src/api/index.js
const API = {
  getUser: async (userId) => (await fetch(`/api/users/${userId}`)).json(),
  getTransactions: async () => (await fetch('/api/transactions')).json(),
};
export default API;
```

**Pros:** simple, centralized – fine for small projects. **Cons:** grows into one huge object, no separation between
resources.

## Approach 2: one API object per resource

```js
// src/api/userAPI.js
const userAPI = {
  getUser: async (userId) => (await fetch(`/api/users/${userId}`)).json(),
};
export default userAPI;

// src/api/transactionAPI.js
const transactionAPI = {
  getTransactions: async () => (await fetch('/api/transactions')).json(),
};
export default transactionAPI;
```

**Pros:** separation of concerns, scales. **Cons:** consumers import several objects.

## Approach 3 (recommended): resource objects merged under one entry point

Namespace the resources instead of spreading them – spreading flattens all methods into one namespace and invites name
collisions.

```js
// src/api/index.js
import userAPI from './userAPI';
import transactionAPI from './transactionAPI';

const API = {
  user: userAPI,               // API.user.getUser(id)
  transaction: transactionAPI, // API.transaction.getTransactions()
};
export default API;
```

**Pros:** separation + one access point, easy to add/remove modules. **Cons:** slightly more setup.

## Conventions

- Consistent naming: `userAPI`, `transactionAPI`.
- Verb-first method names: `getUser`, `createUser`, `updateUser`, `deleteUser`.
- Singular for one item, plural for collections (`getUser` vs `getUsers`), consistently.
- Centralize error handling: check `response.ok` and throw; relative URLs only work in the browser – server components /
  route handlers need an absolute base URL (e.g. from an env var).
