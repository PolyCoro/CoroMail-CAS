"""USER
"""

class User : 

	def __init__(self, ide, ip, key_expiration, password, port,privateKey, publickey, username):
	    self.id = ide
	    self.ip = ip
	    self.key_expiration = key_expiration
	    self.password = password
	    self.port = port
	    self.privateKey = privateKey
	    self.publickey = publickey
	    self.username = username

	def getId(self) : 
		return self.id

	def getIp(self) :
		return self.ip

	def getKey_expiration(self) :
		return self.key_expiration

	def getPassword(self) :
		return self.password

	def getPort(self) :
		return self.port

	def getPrivateKey(self) :
		return self.privateKey

	def getPublicKey(self) :
		return self.publickey

	def getUsername(self) :
		return self.username

	



