#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Leia a hora inicial, minuto inicial, hora final e minuto final de um
jogo. A seguir calcule a duração do jogo. Obs: O jogo tem duração mínima
de um (1) minuto e duração máxima de 24 horas. '''

import os
os.system('clear')

vert = input()

A,B,C,D = vert.split()

a = int(A)
b = int(B)
c = int(C)
d = int(D)

if a > c:
	h = 23 - (a - c)
	m = (60 + d) - b
	if m > 60:
		mn = divmod(m,60)
		h = h + mn[0]
		m = mn[1]		
	print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif a < c:
	h = c - a
	m = d - b
	if m < 0:
		m = (60 - b) + d
		h = h - 1
	print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif a == c and b == d:
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif a == c and b < d:
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif a == c and b > d:
	m = (d - b) + 60
	print("O JOGO DUROU 23 HORA(S) E %d MINUTO(S)" %m)
else:
	print("DADOS INCORRETOS")

