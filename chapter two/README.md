**Chapter two**
=============
**This chapter covers:**
 * [Types](#Types)
 * [Objects and Methods](#Objects-and-Methods)
 *  [Functions continued](#Functions-continued)
 * [Literals](#Literals)
 * [Mutability](#Mutability)
 * [Error handling](#Error-handling)
 * [Importing](#Importing)
## Types
### Types we know so far
Types are an important part of Python, but the language itself generally does most of the work for you. Types are classifications of values. Some examples that we have used and seen so far are:
 * Integers (`int`), these are signed (negative or positive) whole numbers, think numbers like `3` and `-10`
 * Floating point integers (`float`), are (negative or positive) numbers that have a decimal point, even if it's equal to a whole number, think numbers like `3.4`, `-10.1` and `4.0`
 * Booleans (`bool`), `True` or `False`  
    
When you want to check the type of a value, you can use the `type()` method. Like below:
  ```python
  >>>type(34)
  <class 'int'>
  ```
If you want to get a string representation of an object, you can use the `repr()` method. Like below:
  ```python
  >>>repr(34)
  '34'
  ```
`repr()` returns a string of how to define the object as you gave it. You can use the `eval()` method to undo this by turning a `str` into Python code that is executed. Like below:
  ```python
  >>>eval("3 + 2")
  5
  ```  
### The String type
The type I want to introduce to you in this chapter is the string (`str`). Think of a string as a sequence of 0 to a large number of characters ([the maximum amount of characters is dependant on your systems memory](https://stackoverflow.com/questions/1739913/what-is-the-max-length-of-a-Python-string)).  

You can use the same sort of operations to `str` as you can to `int`, as you can see to these examples in interactive mode:
```python
>>> s = "string"
>>> s
'string'
>>> s + "s"
>>> s
'strings'
>>>s * 2
'stringstring'
```
You can't use every operation like `-` or `/` to `str`  
### Changing types
Sometimes you will want to add an int to a string, but if you try to add an `int` or a `float` to a `str` with the `+` operator, you will get an error. How you can get around this is by converting the types of the `int`/`float` to `str` by using `str(int)`, you can also convert numbers that are in `str` form to `int`/`float`, but if it isn't a valid `int`/`float` then you will also get an error. Examples of converting types being:
```python
>>> str(34)
'34'
>>> str(3.4)
'3.4'
>>> str(True)
'True'
>>> int(3.4)
3
>>> int(True)
1
>>> int(False)
0
>>> float(1)
1.0
>>> int("34")
34
>>> float("1")
1.0
>>> float("3.4")
3.4
>>> bool("")
False
>>> bool(" ")
True
>>> 
```
Note that converting a `float` to an `int` will yield the same result as doing integer division and `True` and `False` have integer values equivalent to `1` and `0` respectively.  
    
  A very convienient way you can add values in different types without having to manually convert them to Python strings is by using fstrings, they follow this notation: `f"{x} string {y}"`, there is an example below:
```python
>>> x = 3
>>> y = 2.4
>>> s = 'word'
>>> f"int: {x}, float: {y}, string: {s}"
'int: 3, float: 2.4, string: word'
```
## Objects and Methods
**Everything** in Python is an **object**, `int` objects, `float` objects, `str` objects, function objects.  
  But what are objects? Well, objects are like these bags of functions.  
  Each `type`, `class` and `object` have functions that operate on them. These functions are called **methods**.  
    
  I will give some examples of methods for the `type` `str` in interactive mode:
```python
>>>"string".captialize() # Note that you can just use a string literal instead of a variable to use the method on. (I'll cover literals later in this chapter.)
'String'
>>>"STRING".lower()
'string'
>>>"string".upper()
'STRING'
>>>"ringstringstring".strip("ring") 
'stringst' # Note that it only removes the substring from the ends, and not from inside, this is especially useful for removing leading and trailing whitespace.
>>>"string".split('i')
['str', 'ng'] # This is a list type variable, don't worry, I'll be covering these in the next chapter!
```
To find all the methods for objects you can use:
```python
>>>help(object)
```
Or check it out on the [official Python documentation](https://docs.python.org/3/)
## Functions continued
In the previous chapter, I introduced you to functions, how to define them and how return values with them. This will be a continuation of functions as a topic as there is more that you can do with them.
### Multiline docstrings
Previously I talked about single line docstrings, there is another type that explains the function of the program you are making in more detail. These as you can probably guess from the header, take up multiple lines.  
They are also unsurprisingly more complex, which helps in providing more information to anyone reviewing the code that you are writing.  
  
Sections in function multiline docstrings are:  
 * Args: A list of the parameters and their types that are used in the function.
 * Returns/Yields: A description of what the function returns/yields.
 * Raises: All exceptions that might be raised, so long as they're relevant.

These are all covered in [PEP 257](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings) and by the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)  
  
A multiline docstring using the example from [single line docstrings](../chapter%20one/README.md#Single-line-Docstrings) could look like this:
```python
def function(x, y):
  """Multiply the product of x + y by y and return the result.
  
  Args: 
    x: An integer.
    y: An integer.
    
  Returns:
    The product of x + y multiplied by y.
  """
  return (x + y) * y
  
```
Now, this example is pretty simple. If it is **obvious** what a function does or if it is **short** like the example above is. Then you don't have to include any docstring since it would be redundant.
### Decorators
### Default Values
###  *Args and **Kwargs
### Static analysis
### Type hinting
### Generators
