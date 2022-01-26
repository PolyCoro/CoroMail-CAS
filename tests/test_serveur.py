import unittest
import requests
import shlex
import subprocess
import time
import sqlite3
import os
#import src
from src.serveur import UserSrv
from src.Users import Users
import sys
from src.serveur import UserSrv

class TestUserSrv(unittest.TestCase):

	# SrvSubprocess = None
	# TestPort = "99"
	# SrvAddr = "127.0.0.1"
	# SrvUrl = "http://" + SrvAddr + ":" + TestPort

	
	
	def test_get_usr(self):
		try:
			os.remove('database.db')
		except:
			pass

		conn = sqlite3.connect('database.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, 
													  ip TEXT,
													  key_expiration DATE, 
													  password TEXT, 
													  port int,
													  privateKey TEXT NOT NULL,
													  publicKey TEXT NOT NULL, 
													  username TEXT NOT NULL) """)		
		test = UserSrv(Users())

		test.addUser(12,"102.021.32.12","1986-04-15","RGTGTR6345",253,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim")
		test.addUser(4,"99.99.99.910" ,"1987-08-30","password_PE"   ,2563,"CLE_PRIVATE_PE"   ,"CLE_PUBLIC_PE"   ,"PE")


		self.assertEqual(test.getUser(1),(1,"102.021.32.12","1986-04-15","RGTGTR6345",253,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim"))
		self.assertEqual(test.getUser(2),(2,"99.99.99.910" ,"1987-08-30","password_PE"   ,2563,"CLE_PRIVATE_PE"   ,"CLE_PUBLIC_PE"   ,"PE"))



	def test_return_key(self):

		try:
			os.remove('test.db')
		except:
			pass

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, password TEXT, port int, publicKey TEXT, username TEXT) """)

		test = UserSrv(Users())

		test.addUser(12,"102.021.32.12","1986-04-15","RGTGTR6345",102,"CLE_PRIVATE_KARIM","MLKJHGFDSQ","Karim")
		test.addUser(4,"99.99.99.910" ,"1987-08-30","password_PE"   ,2563,"CLE_PRIVATE_PE"   ,"AZERTYUIOP"   ,"PE")

		self.assertEqual(test.returnKey("Karim","PE"), ('https://102.021.32.12:102', '{"public_key": "AZERTYUIOP"}'))
		self.assertEqual(test.returnKey("PE","Karim"), ('https://99.99.99.910:2563', '{"public_key": "MLKJHGFDSQ"}'))
		


	
	# def test_hashed(self):
    #     self.assertEqual(test.hashed("example"),hash("example"))

	def test_hashed(self):
		test = UserSrv(Users())
		self.assertEqual(test.hashed("Python Programming"),hash("Python Programming"))
		self.assertEqual(test.hashed("Python"), hash("Python"))

	
	# def setUp(self):
	# 	cmd = "python user_server.py --port="+self.TestPort
	# 	args = shlex.split(cmd)
	# 	self.SrvSubprocess  = subprocess.Popen(args) # launch command as a subprocess
	# 	time.sleep(3)

	# def tearDown(self):
	# 	print("killing subprocess user_server")
	# 	self.SrvSubprocess.kill()
	# 	self.SrvSubprocess.wait()

	# def test_launchSrv(self):
	# 	response = requests.get(self.SrvUrl+"/isalive")
	# 	self.assertEqual(response.status_code,200)

if __name__ == '__main__':
	unittest.main()
