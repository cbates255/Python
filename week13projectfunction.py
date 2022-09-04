#A function for the week 13 project.
import random
import string

def ec2_name_gen(how_many, dept,):
    counter = 1
    allowed = ['marketing', 'Marketing', 'Finops', 'FinOps', 'Accounting' 'finops', 'finOps', 'accounting']
    if dept not in allowed:
            print('This generator is restricted to specified departments only. All other departments are forbidden')
    else:
        while counter <= how_many:
            letters = random.choices(string.ascii_letters, k=3)
            letterlist = "".join(letters)
            numbers = random.sample(range(100, 999), k=1)
            print (dept.title()+'-'+letterlist+str(*numbers))
            counter += 1
            
ec2_name_gen(3, 'marketing')