#
# Example file for working with classes
#

# Python and Javascript can both write in procedural and object-oriented

# self - this keyword
# usually is the first parameter in methods


class myClass():
    def method1(self):
        print("myClass method")

    def method2(self, someString):
        print("myClass method2 " + someString)


class anotherClass(myClass):  # INHERITANCE
    def method1(self):
        print("anotherclass method")
        myClass.method1(self)  # INVOKING METHOD OF THE PARENT CLASS

    def method2(self, someString):
        print("naotherClass " + someString)
        myClass.method2(self, "another Class" + someString)


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string in method2")


if __name__ == "__main__":
    main()
