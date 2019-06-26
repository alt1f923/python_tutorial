**Topic one**
=============
**This topic covers:**
 * Getting started
 * What is Python
 * The Python shell
 * Expressions
 * Assignment
 * Conditionals
 * Functions
 * Objects and methods
 * Types

## Getting started
  Let's start your introduction to python by making sure you have installed it correctly.  
    
  Make sure you have the latest version: <https://www.python.org/downloads/>  
  I'm personally running version 3.7.3, but any version after 3.6 as far as I'm aware will work for what I'll be doing, but to be on the safe side, try to make sure you're on the latest version.  
    
  When you go to install it make sure you check the box that adds python to PATH. It's on one of the first slides at the bottom of the installer and is usually unchecked by default.  
  This is important as it means you can run python scripts, access the python shell, and most importantly for later it'll mean you can use pip from the command prompt.  
    
  Now that you have python installed and in your systems PATH environment variable. We can begin. Feel free to use whatever editor you prefer, it doesn't really matter. Don't let anyone tell you otherwise, however what is important, is to check out python lints and formatters, if you have other people working on your code with you, or if you end up taking an extended break from your code, having it be readable and easier to understand is a godsend.  
  You can check such things out here:  
  <https://github.com/python/black>  
  <https://www.pylint.org/>    
    
  Programming is about expressing your creative thought into logic that can be understood by a computer, it's why I personally find it so fun. Try to remember that, it's supposed to be fun.


## What is Python
  Python may be different to languages that you have used before or will use in the future. Python is an interpreted high level language. What that means is, python will talk to your computer and convert the code you've written into instructions that it can understand one line at a time.  
  That's what an interpreter does, a compiler on the other hand will convert the entire program to instructions that the computer can understand in one go. They both have their advantages, but generally compilers are faster than interpreters, but I wouldn't worry about that, python is relevant and widely appreciated by programmers worldwide despite that.  
  Continuing the explaination, to be high level as a programming language, the language is far less complex and thus easier for humans to understand, sacrificing performance and control in return for an easier programming experience.  
  Because the logic behind programs is generally the same despite this, you still have to think the same way when programming in a lower level language like rust or c++ as you do when you program in python, but an advantage of it is you can implement your creative ideas quickly and easily.  
    
  Here's a good video that explains the concept well, better than I ever could, even if it is a little dated: <https://www.youtube.com/watch?v=_C5AHaS1mOA>

## The Python shell
  One of the advantages of Python being an interpreted language is that you can write code and get instant feedback. A way to do this is by using the python shell, to open it you can open the default python IDLE, or type "py" into cmd or powershell. (If this doesn't work try "python" or "python3", if you can't get it to work at all, make sure Python is in your PATH)  
    
  A good way to get an understanding of how the interpreter works is to use the shell, think of every line in your code as another line typed out into the shell. One by one.  
  For the first few topics, I will be using the python shell to demonstrate them.  

## Expressions
  The first concept I would like to introduce to you is **Expressions**. You should be familar with these if you've done any form of mathematics in your life, you might not be familar with the terminology 
surrounding them and that's okay. That's not what is important here, the skills are.  
    
  Here is an example of an Expression.  
  (52 + 7  * 4) - 11  
  You probably know exactly what an expression is now, just by looking at that, but indulge me for a moment, expressions are built up of **operands** and **operators**. Operands in this example being 52, 7, 4 and 11. 
The operators in this case are +, * and -. What it equals isn't really important, but if you figure it out, good for you.  
  Operands can be anything that can represent a value, so if you have `x` that equals a number then that would be a valid operand.  
Operators are the symbols that denote what operation should be done to it's accompanying operands. There are few of them, the ones I want to show you are:  
 * `+` for addition
 * `-` for subtraction
 * `*` for multiplication
 * `/` for division
 * `//` for integer division (AKA floor division/rounding down to the closest lowest whole number)
 * `**` for exponentiation
 * `%` for modular arithmetic (AKA modulus/modulo/mod)  
    
  You might have noticed that the first 4 are pretty simple, and they are.  
    
  Here are some examples of these operations in use, feel free to play around with the python shell by writing some expressions yourself!
  ```python
  >>> 3 + 2
  5
  >>> 3 - 2
  1
  >>> 3 * 2
  6
  >>> 3 / 2
  1.5
  >>> 3 // 2
  1
  >>> 3 // 2 + 1 #Please note that to do ceiling division, you just add one onto the result of floor division
  2
  >>> 3 ** 2
  9
  >>> 3 % 2
  1
  ```
      
  If you need any help understanding integer division, exponentiation or modular arithmetic, then I would recommend checking out these links:  
   * [Floor and Ceiling division](https://www.youtube.com/watch?v=RxNs4SwP6lk)  
   * [Exponentiation](https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals#pre-algebra-exponents)  
   * [Modular arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography#modarithmetic)  
## Assignment

## Conditionals

## Functions

## Objects and methods

## Types