# # keyword arguments by parameters
# def positional_argu(name, roll): 
# 	print(name, roll, sep=' | ')
# positional_argu(name='forhad', roll=5088) # arguments

# # positional arguments without parameters
# def positional_argu(name, roll): 
# 	print(name, roll, sep=' | ')
# positional_argu('forhad', 5088)

# # arbitrary number of arguments with positional arguments
# def positional_argu(name, *other_name): # *other_name get & shows result in tuple format
# 	print(name, other_name, sep=' | ')
# positional_argu('forhad', 'israfil', 'tuhin', 'raset')

# # arbitrary number of arguments with keyword arguments
# def positional_argu(name, **other_name):             # **other_name get & shows result in dictionary format
# 	print(name, other_name)
# positional_argu(name='forhad', second_name='israfil', third_name='tuhin', others_name='raset') # pass argu with key must
# # can be written in both positional and keyword arguments,here only for 1st parameter is positional
# positional_argu('forhad', second_name='israfil', third_name='tuhin', others_name='raset') # pass argu with key must

class A:

	def __init__(self, a, b): # constructor/magic method, pre-define & auto called
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a * self.b

class B(A):
	def __init__(self, a, b):
		# A.__init__(self, a, b)
		super().__init__( a, b) # line 37,38 same called parent class function
		self.a = a
		self.b = b


	def sub(self):
		return self.a - self.b

# In the above example, we have called parent class function as:
# Person.__init__(self, student_name, student_age) 
# We can replace this with python super function call as below.
# super().__init__(student_name, student_age)

# r = A(7,8)
# print(r)
# temp = r.add()
# print(temp)
# temp1 = r.mul()
# print(temp1)

r1 = B(55,5)
temp2 = r1.sub()
print(temp2)
temp3 = r1.mul()
print(temp3)


# Polymorphic Classes
# class Shark():
#     def swim(self):
#         print("The shark is swimming.")
#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")
#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")
# class Clownfish():
#     def swim(self):
#         print("The clownfish is swimming.")
#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")
#     def skeleton(self):
#         print("The clownfish's skeleton is made of bon