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

    FontLettere = pygame.font.SysFont('Impact', 60)

    imgSfondo = pygame.image.load("sfondo-verde-chiaro.webp") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    tasti_mouse = {
        "GIOCA": pygame.Rect(67,510, 200,70),
        "CLASSIFICA": pygame.Rect(300,510, 300,70),
    }

    running = True
    while running:

        schermo.blit(imgSfondo, (0, 0))

        # Disegno pulsanti
        for tasto, rect in tasti_mouse.items():
            pygame.draw.rect(schermo, "white", rect)
            testo = FontLettere.render(tasto, True, "black")
            schermo.blit(testo, (rect.x + 10, rect.y + 5))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        if tasto == "GIOCA":
                            gioco()
                        elif tasto == "CLASSIFICA":
                            print("CLASSIFICA")

        pygame.display.flip()

    pygame.quit()
    
    
def gioco() -> None:
    
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
        ParoleAccUtente.append(riga.strip())
    
    ParolaSceltaComputer = random.choice(ParoleComputer)
    print("PAROLA SEGRETA:", ParolaSceltaComputer)
    pygame.mixer.init() 
    pygame.mixer.music.load("suonoSottofondo.mp3")
    pygame.mixer.music.set_volume(0.4) #suonoSottofondo.pygame.mixer.music.set_volume(0.4) sbagliato perche mixer non si assegna alle variabili
    pygame.mixer.music.play(-1)
    
    suonoSconfitta = pygame.mixer.Sound("suonoSconfitta.mp3")
    suonoVittoria = pygame.mixer.Sound("suonoVittoria.mp3")
    suonoSconfitta.set_volume(0.7)
    suonoVittoria.set_volume(0.7)
    

    #variabili---------------------------------
    listaParola = []
    tentativi = []
    maxTentativi = 6
    giocoFinito = False
    tempo_finale = 0
    #messaggioFinale = ""
# ---------------- TASTIERA CLICCABILE ----------------
#dizionario, ad ogni lettera viene corrisposto un rettangolo di dimensioni (circa) 60x70 e la posizione dove si trova la lettera nella tastiera
    tasti_mouse = {
        # PRIMA RIGA
        "Q": pygame.Rect(67,510, 65,70),
        "W": pygame.Rect(138,510, 65,70),
        "E": pygame.Rect(210,510, 60,70),
        "R": pygame.Rect(275,510, 60,70),
        "T": pygame.Rect(345,510, 60,70),
        "Y": pygame.Rect(410,510, 60,70),
        "U": pygame.Rect(480,510, 60,70),
        "I": pygame.Rect(547,510, 60,70),
        "O": pygame.Rect(615,510, 60,70),
        "P": pygame.Rect(680,510, 60,70),

        # SECONDA RIGA
        "A": pygame.Rect(100,585, 60,70),
        "S": pygame.Rect(170,585, 60,70),
        "D": pygame.Rect(240,585, 60,70),
        "F": pygame.Rect(310,585, 60,70),
        "G": pygame.Rect(380,585, 60,70),
        "H": pygame.Rect(450,585, 60,70),
        "J": pygame.Rect(515,585, 60,70),
        "K": pygame.Rect(583,585, 60,70),
        "L": pygame.Rect(650,585, 60,70),

        # TERZA RIGA
        "INVIO": pygame.Rect(70,660, 95,70),
        "Z": pygame.Rect(170,660, 60,70),
        "X": pygame.Rect(240,660, 60,70),
        "C": pygame.Rect(310,660, 60,70),
        "V": pygame.Rect(380,660, 60,70),
        "B": pygame.Rect(450,660, 60,70),
        "N": pygame.Rect(515,660, 60,70),
        "M": pygame.Rect(583,660, 60,70),
        "CANC": pygame.Rect(650,660, 95,70),
    }

    running = True
# ---------------- TIMER ----------------
    FontTimer = pygame.font.SysFont('Impact', 40)  
    tempo_inizio = pygame.time.get_ticks()  
    # Il timer inizia il momento esatto (in millisecondi) in cui parte la partita
    tempo_salvato = False  
    # Serve per evitare di scrivere più volte il tempo nel file

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # ---------------- MOUSE ----------------
            #se viene fatto click con il mouse ricavo la posizione di dove si trovava l'indicatore al momento del click
            if event.type == pygame.MOUSEBUTTONDOWN and not giocoFinito:
                pos_mouse = pygame.mouse.get_pos()
                #scorre tutte le lettere e i rettangoli presenti nel dizionario e se l'indicatore si trova all'interno del rettangolo entra nel ciclo if
                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        
                        if tasto == "INVIO":
                            if len(listaParola) == 5:
                                parolaInserita = "".join(listaParola)
                                tentativi.append(parolaInserita)
                                listaParola = []

                                if parolaInserita == ParolaSceltaComputer:
                                    giocoFinito = True
                                    print("Hai Vinto!")

                                elif len(tentativi) == maxTentativi:
                                    giocoFinito = True
                                    print("STUPIDOOO!")

                        elif tasto == "CANC":
                            if len(listaParola) > 0:
                                listaParola.pop()

                        else:
                            if len(listaParola) < 5:
                                listaParola.append(tasto)

            # ---------------- TASTIERA ----------------
            if event.type == pygame.KEYDOWN:

                if event.type == pygame.QUIT:
                    running = False
                    
                if event.key == pygame.K_ESCAPE:
                    running = False
                
            if event.type == pygame.KEYDOWN and not giocoFinito:

                if event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
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
                            pygame.mixer.music.stop()
                            suonoVittoria.play()
                        
                        # CONTROLLO SCONFITTA
                        elif len(tentativi) == maxTentativi:
                            #messaggioFinale = "HAI PERSO! Era: " + ParolaSceltaComputer
                            giocoFinito = True
                            print("STUPIDOOO!")
                            file = open("FileVincite.txt", "a")
                            file.write(f"Ritenta, sarai più fortunato\nla parola era {ParolaSceltaComputer}")
                            file.close()
                            pygame.mixer.music.stop()
                            suonoSconfitta.play()

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

                    
                elif parola[num] != listaSceltaComputer[num] and parola[num] not in listaSceltaComputer:
                    colore = (200, 0, 0)  # rosso
                    #listaSceltaComputer[listaSceltaComputer.index(parola[num])] = ""
                    
                elif parola[num] != listaSceltaComputer[num] and parola[num] in listaSceltaComputer:
                    colore = (220, 200, 0) #giallo

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

        # ---------------- DISEGNO TIMER ----------------

        if not giocoFinito:

            tempo_attuale = (pygame.time.get_ticks() - tempo_inizio) // 1000
            # Calcolo il tempo trascorso:
            # // 1000 serve per trasformare i millisecondi in secondi

        else:
            tempo_attuale = tempo_finale
            # Mostro il tempo finale

        testo_timer = FontTimer.render(f"{tempo_attuale}s", True, (0, 0, 0))
        # Creo il testo con il tempo

        schermo.blit(testo_timer, (50, 20))
        # Disegno il timer in alto a sinistra dello schermo
        

        pygame.display.flip()

    pygame.quit()

#------------------------------------
    
if __name__ == "__main__":
    main()
