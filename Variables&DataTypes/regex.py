"""
#Using the re.match function example
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'cats', line, re.M|re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())
"""
#Using the re.search function example
import re
line = "Cats are smarter than dogs"
matchObj = re.search(r'dogs', line, re.M|re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())