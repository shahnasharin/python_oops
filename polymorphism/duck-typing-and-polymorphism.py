#-----------------------------------Duck Typing and Polymorphism------------------------------------


class Bird:
    def sound(self):
        pass

class Duck(Bird):
    def sound(self):
        return "Quack!"

class Crow(Bird):
    def sound(self):
        return "Caw!"

def bird_call(bird):
    return bird.sound()

duck = Duck()
crow = Crow()

print(bird_call(duck))  # Output: Quack!
print(bird_call(crow))  # Output: Caw!
