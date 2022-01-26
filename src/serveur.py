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
from flask import render_template, jsonify, request
import requests

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
        #   return True 
        # else : 
        #   return False
    
    def hashed(self,password):
        return hash(password)

    def getUser(self,id):
        self.cursor.execute("""SELECT id,ip,key_expiration,password,port,privateKey,publicKey,username FROM users WHERE id=?""", (id,))
        user = self.cursor.fetchone()
        return user

@APP.route('/users_list',methods = ['POST', 'GET',])
def device():
    
    if request.method == 'POST':
        name = request.json
        Serveur.addUser(name['id'],name['ip'],name['key_expiration'],name['password'],name['port'],name['privateKey'],name['publicKey'],name['username'])
        # id ip key_expiration password port privateKey publicKey username
        Serveur.cursor.execute("SELECT * FROM users")
        print(Serveur.cursor.fetchall())
        return jsonify({'status': 'post ok'})

    #GET 
    elif request.method == 'GET':
        args = request.args
        name = args['username']
        Serveur.cursor.execute("""SELECT ip FROM users WHERE username=?""", (name,))
        ip = Serveur.cursor.fetchone()
        return jsonify({'status': 'get ok'})
        
         

if __name__ == '__main__':
    Serveur = UserSrv(Users())
    APP.run(debug=True,port=5001)

    # ARGS = docopt(__doc__)
    # if ARGS['--port']:
    #   APP.run(host='0.0.0.0', port=ARGS['--port'])
    # else:
    #   logging.error("Wrong command line arguments")