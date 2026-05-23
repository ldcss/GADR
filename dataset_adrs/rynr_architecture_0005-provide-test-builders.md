# 5. Provide Test Builders

Date: 2018-06-06

## Status

Proposed

## Context

When creating tests, it helps to have good bean objects. But when you
need a bigger structure of some objects, it's a big thing to create them
on demand. It would be nice to have a builder pattern implemented for
most objects. This is of course depending on the language and the tools
used.

## Decision

For `java`, create a `TestBuilder` for each bean class used in tests.
The `TestBuilder` creates default values for the objects but can have
them easily be overwritten.

Here's an example:

``` java
public class CustomerTestBuilder {

  private String companyName;
  private Address address;

  public CustomerTestBuilder() {
    this.companyName = "ACME Inc.";
    this.address = new AddressTestBuilder().build();
  }

  public CustomerTestBuilder withCompanyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  public CustomerTestBuilder withoutCompanyName() {
    this.companyName = null;
    return this;
  }

  public CustomerTestBuilder withAddress(Address address) {
    this.address = address;
    return this;
  }

  public CustomerTestBuilder withoutAddress() {
    this.address = null;
    return this;
  }

  public Customer build() {
    Customer result = new Customer();
    result.setCompanyName(this.companyName);
    result.setAddress(this.address);
    return result;
  }
}
```

## Consequences

No consequences yet, as this is still a proposal. But as a consequence,
there shall always be a simple way to retrieve objects for the tests.
