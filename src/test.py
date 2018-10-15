#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import usuarios
import videojuegos

class Test(unittest.TestCase):

    def testVideojuegos(self):
        self.assertEqual(self.videojuegos.Videojuegos().getVideojuego("cad"),False,"El ID del videojuego debe ser entero")
        self.assertEqual(self.videojuegos.Videojuegos().getVideojuego(1),str('BattleRoyale'),"El ID del videojuego es correcto y es devuelto")

    def testUusarios(self):
        self.assertEqual(self.usuarios.Usuarios().getUsuario("cad"),False,"El ID del usuario debe ser entero")
        self.assertEqual(self.usuarios.Usuarios().getUsuario(1),str('Fernando Flores'),"El ID del usuario es correcto y es devuelto")


if __name__ == '__main__':
    unittest.main()                                                  
