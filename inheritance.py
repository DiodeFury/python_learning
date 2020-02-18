#父类与继承
class mammal:  #哺乳动物
    def walk(self):
        print("walk")


class dog(mammal):      #从mammal（父类）继承walk
    pass                #python不喜欢空类，所以加一个pass


class cat(mammal):
    pass


dog1 = dog()
dog1.walk()