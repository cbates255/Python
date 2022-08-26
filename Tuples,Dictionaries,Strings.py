#Learning today about tuples, dictionaries, and strings

from cgi import test
from curses.ascii import isdigit
from re import template

#Working with tuples and lists
testlist = [1, 2, 3, 4, 5]
testtuple = (testlist, "Amber", "Owen", "Addy", "Noah")
print(testlist)
print(testtuple)

testlist[0] = 10
print(testtuple)
testlist.extend(range(20,25))
print(testlist)

#Now going to practice some dictionaries (key and value)
favcolors = {"chad": "blue", "chris": "red", "don": "green"}
print(favcolors["chad"])
print("chris" in favcolors)
favcolors["larry"] = "orange"
print(list(favcolors.keys()))
print(list(favcolors.values()))

mensgroup = list(favcolors.keys())
print(mensgroup)
colorsgroup = list(favcolors.values())
print(colorsgroup)

#Now doing some work with strings
sample_string = "football"
print(sample_string.capitalize())
print(sample_string.upper())
print(sample_string.isupper())
print(sample_string == "football")

url = "http://www.testing.com/users/dave"
users = url.split("/")[-1]
print(users)

lines = ['first line', 'second line', 'third line']
output = '\n'.join(lines)
print(output)

#Formatting a string. Super cool.
template = "Hello my name is {}, and I really enjoy {}, have a great day."
print(template.format('Chad', 'Python'))
