# HTTPS and TLS

HTTPS is HTTP over **TLS** (Transport Layer Security). It provides confidentiality, integrity and server authentication.
Same methods and status codes as HTTP, default port **443**.

> SSL (Secure Sockets Layer) is the deprecated predecessor. Only TLS 1.2 and 1.3 should be enabled; "SSL certificate"
> is just a legacy name for a TLS certificate.

- HTTPS is essential for anything sensitive (banking, shopping, logins) and is expected by browsers and search engines.
- **Certificates:** the server needs a certificate issued by a Certificate Authority (CA). It binds the domain to the
  server's public key; clients trust it because the CA chains to a root they already trust (e.g. Let's Encrypt is free).
- **Handshake (simplified, TLS 1.3):**
    1. Client and server agree on parameters and perform an ephemeral Diffie-Hellman (ECDHE) key exchange.
    2. The server proves its identity by sending its certificate and signing the handshake with its private key.
    3. Both sides derive the same symmetric session keys from the exchange.
    4. All application data is encrypted with those symmetric keys.
- **Why both kinds of crypto:** asymmetric crypto (key exchange, signatures) establishes trust and a shared secret;
  symmetric crypto (AES, ChaCha20) is much faster for the bulk data. Ephemeral keys give **forward secrecy**: recording
  traffic and later stealing the server key does not decrypt old sessions. (Older TLS versions could also use RSA key
  transport – the client encrypts a secret with the server's public key – this
  was removed in TLS 1.3.)
