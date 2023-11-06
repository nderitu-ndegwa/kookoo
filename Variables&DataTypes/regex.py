import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'cats', line, re.M|re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())