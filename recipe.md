# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

> As a user
> So that I can find my tasks among all my notes
> I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def includes_todo(line):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        line: a string which may or may not contain "#TODO" (e.g. "Wash the dishes")

    Returns: (state the return value and its type)
        a boolean, whether string contains substring or not (e.g. True)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
given input empty string ""
returns False
"""
includes_todo("")
#=>False

"""
given input "#TODO buy milk"
returns True
"""
includes_todo("#TODO buy milk")
#=>True

"""
given input "drink tea"
returns True
"""
includes_todo("drink tea")
#=>False

"""
given input "learn to test-drive my code #TODO"
returns True
"""
includes_todo("learn to test-drive my code #TODO")
#=>True

"""
given input with lower case todo  "learn to test-drive my code #todo"
returns False
"""
includes_todo("learn to test-drive my code #todo")
#=>False

"""
given input without # in front of todo
"learn to test-drive my code TODO"
returns False
"""
includes_todo("learn to test-drive my code TODO")
#=>False

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

Ensure all test function names are unique, otherwise pytest will ignore them!
