#-------------------------using protected variable-----------------

class MyClass:
    def __init__(self):
        self._protected_var = 10  # Protected variable (name mangling)

    def print_protected_var(self):
        print(self._protected_var)

class MySubclass(MyClass):
    def __init__(self):
        super().__init__()

    def modify_protected_var(self, new_value):
        self._protected_var = new_value

obj = MySubclass()

# Accessing and modifying protected variable.
obj.print_protected_var()     # Output: 10
obj.modify_protected_var(20)
obj.print_protected_var()     # Output: 20
