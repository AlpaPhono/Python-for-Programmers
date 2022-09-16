# Regular Expressions Special Characters and Anchors
 
## Introduction
Using **Anchors** to match the beginning or end of a string
learning about capture groups

## Example 1
>pattern = r'sta+r'<br/>
>text = 'staar'<br/>
>
>matches = re.findall(pattern, text)<br/>
>
>print(f"EXAMPLE:\n\n Pattern: {pattern}\n Text: {text}\n Matches: {matches}\n")<br/>

This example shows how the plus sign matches anythinhg on the lhs one or more times<br/>

>Matches: ['staar']

## Example 2

>pattern2 = r'st.r'<br/>
>text2 = 'staar'<br/>
>
>matches2 = re.findall(pattern2, text2)<br/>
>
>print(f"EXAMPLE2:\n\n Pattern2: {pattern2}\n Text2: {text2}\n Matches2: {matches2}\n")<br/>

This example uses the period symbol which matches any character, but only one character.<br/>
This example doesn't return any matches because there are two characters between the t and the r in the text string<br/>
> Matches2: []

## Example 3

>pattern3 = r'sta*r'<br/>
>text3 = 'str'<br/>
>
>matches3 = re.findall(pattern3, text3)<br/>
>
>print(f"EXAMPLE3:\n\n Pattern3: {pattern3}\n Text3: {text3}\n Matches3: {matches3}\n")<br/>

This example uses the * symbol. This symbol matches the LHS 0 or more times<br/>
This is why it returns a match even though there isnt an a in the text string.<br/>
>Matches3: ['str']

## Example 4

>pattern4 = r'st.+r'<br/>
>text4 = 'staar' <br/>
>
>matches4 = re.findall(pattern4, text4)<br/>
>
>print(f"EXAMPLE4:\n\n Pattern4: {pattern4}\n Text4: {text4}\n Matches4: {matches4}\n")<br/>

This returns somethinhg as opposed to example 2. The . character substiutes as an 'a' character once and the + symbol matches the lhs characters one or more times.<br/.
- if a's are removed from text4 variable there will be no matches

> Matches4: ['staar']

## Example 5

>pattern5 = r'st.*r'<br/>
>text5 = 'str'<br/>
> 
>matches5 = re.findall(pattern5, text5)<br/>
>
>print(f"EXAMPLE5:\n\n Pattern5: {pattern5}\n Text5: {text5}\n Matches5: {matches5}\n")<br/>

Returns a match.<br/>
The asterisk will match the LHS charcter zero or more times<br/>

> Matches5: ['str']

## Example 6

>pattern6 = r'sta{3}r'
>text6 = 'str star staar staaar staaaar'
>
>matches6 = re.findall(pattern6, text6)
>
>print(f"EXAMPLE6:\n\n Pattern6: {pattern6}\n Text6: {text6}\n Matches6: {matches6}\n")

This example uses the repetition quantifier to match the word in the text that contains the 'a' character 3 times.<br/>
- value in the curly brackets must be a positive integer.
- when pattern6 = r'sta{2,3}r'<br/>
    - Matches6: ['staar', 'staaar']
- if pattern6 = r'sta{0,}r'
    - all words in text will match 
    -  this quantifier means 
    -this quantifier behaves like the asterisk quantifier 
> Matches6: ['staaar']

## Example 7

>pattern7 = r'sta{0,1}r'<br/>
>text7 = 'str star staar staaar staaaar'<br/>
>
>matches7 = re.findall(pattern7, text7)<br/>
>print(f"EXAMPLE7:\n\n Pattern7: {pattern7}\n Text7: {text7}\n Matches7: {matches7}\n")<br/>

- This example uses the quantifer that means match the LH character zero or one time
- This is commonly denoted with a **'?'**

## Example 8
>pattern8 = r'a\d+'
>text8 = 'a123b a1234b a12345b'
>
>matches8 = re.findall(pattern8, text8)
>
>print(f"EXAMPLE8:\n\n Pattern8: {pattern8}\n Text8: {text8}\n Matches8: {matches8}\n")

- This example uses the digit quantifier and the plus quantifier. 
- \d matches any one digit
- + matches LHS one or many times 
- It will match every string in text8, omitting the b

> Matches8: ['a123', 'a1234', 'a12345']

- if pattern8 = r'a\d+?'
- matches8 will be a1, a1, a1
- the ? quantifier modifies the + to make it match as few as possible
<br/>
- if pattern8 = r'a\d+?b' it will match every character in text8.
- **I dont understand why** 
    - Ill come back to this later.