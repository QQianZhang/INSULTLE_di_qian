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
            
ParoleComputer = ["RINCO", "SCEMO", "TONTO", "PAZZO", "LENTO", "EBETE", "PIGRO", "ROZZO", "FOLLE", "MOLLE", "ASINO", "CAPRA", "CAGNA", "FESSO", "VERME", "PIRLA", "CLOWN", "MATTO"]
ParoleAccUtente = ["acqua", "adulto", "aereo", "aglio", "aiuto", "album", "amaro", "amico", "amica", "amore", "ampio", "anima", "anno", "ansia", "apice", "aroma", "asino", "aspro", "attua", "avere", "bacio", "banca", "barca", "basso", "beato", "bella", "bello", "benda", "birra", "bocca", "bolle", "bordo", "bosco", "bravo", "breve", "bruno", "buono", "burro", "caldo", "calma", "calvo", "campo", "canto", "capra", "carne", "carro", "carta", "cassa", "cella", "censo", "cento", "certo", "cielo", "cifra", "citta", "colpa", "collo", "conto", "copra", "corda", "corpo", "corso", "costa", "crema", "cuore", "danno", "degno", "denso", "dente", "detto", "dieci", "disco", "dolce", "donna", "dorme", "dorso", "duomo", "edera", "entra", "esame", "esito", "estate", "falso", "fango", "fatta", "fatto", "ferma", "ferro", "festa", "fiore", "filo", "firma", "fisso", "fiume", "foglia", "folla", "fondo", "forno", "forse", "forte", "fossa", "frase", "freno", "frigo", "fuoco", "fuori", "gallo", "gamba", "gatto", "gente", "genio", "gesso", "gioco", "gioia", "grado", "grano", "grato", "grave", "grido", "guida", "gusto", "hotel", "idolo", "igloo", "imita", "invia", "labbro", "lampo", "largo", "latte", "leale", "legno", "lento", "libro", "lieto", "limbo", "limone", "linea", "lista", "litro", "luogo", "lusso", "madre", "magia", "mamma", "manda", "mango", "marca", "marea", "marmo", "massa", "matto", "mezzo", "miele", "misto", "molto", "mondo", "morte", "mossa", "motto", "museo", "nasce", "nervo", "nesso", "nobile", "norma", "notte", "nuovo", "nuova", "occhi", "odora", "offre", "oliva", "ombra", "opera", "orari", "ormai", "osare", "padre", "paese", "palco", "palla", "palma", "panca", "paura", "pezzo", "piano", "piede", "piena", "pieno", "pietra", "pigro", "pinna", "pista", "pizza", "porta", "posto", "prato", "preme", "primo", "prova", "pugno", "punta", "punto", "quale", "quota", "radio", "reale", "regno", "resta", "ricco", "ritmo", "rocca", "rosso", "rotta", "ruota", "ruolo", "sacco", "salto", "salvo", "santo", "scala", "scena", "scopo", "scuro", "sedia", "segno", "sella", "senno", "senso", "serio", "serra", "sesto", "sogno", "soldi", "sonno", "sopra", "sorte", "spada", "spesa", "spina", "stato", "stile", "stima", "suono", "tacco", "taglio", "tanto", "tassa", "tazza", "tempo", "tenue", "terra", "testa", "tetto", "tigre", "tondo", "torre", "torta", "trama", "treno", "trova", "tutto", "udire", "ulivo", "umano", "umile", "unico", "unire", "usare", "utile", "valle", "vanto", "vasca", "verde", "verme", "verso", "vetro", "viale", "villa", "vinci", "viola", "vista", "visto", "vitto", "volpe", "volta", "volto", "zaino", "zampa", "zebra", "zitto", "zolla", "zucca"] 
#Questa lista moooolto lunga sono tutte le parole che l'utente può inserire così da verificare le lettere
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
