import re
text = ''' 101 COM PythonPart1
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''
s = re.findall('\d+\d',text)
print(s)