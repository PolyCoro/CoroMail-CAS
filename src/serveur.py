"""UserSrv

Usage:
	UserSrv.py --port=<int>

Options:
	-h --help     Show this screen.
	--port=<int>  port used

"""
import logging
import sqlite3
from docopt import docopt
from flask import Flask
from flask import Response


APP = Flask(__name__)

@APP.route('/isalive', methods=['GET'])
def is_alive():
	return Response(status=200)

class UserSrv:

	def __init__(self):
		# self.users = []
		try:
			self.database = sqlite3.connect('database.db')
		except sqlite3.error : 
			print("Error open db.\n")
		self.cursor = self.database.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, password TEXT, port int, username TEXT) """)

	def addUser(self,ip, password, port, username):
		if  ip == "" or password == "" or username == "":
			return False
		self.cursor.execute("""INSERT INTO users(ip, password, port, username) VALUES(?,?,?,?)""",(ip, password, port, username))	
		if self.cursor.rowcount == 0:
			return False
		return True

	# def returnKey(self,keyAsker,keyGiver):
		
	# 	self.cursor.execute("""SELECT publicKey FROM users WHERE username = ? """,(keyGiver,))
	# 	publicKeyGiver = self.cursor.fetchall()
	# 	self.cursor.execute("""SELECT ip FROM users WHERE username = ? """,(keyAsker,))
	# 	ipKeyAsker = self.cursor.fetchall()
	# 	self.cursor.execute("""SELECT port FROM users WHERE username = ? """,(keyAsker,))
	# 	portKeyAsker = self.cursor.fetchall()
	# 	print(publicKeyGiver)
	# 	url = "https://" + ipKeyAsker + "/" + portKeyAsker
	# 	donnee = json.loads({public_key : publicKeyGiver})
	# 	r = requests.post(url, data=donnee)

	# 	return True
	
	def hashed(self,password):
		# return password
		return hash(password)

	

	def getUser(self,id):
		self.cursor.execute("""SELECT id, ip, password, port, username FROM users WHERE id=?""", (id,))
		user = self.cursor.fetchone()
		return user

if __name__ == '__main__':
	ARGS = docopt(__doc__)
	if ARGS['--port']:
		APP.run(host='0.0.0.0', port=ARGS['--port'])
	else:
		logging.error("Wrong command line arguments")