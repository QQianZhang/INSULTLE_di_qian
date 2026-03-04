import pygame
from __init__ import main

def schermataIniziale() -> None:
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
                            main()
                        elif tasto == "CLASSIFICA":
                            print("CLASSIFICA")

        pygame.display.flip()

    pygame.quit()


