# Regular Expression Character Classes 

## Introduction 
A **regular expression** is a tool for matching patterns in text. <br/>
Useful for filtering, reporting and validating textual data.<br/>
Can be used to find and replace subsets of a piece of text.<br/>

## Example 1
>import re <br/>
>pattern = r'ab' <br/>
>text = 'bac acb'<br/>
>
>matches = re.findall(pattern, text)<br/>
>
>print(f"#EXAMPLE 1:\n\nPattern: {pattern}\nText: {text}\nMatches: {matches}\n")<br/>

- line 1 imports the regular expressions module
- Two variables (line 5 and 6) are declaired called pattern and text
    - r'ab'  The r with text within a single quote signifies a raw string. Everything within the quotes will be taken as a literial string.
- line 8 uses the variables and the findall method from the re module to create a list for strings that match the pattern
    - returns a list of non-overlapping matches in a string,
    - findall(pattern: str | Pattern[str], string: str, flags: _FlagsType = ...) -> list (python)

- If text variable is changed to 'bac acb'  the matches variable will return an empty list []

## Example 2
>pattern2 = r'.'<br/>
>text2 = 'abcdef'<br/>
>
>matches2 = re.findall(pattern2,text2)<br/>
>
>print(f"#EXAMPLE 2:\n\nPattern2: {pattern2}\nText2: {text2}\nMatches2: {matches2}\n")<br/>

This example has the pattern2 variable assigned to r'.'
- The period '.' charcter class will match any single character. <br/>
- The preriod is usually used along side a quantifier or other regular expression elements to do something more complex.

matches2 return: ['a', 'b', 'c', 'd', 'e', 'f']

## Example 3
>pattern3 = r'\d'<br/>
>text3 = 'FirstWord 1 LastWord'<br/>
>
>matches3 = re.findall(pattern3, text3)<br/>
>
>print(f"#EXAMPLE 3:\n\nPattern3: {pattern3}\nText3: {text3}\nMatches3: {matches3}\n")<br/>
This example is to show the utility of the r'/d' character class. which matches a single digit.<br/>

matches 3 will return: Matches3: ['1']

## Example 4
>pattern4 = r'\D'<br/>
>text4 = 'FirstWord 1 LastWord'<br/>
>
>matches4 = re.findall(pattern4, text4)<br>
>
>print(f"#EXAMPLE 4:\n\nPattern4: {pattern4}\nText4: {text4}\nMatches4: {matches4}\n")<br>

This example illustrates the power of the r'\D' character class. It is used to match any non digit characters.<br/>
It is the opposite of the r'\d'.<br/> 
It also includes the white spaces in the matches list<br/>

Matches4: ['F', 'i', 'r', 's', 't', 'W', 'o', 'r', 'd', ' ', ' ', 'L', 'a', 's', 't', 'W', 'o', 'r', 'd']

## Example 5
>pattern5 = r'\w' <br/>
>text5 = 'FrirstWord 1 LastWord'<br/>
>
>matches5 = re.findall(pattern5, text5)<br/>
>
>print(f"#EXAMPLE 5:\n\nPattern5: {pattern5}\nText5: {text5}\nMatches5: {matches5}\n")<br/>

<br/>This example shows that the 'w' character classes matches any *"word charcters"*<br/>
Word charcters are defined by ASCII charcter encoding<br/>

Matches5: ['F', 'r', 'i', 'r', 's', 't', 'W', 'o', 'r', 'd', '1', 'L', 'a', 's', 't', 'W', 'o', 'r', 'd']

## Example 6
>pattern6 = r'\s'<br/>
>text6 = 'FirstWord 1 LastWord'<br/>
>
>matches6 = re.findall(pattern6, text6)<br/>
>
>print(f"EXERCISE 6:\n\nPattern6: {pattern6}\nText6: {text6}\nMatches6: {matches6}\n")<br/>

<br/>This example is made to illustrate that the '\s' character class will only match white spaces.<br/>

Matches6: [' ', ' ']
-----
The previous examples have been focused on mathing single characters.<br/>
Whole strings can be matched as well.<br/>
To match strings you will have to use a feature of regular expressions called **Quantifiers** or "special Characters"
**The plus Quantifer (+)**
- Matches the preceding regular expression (lefthand) one or more times.

## Example 7
>pattern7 = r'\w+'
>text7 = 'FirstWord 1 LastWord'<br/>
>
>matches7 = re.findall(pattern7, text7)<br/>
>
>print(f"EXERCISE 7:\n\nPattern7: {pattern7}\nText7: {text7}\nMatches7: {matches7}\n")<br/>

The combination of the word character class with the plus symbol quantifier will match one or more word charcters.
- The word charcter class defines the type of charcter you want to match
- the plus symbol says taht you want to match one or more of that character.<br/>

Matches7: ['FirstWord', '1', 'LastWord']

## Example 8




