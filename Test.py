class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def add_gender(self, gender):
        self.gender = gender
    
    def get_name(self):
        return self.name

human1 = Human("prathiksha","25")
human1.add_gender("female")

value = human1.get_name()
print(value)

# human2 = Human("Sampreeth", "27")
# human2.add_gender("male")
