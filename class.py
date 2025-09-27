class Hello:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def get_name(self):
        return self.name
    def get_height(self):
        return self.height



person = Hello("Alex", 190)
print(person.get_name())
print(person.get_height())