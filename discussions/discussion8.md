# Discussion 8 Lambda Calculus

## Reminders
1. Project 2 is out!! 
2. Exam grades are out! Regrade requests are due by Thursday at 11:59pm

# Lambda Calculus Review

### Call by Value
"eager evaluation" </br>
before doing a beta reduction, we make sure the argument cannot, itself, be further evaluated

(λz. z) ((λy. y) x) → (λz. z) x → x

### Call by Name
"lazy evaluation" </br>
we can specifically choose to perform beta-reduction *before* we evaluate the argument

(λz. z) ((λy. y) x) → (λy. y) x → x

### Scoping Rules
Lambda calculus has an ambiguous grammar:

e -> x \
    | e e \
    | λx.e

In order to fix that, we can define explicit parentheses to enforce the scoping/application rules which are as follows: 
- Scope of a parameter lasts until **either**:
    - the first unmatched parenthesee
    OR 
    - the end of the line
- Lambda Calculus is Left-associative

### Church Encodings:
We can translate logical/mathematical expressions into lambda calculus!

True: λx.λy.x

False: λx.λy.y

If x then y else z: x y z

Not a: (λx.x (λx.λy.y) (λx.λy.x)) a


Using these, we can derive many logical operators (not, and, or, etc.)

### Exercises

1) (λa. a) b

**Make the parentheses explicit in the following expressions:**

2) a b c

3) λa. λb. c b

4) λa. a b λa. a b

**Identify the free variables in the following expressions:**

5) λa. a b a

6) a (λa. a) a

7) λa. (λb. a b) a b

**Apply alpha-conversions to the following:**

8) λa. λa. a

9) (λa. a) a b

10) (λa. (λa. (λa. a) a) a)

**Apply beta-reductions to the following:**

11) (λa. a b) x b

12) (λa. b) (λa. λb. λc. a b c)

13) (λa. a a) (λa. a a)

**Using Church encodings:**

14) Show that "true and false" evaluates to false

15) Derive "or" in church encodings

16) Derive "and" 

17) Numbers!



