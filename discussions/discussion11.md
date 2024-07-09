# Discussion 11

## Reminders
* Project 3 is due on July 16th!
* Final Exam is next week July 19th!!! (GOOD LUCK)

## Linked Lists in Rust vs. C

We will work with and write functions for Linked List structures in both Rust and C, to see the differences between a memory-safe language and memory-unsafe language.

### Linked List Structure
Before we start coding functions, let's understand the Linked List structure that we are working with.

#### Linked List in C

```
struct Node {
   int data;
   struct Node *next;
};
```

We will insert by pushing items onto the Linked List, meaning we will simply add them to the end of the list.

```
void insert(struct Node** head, int data){
    struct Node* nodeToInsert = malloc(sizeof(struct Node));

    // Initialize the values of the new node
    nodeToInsert->data = data;
    nodeToInsert->next = NULL;

    // If the head pointer is empty, make the new node the first thing
    if (*head == NULL) {
        *head = nodeToInsert;
        return;
    }

    // Otherwise loop through till the end, and make the previous end point to the new node 
    struct Node* curr = *head;
    while (curr->next != NULL){
        curr = curr->next;
    }
    curr->next = nodeToInsert;
}
```

Given this, and the Rust code that can be found in ll.rs, we will try to create the following functions in C. Translation!


### Freeing Linked List
`void deleteList(struct Node** head)`

In C, we will free a Linked List by looping through the Linked List and free the nodes one by one.

### Reversing Linked Lists
`void reverseList(struct Node** head)`

In C, we will reverse a Linked List by changing the reference of the pointers.

## Rust Exam Review

### Basics:

- Rust aims to be a “safe” language, which it does by being “over-protective”

- Rust has statements, codeblocks, and expressions:

- Codeblocks are run independently from the rest of the function, with their own scope:

```
let x = 3;
{ //start of codeblock
	1 + 2; //statement
	3 + 5 //expression
} //end of codeblock
```

Statements are evaluated, and end with semi-colons. Often, these are function calls or let statements.
Expressions do not have a semi-colon and are returned.
Closures are like anonymous expressions!

```
let f = |x| x + 3;
// f(5) -> 8
```
### Ownership:

#### Rust’s Ownership rules:

- Every value has an owner

- There can only be one owner of a value at a time

- When the owner goes out of scope, the value will be dropped (freed from memory)

#### Examples:
```
let s = String::from("Hello"); // s is the owner of Hello

let x = s; // x has taken ownership, s is no longer valid
let a = String::from("cmsc330"); // a is owner
{ 
	let b = a; // b is owner
	{ 
		let c = b; // c is owner
	}
}
// no owner, because c is out of scope
```

### Borrowing:

When you don’t want to transfer ownership over to a function, you should let the function borrow the value. This is done by sending in a reference to the value → &x

#### Rules of Borrowing:

- Every reference must be valid

One of the following (NOT both) must be true:

- you can have any number of immutable references

- you can have one mutable reference

Examples
```
let x = String::from("Hello");
{
	let y = &x; // temporarily borrows (immutable reference)
	println!("can use {} and {}", x, y);
}
// y now out of scope
println!("can use {}", x);
fn main() {
	let x = String::from("Hello");
	let y = get_len(&x); //function borrows x's value
	println!("{} has length {}", x, y); // then returns value to x
}

fn get_len(a: &String) -> usize {
	a.len()
}
```
### Lifetimes:

The goal of lifetimes is to prevent dangling pointers, an issue we saw often in C. To prevent this, we say that a value lives until it either

- goes out of scope (function or codeblock it was defined in ends) OR

- its final use

We show lifetimes using the ’a, ’b format (don’t confuse with OCaml generic types!)

Examples:
```
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {}", r); //          |
}                         // ---------+
```
```
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {}", r); //   |       |
                          // --+       |
}                         // ----------+
```
If we want a value to live longer, we can use lifetime annotations

```
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```