#This project will create an EC2 name generator
from itertools import count
from ntpath import join
import random
import string

counter = 1

letters = random.choices(string.ascii_letters, k=3)
letterlist = "".join(letters)
numbers = random.sample(range(100, 999), k=1)

how_many = int(input("How many EC2's will be created? "))
dept = input("What is your department? ")

while counter <= how_many:
    print(dept+'-'+letterlist+numbers)
    counter += 1
