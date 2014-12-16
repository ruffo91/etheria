
import pygame
import sys
from pygame.locals import *
from random import randint 

# DEFINICION DE VARIABLES
estado = "ninguno"


# DEFINICION DE FUNCIONES
def salir():
    pygame.quit()
    sys.exit()
    

# CONFIGURACION INICIAL

pygame.init()
ventana = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Etheria")
estado = "login"


# BUCLE DE VENTANA
while True:
    
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == QUIT:
            salir()
        
        if evento.type == KEYDOWN and evento.key == K_ESCAPE and estado == "login":
            salir()
        
    # PONEMOS LA IMAGEN DE FONDO
    fondo = pygame.image.load("images/eter.jpg")        
    ventana.blit(fondo, (0, 0))
    
    # PONEMOS LOS DOS CAMPOS DE TEXTO
    textUser = pygame.image.load("images/text.png")
    ventana.blit(textUser, (1024 / 2 - 250, 768 / 2 + 50))
    textPass = pygame.image.load("images/text.png")
    ventana.blit(textPass, (1024 / 2 - 250, 768 / 2 - 50))
    
    pygame.display.update()
    
