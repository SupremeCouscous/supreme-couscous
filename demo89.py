class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("object not exist, create one")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        print("direct return")
        return cls._instances[cls]


class ATM():
    def __init__(self, currentTicket):
        self.ticket = currentTicket

    pass


class SingletonATM(metaclass=MetaSingleton):
    def __init__(self, currentTicket):
        self.ticket = currentTicket

        pass


class CarFactory():
    pass


class SingletonCarFactory(metaclass=MetaSingleton):
    pass


a1 = ATM(1)
a2 = ATM(1)
a2.ticket += 10
print(a1 == a2, a1 is a2)
print(a1.ticket, a2.ticket)
a3 = SingletonATM(1)
a4 = SingletonATM(1)
a4.ticket += 10
print(a3 is a4)
print(a3.ticket, a4.ticket)
print(hex(id(a3)), hex(id(a4)))
c1 = SingletonCarFactory()
c2 = SingletonCarFactory()
print(c1 is c2)
print(hex(id(c1)), hex(id(c2)))