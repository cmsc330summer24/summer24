# Discussion 10

## Reminders
* Project 2 is due on July 5th!
* No class or office hours on July 5th

## What is Rust? 

Modern language designed for concurrency; it's similar to C++ and OCaml, but does it in a fast, type-safe, and thread-safe manner
* How does it achieve speed and safety? It avoids Garbage Collection, and instead uses rules for memory management 

	`let mut x = String::from("hello");` &lt;- Mutability

	`do_something(&mut x);` &lt;- Borrowing, avoids ownership change

	`println("{}",x);`

### Mutability

* Variables can either be declared as mutable (`mut`) or immutable
    * Similar to `const` in C (but the opposite)
    * Mutable means the variable can be reassigned, e.g. `let mut x = 0; x = x + 5;`

### Slices (briefly)
When you send in a pointer to an array it is automatically makes a slice. 

Slices are something called a "smart pointer" which is just a pointer (like in C) but with metadata.

They are also used to get a part of a collection, hence the name slice. We are using them to grab the entire collection. Read more about them in Rust by example [here](https://doc.rust-lang.org/rust-by-example/primitives/array.html) or the Rust Book [here](https://doc.rust-lang.org/book/ch04-03-slices.html)!

## Rust Coding
Now that we now more about rust, let's do more coding with rust.

Implement the following functions

`fn gauss(n: i32) -> i32`
* **Description**: Returns the sum 1 + 2 + ... + n.  If n is negative, return -1.
* **Examples**:
```
gauss(3) => 6
gauss(10) => 55
gauss(-17) => -1
```

`fn in_range(lst: &[i32], s: i32, e: i32) -> i32`
* **Description**: Returns the number of elements in the slice that are in the range [s,e].
* **Examples**:
```
in_range(&[1,2,3], 2, 4) => 2
in_range(&[1,2,3], 4, 7) => 0
```

`fn subset<T: PartialEq>(set: &[T], target: &[T]) -> bool`
* **Description**: Returns true if target is a subset of set (represented as a slice), false otherwise.
* **Examples**:
```
subset(&[1,2,3,4,5], &[1,5,2]) => true
subset(&[1,2,3,4,5], &[1,2,7]) => false
subset(&['a','b','c'], &[]) => true
```

`fn mean(lst: &[f64]) -> Option<f64>`
* **Description**: Returns the mean of elements in lst. If it is empty, return None.
* **Examples**:
```
mean(&[2.0, 4.0, 9.0]) => Some(5.0)
mean(&[]) => None
```

`fn to_decimal(lst: &[i32]) -> i32`
* **Description**: Converts a binary number to decimal, where each bit is stored in order in the slice.
* **Examples**:
```
to_decimal(&[1,0,0]) => 4
to_decimal(&[1,1,1,1]) => 15
```

<!-- `fn factorize(n: u32) -> Vec<u32>`
* **Description**: Decomposes an integer into its prime factors and returns them in a vector.  You can assume factorize will never be passed anything less than 2.
* **Examples**:
```
factorize(5) => [5]
factorize(12) => [2,2,3]
```

`fn rotate(lst: &[i32]) -> Vec<i32>`
* **Description**: Takes all of the elements of the given slice and creates a new vector.  The new vector takes all the elements of the original and rotates them, so the first becomes the last, the second becomes first, and so on.
* **Examples**:
```
rotate(&[1,2,3,4]) => [2,3,4,1]
rotate(&[6,7,8,5]) => [7,8,5,6]
```

`fn substr(s: &String, target: &str) -> bool`
* **Description**: Returns true if target is a subtring of s, false otherwise.  You should not use the contains function of the string library in your implementation.
* **Examples**:
```
substr(&"rustacean".to_string(), &"ace") => true
substr(&"rustacean".to_string(), &"rcn") => false
substr(&"rustacean".to_string(), &"") => true
``` -->
## Submitting
Submit the discussion as you normally would with `git add`, `git commit -m "[message]"`, and `git push`. Then use the submit command to submit your code to github. 

## Testing
Use the command `cargo test` to test your code locally.
