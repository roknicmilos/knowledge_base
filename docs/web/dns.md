# DNS

Domain Name System: maps domain names to IP addresses (and other records).

## Resolution steps for `google.com`

1. The browser checks its own cache, then the OS cache (and the hosts file). If found, it connects to that IP.
2. Otherwise the OS asks the **recursive resolver** (usually configured by the ISP/router, or a public one such as
   1.1.1.1 / 8.8.8.8). If the resolver has a fresh cached answer it returns it.
3. If not, the resolver performs the lookup itself, step by step (**iterative resolution**):
    1. asks a **root server** → gets a referral to the `.com` TLD servers,
    2. asks the **TLD server** → gets a referral to the domain's authoritative nameservers,
    3. asks the **authoritative nameserver** → gets the answer (e.g. the `A`/`AAAA` record).
4. The resolver caches the answer for the record's **TTL** and returns it to the client; the browser/OS cache it too and
   then connect to the IP.

## Common record types

| Record   | Purpose                                   |
|----------|-------------------------------------------|
| A / AAAA | Name → IPv4 / IPv6 address                |
| CNAME    | Alias to another name                     |
| MX       | Mail servers                              |
| TXT      | Arbitrary text (SPF, domain verification) |
| NS       | Authoritative nameservers for the zone    |
