peoplelist = []

class people:
    
    def __init__(self, name, length, gender):
        self.name = name
        self.length = len(name)
        self.gender = gender
        peoplelist.append(self.name)
        
    def too_long(self):
        if self.length > 4:
            print (self.name+"'s", 'name is too long.')
        else:
            print (self.name+"'s", 'name is not too long.')
            
    def alivein80(self, age):
        if age + 80 > 90:
            print (self.name, 'will probably be dead in 80 years.')
        else:
            print (self.name, 'will be probably be alive in 80 years.')

troy = people('Troy', 0, 'male')
shannon = people('Shannon', 0, 'female')

troy.too_long()
shannon.too_long()

troy.alivein80(11)
shannon.alivein80(10)

print(sorted(peoplelist))

username = input('Write your name:')
usergender = input('Write your gender:')
userage = input('Write your age:')

user = people(username, 0, usergender)

user.alivein80(int(userage))
