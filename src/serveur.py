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
import requests,json

import sys
sys.path.append("/home/ei-se/Documents/coroMail/CoroMail-CAS/src")
from Users import Users



APP = Flask(__name__)

@APP.route('/isalive', methods=['GET'])
def is_alive():
	return Response(status=200)

class UserSrv(Users):
	def __init__(self,db):
		super().__init__()
		
	

	def returnKey(self,keyAsker,keyGiver):
		
		self.cursor.execute("""SELECT publicKey FROM users WHERE username = ? """,[keyGiver])
		publicKeyGiver = self.cursor.fetchall()
		
		self.cursor.execute("""SELECT ip FROM users WHERE username = ? """,[keyAsker])
		ipKeyAsker = self.cursor.fetchall()
		
		self.cursor.execute("""SELECT port FROM users WHERE username = ? """,[keyAsker])
		portKeyAsker = self.cursor.fetchall()
		
		url = "https://" + str(ipKeyAsker) + ":" + str(portKeyAsker)


		translation_table = dict.fromkeys(map(ord, "[(',)]"), None)
		url = url.translate(translation_table)
		publicKeyGiver = str(publicKeyGiver).translate(translation_table)
		
		donnee = json.dumps({"public_key" : publicKeyGiver})
		return url,donnee
		
		r = requests.post(url, data= donnee)
		print('test')

		# if r.status_code == requests.codes.ok :
		# 	return True	
		# else : 
		# 	return False
	
	def hashed(self,password):
		return hash(password)

	def getUser(self,id):
		self.cursor.execute("""SELECT id,ip,key_expiration,password,port,privateKey,publicKey,username FROM users WHERE id=?""", (id,))
		user = self.cursor.fetchone()
		return user

@app.route('/users_list',methods = ['POST', 'GET',])
def device():

    if request.method == 'POST':
        self.addUser(request.json[0],request.json[1],request.json[2],request.json[3],request.json[4],request.json[5],request.json[6],request.json[7])
        # id ip key_expiration password port privateKey publicKey username
        return jsonify({'status': 'post ok'})

    #GET 
    elif request.method == 'GET':
    	self.cursor.execute("""SELECT ip FROM users WHERE id=?""", (request.json[0],))
		ip = self.cursor.fetchone()
		return jsonify({'status': 'get ok','ip': ip})
     



if __name__ == '__main__':
	app.run(debug=True,port=5001)
	# ARGS = docopt(__doc__)
	# if ARGS['--port']:
	# 	APP.run(host='0.0.0.0', port=ARGS['--port'])
	# else:
	# 	logging.error("Wrong command line arguments")