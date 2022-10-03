# Functions 
> A way of isolating code that is needed in more than one place.
> They are defined with the def statement.
> Can return one object of any type, using the return statement. If there is no return statement the function returns "None"

## Example
def say_hello():
    print('hello, world')
    print()
...<br/>
...<br/>
hello = say_hello()<br/>
hello, world<br/>
> This example is to show that variables can hold functions.
>This variable is of the type **None** because the function has no return statement.

## Example 
def get_hello():
    return 'Hello, world'
...<br/>
...<br/>
hello = get_hello()<br/>
print(hello)<br/>
'Hello, world'<br/>
>This variable hello in this example is of the type string because the return statement of the function is a string.

# Function Parameters 
- can be required or optional
- can be postional or named
[arguement breakdown]

## Examples 
![function 1](Python-for-Programmers\image_resource\fun1.png)
example of basic function with no arguments<br/>
![function 2](Python-for-Programmers\image_resource\fun2.png)
<br/>
![function 3](Python-for-Programmers\image_resource\fun3.png)
example of function with default required arguement<br/>
![function 4](Python-for-Programmers\image_resource\fun4.png)
example of function with required and optional arguements<br/>
![function 5](Python-for-Programmers\image_resource\fun5.png)
example of a function with only keyword only parameters<br/>