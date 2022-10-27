import re
txt1 = 'Life is too short, you need python'
txt2 = 'The best moments of my life'
print(re.search('Life',txt1))
print(re.search('Life',txt2))
match = re.search('Life',txt1)
print(match.group())