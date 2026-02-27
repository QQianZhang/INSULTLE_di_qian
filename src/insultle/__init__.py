# INSULTLE
# Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

import pygame
import random
#from pathlib import Path

def main() -> None:
    pygame.init()

    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    FontLettere = pygame.font.SysFont('Impact', 60)
#    
    vocabolario = open("Vocabolario.txt", "r")
    ParoleComputer = ["RINCO", "SCEMO", "TONTO", "PAZZO", "LENTO", "EBETE", "PIGRO", "ROZZO", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO"]
    ParoleAccUtente = []
    for riga in vocabolario:
        ParoleAccUtente.append(riga.strip())
    
    ParolaSceltaComputer = random.choice(ParoleComputer)
    print("PAROLA SEGRETA:", ParolaSceltaComputer)
    
    #variabili---------------------------------
    listaParola = []
    tentativi = []
    maxTentativi = 6
    giocoFinito = False
    #messaggioFinale = ""

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN and not giocoFinito:
                
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
                            #messaggioFinale = "HAI VINTO!"
                            giocoFinito = True
                            print("Hai Vinto!")
                            file = open("FileVincite.txt", "a")
                            file.write("Partita vinta!\n")
                            file.close()
                        
                        # CONTROLLO SCONFITTA
                        elif len(tentativi) == maxTentativi:
                            #messaggioFinale = "HAI PERSO! Era: " + ParolaSceltaComputer
                            giocoFinito = True
                            print("STUPIDOOO!")
                            file = open("FileVincite.txt", "a")
                            file.write(f"Ritenta, sarai più fortunato\nla parola era {ParolaSceltaComputer}")
                            file.close()

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
        rigaAttuale = len(tentativi)

        for num in range(len(listaParola)):

            colonna = num

            coordinataX = 200 + colonna * 92
            coordinataY = 20 + rigaAttuale * 77

            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))


        # MESSAGGIO FINALE
#         conta = 0
#         if giocoFinito and conta == 0:
# #             testo_finale = FontMessaggio.render(messaggioFinale, True, "black")
# #             schermo.blit(testo_finale, (200, 600))
#             print("Hai Vinto!")
#             file = open("FileVincite.txt", "a")
#             file.write("Partita vinta!\n")
#             conta += 1
#             file.close()
#         else:
#             file = open("FileVincite.txt", "a")
#             file.write("Ritenta, sarai più fortunato\n")
#             conta += 1
#             file.close()

        pygame.display.flip()

    pygame.quit()

#------------------------------------
    
if __name__ == "__main__":
    print(main())