import re 

pattern = r'sta+r'
text = 'staar'

matches = re.findall(pattern, text)

print(f"EXAMPLE:\n\n Pattern: {pattern}\n Text: {text}\n Matches: {matches}\n")