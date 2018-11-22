#!/usr/bin/python3 
# -*- coding: utf-\ -*-




#===========================================================
# Génération de nombre premier de grande taille à n chiffres
#===========================================================


import random
import math
import subprocess

random.seed()



def est_premier(n):
	""" Optimisable par test de Mil"""
	p = int(n)
	if n == 2:
		return True
	k = 2	# potentiel diviseur of p 
	if p==1 or p%k == 0:
		return False
	k +=1
	while k <= int(math.sqrt(p)):
		if p % k ==0:
			return False
		k += 2
	return True


def generation_premier(n):
	"""génère une str = un nombre premier à n chiffres avec n>1"""
	assert(n>1)
	p = "4"		# nombre non premier pour initialiser

	while not( est_premier( int(p) )):
		p = ""
		p += str(random.randint(1,9))
		for i in range(1,n-1):
			p += str(random.randint(0,9))
		p += random.choice('1379')
	#print(p)
	return p


def est_premier_enonce(p):
	commande = "openssl prime "
	r  = subprocess.run(commande+str(p),shell=True,stdout=subprocess.PIPE)
	res = r.stdout
	if res[-10:-7] == b'not':
		return True
	else:
		return False



#==================
# Temps d'exécution
#==================

"""
import time

i = generation_premier(12)


start_time = time.time()
est_premier(i)
print(time.time() - start_time, "secondes")


start_time = time.time()
est_premier_enonce(i)
print(time.time() - start_time, "secondes")


"""
