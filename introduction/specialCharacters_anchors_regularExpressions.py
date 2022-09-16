import re 

pattern = r'sta+r'
text = 'staar'

matches = re.findall(pattern, text)

print(f"EXAMPLE:\n\n Pattern: {pattern}\n Text: {text}\n Matches: {matches}\n")

#######
# EXAMPLE 2

pattern2 = r'st.r'
text2 = 'staar'

matches2 = re.findall(pattern2, text2)

print(f"EXAMPLE2:\n\n Pattern2: {pattern2}\n Text2: {text2}\n Matches2: {matches2}\n")

####################

# EXAMPLE 3

pattern3 = r'sta*r'
text3 = 'str'

matches3 = re.findall(pattern3, text3)

print(f"EXAMPLE3:\n\n Pattern3: {pattern3}\n Text3: {text3}\n Matches3: {matches3}\n")

#########

# EXAMPLE 4

pattern4 = r'st.+r'
text4 = 'staar' 

matches4 = re.findall(pattern4, text4)

print(f"EXAMPLE4:\n\n Pattern4: {pattern4}\n Text4: {text4}\n Matches4: {matches4}\n")

#########

# EXAMPLE 5

pattern5 = r'st.*r'
text5 = 'str'
 
matches5 = re.findall(pattern5, text5)

print(f"EXAMPLE5:\n\n Pattern5: {pattern5}\n Text5: {text5}\n Matches5: {matches5}\n")

#################

# EXAMPLE 6
pattern6 = r'sta{2,3}r'
text6 = 'str star staar staaar staaaar'

matches6 = re.findall(pattern6, text6)

print(f"EXAMPLE6:\n\n Pattern6: {pattern6}\n Text6: {text6}\n Matches6: {matches6}\n")

#################

# EXAMPLE 7
pattern7 = r'sta{0,1}r'
text7 = 'str star staar staaar staaaar'

matches7 = re.findall(pattern7, text7)

print(f"EXAMPLE7:\n\n Pattern7: {pattern7}\n Text7: {text7}\n Matches7: {matches7}\n")

#############

# EXAMPLE 8

pattern8 = r'a\d+?b'
text8 = 'a123b a1234b a12345b'

matches8 = re.findall(pattern8, text8)

print(f"EXAMPLE8:\n\n Pattern8: {pattern8}\n Text8: {text8}\n Matches8: {matches8}\n")




