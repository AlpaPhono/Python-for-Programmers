# Modules 
A module is a file containing python definitions and statements that can be called upon in another python file.<br/>
The file name is the module name with the suffix .py<br/>
- To use a module named spam.py you would type *import spam.py*
    - Doing this would allow you to use the module name to get acess to the functions or other attributes.
- pyhton classes are also implimented as modules 

## Using Import 
- The import statement imports modules 
- Three variations 
    - import module 
    - from module improt functionn-list 
    - from module improt * (use with caution)

### Import module
Loads the module so that its data and functions can be used. but does not put its attributes (names of classes,functions and variables) into the current name space.<br/>
<br/>
When trying to use a function or class from an import like this you must first reference the module.

**Example**
<br/>
![Import module](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/importmodule.png)

### From module import function
Imports only the function(s) specified into the current namespace. Other functions are not available.
![From module import function](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/frommoduleimportfunction.png)

- you can also alias functions that you import as something else. e.g form samplelib import spam as pig, ham as hog

### From module import *
- Loads the module and imports all the functions that do not start wiht an underscore into the current namespace<br/>
- Should be used with caution as it can overwrite built in attributes or attributes from a different module that share the same name.

## Module search path
When specifying a module to load with the import statement, it first looks in the current directory and then searches the directories listed in sys.path<br/>
Directories can be added to the sys.path by adding them to the PYTHONPATH environment variable.

![Setting python path for windows](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/windowspath.png)

![Setting python path for Linux/OSX](https://github.com/AlpaPhono/Python-for-Programmers/blob/main/image_resource/linuxpath.png)

## Executing modules as scripts

*I dont understand this section of the video*
