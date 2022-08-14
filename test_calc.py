import unittest
import calc

# Creating a class and inheriting from unittest.TestCase
# we now have assert stuff
class TestCalc(unittest.TestCase):
	# Method needs to start with test_ (needs to start with test)
    # Otherwise it will say "0 tests ran"
	def test_add(self):
		self.assertEqual(calc.add(10, 5), 15, 'Wrong answer')
		self.assertEqual(calc.add(-1, -1), -2, 'Wrong answer')
		self.assertEqual(calc.add(-1, 1), 0, 'Wrong answer')

	def test_subtract(self):
		self.assertEqual(calc.subtract(10, 5), 5, 'Wrong answer')
		self.assertEqual(calc.subtract(-1, -1), 0, 'Wrong answer')
		self.assertEqual(calc.subtract(-1, 1), -2, 'Wrong answer')



if __name__ == "__main__": # If we say this name we should run this thing directly
    unittest.main()
