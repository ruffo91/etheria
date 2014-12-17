import threading
import pygame
from pygame.locals import *

class unit(threading.Thread):
    
    # DEFINICION DE LOS GET SET
    
    def getVida(self):
        return self.vida
    
    def setVida(self, vida):
        self.vida = vida
        
        
    def getNivel(self):
        return self.nivel
    
    def setNivel(self, nivel):
        self.nivel = nivel
        
        
    def getTextura(self):
        return self.textura
    
    def setTextura(self, textura):
        self.textura = textura
        
        
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = int(x)
        
    
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = int(y)
        
        
    def getO(self):
        return self.o
    
    def setO(self, o):
        self.o = o
        
        
    def getMapa(self):
        return self.mapa
    
    def setMapa(self, mapa):
        self.mapa = mapa
        
        
    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
        
    
    def getPantalla(self):
        return self.pantalla
    
    def setPantalla(self, pantalla):
        self.pantalla = pantalla
        
    
    def getSprite(self):
        return self.sprite
    
    def setSprite(self, sprite):
        self.sprite = sprite
        
    
    # METODOS
    
    def mover(self, o, velocidad):
        # MOVERSE AL SUR
        if o == 0: 
            self.setY(self.getY() - velocidad)
        # MOVERSE AL SUROESTE
        elif o == 1:
            self.setX(self.getX() - velocidad)
            self.setY(self.getY() - velocidad)
        # MOVERSE AL OESTE
        elif o == 2:
            self.setX(self.getX() - velocidad)
        # MOVERSE AL NOROESTE
        elif o == 3:
            self.setX(self.getX() - velocidad)
            self.setY(self.getY() + velocidad)
        # MOVERSE AL NORTE
        elif o == 4:
            self.setY(self.getY() + velocidad)
        # MOVERSE AL NORESTE
        elif o == 5:
            self.setX(self.getX() + velocidad)
            self.setY(self.getY() + velocidad)
        # MOVERSE AL ESTE
        elif o == 6:
            self.setX(self.getX() + velocidad)
        # MOVERSE AL SUROESTE
        elif o == 7:
            self.setX(self.getX() + velocidad)
            self.setY(self.getY() - velocidad)
            
        # ASIGNAMOS LA POSICION AL PLAYER
        self.setO(o)
            
    
    def teletransportar(self, x, y, o, mapa):
        self.setX(x)
        self.setY(y)
        self.setO(o)
        self.setMapa(mapa)
    
    def update(self):
        while self.getVida() > 0:
            pass
        
    def cargarTextura(self):
        self.setSprite(pygame.image.load(str(self.getTextura())))
        
    def renderizar(self):
        self.pantalla.ventana.blit(self.sprite, (self.getX(), self.getY()))
        
    def run(self):
        pass
        
        
    # CONSTRUCTOR
    
    def __init__(self, datos, pantalla):
        threading.Thread.__init__(self) 
        
        self.setNivel(datos["nivel"])
        self.setVida(datos["vida"])
        self.setTextura(datos["textura"])
        self.teletransportar(datos["x"], datos["y"], datos["o"], datos["mapa"])
        self.cargarTextura()
        self.setPantalla(pantalla)
        
        self.stoprequest = threading.Event()
        
        