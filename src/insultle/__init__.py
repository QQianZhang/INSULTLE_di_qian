# INSULTLE
# Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

import pygame
import random
import time
from datetime import date
from platformdirs import PlatformDirs
from pathlib import Path
#from FileClassifica import classifica 

pygame.init()
pygame.mixer.init() 

#dirs = PlatformDirs("insultle", ensure_exists=True)

suonoSconfitta = pygame.mixer.Sound("suonoSconfitta.mp3")
suonoVittoria = pygame.mixer.Sound("suonoVittoria.mp3")
suonoSconfitta.set_volume(0.7)
suonoVittoria.set_volume(0.7)

giocoFinito = False
parolaSceltaComputer = ""
testo = "INSULTLE\nVi siete divertiti a giocare ad Insultle??? \nSe sì lasciate una bella recensione (10/10)\n"

#-------- NOME GIOCATORE, SFONDO E ALTRE SCRITTE ---------------- 
def nome():
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle")
    FontLettere = pygame.font.SysFont('Impact', 60)

    imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    nome_giocatore = ""

    running = True
    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return nome_giocatore   # restituisce il nome

                elif event.key == pygame.K_BACKSPACE:
                    nome_giocatore = nome_giocatore[:-1]

                else:
                    nome_giocatore += event.unicode

        # sfondo
        schermo.blit(imgSfondo,(0,0))

        # scritta
        testo = FontLettere.render("INSERISCI IL TUO NOME", True, "black")
        schermo.blit(testo,(150,200))

        # rettangolo bianco
        rect_nome = pygame.Rect(200,300,400,80)
        pygame.draw.rect(schermo,"black",rect_nome)

        # nome scritto
        testo_nome = FontLettere.render(nome_giocatore,True,"white")
        schermo.blit(testo_nome,(rect_nome.x+10,rect_nome.y+10))

        pygame.display.flip()
    
#---------------- VITTORIA ----------------
def vittoria(nome_giocatore,tempo):
    global giocoFinito
    pygame.mixer.music.stop()
    suonoVittoria.play()
    giocoFinito = True
    with open("fileVincente.txt", "a") as file:
       file.write(f"{testo}BRAVO {nome_giocatore} HAI VINTO!! ci hai messo: {tempo}sec \n")

#---------------- SCONFITTA ----------------   
def sconfitta():
    global giocoFinito
    global parolaSceltaComputer
    giocoFinito = True
    print("STUPIDOOO")
    
    with open("fileVincente.txt", "a") as file:
       file.write(f"{testo} PECCATO, ritenta che sarai più fortunato!!! \nla parola era: {parolaSceltaComputer} \n")


#---------------- SCHERMATA INIZIALE ----------------
def schermataIniziale():
    #imposto lo sfondo
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    FontLettere = pygame.font.SysFont('Impact', 60)

    imgSfondo = pygame.image.load("sfondoBIANCO.jfif") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))
    imgRegole = pygame.image.load("RegoleInsultle(1).png") 
    imgRegole = pygame.transform.scale(imgRegole,(400,400))
    #creo due tasti che mi portano al gioco vero e proprio
    tasti_mouse = {
        "GIOCA": pygame.Rect(80,510, 170,70),
        "PAROLA DEL GIORNO": pygame.Rect(330,510, 460,70),
    }

    running = True
    while True:
        #mostro le regole e lo sfondo bianco
        schermo.blit(imgSfondo, (0, 0))
        schermo.blit(imgRegole, (200, 50))

        # Disegno pulsanti
        for tasto, rect in tasti_mouse.items():
            pygame.draw.rect(schermo, "green", rect)
            testo = FontLettere.render(tasto, True, "black")
            schermo.blit(testo, (rect.x + 10, rect.y + 5))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            #se clicco un tasto del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        if tasto == "GIOCA":
                            running = False #così la schermata iniziale non c'è più, sennò la schermata di gioco si sovrapponeva a quella iniziale
                            nome_giocatore = nome()
                            gioco(nome_giocatore) #va alla funzione gioco
                        elif tasto == "PAROLA DEL GIORNO":
                            running = False
                            nome_giocatore = nome()
                            parolaDelGiorno(nome_giocatore) #va alla funzione parola del giorno

        pygame.display.flip()
    
#---------------- GIOCO ----------------  
def gioco(nome_giocatore):
    
    global giocoFinito
    global parolaSceltaComputer
    
    giocoFinito = False
    
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    FontLettere = pygame.font.SysFont('Impact', 60)
    
    ParoleComputer = ["RINCO", "SCEMO", "SCEMA", "TONTO", "TONTA", "PAZZO", "PAZZA", "LENTO", "LENTA", "EBETE", "PIGRO", "PIGRA", "ROZZO", "ROZZA", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO", "MATTA", "TARDO", "TARDA"]
    
    #apre il file vocabolario  e togli lo spazio finale da ogni parola
    with open("Vocabolario.txt", "r") as vocabolario:
        paroleAccettabili = [p.strip().upper() for p in vocabolario.readlines()]

    
    parolaSceltaComputer = random.choice(ParoleComputer)
    print("PAROLA SEGRETA:", parolaSceltaComputer)
    
    pygame.mixer.music.load("suonoSottofondo.mp3")
    pygame.mixer.music.set_volume(0.4) #suonoSottofondo.pygame.mixer.music.set_volume(0.4) sbagliato perche mixer non si assegna alle variabili
    pygame.mixer.music.play(-1)

    # ---------------- VARIABILI ----------------
    listaParola = []
    tentativi = []
    
    maxTentativi = 6

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

# ---------------- TIMER ----------------
    FontTimer = pygame.font.SysFont('Impact', 40)  
    tempo_inizio = pygame.time.get_ticks()
    tempoAttuale = 0
    # Il timer inizia il momento esatto (in millisecondi) in cui parte la partita
    #tempo_salvato = False  
    # Serve per evitare di scrivere più volte il tempo nel file
    running = True
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
                            parolaInserita = "".join(listaParola)
                            if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                                tentativi.append(parolaInserita)
                                listaParola = []

                                if parolaInserita == parolaSceltaComputer:
                                    vittoria(nome_giocatore, tempoAttuale)

                                elif len(tentativi) == maxTentativi:
                                    sconfitta()

                        elif tasto == "CANC":
                            if len(listaParola) > 0:
                                listaParola.pop()

                        else:
                            if len(listaParola) < 5:
                                listaParola.append(tasto)

            # ---------------- TASTIERA ----------------
            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_ESCAPE:
                    running = False
                
            if event.type == pygame.KEYDOWN and not giocoFinito:

                if event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                    listaParola.pop()
                
                elif event.key == pygame.K_RETURN:
                    parolaInserita = "".join(listaParola)
                    if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                        
                        tentativi.append(parolaInserita)
                        listaParola = []

                        # ---------------- CONTROLLO VITTORIA ----------------
                        if parolaInserita == parolaSceltaComputer: 
                            vittoria(nome_giocatore,tempoAttuale) 
                                
                        # ---------------- CONTROLLO SCONFITTA ----------------
                        elif len(tentativi) == maxTentativi:
                            sconfitta()

                else:
                    letteraPremuta = event.unicode
                    if letteraPremuta.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(listaParola) < 5:
                        listaParola.append(letteraPremuta.upper())
                        
            if event.type == pygame.KEYDOWN and giocoFinito:
                if event.key == pygame.K_r:
                    running = False 
                    gioco(nome_giocatore)
                

            
        #mostro lo sfondo
        schermo.blit(imgSfondo, (0, 0))

        # Disegno i tentativi colorati (verde, giallo, rosso)
        for riga in range(len(tentativi)):
            parola = tentativi[riga]
            segreta = list(parolaSceltaComputer)
            colori = [""] * 5

            # Verde
            for i in range(5):
                if parola[i] == segreta[i]:
                    colori[i] = (0, 200, 0)
                    segreta[i] = None

            # Giallo / Rosso
            for i in range(5):
                if colori[i] == "":
                    if parola[i] in segreta:
                        colori[i] = (220, 200, 0)
                        segreta[segreta.index(parola[i])] = None
                    else:
                        colori[i] = (200, 0, 0)

            # Disegna caselle
            for num in range(5):
                coordinataX = 200 + num * 92
                coordinataY = 20 + riga * 77
                pygame.draw.rect(schermo, colori[num], (coordinataX, coordinataY, 70, 70))
                testo = FontLettere.render(parola[num], True, "black")
                schermo.blit(testo, (coordinataX + 15, coordinataY))

        # Disegno la parola in corso (listaParola)
        rigaAttuale = len(tentativi)
        for num in range(len(listaParola)):
            coordinataX = 200 + num * 92
            coordinataY = 20 + rigaAttuale * 77
            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))

        # Disegno il timer
        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        schermo.blit(testoTimer, (50, 20))

        # Aggiorno lo schermo
        pygame.display.flip()

        

        # ---------------- DISEGNO PAROLA IN CORSO ----------------
        rigaAttuale = len(tentativi)

        for num in range(len(listaParola)):

            colonna = num

            coordinataX = 200 + colonna * 92
            coordinataY = 20 + rigaAttuale * 77

            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))

        # ---------------- DISEGNO TIMER ----------------
        #tempoAttuale = 0
        if not giocoFinito :

            tempoAttuale = (pygame.time.get_ticks() - tempo_inizio) // 1000
            # Calcolo il tempo trascorso:
            # // 1000 serve per trasformare i millisecondi in secondi0.

        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        # Creo il testo con il tempo
        
        schermo.blit(testoTimer, (50, 20))
        # Disegno il timer in alto a sinistra dello schermo
        

        pygame.display.flip()

    #pygame.quit()
def parolaDelGiorno(nome_giocatore): #il codice è esattamente identico alla funzione gioco eccetto che la parola non viene scelta a caso ma in base al giorno del mese ed è uguale per tutta la giornata
    
    global giocoFinito
    global parolaSceltaComputer
    
    giocoFinito = False
    
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    FontLettere = pygame.font.SysFont('Impact', 60)
    
    ParoleComputer = ["RINCO", "SCEMO", "SCEMA", "TONTO", "TONTA", "PAZZO", "PAZZA", "LENTO", "LENTA", "EBETE", "PIGRO", "PIGRA", "ROZZO", "ROZZA", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO", "MATTA", "TARDO", "TARDA"]
    
    #apre il file vocabolario  e togli lo spazio finale da ogni parola
    with open("Vocabolario.txt", "r") as vocabolario:
        paroleAccettabili = [p.strip().upper() for p in vocabolario.readlines()]

    oggi = date.today().day
    if oggi -1 == 27:
        oggi = 14
    elif oggi -1 == 28:
        oggi = 15
    elif oggi -1 == 29:
        oggi = 16
    elif oggi -1 == 30:
        oggi = 17
        
    parolaSceltaComputer = ParoleComputer[(oggi-1)]
    print("PAROLA SEGRETA:", parolaSceltaComputer)
    
    pygame.mixer.music.load("suonoSottofondo.mp3")
    pygame.mixer.music.set_volume(0.4) #suonoSottofondo.pygame.mixer.music.set_volume(0.4) sbagliato perche mixer non si assegna alle variabili
    pygame.mixer.music.play(-1)

    # ---------------- VARIABILI ----------------
    listaParola = []
    tentativi = []
    
    maxTentativi = 6

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

# ---------------- TIMER ----------------
    FontTimer = pygame.font.SysFont('Impact', 40)  
    tempo_inizio = pygame.time.get_ticks()
    tempoAttuale = 0
    # Il timer inizia il momento esatto (in millisecondi) in cui parte la partita
    #tempo_salvato = False  
    # Serve per evitare di scrivere più volte il tempo nel file
    running = True
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
                            parolaInserita = "".join(listaParola)
                            if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                                tentativi.append(parolaInserita)
                                listaParola = []

                                if parolaInserita == parolaSceltaComputer:
                                    vittoria(nome_giocatore, tempoAttuale)

                                elif len(tentativi) == maxTentativi:
                                    sconfitta()

                        elif tasto == "CANC":
                            if len(listaParola) > 0:
                                listaParola.pop()

                        else:
                            if len(listaParola) < 5:
                                listaParola.append(tasto)

            # ---------------- TASTIERA ----------------
            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_ESCAPE:
                    running = False
                
            if event.type == pygame.KEYDOWN and not giocoFinito:

                if event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                    listaParola.pop()
                
                elif event.key == pygame.K_RETURN:
                    parolaInserita = "".join(listaParola)
                    if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                        
                        tentativi.append(parolaInserita)
                        listaParola = []

                        # ---------------- CONTROLLO VITTORIA ----------------
                        if parolaInserita == parolaSceltaComputer: 
                            vittoria(nome_giocatore,tempoAttuale) 
                                
                        # ---------------- CONTROLLO SCONFITTA ----------------
                        elif len(tentativi) == maxTentativi:
                            sconfitta()

                else:
                    letteraPremuta = event.unicode
                    if letteraPremuta.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(listaParola) < 5:
                        listaParola.append(letteraPremuta.upper())
                        
            if event.type == pygame.KEYDOWN and giocoFinito:
                if event.key == pygame.K_r:
                    running = False 
                    gioco(nome_giocatore)
                

            
        #mostro lo sfondo
        schermo.blit(imgSfondo, (0, 0))

        # Disegno i tentativi colorati (verde, giallo, rosso)
        for riga in range(len(tentativi)):
            parola = tentativi[riga]
            segreta = list(parolaSceltaComputer)
            colori = [""] * 5

            # Verde
            for i in range(5):
                if parola[i] == segreta[i]:
                    colori[i] = (0, 200, 0)
                    segreta[i] = None

            # Giallo / Rosso
            for i in range(5):
                if colori[i] == "":
                    if parola[i] in segreta:
                        colori[i] = (220, 200, 0)
                        segreta[segreta.index(parola[i])] = None
                    else:
                        colori[i] = (200, 0, 0)

            # Disegna caselle
            for num in range(5):
                coordinataX = 200 + num * 92
                coordinataY = 20 + riga * 77
                pygame.draw.rect(schermo, colori[num], (coordinataX, coordinataY, 70, 70))
                testo = FontLettere.render(parola[num], True, "black")
                schermo.blit(testo, (coordinataX + 15, coordinataY))

        # Disegno la parola in corso (listaParola)
        rigaAttuale = len(tentativi)
        for num in range(len(listaParola)):
            coordinataX = 200 + num * 92
            coordinataY = 20 + rigaAttuale * 77
            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))

        # Disegno il timer
        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        schermo.blit(testoTimer, (50, 20))

        # Aggiorno lo schermo
        pygame.display.flip()

        

        # ---------------- DISEGNO PAROLA IN CORSO ----------------
        rigaAttuale = len(tentativi)

        for num in range(len(listaParola)):

            colonna = num

            coordinataX = 200 + colonna * 92
            coordinataY = 20 + rigaAttuale * 77

            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))

        # ---------------- DISEGNO TIMER ----------------
        #tempoAttuale = 0
        if not giocoFinito :

            tempoAttuale = (pygame.time.get_ticks() - tempo_inizio) // 1000
            # Calcolo il tempo trascorso:
            # // 1000 serve per trasformare i millisecondi in secondi0.

        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        # Creo il testo con il tempo
        
        schermo.blit(testoTimer, (50, 20))
        # Disegno il timer in alto a sinistra dello schermo
        

        pygame.display.flip()

    #pygame.quit()
#------------------------------------
    
if __name__ == "__main__":
    schermataIniziale()
    pygame.quit()
