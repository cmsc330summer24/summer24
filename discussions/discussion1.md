# Discussion 1: Git and Python
## Git Basics
[Git Practice Repo](https://github.com/CliffBakalian/git-basics)

## Python

Python is a widely-used programming language that has lots of features and libraries to support even more. Some you may have heard of before are MatPlotLib, Numpy, PyTorch, etc. 

Python is also object-oriented (like C and Java), so during this discussion we will: 
- get familiar with Python syntax through the Basics.py practice file
- see how to instantiate and work with classes through the Roster.py practice file

> [!NOTE]
> **You are not expected to complete all of this. In order to get full credit for this discussion you must complete... However, this full discussion is great extra practice, which is why we included the entire thing. Please look at it on your own time to get familiar with the language!**


## Basics Practice

This file contains a total of 6 functions to practice with. The first three are relatively simple, and the last 3 increase in difficulty. 

#### `isPalindrome(n)`
- **Description**: Returns `true` if `n` is a palindrome and `false` otherwise. A palindrome is the same read forward and backward.
- **Type**: `(Integer) -> Bool`
- **Assumptions**: `n` is non-negative; `n` will not be provided with any leading 0s.
- **Hint**: It may be easier to do this after converting the provided integer to a String.
- **Examples**:
  ```py
  isPalindrome(0) == True
  isPalindrome(1) == True
  isPalindrome(10) == False
  isPalindrome(101) == True
  isPalindrome(120210) == False

#### `nthmax(n, a)`
- **Description**: Returns the `n`th largest element in the array `a` or `None` if it does not exist. The largest element is specified using n = 0. Treat duplicated values seperately.
- **Type**: `(Integer, Array) -> Integer or None`
- **Assumptions**: `n` is non-negative.
- **Examples**:
  ```py
  nthmax(0, [1,2,3,0]) == 3
  nthmax(1, [3,2,1,0]) == 2
  nthmax(2, [7,3,4,5]) == 4
  nthmax(5, [1,2,3]) == None

#### `freq(s)`
- **Description**: Returns a one-character string containing the character that occurs with the highest frequency within 's'. If `s` has no characters, it should return the empty string.
- **Type**: `String -> String`
- **Assumptions**: Only one character will have the highest frequency (i.e. there will be no "ties").
- **Examples**:
  ```py
  freq("") == ""
  freq("aaabb") == "a"
  freq("bbaaa") == "a"
  freq("ssabcd") == "s"
  freq("a12xxxxxyyyxyxyxy") == "x"

#### `zipHash(arr1, arr2)`
- **Description**: Returns a dict that maps corresponding elements in `arr1` and `arr2`, i.e., `arr1[i]` maps to `arr2[i]`, for all i. If the two arrays are not the same length, return `None`.
- **Type**: `(Array, Array) -> Dict or None`
- **Examples**:
  ```py
  zipHash([], []) == {}
  zipHash([1], [2]) == {1: 2}
  zipHash([1, 5], [2, 4]) == {1: 2, 5: 4}
  zipHash([1], [2, 3]) == None
  zipHash(["Mamat", "Hicks", "Vinnie"], ["prof", "prof", "TA"]) == {"Mamat": "prof", "Hicks": "prof", "Vinnie": "TA"}
  ```

#### `hashToArray(hash)`
- **Description**: Returns an array of arrays; each element of the returned array is a two-element array, where the first item is a key from the hash and the second item is its corresponding value. The entries in the returned array must be in the same order as they appear in `hash.keys`.
- **Type**: `(Hash) -> Array`
- **Examples**:
  ```py
  hashToArray({}) == []
  hashToArray({"a": "b"}) == [["a", "b"]]
  hashToArray({"a": "b", 1: 2}) == [["a", "b"], [1, 2]]
  hashToArray({"x": "v", "y": "w", "z": "u"}) == [["x", "v"], ["y", "w"], ["z", "u"]]
  ```

#### `maxFuncChain(init, myfuncs)`
- **Description**: Takes a list of classes, all of which contain a `myfunc` method. The `myfunc` method takes in and Integer and returns and Integer (ie. type: Integer -> Integer). `maxFuncChain` looks at all of these methods and decides which one to apply or not to maximize the final result. For example, if I have a list of classes that hold the following functions:
`[A, B, C]` and an initial value `x`, then I take the maximum value
of
   + `x`
   + `A(x)`
   + `B(A(x))`
   + `C(B(A(x)))`
   + `C(A(x))`
   + `B(x)`
   + `C(B(x))`
   + `C(x)`

- **Type**: `(Integer, Array) -> Integer`
- **Hint**: There is an elegant recursive solution.
- **Examples**:
  ```py

  class AClass:
    def __init__(self):
      return
    def myfunc(x):
      return x + 6

  class BClass:
    def __init__(self):
      return
    def myfunc(x):
      return x + 4


  class CClass:
    def __init__(self):
      return
    def myfunc(x):
      return x * 4

  class DClass:
    def __init__(self):
      return
    def myfunc(x):
      return x + 3

  maxFuncChain(2,[AClass]) == 8
  maxFuncChain(2,[BClass, CClass]) == 24
  maxFuncChain(-4,  [CClass, DClass]) == -1
  ```

## Object-Oriented Practice
For this part, edit the `roster.py`. You will be making a `roster` class that
keeps track of a list of `Person`s. There are 2 types of `Persons`: `Staff` and
`Student`s. The following describes the 4 classes you need to make along with 
any mandatory associated methods. You may add other classes and methods if you
need them. All classes should be written in `roster.py`

## Person
 This is the superclass of `Staff` and `Student`. Every person has a `name`, 
 and `age` attribute. Every `Person` should also have the following 
 methods
 
#### `__init__(name,age)`
- **Description**: creates a Person with `name` and `age`. 
- **Type**: `(String, Integer)-> self`
- **Examples**:
  ```py
  Person('Cliff',84)
  ```

#### `get_age`
- **Description**: Returns the age of the person
- **Type**: `None-> Integer`
- **Examples**:
  ```py
  clyff = Person('Cliff', 84)
  clyff.get_age() == 84
  ```

#### `set_age(x)`
- **Description**: changes the age of the person. You may assume that any age 
is valid. Returns `self`
- **Type**: `Integer -> self`
- **Examples**:
  ```py
  clyff = Person('Cliff', 84)
  clyff.set_age(42)
  clyff.get_age() == 42
  ```

## Student

This is a subclass of a `Person`. Each student has a `grade` attribute.
Every `Student` should also have the following methods

#### `__init__(name,age, grade)`
- **Description**: creates a Student with `name`, `age` and `grade` 
- **Type**: `(String, Integer, Float)-> self`
- **Examples**:
  ```py
  Student('Cliff',16,72.5)
  ```

#### `get_grade`
- **Description**: Returns the grade of the student 
- **Type**: `None-> Float`
- **Examples**:
  ```py
  clyff = Student('Cliff',16,72.5)
  clyff.get_grade() == 72.5
  ```

#### `change_grade(x)`
- **Description**: changes the grade of the student. You may assume that any 
grade is valid. Returns `self`
- **Type**: `Float-> self`
- **Examples**:
  ```py
  clyff = Student('Cliff', 84, 50.0)
  clyff.change_grade(42.0)
  clyff.get_grade() == 42.0
  ```

## Staff

This is a subclass of a `Person`. Each staff member has a `position` attribute
Every `Staff` member should also have the following methods

#### `__init__(name, age, position)`
- **Description**: creates a Student with `name`, `age` and `position` 
- **Type**: `(String, Integer, String)-> self`
- **Examples**:
  ```py
  Staff('Cliff',16,'Professsor')
  ```

#### `get_position`
- **Description**: Returns the position of the staff member 
- **Type**: `None-> String`
- **Examples**:
  ```py
  clyff = Staff('Cliff',16,"TA")
  clyff.get_position() == "TA"
  ```

#### `change_position(newPosition)`
- **Description**: changes the position of the student. You may assume that 
`newPosition` is always valid. Returns `self`
- **Type**: `String -> self`
- **Examples**:
  ```py
  clyff = Staff('Cliff', 84, "TA")
  clyff.change_position("Head TA")
  clyff.get_position() == "Head TA"
  ```

## Roster

This will hold all the `Person`s. You should make your own `__init__` method based on the ones we saw above and what would be the most useful!

#### `add(person)`
- **Description**: Adds the person to the roster. 
- **Type**: `Person -> None`
- **Examples**:
  ```py
  roster = Roster()
  roster.add(Staff('Cliff', 84, 'Professor'))
  ```

#### `size`
- **Description**: Returns how many people are in the roster 
- **Type**: `None -> Integer`
- **Examples**:
  ```py
  roster = Roster()
  roster.size() == 0
  roster.add(Staff('Cliff', 84, 'Professor'))
  roster.size() == 1
  ```

#### `remove(Person)`
- **Description**: remove the person from the roster. You may assume everyone 
in the roster is unique. If the person is not in the roster, do nothing.
- **Type**: `Person -> None`
- **Examples**:
  ```py
  roster = Roster()
  clyff = Person('Cliff', 84)
  roster.add(clyff)
  roster.remove(clyff)
  roster.size() == 0
  ```

#### `get_person(name)`
- **Description**: get the person with `name` in the roster. You may assume that
everyone in the roster has a unique name. If the person is not in the roster, 
return None.
- **Type**: `String-> Person`
- **Examples**:
  ```py
  roster = Roster()
  cliff = Person('Cliff', 84)
  roster.add(cliff)
  cliff == roster.get_person('Cliff')
  ```


## Testing

You should be able to run `python3 -m pytest` in the discussion1 directory and `pytest` will figure the rest out.
