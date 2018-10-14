#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import videojuegos
import usuarios

class Test(unittest.TesCase):

    test = videojuegos.Videojuegos()

    def testVideojuegos(self):
        self.assertEqual(self.test.getVideojuego("cad"),False,"El ID del videojuego debe ser entero")
        self.assertEqual(self.test.getVideojuego(1),str('BattleRoayale'),"El ID del videojuego es correcto y es devuelto")
                    
    test = usuarios.Usuarios()

    def testUusarios(self):
        self.assertEqual(self.test.getUsuario("cad"),False,"El ID del usuario debe ser entero")
        self.assertEqual(self.test.getVideojuego(1),str('Fernando Flores'),"El ID del usuario es correcto y es devuelto")


if __name__ == '__main__':
    unittest.main()                                                  
