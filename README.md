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
    
    Tuples are not commonly iterated through but elements are accesed indvidually or unpacked into variables
    
    Each type has operations specific to them.
    <u> Common Properties <u>
  - share syntax for indexing/slicing
  - share some common methods and functions 
  - All can be iterated over with FOR loop
  
    
###Slicing Syntaxt
  [start:stop:step]

colours = ['red','green','blue','purple','pink','yellow','black'} <br />
c1 = colours[0] will print 'red'<br />
c2 = colours[1:4] will print from slot 1 to 3  'green', 'blue', 'purple' <br />
c3 = colours[-1] will print 'black'  <br />
c4 = colours[:3] will print from 0 to 3  'red','green', 'blue'<br />
c5 = colours[3:] will print from 3 till the end of the list <br />

###Mapping types
- Dictonaries are mapped sets of values (dictionaries have immutable keywords)
- Sets are similar but only contain keys
  - there are normal sets (dynamic) and forzen sets (immutable)
  ** dictionary = {key:value}**
  ** s = set()**
  
## Program Structure
 - All imports at the top
 - Variables, functions, and classes must be declared before use
 - Main function goes at top
 - Main function called at bottom
 
  - global variables 
  - main function
  - functions 
  - call to main function
  
 ## Files and Console I/0

  - print()
    output to the screen
  - open()
    to read a file open it with this function as part of a with statement 
  - input()

    ### Reading files 
    - To read a file line by line, iterate through the file with a for loop.
    - To read the entire file, use file.read();
    - To read all lines into a list, use file.readlines()
    - To read a specified number of bytes, use file.read(n)
    - To navigate within a file use file.seek(offset, whence);
    - To get the current location, use file.tell().

## Conditionals 
several variations of how "if" is used but it all depends on testing whether a value is true or false.

if name == 'root'
  print ("do not run this utility as root")
elif name == 'guest':
  print("sorry - guests are not allowed to run this utility")
else:
  print("starting processing")
limit = sys.args[1] if len(sys.args) > 1 else 100
<br />

*The following values are **false** *
- False
- Empty collections (empty string, empty list, empty dictionary, empty set, etc.)

*short cut if else*
A?B:C

## Loops
Two kinds of loops
- While (waits for condition)
- for (iterates over a sequence (iterable)

 ### While loop
 Used for reading data, typically from a database or when waiting for user input to end a loop.
 - create a list 
 - loop over a list 
 - open text file for reading
 - loop over lines in file 
 - print line with extra newline 
 - loop "forever"
 - read input from keyboard
 - exit loop

 ### For loop
 Used to iterate through a sequence of data 
 
 
# Working With Arrays
  
  ## Lists Versus Tuples
  - use a list when you have a collection of similar objects
  - use a tuple for dissimilar objects
  
  - Tuple: element position is important
  - List: element position is not important 
  
  - use trailing comma to specify a one element tuple - eg result = 5,
  - use empty parenthese to specify empty tuple - eg result = ()

  ###Using the **for** loop to iterate through sequences
  
  for var in iterable:
    statement 
    statement
  
   The variable takes on each element in the sequence and retains the last items value in the sequence.
   To exit early use *break* statement
   To skip the remainder of the iteration and return to the top of the loop use *continue* statement
  
  ## Enumearate function *enumerate()*
  - returns an enumerate object that provides a virtual list of tuples 
  
  can use operaters and keywords for sequences 
  - **Del** deletes an entire string 
  - **In** returns True if the specified object is an element of the sequence
  - **Not in** returns True if the specified object is NOT an element of the sequence
  - **+** adds one sequence to another 
  - *  multiplies a sequence (makes a bigger sequence by repeating the original)
  
  
  ## Range() function *range()*
  - provides a virtual list of numbers
  - retruns a range object 
  - good whe you need to execute code a fixed number of times
  - slice-like parameters
  
  Syntax
  range(stop)
  range(start,stop)
  range(start,stop,step)
  
  
# Working with Dates and Times
  
  ## Python modules for dates and times 
  - Standard library 
    - datetime
    -time 
    - calendar
  - included with Anaconda
    - dateutil
    - for pasing dates from text or working with time zones
  - other
    - arrow
    - attempts to consolidate all date/time related functionality into a single, easy-to-use module
  
  ## Ways to store dates and times 
  3 ways dates and times can be stored
  - (classes) in datetime module 
    - date
    - time 
    - datetime
  - large ineger (epoch time) no. seconds since december 21 1969
  - time tuple
  
  
  
