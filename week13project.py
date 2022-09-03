#This project will create an EC2 name generator
from itertools import count
from ntpath import join
import random
import string

counter = 1
allowed = ['marketing', 'Marketing', 'Finops', 'FinOps', 'Accounting' 'finops', 'finOps', 'accounting']

how_many = int(input("How many EC2's will be created? "))
dept = input("What is your department? ")

if dept not in allowed:
    print('This generator is restricted to specified departments only. All other departments are forbidden')

else:
    while counter <= how_many:
        letters = random.choices(string.ascii_letters, k=3)
        letterlist = "".join(letters)
        numbers = random.sample(range(100, 999), k=1)
        print (dept+'-'+letterlist+str(*numbers))
        counter += 1
