#Using the re.match function example
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'cats', line, re.M|re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())

#Using the re.search function example
import re
line = "Cats are smarter than dogs"
matchObj = re.search(r'dogs', line, re.M|re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.group())


#Using re.findall function example
import re
string = "Python is fun, but it is also cool"
obj = re.findall(r'\w*', string)
print(obj)


#Using the re.sub function example
import re
string = "Python is fun, but it is also cool"
obj = re.sub(r'Python', 'Java', string)
print(obj)


#Using the re.compile function example
import re
string = "Python is fun, but it is also cool"
pattern = re.compile(r'Python')
obj = pattern.match(string)
obj = pattern.search(string)
print(obj.start(), obj.end())

obj = pattern.findall(string)
print(obj)

obj = pattern.sub('Java', string)
print(obj)


#Using the re.finditer function example
import re
string = "Python is fun, but it is also cool"
pattern = re.compile(r'is')
iterator = pattern.finditer(string)
for obj in iterator:
    print(obj.start(), obj.end())
    print(obj.group())
print(iterator)

for match in iterator:
    print(match.span())
