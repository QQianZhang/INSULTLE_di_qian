# INSULTLE
# Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

#libreria standard
import random
import time
from datetime import date
from pathlib import Path

#librerie pip
import pygame
from platformdirs import PlatformDirs

#moduli del mio package
from .resources import *

#inizializzazione di Pygame e del mixer audio
pygame.init() #fondamentale per il gioco (inializza tutto)
pygame.mixer.init() #fondamentale per i suoni

#configurazione delle directory (cartella del computer) dove vengono salvati i file per il gioco, si chiamerà "insultle"
dirs = PlatformDirs("insultle", ensure_exists=True)
percorsoFileVincente = dirs.user_data_dir + "/fileVincente.txt"

#caricamento e configurazione degli effetti sonori
suonoSconfitta = get_sound("suonoSconfitta.mp3")
suonoVittoria = get_sound("suonoVittoria.mp3")
#suonoSconfitta = pygame.mixer.Sound("src/insultle/suonoSconfitta.mp3")
#suonoVittoria = pygame.mixer.Sound("src/insultle/suonoVittoria.mp3")
suonoSconfitta.set_volume(0.7)
suonoVittoria.set_volume(0.7)

#variabili globali 
giocoFinito = False
parolaSceltaComputer = "" #cambia parola ogn volta che rinizia il gioco
testo = "INSULTLE\nVi siete divertiti a giocare ad Insultle??? \nSe sì lasciate una bella recensione (10/10)\n" #testo standard che verrà sempre scritto

#-------- NOME GIOCATORE, SFONDO E ALTRE SCRITTE ---------------- 
def nome():
    
    """
    Funzione che gestisce la schermata di inserimento del nome giocatore.
    Crea una finestra dove il giocatore può digitare il proprio nome.
    Restituisce il nome inserito quando si preme INVIO.
    """
    
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle")
    FontLettere = pygame.font.SysFont('Impact', 60)
    
    #carica l'immagine di sfondo in base alle variabili sopra scritte
    imgSfondo = get_image("sfondoINSULTLE.jpg")
    #imgSfondo = pygame.image.load("src/insultle/sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

    nome_giocatore = "" #stringa vuota in cui andrà aggiunto il nome

    running = True
    
    while running:
        #esami tutto ciò che succede
        for event in pygame.event.get():
            
            #se è la X rossa in alto a destra il gioco finisce
            if event.type == pygame.QUIT:
                #finisce il gioco
                running = False
            
            #se l'evento è un tasto premuto analizzo quale tasto è
            if event.type == pygame.KEYDOWN:
                
                #tasto invio
                if event.key == pygame.K_RETURN:
                    return nome_giocatore   #restituisce il nome
                
                #tasto canc
                elif event.key == pygame.K_BACKSPACE:
                    nome_giocatore = nome_giocatore[:-1] #cancella l'ultimo carattere
                #qualunque altro tasto
                else:
                    nome_giocatore += event.unicode #aggiunge il carattere digitato al nome del giocatoe

        #sfondo
        schermo.blit(imgSfondo,(0,0))

        #scritta
        testo = FontLettere.render("INSERISCI IL TUO NOME", True, "black")
        schermo.blit(testo,(150,200))

        #rettangolo bianco dove va visualizzato il nome
        rect_nome = pygame.Rect(200,300,400,80)
        pygame.draw.rect(schermo,"black",rect_nome)

        # nome scritto
        testo_nome = FontLettere.render(nome_giocatore,True,"white")
        schermo.blit(testo_nome,(rect_nome.x+10,rect_nome.y+10))

        pygame.display.flip()
    
#---------------- VITTORIA ----------------
def vittoria(nome_giocatore,tempo):
    """
    In caso di vittoria:
    - Ferma la musica di sottofondo
    - Riproduce il suono di vittoria
    - Salva il risultato su file
    """
    global giocoFinito #uso la variabile comune al tutto il codice (le def di solito creano altre variabili locali)
    pygame.mixer.music.stop() #fermo la musica di sottofondo
    suonoVittoria.play() #metto il fuono di vittoria
    giocoFinito = True #modifico la variabile globale
    with open(percorsoFileVincente, "w") as file: #apro il file
        #             testo predefinito
        file.write(f"{testo}BRAVO {nome_giocatore} HAI VINTO!! ci hai messo: {tempo}sec \n")
        #lo apro in w perchè non voglio un elenco continuo di "vinto" e "perso"

#---------------- SCONFITTA ----------------   
def sconfitta():
    """
    In caso di sconfitta:
    - Segnala la sconfitta
    - Salva su file la parola segreta
    """

    global giocoFinito #uso la variabile comune al tutto il codice (le def di solito creano altre variabili locali)
    global parolaSceltaComputer
    pygame.mixer.music.stop() #fermo la musica di sottofondo
    suonoSconfitta.play() #metto il fuono di sconfitta
    giocoFinito = True  #modifico la variabile globale   
    with open(percorsoFileVincente, "w") as file: #apro il file
        #             testo predefinito
        file.write(f"{testo} PECCATO, ritenta che sarai più fortunato!!! \nla parola era: {parolaSceltaComputer} \n")
        #lo apro in w perchè non voglio un elenco continuo di "vinto" e "perso"

#---------------- SCHERMATA INIZIALE ----------------
def main():
    
    """
    Mostra la schermata principale con le regole e due pulsanti:
    - GIOCA: avvia una partita normale con parola casuale
    - PAROLA DEL GIORNO: avvia una partita con la parola del giorno
    """

    #imposto le variabili per lo sfondo
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 
    FontLettere = pygame.font.SysFont('Impact', 60)
    
    #parole da indovinare
    ParoleComputer = ["RINCO", "SCEMO", "SCEMA", "TONTO", "TONTA", "PAZZO", "PAZZA", "LENTO", "LENTA", "EBETE", "PIGRO", "PIGRA", "ROZZO", "ROZZA", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO", "MATTA", "TARDO", "TARDA"]
    #carico le immagini
    imgSfondo = get_image("sfondoBIANCO.jfif")
    #imgSfondo = pygame.image.load("src/insultle/sfondoBIANCO.jfif") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))
    imgSfondo = get_image("RegoleInsultle.png")
    #imgRegole = pygame.image.load("src/insultle/RegoleInsultle.png") 
    imgRegole = pygame.transform.scale(imgRegole,(400,400))
    
    #creo due tasti che mi portano al gioco vero e proprio
    tasti_mouse = {
        "GIOCA": pygame.Rect(80,510, 170,70),
        "PAROLA DEL GIORNO": pygame.Rect(330,510, 460,70),
    }

    running = True
    while running:
        #mostro le regole e lo sfondo bianco
        schermo.blit(imgSfondo, (0, 0))
        schermo.blit(imgRegole, (200, 50))

        #disegno pulsanti
        for tasto, rect in tasti_mouse.items(): #cicla su tutti i tasti della tastiera virtuale
                                                #Ad ogni giro del ciclo:
                                                #tasto = la lettera o parola (es. "Q", "INVIO", "CANC")
                                                #rect = il rettangolo con posizione e dimensioni
            pygame.draw.rect(schermo, "green", rect) #disegna un rettangolo verde sullo schermo
                                                     #schermo = dove disegnare (la finestra di gioco)
                                                     #"green" = colore del rettangolo

            #rect = posizione e dimensione (x, y, larghezza, altezza)
            testo = FontLettere.render(tasto, True, "black")
            schermo.blit(testo, (rect.x + 10, rect.y + 5)) #posizione leggermente spostata dentro il rettangolo
        
        #analizzo ogni evento
        for event in pygame.event.get():

            #se clicco la X in altro a drestra
            if event.type == pygame.QUIT:
                #finisce il gioco
                running = False
            
            #se clicchi un tasto
            if event.type == pygame.KEYDOWN:
                #se è il tasto esc
                if event.key == pygame.K_ESCAPE:
                    #finisce il gioco
                    running = False
                    
            #se clicco un tasto del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos() #prende le coordinate (x, y) del punto dove ha cliccato

                for tasto, rect in tasti_mouse.items(): #cicla tutto i due tasti virtuali sopra creati
                    if rect.collidepoint(pos_mouse): #quando trova quello che corrisponde alla posizione cliccata
                        if tasto == "GIOCA":
                            parolaSpeciale = False
                            running = False #così la schermata iniziale non c'è più, sennò la schermata di gioco si sovrapponeva a quella iniziale
                            nome_giocatore = nome() #salviamo il nome del giocatore
                            
                            #sceglie una parola dalla lista ParoleComputer
                            parolaSceltaComputer = random.choice(ParoleComputer)
                            gioco(nome_giocatore, parolaSceltaComputer,parolaSpeciale, ParoleComputer) #va alla funzione gioco
                        elif tasto == "PAROLA DEL GIORNO":
                            running = False #così la schermata iniziale non c'è più, sennò la schermata di gioco si sovrapponeva a quella iniziale
                            parolaSpeciale = True
                            nome_giocatore = nome() #salviamo il nome del giocatore
                            #SELEZIONE PAROLA DEL GIORNO 
                            oggi = date.today().day
                            if oggi -1 == 27: #se è il 28esimo giorno
                                oggi = 14
                            elif oggi -1 == 28: #se è il 29esimo giorno
                                oggi = 15
                            elif oggi -1 == 29: #se è il 30esimo giorno
                                oggi = 16
                            elif oggi -1 == 30: #se è il 31esimo giorno
                                oggi = 17
                            
                            parolaSceltaComputer = ParoleComputer[(oggi-1)]
                            gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer) #va alla funzione gioco
                            
        
        #aggiorno lo schermo
        pygame.display.flip()
    
#---------------- GIOCO ----------------  
def gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer):
    
    """
    Funzione principale del gioco:
    - Gestisce la logica di Wordle con parole di 5 lettere
    - Permette input da tastiera fisica e tastiera virtuale cliccabile
    - Mostra feedback colorati (verde: lettera giusta posizione giusta, giallo: lettera giusta posizione sbagliata, rosso: lettera sbagliata)
    - Include timer, musica e gestione tentativi
    """
    
    #mi riferisco sempre alle variabili globali dell'intero gioco
    global giocoFinito


    #global parolaSceltaComputer
    
    giocoFinito = False
    
    #variabili sfondo
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
    pygame.display.set_caption("Insultle") 

    #carico sfondo
    imgSfondo = get_image("sfondoINSULTLE.jpg")
    #imgSfondo = pygame.image.load("src/insultle/sfondoINSULTLE.jpg") 
    imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))
    #carico immagine della casa che porterà il giocatore al menù iniziale
    imgCasa = get_image("casa.png")
    #imgCasa = pygame.image.load("src/insultle/casa.png") 
    imgCasa = pygame.transform.scale(imgCasa,(50,50))
    #carico immagine tasto retry che fa ripartire il gioco da capo
    imgRetry = get_image("retry.jpg")
    #imgRetry = pygame.image.load("src/insultle/retry.jpg") 
    imgRetry = pygame.transform.scale(imgRetry,(50,50))

    FontLettere = pygame.font.SysFont('Impact', 60)
    
   
    #apre il file vocabolario (le parole accettabili) e togli lo spazio finale da ogni parola
    with open( get_data("Vocabolario.txt"), "r") as vocabolario: #apre il file vocabolario in lettura
        paroleAccettabili = [p.strip().upper() for p in vocabolario.readlines()] #legge tutte le tighe e restituisce una lista con
                                                                                 #le parole accettabili senza \n (strip)

    
    
    #avvia la musica di sottofondo
    get_sound("suonoSottofondo.mp3")
    #pygame.mixer.music.load("src/insultle/suonoSottofondo.mp3")
    pygame.mixer.music.set_volume(0.4) #suonoSottofondo.pygame.mixer.music.set_volume(0.4) sbagliato perche mixer non si assegna alle variabili
    pygame.mixer.music.play(-1) #rendo quella musica un loop

    # ---------------- VARIABILI ----------------
    listaParola = []
    tentativi = []
    
    maxTentativi = 6

# ---------------- TASTIERA CLICCABILE ----------------
#dizionario, ad ogni lettera viene corrisposto un rettangolo di dimensioni (circa) 60x70 e la posizione dove si trova la lettera nella tastiera
    tasti_mouse = {
        "casa": pygame.Rect(650,20,50,50),
        "retry": pygame.Rect(710,20,50,50),
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
    
    running = True
    while running:
                # ---------------- DISEGNO TIMER ----------------
        #aggiorna e disegna il timer (solo se il gioco non è finito)
        if not giocoFinito :
            
            #calcolo il tempo trascorso
            tempoAttuale = (pygame.time.get_ticks() - tempo_inizio) // 1000
            # // 1000 serve per trasformare i millisecondi in secondi0.
        #creo il testo con il tempo
        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
            
        #disegno il timer in alto a sinistra dello schermo
        schermo.blit(testoTimer, (50, 20))        

        #pygame.display.flip()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            # ---------------- MOUSE ----------------
            #se viene fatto click con il mouse ricavo la posizione di dove si trovava l'indicatore al momento del click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                #scorre tutte le lettere e i rettangoli presenti nel dizionario e se l'indicatore si trova all'interno del rettangolo entra nel ciclo if
                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        
                        #se il mouse si trova sopra il tasto invio
                        if tasto == "INVIO":
                            if giocoFinito:
                                continue
                            #la parola sarà composta dagli elementi della lista (le lettere scritte dall'utente)
                            parolaInserita = "".join(listaParola)
                            #se quella lista (quindi la parola) è lunga 5 ed è accettabile
                            if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                                #contiamo un tentativo
                                tentativi.append(parolaInserita)
                                #e svuotiamo la lista delle lettere
                                listaParola = []
                                
                                #se la parola è quella scelta dal pc
                                if parolaInserita == parolaSceltaComputer:
                                    #chiamo al funzione vittoria
                                    vittoria(nome_giocatore, tempoAttuale)
                                
                                #se sono arrivata al massimo dei tentativi
                                elif len(tentativi) == maxTentativi:
                                    #ho perso, chiamo la funzione sconfitta
                                    sconfitta()
                                    
                        #se il tasto è canc
                        elif tasto == "CANC":
                            if giocoFinito:
                                continue
                            #se la lista non è vuota
                            if len(listaParola) > 0:
                                listaParola.pop() #eliminiamo l'ultima lettera inserita
                        #se clicco il tasto casa allora il gioco si interrompre e viene visualizzata la schermata principale
                        elif tasto == "casa":
                            running = False
                            main()
                        #se clicco il tasto riprova il gioco ricomincia da capo, la parola da indovinare cambia solo se non è la parola del giorno
                        elif tasto == "retry":
                            running = False
                            if parolaSpeciale == False:
                                parolaSceltaComputer = random.choice(ParoleComputer)
                            gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer)
                        #se è un qualunque altro tasto
                        else:
                            #è la lista non è piena (dato che le parole sono max da 5)
                            if len(listaParola) < 5:
                                #aggiungo la lettere alla lista
                                listaParola.append(tasto)

            # ---------------- TASTIERA ----------------
            if event.type == pygame.KEYDOWN: #se premo un tasto
                    
                if event.key == pygame.K_ESCAPE: #se il tasto è esc si chiude il gioco
                    running = False
                
            if event.type == pygame.KEYDOWN and not giocoFinito:

                if event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                    listaParola.pop()
                #se premo invio controlla che la parola sia lunga 5 caratteri e sia una parola accettabile
                elif event.key == pygame.K_RETURN: 
                    parolaInserita = "".join(listaParola)
                    if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                        
                        tentativi.append(parolaInserita)
                        listaParola = []
                        
                        # ---------------- CONTROLLO VITTORIA ----------------
                        #se la parola è corretta il giocatore ha vinto
                        if parolaInserita == parolaSceltaComputer: 
                            vittoria(nome_giocatore,tempoAttuale) 
                                
                        # ---------------- CONTROLLO SCONFITTA ----------------
                        #se la parola è sbagliata e il giocatore ha usato tutti i suoi tentativi ha perso
                        elif len(tentativi) == maxTentativi:
                            sconfitta()
                
                #se premo altro
                else:
                    #associo il codice di quel tasto ad un carattere
                    caratterePremuto = event.unicode
                    #se quel carattere è una lettera e la lista non è piena
                    if caratterePremuto.upper() in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(listaParola) < 5:
                        #la aggiungp
                        listaParola.append(caratterePremuto.upper())
                        
            #permette di rigiocare premendo R dopo la fine della partita            
            if event.type == pygame.KEYDOWN and giocoFinito : #è implicito che "and giocoFinito" significa che giocoFinito == True
                #se premo il tasto r (restart)
                if event.key == pygame.K_r:
                    #gioco si interrompe
                    running = False
                    #richiamo la funzione gioco perchè deve ricominciare
                    gioco(nome_giocatore,parolaSceltaComputer, parolaSpeciale, ParoleComputer)
            
        #mostro lo sfondo
        schermo.blit(imgSfondo, (0, 0))
        schermo.blit(imgCasa,(650,20))
        schermo.blit(imgRetry,(710,20))

        # Disegno i tentativi colorati (verde, giallo, rosso)
        for riga in range(len(tentativi)): # == for x in range (0,5), per ogni tentativo fatto
            parola = tentativi[riga] #prendo la parola tentativo
            segreta = list(parolaSceltaComputer) #copio la parola segreta come lista
            colori = [""] * 5 #crea lista vuota per 5 colori

            # Verde
            for i in range(5):
                if parola[i] == segreta[i]: #se nella lista della parola del pc e dell'utente abbiamo la stessa lettera
                                            #ad una stessa pos
                    colori[i] = (0, 200, 0) #verde
                    segreta[i] = "" #rimpiazzo l'elemento della lista con il nulla, 

            # Giallo / Rosso
            for i in range(5):
                if colori[i] == "": #se non è verde
                    if parola[i] in segreta: #e quella lettera c'è nella parola
                        colori[i] = (220, 200, 0) #allora giallo
                        segreta[segreta.index(parola[i])] = "" #rimuovi la prima che trova
                    else:
                        colori[i] = (200, 0, 0) #sennò rosso

            # Disegna caselle
            for num in range(5):
                #calcolo le posizioni 
                coordinataX = 200 + num * 92
                coordinataY = 20 + riga * 77
                #disegno il rect colorato alle pos date 
                pygame.draw.rect(schermo, colori[num], (coordinataX, coordinataY, 70, 70))
                #ci scrivo la lettera sopra
                testo = FontLettere.render(parola[num], True, "black")
                schermo.blit(testo, (coordinataX + 15, coordinataY))

        # ---------------- DISEGNO PAROLA IN CORSO ----------------
        # Disegno la parola in corso (listaParola)
        rigaAttuale = len(tentativi) #trova la linea in cui stiamo scrivendo 
        for num in range(len(listaParola)):
            #calcolo le coordinate 
            coordinataX = 200 + num * 92
            coordinataY = 20 + rigaAttuale * 77
            #disegno rect bianco per la casella
            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            #ci disegno la lettera alla pos num della lista in nero
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))

        # Disegno il timer
        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        schermo.blit(testoTimer, (50, 20))

        # Aggiorno lo schermo
        pygame.display.flip()



    pygame.quit() #chiude Pygame quando il gioco termina

# #------------------------------------
    
if __name__ == "__main__":
    main() #avvia la schermata iniziale
    #pygame.quit() #chiude Pygame quando il gioco termina
