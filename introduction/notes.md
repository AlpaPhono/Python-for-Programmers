# Hello_World.py
**Things I didnt understand** 

## What does %s mean in python
>#CODE3: Use string formatting and interpolation then print to the console
>print("%s - %s" % (message1, message2))

*"%s specifically is used to perform concatenation of strings together. #able to format a value inside a string.  #Automatically provides type conversion from value to string"*  (GeekforGeeks, 2021)

### Simple use of %s
**declaire a string variable**
name = "geek"

**append the variable to a string**
#print("hey, %s!" % name)
**OUTPUT**
Hey, Geek!

### Multiple use
**#CODE3: Use string formatting and interpolation then print to the console**
print("%s - %s" % (message1, message2))

- Code3 in hello_world.py is an example of multiple use.
- Notice there is percentage sign before referencing the variable you are substituting with.
- Also it substitutes respecitve the order in which you have declaired your variables within the parentheses

**OUTPUT**
Hello World - Cloud Academy

### declaring string variables with dictionary
dct = {'str1': 'at',
       'str2': 'GeeksforGeeks',
       'str3': 'Understanding',
       'str4': '%s'}
  
**concatenating strings**
final_str = "%(str3)s %(str4)s %(str1)s %(str2)s" % dct
  
**printing the final string**
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)

- Notice the key's are referenced inside parantheses but unlike normal vars the % sign is before the brackets and the s comes after.

- Instead of referencing the the variable at the end you reference the dictrionary the keys came from.
**OUTPUT**
Concatenating multiple strings using Python '%s' operator:

Understanding %s at GeeksforGeeks

### List as a string for %s
**declaring string variables**
str1 = 'Understanding'
str2 = 'integers'
str3 = 'at'
str4 = 'GeeksforGeeks = '
  
**declaring list variables**
lst = [1, 2, 3]
  
**concatenating strings as well as list**
final_str = "%s %s %s %s %s" % (str1, str2, str3, str4, lst)
  
**printing the final string**
print("Concatenating multiple values using Python '%s' operator:\n")
print(final_str)

**OUTPUT**
Concatenating multiple values using Python '%s' operator:

Understanding integers at GeeksforGeeks =  [1, 2, 3]
----

# WALK_EX.py
This code is focused on showing that python is able to create scripts that can edit files and directories within a machines system.

**CODE1**
imports the OS module allowing the use of its many functions.
**CODE2**
Creates a variable called START_DIR which holds a string variable that represents the parent directory in a bash command line.
**CODE3**
Creates a function called traversal 
- the first for loop creates three variables that will be used during the iteration. 
- os.walk() expects a path to satisfy its parentheses hence the use of *START_DIR* (Pyhton101,2017)
os.walk() returns a tuple of (directory path,subdirectories, files)
- The second iteration is used to iterate through all the files in the os.walk(STAR_DIR) tuple
- the if conditional stating that if the file ends with .py then print its name onto the console

- os.path is a sub-module in the os module that has its own set of "methods".
       - os.path.join  - the join method expects two arguments in its parentheses (1st path component, 2nd path component)
       in this example it combines the path of the directory and the path in which the python file has been found

**CODE4**
The explination for this is long and will be reviewed later.


# References 
- GeeksforGeeks, 2 February 2021, What does %s mean in a Python format string? [Online] visted: 13/09/2022
link:https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#:~:text=%25s%20specifically%20is%20used%20to,conversion%20from%20value%20to%20string.

python101.pythonlibrary, Driscoll. M, 13.9.2017, Chapter 16 - The os Module [Online] visited: 13/09/2022, link:https://python101.pythonlibrary.org/chapter16_os.html