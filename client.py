#!/usr/bin/python3 
# -*- coding: utf-\ -*-

import socket
import generation.py
import RSA.py


# doit pouvoir être client ET serveur


s = socket(AF_INET, SOCK_STREAM)
port = 7890
#localhost = '127.0.0.1'


class Ami:
	def __init__(self, IP, pseudo):
		self.IP = IP
		self.pseudo = pseudo


liste_amis = []


#Thread d'écriture
while True:
	com = input()

	if com[0] == "#":	# com = #connect ou #disconnect
		if len(com) > 8 and com[1:8] == "connect":
			IP_ami = com[9:]
			s.connect( (IP_ami, port) )

		# A IMPLEMENTER : gestion de la déconnexion
		#if len(com) > 10 and com[1:10] == "disconnect":
		#	IP_disconnect = com[11:]

	else:	# commande = envoi de message
		if liste_amis == []:	# aucune connexion
			print("Connectez-vous d'abord avec la commande : #connect IP ")
		else:	# envoi du message 
			#msg = chiffrement_RSA(com)

#Thread de lecture








########################################################################################################

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
