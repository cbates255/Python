#Learning today about tuples, dictionaries, and strings

from cgi import test

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



