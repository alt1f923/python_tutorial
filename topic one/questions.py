# Question one
def add(x, y):
    """
    Write a function that takes integers x and y and returns the value of their product (x + y)
    """

# Question two
def add_division(x, y, z):
    """
    Write a function that takes integers x, y and z and returns the value of x + y over the value of z
    You MUST use the add() function for this question
    You can assume z will never be 0
    """

# Question three
def fstring(s1, s2, x, y):
    """
    Write a function that takes strings s1 and s2 and integers x and y and returns a string containing them in the same format as:
    s2 + ' ' + s1 + str(add(x, y))
    You must use a fstring for this question 
    """

# Question four
def string_case_concatenation(s1):
    """
    Write a function that takes the string s1 and returns the value of s1 + the value of s1 in lowercase + the value of s1 in uppercase
    s1 itself must not be edited
    """

# Question five
def word_square(s1):
    """
    Write a function that takes a string s1 and returns the square of it as an integer
    You can assume s1 will always be a valid int e.g. s1 = '32'
    """

# Question six
def float_to_int(x):
    """
    Write a function that takes an float x and returns an integer that is the lowest whole number. e.g. 4.99999 -> 4
    There is more than one way to do this, use whatever one you are most comfortable with
    """

# Question seven
def fizzbuzz(n):
    """
    Write a function that will return 1 of 4 values: 
    if n is a multiple of 3 return 'fizz', 
    if a multiple of 5 return 'buzz', 
    if both return 'fizzbuzz', 
    if neither return n
    """

if __name__ == "__main__":
    # Some test cases for you, feel free to edit these!
    # A lot of editors (including the default IDLE) have ways to mass comment out lines of code that you have highlighted, 
    # Be sure to comment out functions you haven't finished yet, otherwise you'll get syntax errors

    # Question one
    x, y = 2, 4 # Don't be intimidated if you're confused by this line, I'll explain it in the next topic :)
    print(f'{add(x, y)} {add(x, y) == 6}')  # The first value is what the function outputs and the second is a boolean
                                            # of whether it has returned the correct answer in the case of 2 + 4

    # Question two
    x, y, z = 2, 4, 6
    print(f'{add_division(x, y, z)} {add_division(x, y, z) == 1}')

    # Question three
    s1, s2, x, y = 'a', 'b', 2, 4
    print(f'{fstring(s1, s2, x, y)} {fstring(s1, s2, x, y) == "b a6"}')
    
    # Question four
    s1 = 'aB'
    print(f'{string_case_concatenation(s1)} {string_case_concatenation(s1) == "aBabAB"}')

    # Question five
    s1 = '3'
    print(f'{word_square(s1)} {word_square(s1) == 9}')

    # Question six
    x = 4.999999
    print(f'{float_to_int(x)} {float_to_int(x) == 4}')

    # Question seven
    n = 15
    print(f'{fizzbuzz(n)} {fizzbuzz(n) == "fizzbuzz"}')
    n = 3
    print(f'{fizzbuzz(n)} {fizzbuzz(n) == "fizz"}')
    n = 5
    print(f'{fizzbuzz(n)} {fizzbuzz(n) == "buzz"}')
    n = 1
    print(f'{fizzbuzz(n)} {fizzbuzz(n) == 1}')
    