# name = input()
# print(f"Hello, {name}") #format string returns what's typed into input
#---------------------------------------------------------------
# #integer type
# i = 28
# print(f"i is {i}")

# #float type
# f = 2.8
# print(f"f is {f}")

# #boolean type
# b = True 
# print(f"b is {b}")

# #none type
# n = None
# print(f"n is {n}")
#---------------------------------------------------------------
# x = 25

# if x > 0:
#     print("x is positive")
#     if x > 22:
#         print("banana")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is zero")
#---------------------------------------------------------------
# name = "Brandy" # python string variable
# coordinates = (10.0, 20.0) # python tupple - grouping values together in a single name
# names = ["Brandy", "Theo", "Karma"] # python list (like an array)
#-------------------------------------------------------------
### Lists
# names = ["Brandy", "Theo", "Karma"]
# for name in names: #for every value(name) in names list
#     print(name) #print each value(name)
#-------------------------------------------------------------
### Sets
# s = set() 
# s.add(1)
# s.add(3)
# s.add(5)
# s.add(3)
# print(s) #returns {1,3,5}
#-------------------------------------------------------------
### Dictionaries
# ages = {"Alice":22, "Brandy":23, "Austin":24}
# ages["Donald"]=18
# ages["Brandy"] += 1 #increase its value by 1 (24)

# print(ages)
#-------------------------------------------------------------
### Functions
# def square(x):
#     return x * x
# for i in range(10):
#     print("{} squared is {}".format(i,  square(i))) #i squared is square(i)
#-------------------------------------------------------------
### Classes
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(3,5)
# print(p.x)
# print(p.y)