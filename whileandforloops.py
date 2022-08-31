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