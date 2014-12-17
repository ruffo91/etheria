import pygame
import threading

class escenario(threading.Thread):
    
    # METODOS GET SET
    
    def getPantalla(self):
        return self.pantalla
    
    def setPantalla(self, pantalla):
        self.pantalla = pantalla
    
    def getTextura(self):
        return self.textura
    
    def setTextura(self, textura):
        self.textura = str(textura)
    
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
    
    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = int(velocidad)
        
    def getAndando0(self):
        return self.andando0
        
    def setAndando0(self, andando):
        self.andando0 = andando
        
    def getAndando1(self):
        return self.andando1
        
    def setAndando1(self, andando):
        self.andando1 = andando
        
    def getAndando2(self):
        return self.andando2
        
    def setAndando2(self, andando):
        self.andando2 = andando
        
    def getAndando3(self):
        return self.andando3
        
    def setAndando3(self, andando):
        self.andando3 = andando
        
    def getSprite(self):
        return self.sprite
    
    def setSprite(self, sprite):
        self.sprite = sprite
    
    
    # METODOS
    
    def teletransportar(self, x, y):
        self.setX(x)
        self.setY(y)
        
    def andar(self):
        if(self.getAndando0()):
            self.setY(self.getY() - self.getVelocidad())
        if(self.getAndando1()):
            self.setX(self.getX() + self.getVelocidad())
        if(self.getAndando2()):
            self.setY(self.getY() + self.getVelocidad())
        if(self.getAndando3()):
            self.setX(self.getX() - self.getVelocidad())
            
    def cargarTextura(self):
        self.setSprite(pygame.image.load(str(self.getTextura())))
    
    def renderizar(self):
        self.andar()
        self.pantalla.ventana.fill((0,0,0))
        self.pantalla.ventana.blit(self.sprite, (self.getX(), self.getY()))
    
    def run(self):
        
        #self.andar()
        #self.renderizar()
        #self.renderizar()
        #self.run()
        pass
        
        
    # CONSTRUCTOR
    
    def __init__(self, datos, pantalla):
        threading.Thread.__init__(self) 
        self.setAndando0(False)
        self.setAndando1(False)
        self.setAndando2(False)
        self.setAndando3(False)
        self.setTextura(datos["textura"])
        self.cargarTextura()
        self.teletransportar(datos["x"], datos["y"])
        self.setVelocidad(datos["velocidad"])
        self.setPantalla(pantalla)
        
        self.stoprequest = threading.Event()
        
        