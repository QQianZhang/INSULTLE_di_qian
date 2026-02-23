#INSULTLE
#Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

import pygame
import random
from pathlib import Path

pygame.init()

Larghezza_Schermo = 822
Altezza_Schermo = 745

schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
pygame.display.set_caption("Insultle") 

imgSfondo = pygame.image.load("sfondoINSULTLE.jpg")           
imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

FontLettere = pygame.font.SysFont('Impact', 60)

vocabolario = open("Vocabolario.txt", "r")
ParoleComputer = ["RINCO", "SCEMO", "TONTO", "PAZZO", "LENTO", "EBETE", "PIGRO", "ROZZO", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO"]
ParoleAccUtente = []
for riga in vocabolario:
    ParoleAccUtente.append(riga.strip())  #Aggiunge alla lista delle parole accettate tutte quelle del vocabolario e senza /n
#Non ci sono solo gli insulti, erano troppo pochi, così l'utente può inserire la parola che vuole, verificare le lettere e poi scrivere l'insulto
ParolaSceltaComputer = random.choice(ParoleComputer)
print(ParolaSceltaComputer)
#Sceglie un insulto a caso dalla lista
#qian: lo ho messo fuori da running perchè se lo mettiamo dentro, ogni volta che l'utente scrivere una lettere la parola cambia
#perchè la pagina viene "ricaricata"

letteraPremuta = ""
listaParola = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                listaParola.pop()

            else:
                letteraPremuta = event.unicode
                if letteraPremuta.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    listaParola.append(letteraPremuta.upper())

    schermo.blit(imgSfondo, (0, 0))
    
    ParolaInserita= ""
    for x in range(len(listaParola)):
        lettera = listaParola[x]
        ParolaInserita += lettera
        
        colonna = x % 5 #in base al resto della divisione scelgo la colonna, quando è x = 0 (prima lettera) il resto sarà 0 e la colonna 0 (la prima),
                        #quando sarà 5 (sesta lettera) il resto sarà 0 e la colonna 0 (ma della seconda riga)
        riga = x // 5

        coordinataX = 200 + colonna * 92
        coordinataY = 20 + riga * 77 

        testoResoImg = FontLettere.render(lettera, True, "black")
        schermo.blit(testoResoImg, (coordinataX, coordinataY))
                
        if x % 4 == 0:
            if ParolaInserita == ParolaSceltaComputer:  
                print("Hai Vinto!")
                file = open("FileVincite.py", "a")
                file.write("Partita vinta!\n")
                file.close()
                pygame.quit()
            else:
                print("Hai perso...")
                file = open("FileVincite.py", "a")
                file.write("Partita persa!\n")
                file.close()
        
        pygame.display.flip()
        
pygame.quit()
