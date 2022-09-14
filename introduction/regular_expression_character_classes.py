import re 

#EXAMPLE 1:

pattern = r'ab'
text = 'bac acb'

matches = re.findall(pattern, text)

print(f"#EXAMPLE 1:\n\nPattern: {pattern}\nText: {text}\nMatches: {matches}\n")

##########################

