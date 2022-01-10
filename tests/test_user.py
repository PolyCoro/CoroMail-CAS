
import unittest

import sys
sys.path.append("/home/deac/workworkwork/CoroMail-CAS/src")
from user import User


class TestFuncs(unittest.TestCase):


	def test_getPassword(self):
		usr = User("Pierre","password","127.0.0.2","abcde")
		self.assertEqual( usr.getPassword() , "password" )
		usr = User("Pierre","","127.0.0.2","")
		self.assertEqual( usr.getPassword() , "" )
		usr = User("Pierre","test_mdp_@Véc $df","127.0.0.2","5&mA^")
		self.assertEqual( usr.getPassword() , "test_mdp_@Véc $df" )

	def test_getKey(self):
		usr = User("Pierre","password","127.0.0.2","abcde")
		self.assertEqual( usr.getKey() , "abcde" )
		usr = User("Pierre","password","127.0.0.2","")
		self.assertEqual( usr.getKey() , "" )
		usr = User("Pierre","password","127.0.0.2","5&mA^")
		self.assertEqual( usr.getKey() , "5&mA^" )
	
	def test_getIP(self):
		usr = User("Pierre","password","127.0.0.2","abcde")
		self.assertEqual( usr.getIP() , "127.0.0.2" )
		usr = User("Pierre","password","","54875")
		self.assertEqual( usr.getIP() , "" )
		usr = User("Pierre","password","194.0.0.1","5&mA^")
		self.assertEqual( usr.getIP() , "194.0.0.1" )	
		

if __name__ == '__main__':
	unittest.main()