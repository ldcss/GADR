# Secrets and Environment Variables Decision record

* **Issue**: We need access to database's info, such as username, port, host, etc.

* **Decision**: We decided to create environment variables in the hosting platform so we can access these info without leaking it in our code.

* **Status**: Decided

* **Pros**: The code can be very simple.

* **Cons**: Everytime the host changes, environment variable needs to be reset. But we believe it is something that we cannot avoid. The use of secrets makes sure confidential information won't be accessible through reading the code.