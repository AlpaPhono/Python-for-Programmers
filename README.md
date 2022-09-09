# Python-for-Programmers

>This repository is to track my progress working on the **Cloud academy Introduction to Python for Programmers** learning pathway.

*RECAP*

## Names, Data types, and Variables in Python
###Names 
- can contain letters digits and underscores
- cant start with a digit

###Datatypes
- Numeric types 
  - bool 
  - int
  -float 
  -complex
  
  ###Sequence Types
  - Strings are text (arrays of unicode characters
    **s = "text";**
  - Bytes are arrays of bytes
    **b = b"text";**
  - Lists are sequences of values
    **my_list = []**
    **sequence[start:limit:stride]**
  - Tuples are immutable sequences of values 
    **my_tuple = 'Mary', 'Poppins', 'London' **
    
    Each type has operations specific to them.
    
###Slicing Syntaxt

colours = ['red','green','blue','purple','pink','yellow','black'}
c1 = colours[0] will print 'red'
c2 = colours[1:4] will print from slot 1 to 3  'green', 'blue', 'purple'
c3 = colours[-1] will print 'black' 
c4 = colours[:3] will print from 0 to 3  'red','green', 'blue'
c5 = colours[3:] will print from 3 till the end of the list

###Mapping types
- Dictonaries are mapped sets of values (dictionaries have immutable keywords)
- Sets are similar but only contain keys
  - there are normal sets (dynamic) and forzen sets (immutable)
  ** dictionary = {key:value}**
  ** s = set()**
  
 ### Program Structure
 - All imports at the top
 - Variables, functions, and classes must be declared before use
 - Main function goes at top
 - Main function called at bottom
 
  - global variables 
  - main function
  - functions 
  - call to main function
  
### Files and Console I/0

- print()
  output to the screen
- open()
  to read a file open it with this function as part of a with statement 
- input()

  #### Reading files 
  - To read a file line by line, iterate through the file with a for loop.
  - To read the entire file, use file.read();
  - To read all lines into a list, use file.readlines()
  - To read a specified number of bytes, use file.read(n)
  - To navigate within a file use file.seek(offset, whence);
  - To get the current location, use file.tell().
  
### Conditionals 
There are 

if name == 'root'
  print ("do not run this utility as root")
elif name == 'guest':
  print("sorry - guests are not allowed to run this utility")
else:
  print("starting processing")
limit = sys.args[1] if len(sys.args) > 1 else 100


