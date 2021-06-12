"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
"""


class Singleton:
    instances = []
    instantiation_count = 0

    def __init__(self, value):
        Singleton.instantiation_count += 1
        if Singleton.instantiation_count < 3:
            self.value = value
            self.__class__.instances.append(self)
        elif Singleton.instantiation_count & 1:
            self = self.__class__.instances[0]
        else:
            self = self.__class__.instances[1]


if __name__ == "__main__":
    obj1 = Singleton('instance1')
    obj2 = Singleton('instance2')
    obj3 = Singleton('instance3')
    obj4 = Singleton('instance4')
    print(obj1.value)
    print(obj2.value)
    print(obj3.value)
    print(obj4.value)

    print(Singleton.instances)
