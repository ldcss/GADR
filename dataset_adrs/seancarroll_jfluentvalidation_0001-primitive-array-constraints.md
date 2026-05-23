# Primitive Array Constraint Implementation

- Status: proposed
- Deciders: Sean Carroll
- Date: 2019-05-28

Technical Story: Implementing constraints for arrays that will support Object as well as primitive types. 

## Context and Problem Statement

My first pass at building out array constraint was to use a generic parameter `A` with `java.lang.reflect.Array` to obtain 
the length of the property representing `A`. 
I was curious what the cost of using `java.lang.reflect.Array` compared to grabbing the `length` property from a known type was. 
Anything with a name like `reflect*` gives me nightmares about terrible performance. 
I decided to write a JMH benchmark to determine the performance impact `java.lang.reflect.Array` to assist in determining 
which implementation to use. 

## Decision Drivers

1. We want to keep performance in mind and attempt to be as performant as possible across all constraints.
2. Avoid adding Additional classes and limit duplicating logic across constraints when possible.

## Considered Options

The benchmark code initially used JDK `1.8.0_30` and they showed a fairly large impact. 
I then found a Stack Overflow post ([see links](#links)) suggesting that the performance issue was resolved in JDK `1.8.0_45` so I 
upgraded to `1.8.0_211-b12` however I'm still seeing roughly the same performance penalty. 

### Option 1

```java
package jfluentvalidation.constraints.array.length;

import jfluentvalidation.common.Iterables;
import jfluentvalidation.constraints.Constraint;
import jfluentvalidation.validators.RuleContext;

import java.lang.reflect.Array;
import java.util.function.IntSupplier;

public class ArrayExactLengthConstraint<T, A> implements Constraint<T, A> {

    private IntSupplier lengthSupplier;

    public ArrayExactLengthConstraint(Iterable<?> other) {
        this(() -> Iterables.size(other));
    }

    public ArrayExactLengthConstraint(Object other) {
        this(() -> Array.getLength(other));
    }

    public ArrayExactLengthConstraint(int length) {
        this(() -> length);
    }

    public ArrayExactLengthConstraint(IntSupplier lengthSupplier) {
        this.lengthSupplier = lengthSupplier;
    }


    @Override
    public boolean isValid(RuleContext<T, A> context) {
        int len = Array.getLength(context.getPropertyValue());
        return len == lengthSupplier.getAsInt();
    }
}
```

### Option 2

```java
package jfluentvalidation.constraints.array.length;

import jfluentvalidation.common.Arrays;
import jfluentvalidation.common.Iterables;
import jfluentvalidation.constraints.Constraint;
import jfluentvalidation.internal.Ensure;
import jfluentvalidation.validators.RuleContext;

import java.lang.reflect.Array;
import java.util.function.IntSupplier;

public class BooleanArrayExactLengthConstraintAlternative<T> implements Constraint<T, boolean[]> {

    private final IntSupplier lengthSupplier;

    public BooleanArrayExactLengthConstraintAlternative(Iterable<?> other) {
        Ensure.notNull(other);
        this.lengthSupplier = () -> Iterables.size(other);
    }

    public BooleanArrayExactLengthConstraintAlternative(Object other) {
        Ensure.argument(Arrays.isArray(other));
        this.lengthSupplier = () -> Array.getLength(other);
    }

    public BooleanArrayExactLengthConstraintAlternative(int length) {
        this.lengthSupplier = () -> length;
    }

    @Override
    public boolean isValid(RuleContext<T, boolean[]> context) {
        int len = context.getPropertyValue().length;
        return ArrayLength.exact(len, lengthSupplier.getAsInt());
    }
}
```

## Decision Outcome

I decided to choose option 1 as I prioritized performance above the overhead to maintain additional classes and having 
duplicate logic. 
While it might be premature optimization and such a small impact (1 - 2 ns) the benchmark results below still convinced me. 
I'm sure someone can convince me that the overhead is insignificant or that I simply messed up the bencharmark at which point
it should be easier refactor to option 2. 
I've included a rough [implementation of option 2](#option-2-implementation) just in case.

```java
package jfluentvalidation.constraints.array;

import jfluentvalidation.constraints.array.length.ArrayExactLengthConstraint;
import jfluentvalidation.constraints.array.length.BooleanArrayExactLengthConstraint;
import jfluentvalidation.constraints.array.length.BooleanArrayExactLengthConstraintAlternative;
import jfluentvalidation.rules.PropertyRule;
import jfluentvalidation.validators.RuleContext;
import jfluentvalidation.validators.ValidationContext;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@State(Scope.Benchmark)
public class LengthBenchmark {

    public static class Foo {

        private boolean[] bar;

        public Foo(boolean[] bar) {
            this.bar = bar;
        }
    }

    RuleContext<Foo, boolean[]> ruleContext;
    BooleanArrayExactLengthConstraintAlternative booleanArrayExactLengthConstraintAlternative;
    ArrayExactLengthConstraint arrayExactLengthConstraint;
    BooleanArrayExactLengthConstraint booleanArrayExactLengthConstraint;

    @Setup
    public void prepare() {
        Foo f = new Foo(new boolean[5]);

        PropertyRule propertyRule = new PropertyRule(foo -> f.bar, "bar");
        ruleContext = new RuleContext<>(new ValidationContext(f), propertyRule);

        booleanArrayExactLengthConstraintAlternative = new BooleanArrayExactLengthConstraintAlternative(5);
        arrayExactLengthConstraint = new ArrayExactLengthConstraint(5);
    }

    @Benchmark
    public void booleanArrayExactLengthConstraintAlternative() {
        booleanArrayExactLengthConstraintAlternative.isValid(ruleContext);
    }

    @Benchmark
    public void arrayExactLengthConstraint() {
        arrayExactLengthConstraint.isValid(ruleContext);
    }


    public static void main(String[] args) throws Exception {
        new Runner(new OptionsBuilder()
            .include(LengthBenchmark.class.getSimpleName())
            .forks(1)
            .warmupIterations(2)
            .measurementIterations(5)
            .build())
            .run();
    }
}
```

Run 1

| Benchmark                                                     | Mode | Cnt | Score | Error   | Units |
|---------------------------------------------------------------|------|-----|-------|---------|-------|
| LengthBenchmark.arrayExactLengthConstraint                    | avgt | 25  | 2.504 | ± 0.143 | ns/op |
| LengthBenchmark.booleanArrayExactLengthConstraintAlternative  | avgt | 25  | 2.099 | ± 0.022 | ns/op |

object cast has a performance impact of roughly ~19%

Run 2

| Benchmark                                                     | Mode | Cnt | Score | Error   | Units |
|---------------------------------------------------------------|------|-----|-------|---------|-------|
| LengthBenchmark.arrayExactLengthConstraint                    | avgt | 25  | 2.436 | ± 0.049 | ns/op |
| LengthBenchmark.booleanArrayExactLengthConstraintAlternative  | avgt | 25  | 2.041 | ± 0.013 | ns/op |

object cast has a performance impact of roughly ~19%

Run 3

| Benchmark                                                     | Mode  | Cnt | Score     | Error       | Units  |
|---------------------------------------------------------------|-------|-----|-----------|-------------|--------|
| LengthBenchmark.arrayExactLengthConstraint                    | thrpt | 25  | 0.424     | ± 0.001     | ops/ns |
| LengthBenchmark.booleanArrayExactLengthConstraintAlternative  | thrpt | 25  | 0.626     | ± 0.001     | ops/ns |
| LengthBenchmark.arrayExactLengthConstraint                    | avgt  | 25  | 2.362     | ± 0.022     | ns/op  |
| LengthBenchmark.booleanArrayExactLengthConstraintAlternative  | avgt  | 25  | 1.599     | ± 0.007     | ns/op  |
| LengthBenchmark.arrayExactLengthConstraint                    | ss    | 5   | 48261.200 | ± 4493.186  | ns/op  |
| LengthBenchmark.booleanArrayExactLengthConstraintAlternative  | ss    | 5   | 18690.000 | ± 23530.434 | ns/op  |


A ~20% performance impact on throughput and even larger on average time is a bit too much for me to ignore. 

### Positive Consequences

- Gain roughly a 20% performance instead in average time and throughput.

### Negative Consequences

- We need 36 classes (8 primitive types + 1 object type and 4 constraint classes for each type) compared to 4 constraint classes 
(ExactLength, BetweenLength, MinimumLength, MaximumLength) to implement array length constraints for primitive arrays.
- Duplicate logic in constraint classes across types.

## Pros and Cons of the Options

### Option 1

- Pro, total files is greatly reduced. 
- Pro, easier to maintain.
- Con, not as performant.

### Option 2

- Pro, greater throughput and average time.
- Con, large increase in the number of files.
- Con, duplicate logic across constraint files.

## Links

- https://stackoverflow.com/questions/30306160/performance-of-java-lang-reflect-array
- https://bugs.openjdk.java.net/browse/JDK-8051447

## Notes

### Option 2 Implementation

```java
package jfluentvalidation.constraints.array.length;

import jfluentvalidation.common.Iterables;
import jfluentvalidation.constraints.Constraint;
import jfluentvalidation.validators.RuleContext;

import java.lang.reflect.Array;
import java.util.function.IntSupplier;

public class ArrayExactLengthConstraint<T, A> implements Constraint<T, A> {

    private IntSupplier lengthSupplier;
    private Integer length;

    public ArrayExactLengthConstraint(Iterable<?> other) {
        this(() -> Iterables.size(other));
    }

    public ArrayExactLengthConstraint(Object other) {
        this(() -> Array.getLength(other));
    }

    public ArrayExactLengthConstraint(int length) {
        this(() -> length);
    }

    public ArrayExactLengthConstraint(IntSupplier lengthSupplier) {
        this.lengthSupplier = lengthSupplier;
    }
    public ArrayExactLengthConstraint(Integer length) {
        this.length = length;
    }



    @Override
    public boolean isValid(RuleContext<T, A> context) {
        int len = Array.getLength(context.getPropertyValue());
        return len == (length != null ? length : lengthSupplier.getAsInt());
    }
}
```

```java
package jfluentvalidation.constraints.array.length;

import jfluentvalidation.constraints.Constraint;
import jfluentvalidation.validators.RuleContext;

import java.lang.reflect.Array;
import java.util.function.IntSupplier;

public class ArrayLengthConstraint<T, A> implements Constraint<T, A> {

    private IntSupplier minSupplier;
    private IntSupplier maxSupplier;

    public ArrayLengthConstraint(IntSupplier minSupplier, IntSupplier maxSupplier) {
        this.minSupplier = minSupplier;
        this.maxSupplier = maxSupplier;
    }

    public ArrayLengthConstraint(int min, int max) {
        this.minSupplier = () -> min;
        this.maxSupplier = () -> max;
    }

    @Override
    public boolean isValid(RuleContext<T, A> context) {
        int len = Array.getLength(context.getPropertyValue());
        int min = minSupplier.getAsInt();
        int max = maxSupplier.getAsInt();
        if (len < min || (len > max && max != -1)) {
            return false;
        }

        return true;
    }


}
```

```java
package jfluentvalidation.constraints.array.length;

public class ArrayMaximumLengthConstraint<T, A> extends ArrayLengthConstraint<T, A> {

    public ArrayMaximumLengthConstraint(int max) {
        super(0, max);
    }

}
```

```java
package jfluentvalidation.constraints.array.length;

public class ArrayMinimumLengthConstraint<T, A> extends ArrayLengthConstraint<T, A> {

    public ArrayMinimumLengthConstraint(int min) {
        super(min, -1);
    }

}
```
