
import unittest

import sys
#import src
from src.user import User


class TestFuncs(unittest.TestCase):


	def test_getPassword(self):
		usr = User(3,"120.203.837"," ","password",0,"ef","ef","ef")
		self.assertEqual( usr.getPassword() , "password" )
		


		

if __name__ == '__main__':
	unittest.main()
