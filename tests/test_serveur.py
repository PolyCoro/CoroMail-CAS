import unittest
import requests
import shlex
import subprocess
import time
import sqlite3
import os
import src
from src.serveur import UserSrv

class TestUserSrv(unittest.TestCase):

	# SrvSubprocess = None
	# TestPort = "99"
	# SrvAddr = "127.0.0.1"
	# SrvUrl = "http://" + SrvAddr + ":" + TestPort

	def test_addUser(self):
		# ouverture/initialisation de la base de donnee 
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
		test = UserSrv()

		res = test.addUser("102.021.32.12","2016-08-30 12:54:12","password_karim",102,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE username='Karim'")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 1)
			self.assertEqual(row['ip'], "102.021.32.12")
			self.assertEqual(row['key_expiration'], "2016-08-30 12:54:12")
			self.assertEqual(row['password'], "password_karim")
			self.assertEqual(row['port'], 102)
			self.assertEqual(row['privateKey'], "CLE_PRIVATE_KARIM")
			self.assertEqual(row['publicKey'], "CLE_PUBLIC_KARIM")
			self.assertEqual(row['username'], "Karim")

		res = test.addUser("99.99.99.910","1987-08-30 00:54:12","password_PE",2563,"CLE_PRIVATE_PE","CLE_PUBLIC_PE","PE")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE id=2")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 2)
			self.assertEqual(row['ip'], "99.99.99.910")
			self.assertEqual(row['key_expiration'], "1987-08-30 00:54:12")
			self.assertEqual(row['password'], "password_PE")
			self.assertEqual(row['port'], 2563)
			self.assertEqual(row['privateKey'], "CLE_PRIVATE_PE")
			self.assertEqual(row['publicKey'], "CLE_PUBLIC_PE")
			self.assertEqual(row['username'], "PE")

		res = test.addUser(" ","1235-08-30 18:16:12","ef",0,"ef","ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], " ")
			self.assertEqual(row['key_expiration'], "1987-08-30 00:54:12")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], "ef")
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")
	
		res = test.addUser("120.203.837"," ","ef",0,"ef","ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "120.203.837")
			self.assertEqual(row['key_expiration'], " ")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], "ef")
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")


		res = test.addUser("120.203.837","1235-08-30 18:16:12"," ",0,"ef","ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "120.203.837")
			self.assertEqual(row['key_expiration'], " ")
			self.assertEqual(row['password'], " ")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], "ef")
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")
		
		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0," ","ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "120.203.837")
			self.assertEqual(row['key_expiration'], " ")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], " ")
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")

		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0,"ef"," ","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "120.203.837")
			self.assertEqual(row['key_expiration'], " ")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], "ef")
			self.assertEqual(row['publicKey'], " ")
			self.assertEqual(row['username'], "ef")
		
		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0,"ef","ef"," ")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "120.203.837")
			self.assertEqual(row['key_expiration'], " ")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['privateKey'], "ef")
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], " ")

		
		

		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0,"ef","ef","")
		self.assertEqual(res,False)

		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0,"ef","","ef")
		self.assertEqual(res,False)

		res = test.addUser("120.203.837","1235-08-30 18:16:12","ef",0,"","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser("120.203.837","1235-08-30 18:16:12","",0,"ef","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser("120.203.837","","ef",0,"ef","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser("","1235-08-30 18:16:12","ef",0,"ef","ef","ef")
		self.assertEqual(res,False)

		
		conn.commit()
		conn.close()
	
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
		test = UserSrv()

		test.addUser("102.021.32.12","2016-08-30 12:54:12","passwordKarim" ,102 ,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim")
		test.addUser("99.99.99.910" ,"1987-08-30 00:54:12","password_PE"   ,2563,"CLE_PRIVATE_PE"   ,"CLE_PUBLIC_PE"   ,"PE")


		self.assertEqual(test.getUser(1),(1,"102.021.32.12","2016-08-30 12:54:12","passwordKarim",102,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim"))
		self.assertEqual(test.getUser(2),(2,"99.99.99.910","1987-08-30 00:54:12","password_PE",2563,"CLE_PRIVATE_PE","CLE_PUBLIC_PE","PE"))


	def test_hashed(self):
		test = UserSrv()
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