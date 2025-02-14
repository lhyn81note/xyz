
class baseclass():

    x='init'

    def __init__(self,y) -> None:
        self.x = y
    

# d1=baseclass(5)
# d2=baseclass(10)
# print(baseclass.abc())
# print(d1.abc())

# baseclass.x='abc'
# print("#######")
# print(d1.x)
# print(d2.x)

# d1.x='d1'
# print("#######")
# print(d1.x)
# print(d2.x)

# baseclass.x='???'
# print("#######")
# print(d1.x)
# print(d2.x)

# d2.x='!!!'
# print("#######")
# print(d1.x)
# print(d2.x)

# baseclass.x='???'
# print("#######")
# print(d1.x)
# print(d2.x)

class C1(baseclass):
    def __init__(self, y) -> None:
        super().__init__(y)

class C2(baseclass):
    def __init__(self, y) -> None:
        super().__init__(y)


c1=C1(2)
c2=C2(3)
c1.x=100
print(c1.x)
print(c2.x)