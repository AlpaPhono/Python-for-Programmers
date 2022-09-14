# Regular Expression Character Classes 

## Introduction 
A **regular expression** is a tool for matching patterns in text. <br/>
Useful for filtering, reporting and validating textual data.<br/>
Can be used to find and replace subsets of a piece of text.<br/>

## Example 1

>pattern = r'ab'
>text = 'bac acb'
>
>matches = re.findall(pattern, text)

print(f"#EXAMPLE 1:\n\nPattern: {pattern}\nText: {text}\nMatches: {matches}\n")
- line 1 imports the regular expressions module
- Two variables (line 5 and 6) are declaired called pattern and text
    - r'ab'  The r with text within a single quote signifies a raw string. Everything within the quotes will be taken as a literial string.
- line 8 uses the variables and the findall method from the re module to create a list for strings that match the pattern
    - returns a list of non-overlapping matches in a string,
    - findall(pattern: str | Pattern[str], string: str, flags: _FlagsType = ...) -> list (python)

- If text variable is changed to 'bac acb'  the matches variable will return an empty list []