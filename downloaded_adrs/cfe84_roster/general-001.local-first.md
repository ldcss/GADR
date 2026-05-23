# Decision

Build the application `local-first`.

# Details

The application saves its state on a database local to the machine first, state is replicated to a server after.

# Reason

The application is made to work during one-to-ones, and on the field with team members. It should not stall, and not rely on network connectivity.