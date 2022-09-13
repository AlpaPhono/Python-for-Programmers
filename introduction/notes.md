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



# References 
- GeeksforGeeks, 2 February 2021, What does %s mean in a Python format string? [Online] visted: 13/09/2022
link:https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#:~:text=%25s%20specifically%20is%20used%20to,conversion%20from%20value%20to%20string.

