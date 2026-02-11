import pygame
import random


pygame.init()

Larghezza_Schermo = 822
Altezza_Schermo = 745

schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
pygame.display.set_caption("Insultle") 

imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

FontTitolo = pygame.font.SysFont('Impact', 50)
FontoLettere = pygame.font.SysFont('Impact', 20)

Titolo = FontTitolo.render("INSULTLE", True, "#B5E61D")
letteraA = FontoLettere.render("A", True, "black")

running = True
LetteraA = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                LetteraA = True 
        
        schermo.blit(imgSfondo,(0,0) )
        schermo.blit(Titolo, (50,50))
        schermo.blit(letteraA, (15,25))
        pygame.display.flip()
        
pygame.quit()