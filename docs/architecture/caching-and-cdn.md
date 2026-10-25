# Caching and CDN

## Cache

A high-speed storage layer holding a subset of data (typically from a slower store) for faster access to frequently used
or
expensive-to-compute data. Reduces latency, load on primary sources (DB, file storage, external API), and improves
scalability and user experience.

### Strategies

- **Lazy loading / cache-aside** – the app reads from the cache first; on a miss it fetches from the primary source,
  stores
  it in the cache and returns it.
- **Write-through** – every write to the primary source is also written to the cache (synchronously).
- **Write-back / write-behind** – write to the cache first, flush to the primary source later (fast, risk of data loss).
- **Eviction policies** – LRU, LFU, FIFO when the cache is full.

### Types

- **Memory cache** – RAM (Redis, Memcached).
- **Browser cache** – web assets (CSS, JS, images).
- **Application cache** – e.g. query results in a web app.
- **Database cache** – query results/buffers to reduce DB load.
- **Hardware cache** – CPU L1/L2/L3.

### Issues to plan for

- **Consistency** – keep the cache in sync with the source: write-through and/or **TTL** (time-to-live).
- **Invalidation** – when to remove stale data. Too early hurts performance; too late serves stale data.
- **Cache stampede** – many requests repopulate the cache at once after a popular entry expires. Mitigate with locks
  (only one request refills while others wait), randomized TTLs (jitter), and proactive refresh before expiry.

## CDN – Content Delivery Network

A distributed caching layer designed for static assets (images, video, JS, CSS) and, in some cases, dynamic content.

- Many **edge servers** around the world; a user is served from the nearest one instead of the origin → lower latency.
- Can keep serving cached content while the origin is temporarily unavailable.
- Optimized for large assets (video, high-res images); improves speed and reliability for geographically spread users.
- Examples: CloudFront, Cloudflare, Fastly.
