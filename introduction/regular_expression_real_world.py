import re 

# Exercise 1

pattern = r'\d(?=c).'
text = 'a1 b2 3c 4d'

matches = re.findall(pattern, text)

print(f"EXERCISE: 1\n\n Pattern: {pattern}\n Text: {text}\n Matches: {matches}")