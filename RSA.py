#!/usr/bin/python3
# coding: utf-8

#=================================#
# Fonctions relatives au code RSA #
#=================================#

from generation import generation_premier

# exposant de clé publique
e = 65537

def egcd(a, b):
    ''' Algorithme d'Euclide étendu (tiré de l'énoncé) '''
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    ''' Détermine l'inverse de a modulo m (tiré de l'énoncé) '''
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    return x % m

def lpowmod(x, y, n):
    ''' Puissance modulaire : (x**y)%n, avec x, y et n entiers (tiré de l'énoncé) '''
    result = 1
    while y>0:
        if y&1>0:
            result = (result*x)%n
        y >>= 1
        x = (x*x)%n
    return result

def parametres_RSA(taille_p=10, taille_q=10):
    ''' Génère les paramètres nécessaires au chiffrement RSA '''
    p = int(generation_premier(taille_p))
    q = int(generation_premier(taille_q))
    phi = (p - 1) * (q - 1)
    n = p * q
    # exposant de clé privée
    d = modinv(e, phi)
    return n, d

def chiffrement_RSA(m, n):
    ''' Chiffre le message m à l'aide de la clé publique n '''
    return lpowmod(m, e, n)

def dechiffrement_RSA(c, n, d):
    ''' Déchiffre le message c à l'aide de la clé publique n 
        et de la clé privée d '''
    return lpowmod(c, d, n)

# Test de chiffrement/déchiffrement
n, d = parametres_RSA()
m = 1234567890
c = chiffrement_RSA(m, n)
print(c)
M = dechiffrement_RSA(c, n, d)
print(M)
if M == m:
    print(":-)")
