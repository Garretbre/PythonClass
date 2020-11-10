class Car: 
	
        # public data member 
	speed = None

        # protected data member 
	_color = None
	
        # private data member 
	__weight = None
	
	# constructor 
	def __init__(self, speed, color, weight): 
		self.speed = speed 
		self._color = color
		self.__weight = weight
	
	# public member function 
	def displayPublicMembers(self): 

		# accessing public data members 
		print("Public Data Member: ", self.speed) 
		
	# protected member function 
	def _displayProtectedMembers(self): 

		# accessing protected data members 
		print("Protected Data Member: ", self._color) 
	
	# private member function 
	def __displayPrivateMembers(self): 

		# accessing private data members 
		print("Private Data Member: ", self.__weight) 

	# public member function 
	def accessPrivateMembers(self):	 
			
		# accessing private memeber function 
		self.__displayPrivateMembers() 

# derived class 
class wheels(Car): 

	# constructor 
	def __init__(self, speed, color, weight): 
				Car.__init__(self, speed, color, weight) 
			
	# public member function 
	def accessProtectedMemebers(self): 
				
				# accessing protected member functions of super class 
				self._displayProtectedMembers() 

# creating objects of the derived class	 
obj = wheels("Ferarri", 4, "Winners !") 

# calling public member functions of the class 
obj.displayPublicMembers() 
obj.accessProtectedMemebers() 
obj.accessPrivateMembers() 

# Object can access protected member 
print("Object is accessing protected member:", obj._color) 


