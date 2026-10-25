# Password hashing

Never store raw passwords. Store the output of a **password hash** so a database leak doesn't reveal the passwords.

- A hash function maps input to a fixed-length, seemingly random output. It is **one-way** (not encryption: there is
  nothing to decrypt).
- On login: hash the provided password with the same algorithm (and the stored salt/parameters) and compare it with the
  stored hash (constant-time comparison).
- Hashed passwords are still vulnerable to brute force, dictionary attacks and phishing – so the algorithm must be slow
  and salted.

## Which algorithm

Do **not** use MD5, SHA-1 or a plain/fast SHA-256 – they are built to be fast, which helps attackers. Use a dedicated,
tunable password-hashing function:

1. **Argon2id** (preferred),
2. scrypt,
3. bcrypt,
4. PBKDF2 (when FIPS compliance is required).

Tune the cost so that one hash takes tens to hundreds of milliseconds; re-hash on login when parameters are raised.

## Salt

A unique random value per password, mixed into the hash input (modern libraries do this for you and embed it in the
output string). Identical passwords then produce different hashes and precomputed (rainbow) tables are useless. The salt
is **not secret** and is stored next to the hash.

## Pepper

A **secret** value shared by the application, stored *outside* the database (secrets manager, HSM, environment) and
combined with the password (typically via HMAC or by encrypting the hash). If only the database leaks, the attacker
can't
even start cracking. It complements the salt, doesn't replace it, and it has to be long and random – a one-letter pepper
(52 guesses) would be trivial to brute-force. Rotating a pepper is operationally hard; weigh that.
