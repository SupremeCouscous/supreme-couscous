class SingletonParent(object):
    _instance = None

    def __init__(self):
        print("[parent]init is called")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("[parent], really new a instance")
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonATM(SingletonParent):
    pass


s1 = SingletonATM()
s2 = SingletonATM()
s3 = SingletonATM()
s4 = SingletonATM()
s5 = SingletonATM()
print(s1 is s2)