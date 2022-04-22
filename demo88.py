print("progra start")


class SimpleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("[simplemeta] __new__")
        print("[simplemeta] class name:", clsname)
        print("[simplemeta] 父類別:", superclasses)
        print("[simplemeta] attribute:", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

    def __call__(self, *args, **kwargs):
        print("*simplemeta*__call__")
        print("*simplemeta*", [arg for arg in args])
        return super().__call__(*args, **kwargs)





