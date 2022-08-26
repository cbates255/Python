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