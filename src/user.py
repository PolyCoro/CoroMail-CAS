"""USR
"""

class User : 

	def __init__(self, name, password, IP, publickey):
	    self.Name = name
	    self.__password = password
	    self.__IP = IP
	    self.__publickey = publickey

	def getPassword(self) :
		return self.__password

	def getKey(self) :
		return self.__publickey

	def getIP(self) :
		return self.__IP

if __name__ == '__main__':
	usr = User("Pierre","password","127.0.0.2","abcde")
	print(usr.getKey())
	print(usr.getIP())