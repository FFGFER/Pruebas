#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Funcionalidad:
	
	def __init__(self):
	
		with open('videojuegos.json', 'r') as file:
			self.vg = json.load(file)
			
		with open('usuarios.json', 'r') as file:
			self.usr = json.load(file)
			
	def getVideojuego(self,idgame):
		
		try:
			idgame = abs(int(idgame))
			videojuego = self.vg["Videojuego"][idgame-1]["Nombre"]
		
		except:
			videojuego = False
		
		return videojuego
		
	def getUsuario(self,idusr):
		
		try:
			idusr = abs(int(idusr))
			usuario = self.usr["Usuario"][idusr-1]["Nombre"]
		
		except:
			usuario = False
		
		return usuario