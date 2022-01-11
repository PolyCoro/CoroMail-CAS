import unittest
import requests
import shlex
import subprocess
import time
import sqlite3
import os
#import src
#from src.serveur import UserSrv
import sys
sys.path.append("/home/ei-se/Documents/coroMail/CoroMail-CAS/src")
from serveur import UserSrv

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
		c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, password TEXT, port int, publicKey TEXT, username TEXT) """)
		
		test = UserSrv()

		res = test.addUser("102.021.32.12" ,"password_karim",102,"CLE_KARIM","Karim")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE username='Karim'")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 1)
			self.assertEqual(row['ip'], "102.021.32.12")
			self.assertEqual(row['password'], "password_karim")
			self.assertEqual(row['port'], 102)
			self.assertEqual(row['publicKey'], "CLE_KARIM")
			self.assertEqual(row['username'], "Karim")

		res = test.addUser("99.99.99.910","password_PE",2563,"CLE_PE","PE")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE id=2")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 2)
			self.assertEqual(row['ip'], "99.99.99.910")
			self.assertEqual(row['password'], "password_PE")
			self.assertEqual(row['port'], 2563)
			self.assertEqual(row['publicKey'],"CLE_PE")
			self.assertEqual(row['username'], "PE")

		res = test.addUser(" ","ef",0,"ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE ip=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")

		res = test.addUser("ef"," ",0,"ef","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE password=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 3)
			self.assertEqual(row['ip'], "")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], "ef")

		res = test.addUser("ef","ef" ,0,"ef"," ")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE username=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 4)
			self.assertEqual(row['ip'], "ef")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], " ")
		
		res = test.addUser("ef","ef" ,0," ","ef")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE username=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 4)
			self.assertEqual(row['ip'], "ef")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 0)
			self.assertEqual(row['publicKey'], " ")
			self.assertEqual(row['username'], " ")
		
		res = test.addUser("ef&!$","ef" ,0,"ef"," ")
		self.assertEqual(res,True)
		c.execute("SELECT * FROM users WHERE username=' '")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['id'], 5)
			self.assertEqual(row['ip'], "ef&!$")
			self.assertEqual(row['password'], "ef")
			self.assertEqual(row['port'], 1)
			self.assertEqual(row['publicKey'], "ef")
			self.assertEqual(row['username'], " ")

		res = test.addUser("","ef" ,0,"ef", "ef")
		self.assertEqual(res,False)

		res = test.addUser("ef","" ,0,"ef", "ef")
		self.assertEqual(res,False)

		res = test.addUser("ef","ef" ,0,"ef", "")
		self.assertEqual(res,False)

		res = test.addUser("ef","ef" ,0,"", "ef")
		self.assertEqual(res,False)

		
		conn.commit()
		conn.close()
	
	def test_get_usr(self):
		try:
			os.remove('test.db')
		except:
			pass

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, password TEXT, port int, publicKey TEXT, username TEXT) """)

		test = UserSrv()

		test.addUser("102.021.32.12" ,"password_karim", 102,"key","Karim")
		test.addUser("99.99.99.910","password_PE", 2563,"keyPublic","PE")


		self.assertEqual(test.getUser(1), (1,"102.021.32.12" ,"password_karim",102, "key","Karim"))
		self.assertEqual(test.getUser(2), (2,"99.99.99.910","password_PE",2563, "keyPublic","PE"))


	def test_returnKey(self):

		try:
			os.remove('test.db')
		except:
			pass

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, password TEXT, port int, publicKey TEXT, username TEXT) """)

		test = UserSrv()

		test.addUser("102.021.32.12" ,"password_karim",102, "AZERTYUIOP" ,"Karim")
		test.addUser("99.99.99.910","password_PE",2563, "MLKJHGFDSQ" ,"PE")

		self.assertEqual(test.returnKey("Karim","PE"), ('https://102.021.32.12:102', '{"public_key": "MLKJHGFDSQ"}'))
		self.assertEqual(test.returnKey("PE","Karim"), ('https://99.99.99.910:2563', '{"public_key": "AZERTYUIOP"}'))
		


	
	# def test_hashed(self):
    #     self.assertEqual(test.hashed("example"),hash("example"))
	
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