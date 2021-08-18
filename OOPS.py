#Single Inheritance
# class parent:
#     def func1(self):
#         print("This is function from parent class.")

# class child(parent):
#     def func2(self):
#         print("This is function from child class")
# p1=parent()
# p2=child()
# p1.func1()
# #p1.func2() >Base class or parent class cannot access methods and variables from child or derived class
# p2.func1()
# p2.func2()

#Multiple Inheritance
# class parent1:
#     def func1(self):
#         print("This is first parent class")
# class parent2:
#     def func2(self):
#         print("This is second parent class")
# class child(parent1, parent2):
#     def func3(self):
#         print("This is child inheriting properties from first and second parent")

# c1=child()
# c1.func1()
# c1.func2()
# c1.func3()

#Multilevel Inheritance
# class first:
#     def func1(self):
#         print("This is the topmost class.")
# class second(first):
#     def func2(self):
#         print("This is the mid level class")
# class child(second):
#     def func3(self):
#         print("This child class in multilevel inheritance")
# c1=child()
# c1.func1()
# c1.func2()
# c1.func3()

#Hierarchical Inheritance
# class base:
#     def func(self):
#         print("This is the base class for hierarchical inheritance")
# class child1(base):
#     def func1(self):
#         print("This is the 1st child class")
# class child2(base):
#     def func2(self):
#         print("This is the 2nd child class")
# class child3(base):
#     def func3(self):
#         print("This is the 3rd child class.")
# c1=child1()
# c1.func()
# c1.func1()
#c1.func2() A derived class cannot access methods and variables of another child class inheriting from same parent class.
#c1.func3()
# c2=child2()
# c3=child3()
# c2.func()
# c2.func2()
# c3.func()
# c3.func3()

#Method Overriding

# class A:
#     def __init__(self):
#         print("This is class A")
    
#     def fxn(self):
#         print("This is fxn of class A")

# class B(A):
#     def __init__(self):
#         print("This is class B")
    
#     def fxn(self):
#         print("This is fxn of class B")

# class C(B):
#     def __init__(self):
#         print("This is class C")
#         super().__init__()

# a=A()
# a.fxn()
# b=B()
# b.fxn()
# c=C()

#OUTPUT

# This is class A
# This is fxn of class A
# This is class B
# This is fxn of class B
# This is class C
# This is class B

#Method Overloading

# class alpha:
#     def adder(self,a,b):
#         return a+b
#     def adder(self, a,b,c):
#         return a+b+c

# c1=alpha()
# #print(c1.adder(2,3)) Python does not solve method overloading, by default last defined function is called!
# print(c1.adder(2,3,4))

#Output

#9

#Threading

# import threading
# import time

# def fxn_one():
#     print("This is first fxn")
#     time.sleep(1)
#     print("Done for 1st fxn")
# def fxn_two():
#     print("This is second fxn")
#     time.sleep(2)
#     print("Done for 2nd fxn")
    
#in case your fxn takes arguments, use threading.Thread(target=functionname, args=(x,))
# t1=threading.Thread(target=fxn_one)
# t2=threading.Thread(target=fxn_two)

# t1.start()
# t2.start()

#Output
# This is first fxn
# This is second fxn
# Done for 1st fxn
# Done for 2nd fxn


###########