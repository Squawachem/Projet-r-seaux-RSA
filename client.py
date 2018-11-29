#!/usr/bin/python3 
# -*- coding: utf-\ -*-

import socket
import generation.py
import RSA.py
from threading import Thread


# doit pouvoir être client ET serveur


s = socket(AF_INET, SOCK_STREAM)
port_defaut = 7890
localhost = '127.0.0.1'
help = "[manuel d'utilisation]"

class Ami:
	def __init__(self, IP, port, pseudo):
		self.IP = IP
		self.port = port
		self.pseudo = pseudo


liste_amis = []



#Thread d'écriture
class Ecriture(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):

		while True:
			com = input()	# com(mande)

			if com[0] == "#":	# com = "#connect" ou "#disconnect"

				if len(com) > 4 and com[1:] == "help":
					print(help)

				if len(com) > 8 and com[1:8] == "connect":
					if com[8:12] == " -p ":	# cas localhost : on donne le port
						IP_ami = localhost
						port_ami = com[12:]	# fin de la commande correspond à l'IP
					else:					# cas IP distante : on donne l'IP
						IP_ami = com[9:]	
						port_ami = port_defaut

					try :
						s.connect( (IP_ami, port_ami) )	
						liste_amis.append( Ami(IP_ami, port_ami, "NULL") )




					except :
						print()

				if len(com) > 11 and com[1:11] == "disconnect":
					IP_ami = com[12:]
					# A FAIRE : GERER LA DECONNEXION



			else: 	# commande = envoi de message

				if liste_amis == []:	# aucune connexion
					print("Connectez-vous d'abord avec la commande : #connect IP ")
				else:	# envoi du message 
					# chiffrement_RSA(com)
					for i in range(len(liste_amis)):
						s.send(com)



#Thread de lecture
class Lecture(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:






E = Ecriture()
E.start()
L = Lecture()
L.start()




########################################################################################################
#Je ne sais plus à quoi ça sert:

while msg!="":

		#reception
		msg += msg 
		msg = s.recv(1024)

	# déchiffrement msg avant print
	print(msg)

############

while True:
	msg += connexion.recv(1024)
	

s.close()



############



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsap_serveur = ('127.0.0.1',7890)

s.connect(tsap_serveur)
while 1:
	ligne = input()
	if not ligne:
		break
	s.sendall(bytes(ligne,'UTF-8'))
s.close()
