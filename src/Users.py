"""USERS
"""
import logging
import sqlite3
from docopt import docopt
from flask import Flask
from flask import Response
import requests,json


class Users : 

	def __init__(self):
		try:
			self.db = sqlite3.connect('database.db',check_same_thread=False)
		except sqlite3.error : 
			print("Error open db.\n")
		self.cursor = self.db.cursor()
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, 
																ip TEXT,
																key_expiration DATE, 
																password TEXT, 
																port int,
																privateKey TEXT NOT NULL,
																publicKey TEXT NOT NULL, 
																username TEXT NOT NULL) """)

	def addUser(self,id,ip,key_expiration,password,port,privateKey,publicKey,username):
		if  key_expiration == "" or ip == "" or password == "" or privateKey == "" or publicKey == "" or username == "":
			return False
		self.cursor.execute("""INSERT INTO users(ip,key_expiration, password,port,privateKey,publicKey,username) VALUES(?,?,?,?,?,?,?)""",(ip,
																																		   key_expiration,
																																		   password, 
																																		   port,
																																		   privateKey, 
																																		   publicKey, 
																																		   username))	
		if self.cursor.rowcount == 0:
			return False
		return True

	def getUsers(self):
		return self.db
