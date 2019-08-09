import unittest
from stack import stack
s=stack()
class Test_stack(unittest.TestCase):
	def test_check_overflow(self):
		if s.top>=s.size-1:
			self.assertEqual(s._push(2),"Size Limit 							increased")

	def test_check_underflow(self):
		if s.top<=-1:
			self.assertEquals(s._pop(),"Stack Empty")
		
	def test_peek_returns_element_at_top(self):
		s._push(3)
		self.assertEqual(s._peek(),3)
		if s.top==-1:
			self.assertEqual(s._peek(),"No element at peek")

	def test_pop_deletes_top_element(self):
		self.assertEqual(s._peek(),s._pop())
		
	def test_push_enters_element_in_stack(self):
		self.assertEquals(s._push(4),s._peek())




if __name__ == '__main__': 
    unittest.main()
