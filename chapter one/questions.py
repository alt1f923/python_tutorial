# Question one
def add(x, y):
    """
    Write a function that takes integers x and y and returns the value of their product (x + y)
    Must work for floats and integers, both negative and postive
    """
    return None

# Question two
def add_division(x, y, z):
    """
    Write a function that takes integers x, y and z and returns the value of x + y over the value of z
    You MUST use the add() function for this question
    You can assume z will never be 0
    Must work for floats and integers, both negative and postive
    """
    return None

# Question three
def float_to_int(x):
    """
    Write a function that takes an float x and returns an integer that is the lowest whole number. e.g. 4.99999 -> 4
    You must use integer division for this question
    """
    return None

# Question four
def mod(x, y):
    """
    Write a function that performs the modulus operation via recursion and returns it, if you're having some problems with it this video might help: https://www.youtube.com/watch?v=Mv9NEXX1VHc
    You can NOT use the modulo operator for this question
    """
    return None

# Question five
def piecewise(n):
    """
    Write a function that will follow these conditions:
    if n is less than 3 then return negative n minus 4
    if n is either 3, 10 or between them then return n squared minus 7
    if n is greater than 10 then return 5 plus the result of 120 over n 
    """
    return None

if __name__ == "__main__": # __name__ == "__main__" will return True when THIS file is run
    # Some test cases for you, feel free to edit these!

    # In the future chapters I might not make these tests for you, but to give you an idea of what is a good idea to do when learning Python
    # and trying to answer these questions, I wrote these up for you.

    # A lot of editors (including the default IDLE) have ways to mass comment out lines of code that you have highlighted, 
    # Be sure to comment out functions you haven't finished yet, otherwise you'll get syntax errors

    # Question one
    x, y = 2, 4 # Don't be intimidated if you're confused by this line, I'll explain it in the next chapter :)
    print(f'{add(x, y)} {add(x, y) == 6}')  # The first value is what the function outputs and the second is a boolean
                                            # of whether it has returned the correct answer in the case of 2 + 4

    # Question two
    x, y, z = 2, 4, 6
    print(f'{add_division(x, y, z)} {add_division(x, y, z) == 1}')

    # Question three
    x = 4.999999
    print(f'{float_to_int(x)} {float_to_int(x) == 4}')
    
    # Question four
    x, y = 10, 55
    print(f'{mod(x, y)} {mod(x, y) == 10}')

    # Question five
    n = '2'
    print(f'{piecewise(n)} {piecewise(n) == -6}')
    n = '3'
    print(f'{piecewise(n)} {piecewise(n) == 2}')
    n = '12'
    print(f'{piecewise(n)} {piecewise(n) == 15}') # Note that 15.0 == 15 will be True
