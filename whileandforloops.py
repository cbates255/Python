from itertools import count


count = 1
while count < 5:
    print("Looping...")
    count += 1
    
test_list = [1, 2, 3, 4, 5]
for number in test_list:
    print(number * 5)
    
colors = ["red", "blue", "purple", "green", "yellow", "orange"]
for color in colors:
    print (color, "is a color.")
    
for color in colors:
    if color == "red":
        continue
    elif color == "blue":
        print(color)
    elif color == "purple":
        break
    
for i in range(10):
    print("Repeating")

upper_number = int(input("How many numbers to input: "))
for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3:
        print("Fizz")
    elif number % 5:
        print("Buzz")
    else:
        print("Number")
    


    
