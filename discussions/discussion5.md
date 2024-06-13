# Discussion 5 Basic Ocaml

## Reminders
1. Project 1 due Tuesday, June 18th 11:59PM
2. Exam next Thursday!!!

# Ocaml
## Part 1: Ocaml expressions, values, and types

Some basics of Ocaml. Ocaml is a compiled and bootstrapped language. It is implicitly typed. That means, the compiler infers the type of your variables and values at compile time. Ocaml is also statically typed, meaning once the type of a variable is infered, the variable must abide by the type throughout its scope. Everything in Ocaml is immutable. Everything means everything. Once you initialize a variable, you cannot change throughout its scope. You should redefine it to change it. That being said, `=` is an equality operator and not the assignment operator outside `let` expressions. 

Some primitive built-in data types are `int`, `float`, `char`, `string`, `bool`, and `unit`. Other composite data types include `tuples`, `lists`, `option`, and variants.

We know the primitive data types but we will learn more about the others later down in the discussion. Arithmetic operators in Ocaml are not overloaded. So, you can use `+`, `-`, `*`, `/` on two ints but not on floats. For floats, they are `+.`, `-.`, `*.`, `/.`. **Notice the period**.

Expressions are something that evaluates to some value. Example: `1 + 2`, `2 < 3`, `"hello"`.

## Part 2: Let bindings and Let expressions

Almost everything in Ocaml is an expression , say `e`. An expression will evaluate to some value of type, say `t`.

Examples:  
- `1: int`
- `true: bool`
- `'e': char`

The `let` syntax is the main way to bind a name to a value. Simply: 

```ocaml
let name = value;; (* syntax *)
let num1 = 5;; (* type: int *)
let num2 = 6;; (* type: int *)
let num3 = num1 + num2;; (* type: int *)
```

We use `let` to create expressions as well. Remember that expressions evaluate to some values. So, the variables initialized in the let expressions are limited to the expression in terms of scope.

Examples:

```ocaml
let x = 8 in x;;  (* will evaluate to 8 *)
let x = 10 in let y = 15 in x + y;; (* nested let expressions *)
let x = 5 in let y = 7 in if x > y then "bigger" else "smaller";; (* expression can be another expression *)
```

## Part 3: Functions and the `rec` keyword

Functions, conventionally, are multiline reusable code that might or might not depend on other variables (arguments). To denote the notion of functions in Ocaml, we can treat the functions as expressions i.e. something that can evaluate to a value. Technically, a function processes the input and generates an output. Putting multiple expressions together can work the same magic. So, we use `let` bindings to bind expression(s) and parameters to some name to make functions.

Example:

```ocaml
let my_function a = a;; (* type 'a -> 'a *)
```
analogous to (java)
```java
<T> T my_function(T a) {
    return a;
}
```

Raising the complexity of the functions:
```ocaml
let my_func param1 param2 = param1 + param2;; (* type: int -> int -> int *)
let to_arr a b = [a; b];;                     (* type: 'a -> 'a -> 'a list *)  
```
analogous to (java)
```java
int my_func(int param1, int param2) {
    return param1 + param2;
}

<T> T[] to_arr(T a, T b) {
    return {a, b};
}
```

```ocaml
let check_empty_string str_param = 
    if str_param = "" then true else false;; (* type: string -> boolean *)

let check_a_string str_param = 
    if str_param = "a" then true else "invalid string";; (* will fail to compile *)
```

Notice how each branch in a function (maybe if-else or pattern matching) should return the same data type.

The general pattern for determining the type of any function is:

`first_param_type -> second_param_type -> ... -> last_param_type -> return_type`.

Let's practice writing functions with specified types!

#### `'a -> 'a -> bool`

#### `('a -> 'b) -> 'a -> 'b -> bool`

#### `int -> (int -> float) -> string` (Challenge)
<br/>

### Recursive functions

The use of `rec` keyword makes a function recursive. You do not need to make recursive calls, but if you want to, you need the `rec` keyword.

```ocaml
let rec factorial num = 
    if num = 1 then 1 else num * (factorial (num - 1)) (* int -> int *)
```

### Ocaml Coding Excercises
Here are some basic Ocaml coding problems to get your self more familiar with Ocaml

### Basic Functions

#### `rev_tup tup`

- **Type**: `'a * 'b * 'c -> 'c * 'b * 'a`
- **Description**: Returns a 3-tuple in the reverse order of `tup`.
- **Examples**:
   ```ocaml
   rev_tup (1, 2, 3) = (3, 2, 1)
   rev_tup (1, 1, 1) = (1, 1, 1)
   rev_tup ("a", 1, "c") = ("c", 1, "a")
   ```

#### `is_even x`

- **Type**: `int -> bool`
- **Description**: Returns whether or not `x` is even.
- **Examples**:
  ```ocaml
  is_even 1 = false
  is_even 4 = true
  is_even (-5) = false
  ```

#### `area p q`

- **Type**: `int * int -> int * int -> int`
- **Description**: Takes in the Cartesian coordinates (2-dimensional) of any pair of opposite corners of a rectangle and returns the area of the rectangle. The sides of the rectangle are parallel to the axes.
- **Examples**:
  ```ocaml
  area (1, 1) (2, 2) = 1
  area (2, 2) (1, 1) = 1
  area (2, 1) (1, 2) = 1
  area (0, 1) (2, 3) = 4
  area (1, 1) (1, 1) = 0
  area ((-1), (-1)) (1, 1) = 4
  ```

### Recursive Functions
  #### `fibonacci n`

- **Type**: `int -> int`
- **Description**: Returns the `n`th term of the fibonacci sequence.
- **Assumptions**: `n` is non-negative, and we will **not** test your code for integer overflow cases.
- **Examples**:
  ```ocaml
  fibonacci 0 = 0
  fibonacci 1 = 1
  fibonacci 3 = 2
  fibonacci 6 = 8
  ```

#### `pow x p`

- **Type**: `int -> int -> int`
- **Description**: Returns `x` raised to the power `p`.
- **Assumptions**: `p` is non-negative, and we will **not** test your code for integer overflow cases.
- **Examples**:
  ```ocaml
  pow 3 1 = 3
  pow 3 2 = 9
  pow (-3) 3 = -27
  ```
  
#### `is_prime x`
- **Type**: `int -> bool`
- **Description**: Returns whether or not `x` is prime.  Note that all negative numbers are non-prime. There are many ways to determine
if a number is prime (for example, [Wilson's Theorem](https://en.wikipedia.org/wiki/Wilson%27s_theorem)). While we provide this resource, note that
this function does not have to be implemented in this way.
- **Examples**:
  ``` ocaml
  is_prime 1 = false
  is_prime 2 = true
  is_prime 3 = true
  is_prime 4 = false
  is_prime 5 = true
  is_prime 60 = false
  is_prime 61 = true
  is_prime -2 = false
  ```

## Part 3: HOF

`map` and `reduce` are common functions in OCaml with slightly different functionality. `map` in OCaml will take in a function and a list and return a new list with the mapped values. `fold_left` is OCaml's version of python's `reduce`. It will go through the list from left to right and reduce to a single value. Unlike in Python, `fold_left` must take in an inital value. There is also a `fold_right` which will go through the list from right to left.

Use `map` and `fold` (left or right) to complete the following functions that you did initially in Python. We will go over how map and fold work internally (and list operations) tomorrow in lecture. For know, you can treat these functions and just that: functions that you know the inputs and the intended output.

`is_present lst x`
- Returns a list of the same length as `lst` which has a `1` at each position in which the corresponding position in `lst` is equal to `x`  and a `0` otherwise.
- Examples:
  + `is_present [1;2;3] 1 == [1;0;0]`
  + `is_present [1;2;1] 1 == [1;0;1]`

`count_occ lst target`
- Returns how many elements in `lst` are equal to `target`
- Examples:
  + `count_occ [1;2;3] 1 == 1`
  + `count_occ [1;1;1] 1 == 3`

`uniq lst`
-    Given a list  returns a list with all duplicate elements removed. Order does not matter.
- Examples:
  + `uniq[1;2;1;2] == [1;2]`
  + `uniq[4;3;2;1] == [4;3;2;1]`

`find_max matrix`
- given a list of lists find the maximum. You may assume the inputs are non-negative ints.
- Examples:
  + `find_max[[1;2];[3;4];[5;6]] == 6`
  + `find_max[[1;1];[1];[1]] == 1`

`count_ones matrix`
- given a matrix count how many 1s are in the matrix
- Examples:
  + `count_ones[[1;1];[1];[1]] == 4`
  + `count_ones[[];[3];[0]] == 0`
