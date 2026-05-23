# Library for Lpa Data Mapping

## Context
The application needed a way to map the Sirius and LPA store data returned from the API into a combined format that could be easily managed and manipulated. This mapping required a solution that could efficiently hydrate complex object structures while maintaining type safety and flexibility. We explored multiple PHP object hydration libraries to find a tool that would support these requirements, simplify data transformation, and integrate seamlessly into our existing codebase.

### Considered Alternatives
1. **Jolicode Automapper**
    - **Docs**: https://github.com/jolicode/automapper
    - **Reason not accepted**: The latest major version of this library required a higher version of PHP. The next compatible version of this library did not have the flexibility we needed to map the Lpa data.

2. **Jane PHP Automapper**
    - **Docs**: https://github.com/janephp/automapper
    - **Reason not accepted**: While Jane PHP Automapper is robust and flexible, it was not actively maintained at the time of evaluation. Additionally, the community support was limited, with fewer contributors and low engagement.

3. **Hydrator from Laminas**
    - **Docs**: https://github.com/laminas/laminas-hydrator
    - **Reason not accepted**: Lacked support for more complex and deeply nested data structures that our application needs to handle. It is incompatible with our application.

4. **jms/serializer**
    - **Docs**: https://github.com/schmittjoh/serializer
    - **Reason not accepted**: Not as easy to use the library compared to the other libraries. Also had poor documentation.

## Decision
After evaluating the available libraries, we decided to use **EventSaucePHP ObjectHydrator** (https://github.com/EventSaucePHP/ObjectHydrator). This decision was based on the following factors:
- The library’s simplicity and ease of use for mapping complex nested objects.
- Strong community support, frequent updates, and a growing user base.
- Excellent documentation.
- Supports advanced type casting, safety and flexibility.
- Compatibility with the types of data structures (e.g., arrays of objects) returned by the Sirius and LPA store APIs.

## Consequence
While EventSauce ObjectHydrator meets our needs, there are potential downsides:

1. **Performance Concerns**: The library may not be optimised for extremely large datasets, which could lead to performance issues in high-load scenarios.

2. **Complexity in Debugging**: Since the library abstracts a lot of functionality, debugging issues related to object hydration can be challenging.

3. **Future Compatibility**: If the library's development slows down or diverges from our use case, we may need to refactor the implementation or migrate to a different hydrator.