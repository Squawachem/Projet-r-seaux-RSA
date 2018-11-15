#!/usr/bin/python3 
# -*- coding: utf-\ -*-

import random
random.seed()
caractere_aleatoire = random.choice('1379')

#===========================================================
# Génération de nombre premier de grande taille à n chiffres
#===========================================================

def est_premier(p):
	k = 2	# potentiel diviseur of p 
	if p%k == 0:
		return False
	k +=1
	while k <= math.sqrt(n):
		k += 2
		print(k)
		if p % k ==0:
			return False

	return True


