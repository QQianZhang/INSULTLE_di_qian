# INSULTLE
# Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

import pygame
import random

def main() -> None:
    pygame.init()

    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    FontLettere = pygame.font.SysFont('Impact', 60)
    FontMessaggio = pygame.font.SysFont('Arial', 40)

    ParoleComputer = ["RINCO", "SCEMO", "TONTO", "PAZZO", "LENTO", "EBETE", "PIGRO", "ROZZO", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO"]

    ParolaSceltaComputer = random.choice(ParoleComputer)
    print("PAROLA SEGRETA:", ParolaSceltaComputer)
    
    #variabili---------------------------------
    listaParola = []
    tentativi = []
    max_tentativi = 6
    gioco_finito = False
    messaggio_finale = ""

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN and not gioco_finito:
                
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                    listaParola.pop()
                
                elif event.key == pygame.K_RETURN:
                    if len(listaParola) == 5:
                        
                        parolaInserita = "".join(listaParola)
                        tentativi.append(parolaInserita)
                        listaParola = []

                        # CONTROLLO VITTORIA
                        if parolaInserita == ParolaSceltaComputer:
                            messaggio_finale = "HAI VINTO!"
                            gioco_finito = True
                        
                        # CONTROLLO SCONFITTA
                        elif len(tentativi) == max_tentativi:
                            messaggio_finale = "HAI PERSO! Era: " + ParolaSceltaComputer
                            gioco_finito = True

                else:
                    letteraPremuta = event.unicode
                    if letteraPremuta.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(listaParola) < 5:
                        listaParola.append(letteraPremuta.upper())
                        
        #mostro lo sfondo
        schermo.blit(imgSfondo, (0, 0))

        # DISEGNO TENTATIVI COLORATI
        for riga in range(len(tentativi)):

            parola = tentativi[riga]
            listaSceltaComputer = list(ParolaSceltaComputer)
            for num in range(5):

                colonna = num

                coordinataX = 200 + colonna * 92
                coordinataY = 20 + riga * 77

                if parola[num] == listaSceltaComputer[num]:
                    colore = (0, 200, 0)# verde
                    listaSceltaComputer[num] = ""
            #for mun in range(5):
                elif parola[num] in listaSceltaComputer:
                    colore = (220, 200, 0)  # giallo
                    
                else:
                    colore = (200, 0, 0)  # rosso


                pygame.draw.rect(schermo, colore, (coordinataX, coordinataY, 70, 70))

                testo = FontLettere.render(parola[num], True, "black")
                schermo.blit(testo, (coordinataX + 15, coordinataY))
        

        # DISEGNO PAROLA IN CORSO (non ancora inviata)
        riga_corrente = len(tentativi)

        for num in range(len(listaParola)):

            colonna = num

            coordinataX = 200 + colonna * 92
            coordinataY = 20 + riga_corrente * 77

            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))


        # MESSAGGIO FINALE
        if gioco_finito:
            testo_finale = FontMessaggio.render(messaggio_finale, True, "black")
            schermo.blit(testo_finale, (200, 600))

        pygame.display.flip()

    pygame.quit()

#------------------------------------
    
if __name__ == "__main__":
    print(main())