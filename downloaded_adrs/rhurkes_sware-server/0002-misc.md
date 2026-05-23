# Miscellaneous small decisions

* Status: accepted
* Date: 2020-04-14

## Context and Problem Statements

There are multiple small decisions that need to be made:
- What process should be used to create keys?
    - Whatever method, having the store own the key generation is preferred as it allows individual loaders to not care about key generation.
    - We used to use ingestion time in microseconds as the ID. In practice this was monotonic, and I was never able to simulate duplicate system times or times that jumped backwards in sequence. Thread-safety came for free when using ZMQ, but would require some extra work in a simplified solution. This work could have been a Mutex or using an MPSC queue (channels), but didn't provide a lot of value as the ingest time was metadata that is only useful in evaluating lag between ingestion and event dissemination.
    - Based on the previous statement, I tried implementing using an AtomicUsize as an ID. This worked well, except it made the API contract a little more gross, and made the store considerably more complicated. Keyless fetches had to iterate backwards through all keys, deserializing the data, and checking if the ingest time was less than the threshold. Having this performance constraint on reads seemed bad. I ended up using a mutex and a while loop to prevent collisions of ingest timestamps as the ID. A mutex and db.get() aren't ideal, but write performance shouldn't be an issue.
    - It would have been nice to leverage some sort of CAS/transaction in RocksDB, but the Rust bindings didn't allow for it.
    - Tested the write performance in release builds at 6.4μs/put for the mutex/CAS-free code, and 9.3μs/put for the final implementation. The mutex performance hit was negligable, so most of the hit came from the CAS behavior. Even on the busiest of weather days, you're still going to be limited in your writes by the time over-the-wire from the sources which will measure in the dozens of milliseconds if not more. A 3μs difference would not be noticeable. sware v1 did writes in 30μs, so this is considerably faster.
    - Can I create a collision? I took 4 threads and put 1M events with each using no throttling. I expected to see 4M keys in RocksDB, and saw 2216421 - almost a 50% collision rate.
- I used to roll up all errors into a WxError type, which essentially just persisted the message from each. It was boilerplate that didn't add a ton of value, so I changed most of these functions to return `()` as an `Err` and log errors where they occur. I also switched from `slog` to `log` as I never really used all the structured logging features.
- On 64 test events, gzipping shrunk the payload down to 14% of its original size. There were further savings by creating an optimized Event struct that doesn't serialize None values, but they were only about 5% smaller. I'll leave it for now, as it's not that much extra work, and compression won't be available in `warp` for a little while.
