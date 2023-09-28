import time


class dog:
    age = 20
    def __init__(self):
        print("dog created")

dog1 = dog()
dog2 = dog()

print(dog1.age)
print(dog2.age)
dog1.age = 50
print(dog1.age)
print(dog2.age)
dog.age = 50
print(dog1.age)
print(dog2.age)