
import unittest

import sys
#import src
sys.path.append("/home/ei-se/Documents/coroMail/CoroMail-CAS/src")
from user import User


class TestFuncs(unittest.TestCase):


	def test_getPassword(self):
		usr = User(3,"120.203.837"," ","password",0,"ef","ef","ef")
		self.assertEqual( usr.getPassword() , "password" )
		


		

if __name__ == '__main__':
	unittest.main()