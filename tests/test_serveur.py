import unittest
import requests
import shlex
import subprocess
import time
from user_server import UserSrv
import sqlite3

# id ip password port username

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int, ip TEXT, password TEXT, port int, username TEXT) """)
conn.commit()

test = UserSrv()

count = 1

test.addUser(1,"102.021.32.12" ,"password_karim",102,"Karim")
test.addUser(2,"99.99.99.910"  ,"password_PE"   ,2563,"PE")
test.addUser(3,"120.325.365.45","password_isma" ,12002,"ISMA")
test.addUser(-1,"","ef" ,0,"ef")
test.addUser(-1,"ef","" ,0,"ef")
test.addUser(-1,"ef","ef" ,0,"")
test.addUser(-1,"ef&!$","ef" ,0,"")

class TestUserSrv(unittest.TestCase):

	# SrvSubprocess = None

	# TestPort = "99"
	# SrvAddr = "127.0.0.1"
	# SrvUrl = "http://" + SrvAddr + ":" + TestPort

	def test_addUser(self):
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE username="Karim" """).fetchone(),(1,"102.021.32.12","password_karim",102,"Karim"))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE password="password_isma" """).fetchone(),(3,"120.325.365.45","password_isma",12002,"ISMA"))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE ip="99.99.99.910" """).fetchone(),(2,"99.99.99.910","password_PE",2563 ,"PE"))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE ip="" """).fetchone(),(-1,"","ef",0 ,"ef"))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE password="" """).fetchone(),(-1,"ef","",0 ,"ef"))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE username="" """).fetchone(),(-1,"ef","ef",0 ,""))
		self.assertEqual(test.cursor.execute("""SELECT * FROM users WHERE ip="ef&!$" """).fetchone(),(-1,"ef&!$","ef",0 ,""))
	
	# def test_hash(self):
    #     self.assertEqual(test.hash("example"),hash("example"))
	
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