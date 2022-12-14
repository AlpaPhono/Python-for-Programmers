# Functions 
> A way of isolating code that is needed in more than one place.
> They are defined with the def statement.
> Can return one object of any type, using the return statement. If there is no return statement the function returns "None"

## Example
def say_hello():<br/>
    print('hello, world')<br/>
    print()<br/>
...<br/>
...<br/>
hello = say_hello()<br/>
hello, world<br/>
> This example is to show that variables can hold functions.
>This variable is of the type **None** because the function has no return statement.

## Example 
def get_hello():<br/>
    return 'Hello, world'<br/>
...<br/>
...<br/>
hello = get_hello()<br/>
print(hello)<br/>
'Hello, world'<br/>
>This variable hello in this example is of the type string because the return statement of the function is a string.

# Function Parameters 
- can be required or optional
- can be postional or named
    - A positional argument can just have a value entered when the function is called
    - A named argument needs to have the argument assigned to a value when the function is called.
    - Positional: def spam(greeting):<br/>
                        print(greeting)<br/>
                spam(hello)
    - Named: def spam(*,greeting):
                    print(greeting)<br/>
                spam(greeting=hello)
![arguement breakdown](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/breakdown.png)

## Examples 
![function 1](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/fun1.png)
example of basic function with no arguments<br/>
![function 2](~\image_resource\fun2.png)
<br/>
![function 3](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/fun3.png)
example of function with default required arguement<br/>
![function 4](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/fun4.png)
example of function with required and optional arguements<br/>
![function 5](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/fun5.png)
example of a function with keyword only parameters<br/>
It can be called with no parameters as it doesnt have any required parameters in its function definition.<br/>

**function 6**<br/>
def fun_6(**named_args):<br/>
    print("fun_six():")<br/>
    for named in named_args:<br/>
        print(name, "==> ", named_args[name])<br/>
...<br/>
...<br/>
fun_six(name="lancelot", quest="grail", colour="red")
fun_six():
name ==> lancelot
quest ==> grail
colour ==> red

Example uses keyword named parameters<br/>
This function is also capable of returning a dictionary of all the named arguements<br/>
def fun_6(**named_args):
    print(named_args)
    print(type(named_args))
...<br/>
...<br/>
fun_six(name="lancelot", quest="grail", colour="red")<br/>
{'name':'lancelot', 'quest':'grail', 'colour','red'}<br/>
<class 'dict'> <br/>

# Default Parameters 
Required parameters can have defaults, assigned with equals sign<br/>
Parameters without defaults cannot be specified after parameters with defaults<br/>

## Examples
![positional and named functions](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/posnamedfun.png)

# Name resolution (AKA SCOPE)
A scope is an area within a python program where an unqualified name can be looked up.<br/>
There are four nested scopes that are searched for names in the following order<br/>
- Local: local names bound within a function
- Nonlocal: local names plus local names of outer function(s)
- Global: the current module's global names
- Builtin: built-in functions (contents of _builtins_module)

## Example

![Scope Example](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/scope.png)