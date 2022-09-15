from distutils.command.build import build


def print_name(name):
    print("Name is", name)
    
print_name("Amber")

def add(num1, num2):
    return num1 + num2

print (add(1, 5))

def contact_card(name, age, car):
    return f"{name} is {age} and drives a {car}."
print(contact_card("Keith", 29, "Civic"))

def can_drive(age, legal_age = 16):
    return age >= legal_age
print(can_drive(16))

def split_name(name):
    names = name.split()
    first_name = names[0]
    last_name = names[-1]
    return(
        "First name:", first_name,
        "Lastname:", last_name
    )
print (split_name("Cal Ripken"))

def build_list(item, count = 1):
    items = []
    for i in range(count):
        items.append(item)
        return items
print(build_list("Apple", 1))



