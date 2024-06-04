# Discussion 2 HOF and Regex

## Reminders



## HOF

What are they?
- Basically use functions as parameters for other functions
- Able to assign functions to variables

What's the point?
- More concise code
- Cleaner code
- Abstraction

### HOF and Lambda Practice

`is_present(lst,x)`
- Returns a list of the same length as `lst` which has a `1` at each position in which the corresponding position in `lst` is equal to `x`, and a `0` otherwise.
- Examples:
  + `is_present([1,2,3],1) == [1,0,0]`
  + `is_present([1,2,1],1) == [1,0,1]`

`count_occ(lst,target)`
- Returns how many elements in `lst` are equal to `target`
- Examples:
  + `count_occ([1,2,3],1) == 1`
  + `count_occ([1,1,1],1) == 3`

`uniq(lst)`
-    Given a list, returns a list with all duplicate elements removed. Order does not matter.
- Examples:
  + `uniq([1,2,1,2]) == [1,2]`
  + `uniq([4,3,2,1]) == [4,3,2,1]`

`find_max(matrix)`
- given a list of lists find the maximum. You may assume the inputs are non-negative ints.
- Examples:
  + `find_max([[1,2],[3,4],[5,6]]) == 6`
  + `find_max([[1,1],[1],[1]]) == 1`

`count_ones(matrix)`
- given a matrix count how many 1s are in the matrix
- Examples:
  + `count_ones([[1,1],[1],[1]]) == 4`
  + `count_ones([[],[3],[0]]) == 0`

`addgenerator(x)`
- return a lambda function that adds x to its parameter
- Examples:
  + `addgenerator(4)(5) == 9`
  + `addgenerator(1)(5) == 6`

`apply_to_self()`
- return a lambda function that takes in 2 parameters. The first is an element and the second is a function. The body of the lambda function should add the element to the application of the function to the element. You may assume that the elementis an int
- Examples:
  + `apply_to_self()(2,lambda x: x + 1) == 5 #2 + (2 + 1)`
  + `apply_to_self()(4,lambda x: -x) == 0 #4 + (-4)`

`ap(fns,args)`
- Applies each function in `fns` to each argument in `args` in order, collecting all results in a single list.
- Examples:
  + `ap([lambda x: x + 1, lambda x: -x],[1,2,3]) == [2,3,4,-1,-2,-3]`
  + `ap([lambda x: x - 1, lambda x: 4],[1,2,3]) == [0,1,2,4,4,4]`

`map2(matrix,f)`
- write a function that is similar to `map` but works on lists of lists
- Examples:
  + `map2([[1,2,3],[4,5,6]],lambda x: -x) == [[-1,-2,-3],[-4,-5,-6]]`
  + `map2([[1,2,3],[4,5,6]],lambda x: 0) == [[0,0,0],[0,0,0]]`


## Regular Expressions (Regex)

What are they?
- Expressions that represent strings, with various symbols that denote patterns

Examples:
- Regex: 'abc' -> matches with the string: abc
- Regex: '[a-z]' -> matches with any single lowercase letter
- Regex: '\d' -> matches a single numerical digit

Python Regex library: https://docs.python.org/3/library/re.html

What's the point?
- Text processing!

### Regex Practice

We are going to process actions that Pokemon can perform during a pokemon battle through a text file. The text file is formatted as follows:

```txt
pokemon1 VS pokemon2
pokemon1 action
pokemon2 action
pokemon1 action
pokemon2 action
```

The possible actions are as follows:

- attack X
- run
- heal Y

Attack and heal will both be followed by a number representing how much damage they did/how much health they restored. The number and the action can be separated by an arbitrary number of spaces (including 0).

Actions will always be separated by a newline. 

Your task is to process this information into a list of actions. 

`process_battle(input_file)`

- Write a function that takes this text file and transforms it into a list of PokemonAction objects. Maintain the order that the actions occur in the file.

- You are to ignore any invalid lines, by these rules:
    - Pokemon names and actions can be separated by one or more spaces, but they **cannot** be flipped or have 0 spaces between them
    - Actions and action numbers (i.e. if heal or attack) can be separated by any number of spaces (0 is fine). 
    - Ignore any lines that do not describe the two pokemon that are at the start of the battle.
    - Ignore any lines that have too many commands
    - Ignore any lines that do not have enough information (i.e. no number after attack/heal) or too much information (i.e. a number after run)

**Note**: If the first line does not follow the format of "pokemon1 vs pokemon2" OR "pokemon1 VS pokemon2" then the entire file is invalid and your function should return an EMPTY LIST

The PokemonAction class is defined as follows, and is also in your regex.py file (**Do not modify this class**):
```python
class PokemonAction:
    def __init__(self, user: str, action: str, value):
        self.user = user # name of the pokemon performing the action
        self.action = action # options: "ATTACK", "HEAL", "RUN"
        self.value = value # an integer if ATTACK or HEAL, None if RUN

    def __repr__(self): #used for printing
        return f'PokemonAction(\'{self.user}\', \'{self.action}\', {self.value})' 
    
    def  __eq__(self, other):
        return self.user == other.user and self.action == other.action and self.value == other.value
    
```

**Examples:**

```txt
# file1.txt

pikachu vs diglett
pikachu attack 30
diglett attack 20
pikachu heal 15
diglett attack 20
pikachu run
```

```txt
# file2.txt

bulbasaur VS charmander
bulbasaur attack2
charmander attack     14
bulbasaur   heal   10
charmander attack 23
pikachu heal 2  # invalid line-- ignore
bulbasaur   run  30 #invalid bc num after run
charmander run
```

Assertions:
```python
process_battle("file1.txt") == [PokemonAction("pikachu", "ATTACK", 30), PokemonAction("diglett", "ATTACK", 20), PokemonAction("pikachu", "HEAL", 15), PokemonAction("diglett", "ATTACK", 20), PokemonAction("pikachu", "RUN", None)]
```

```python
process_battle("file2.txt") == [PokemonAction("bulbasaur", "ATTACK", 2), PokemonAction("charmander", "ATTACK", 14), PokemonAction("bulbasaur", "HEAL", 10), PokemonAction("charmander", "ATTACK", 23), PokemonAction("charmander", "RUN", None)]
```

## Testing

You should be able to run `pytest` and `pytest` will figure the rest out
