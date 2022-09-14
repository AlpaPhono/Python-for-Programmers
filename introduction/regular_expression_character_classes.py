import re 

#EXAMPLE 1:

pattern = r'ab'
text = 'bac acb'

matches = re.findall(pattern, text)

print(f"#EXAMPLE 1:\n\nPattern: {pattern}\nText: {text}\nMatches: {matches}\n")

##########################

#EXAMPLE 2:

pattern2 = r'.'
text2 = 'abcdef'

matches2 = re.findall(pattern2,text2)

print(f"#EXAMPLE 2:\n\nPattern2: {pattern2}\nText2: {text2}\nMatches2: {matches2}\n")

#################################

#EXAMPLE 3:

pattern3 = r'\d'
text3 = 'FirstWord 1 LastWord'

matches3 = re.findall(pattern3, text3)

print(f"#EXAMPLE 3:\n\nPattern3: {pattern3}\nText3: {text3}\nMatches3: {matches3}\n")

################################

#EXAMPLE 4:

pattern4 = r'\D'
text4 = 'FirstWord 1 LastWord'

matches4 = re.findall(pattern4, text4)

print(f"#EXAMPLE 4:\n\nPattern4: {pattern4}\nText4: {text4}\nMatches4: {matches4}\n")

##############################

#Example 5:

pattern5 = r'\w'
text5 = 'FrirstWord 1 LastWord'

matches5 = re.findall(pattern5, text5)

print(f"#EXAMPLE 5:\n\nPattern5: {pattern5}\nText5: {text5}\nMatches5: {matches5}\n")

##############

#Example 6:

pattern6 = r'\s'
text6 = 'FirstWord 1 LastWord'

matches6 = re.findall(pattern6, text6)

print(f"EXERCISE 6:\n\nPattern6: {pattern6}\nText6: {text6}\nMatches6: {matches6}\n")

##########

#Example 7:

pattern7 = r'\w+'
text7 = 'FirstWord 1 LastWord'

matches7 = re.findall(pattern7, text7)

print(f"EXERCISE 7:\n\nPattern7: {pattern7}\nText7: {text7}\nMatches7: {matches7}\n")

###############

#EXERCISE 8:

pattern8 = r'[4-6]'
text8 = 123456789

matches8 = re.findall(pattern8, text8)

print(f"EXERCISE 8:\n\nPattern8: {pattern8}\nText8: {text8}\nMatches8: {matches8}\n")














