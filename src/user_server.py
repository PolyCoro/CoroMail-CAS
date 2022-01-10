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
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int, ip TEXT, password TEXT, port int, username TEXT) """)

	# def find_next_id(self,count):
	# 	if count == 1:
	# 		return 1
	# 	else:
	# 		return count+1

	def addUser(self,id,ip, password, port, username):
		# id += 1
		self.cursor.execute("""INSERT INTO users(id,ip, password, port, username) VALUES(?,?,?,?,?)""",(id,ip, password, port, username))	
		if self.cursor.rowcount == 0:
			return False
		return True

	# def returnKey(keyAsker,keyGiver):
	# 	# requete http au client dans post payload 
	# 	# key public 
	# 	# il y aura une requete au serveur pour donner les deux cles au keygiver
	# 	return keyAsker, keyGiver
	
	# def hash(password):
	# 	return hash(password)

	# def getUser(self,name):
	# 	return self.cursor.execute("""SELECT * FROM users WHERE Name="name" """).fetchone()

if __name__ == '__main__':
	ARGS = docopt(__doc__)
	if ARGS['--port']:
		APP.run(host='0.0.0.0', port=ARGS['--port'])
	else:
		logging.error("Wrong command line arguments")