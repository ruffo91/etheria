
import pygame
import sys
from pygame.locals import *
from random import randint 

# DEFINICION DE VARIABLES
estado = "ninguno"
clock = pygame.time.Clock()
quit = False


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
x = -500
y = -500
velocidad = 5
while not quit:
    
    # EVENTOS
    quit = pygame.event.get(pygame.QUIT)
    pygame.event.poll()
    """for evento in pygame.event.get():
        if evento.type == QUIT:
            salir()
        
        if evento.type == KEYDOWN and evento.key == K_ESCAPE and estado == "login":
            salir()"""
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        y += velocidad
    if teclas[pygame.K_s]:
        y -= velocidad
    if teclas[pygame.K_a]:
        x += velocidad
    if teclas[pygame.K_d]:
        x -= velocidad
        
    # PONEMOS LA IMAGEN DE FONDO
    ventana.fill((0,0,0))
    fondo = pygame.image.load("images/escenario0.jpg")        
    ventana.blit(fondo, (x, y))
    
    # PONEMOS LOS DOS CAMPOS DE TEXTO
    textUser = pygame.image.load("images/pj01.png")
    ventana.blit(textUser, (1024 / 2 - 50, 768 / 2 - 50))
    #textPass = pygame.image.load("images/text.png")
    #ventana.blit(textPass, (1024 / 2 - 250, 768 / 2 - 50))
    pygame.display.flip()
    clock.tick(60)
    
