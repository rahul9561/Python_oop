class test :
    v=10 #thsi is static variable
    def testMethod(self,a):
        print(self.v,a)
    def testMethod2(b,a):
        print(b,a)
    @staticmethod
    def staticImprove():
        print(test.v)


obj1 = test()
print(test.v)
obj1.testMethod(12)
# antoher method
obj2 = test
obj2.testMethod2(1,2)
obj1.staticImprove()
obj1.staticImprove()
print(obj1.v)
print(obj2.v)
test.staticImprove()

# INSTANCE VARIABLE are defined inside the init method using self keyword
# now we cannot acess the variable using just the class name without using any object 
