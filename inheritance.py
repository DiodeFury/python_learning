#父类与继承
class mammal:  #哺乳动物
    def walk(self):
        print("walk")


class dog(mammal):      #从mammal（父类）继承walk
    #pass                当类为空时，python不喜欢空类，所以加一个pass
    def bark (self):
        print("wangwangwang")


class cat(mammal):
    #pass
    def miao(self):
        print("miaomiaomiao")


dog1 = dog()
dog1.bark()
cat2=cat()
cat2.miao()