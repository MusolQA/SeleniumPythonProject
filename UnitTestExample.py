import unittest
from Example import Example
import pytest

class MyTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")
    def setpUp(self):
        print("This will run befere method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = Example.sub(self,5,3)
        self.assertEqual(result, 2)




# if __name__ == '__main__':
#     unittest.main()
