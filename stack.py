class stack:
	data=[]
	top=-1
	size=10
	def _init_(self,size):
		self.data=[]
		self.top=-1
		self.size=size

	def _push(self,item):
		if self.top>=self.size-1:
			return ("Size Limit increased")
		self.data.append(item)
		self.top+=1
		return self.data[self.top]
		
	def _pop(self):
		if self.top<=-1:
			return ("Stack Empty")
		poped_ele=self.data[self.top]
		self.data.pop()
		self.top-=1
		return poped_ele

	def _peek(self):
		if self.top==-1:
			return "No element at peek"
		return self.data[self.top]


