#class_method

class Person():
    kind = "human"

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return  self.kind

a = Person()
print(a.kind)
b = Person
print(b.kind)