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
from Users import Users


class TestUsers(unittest.TestCase):

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
		test = UserSrv(Users())

		res = test.addUser(1,"102.021.32.12","2016-08-30 12:54:12","password_karim",102,"CLE_PRIVATE_KARIM","CLE_PUBLIC_KARIM","Karim")
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

		res = test.addUser(2,"99.99.99.910","1987-08-30 00:54:12","password_PE",2563,"CLE_PRIVATE_PE","CLE_PUBLIC_PE","PE")
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

		res = test.addUser(3," ","1235-08-30 18:16:12","ef",0,"ef","ef","ef")
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
	
		res = test.addUser(3,"120.203.837"," ","ef",0,"ef","ef","ef")
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


		res = test.addUser(3,"120.203.837","1235-08-30 18:16:12"," ",0,"ef","ef","ef")
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
		
		res = test.addUser(3,"120.203.837","1235-08-30 18:16:12","ef",0," ","ef","ef")
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

		res = test.addUser(3,"120.203.837","1235-08-30 18:16:12","ef",0,"ef"," ","ef")
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
		
		res = test.addUser(3,"120.203.837","1235-08-30 18:16:12","ef",0,"ef","ef"," ")
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

		
		

		res = test.addUser(1,"120.203.837","1235-08-30 18:16:12","ef",0,"ef","ef","")
		self.assertEqual(res,False)

		res = test.addUser(1,"120.203.837","1235-08-30 18:16:12","ef",0,"ef","","ef")
		self.assertEqual(res,False)

		res = test.addUser(1,"120.203.837","1235-08-30 18:16:12","ef",0,"","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser(1,"120.203.837","1235-08-30 18:16:12","",0,"ef","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser(1,"120.203.837","","ef",0,"ef","ef","ef")
		self.assertEqual(res,False)

		res = test.addUser(1,"","1235-08-30 18:16:12","ef",0,"ef","ef","ef")
		self.assertEqual(res,False)

		
		conn.commit()
		conn.close()

if __name__ == '__main__':
	unittest.main()
