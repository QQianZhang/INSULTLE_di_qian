

# per compatibilità con PIL anche il modulo pillow si chiama PIL
from PIL import Image
Larghezza_Schermo = 822
Altezza_Schermo = 745
# Per aprire e visualizzare una immagine
# l'immagine deve trovarsi nella stessa cartella dello script
img = Image.open("sfondoINSULTLE.jpg")
croppedImage = img.crop( (0,0,745,822) )
#PRIMA RIGA
letter_Q = croppedImage.crop((67,565, 122, 635)) #50 x70 5px tra le cose
letter_W = croppedImage.crop((127,565, 182, 635)) #+60
letter_E = croppedImage.crop((189,565, 242, 635))
letter_R = croppedImage.crop((250,565, 302, 635))
letter_T = croppedImage.crop((310,565, 367, 635))
letter_Y = croppedImage.crop((375,565, 427, 635))
letter_U = croppedImage.crop((435,565, 487, 635))
letter_I = croppedImage.crop((500,565, 550, 635))
letter_O = croppedImage.crop((560,565, 610, 635))
letter_P = croppedImage.crop((620,565, 670, 635))

#SECONDA RIGA
letter_A = croppedImage.crop((95,650, 150, 720))
letter_S = croppedImage.crop((155,650, 210, 720))
letter_D = croppedImage.crop((220,650, 275, 720))
letter_F = croppedImage.crop((280,650, 335, 720))
letter_G = croppedImage.crop((345,650, 395, 720))
letter_H= croppedImage.crop((405,650, 460, 720))
letter_J = croppedImage.crop((465,650, 520, 720))
letter_K = croppedImage.crop((530,650, 585, 720))
letter_L = croppedImage.crop((590,650, 645, 720))

#TERZA RIGA
letter_invio = croppedImage.crop((67,730, 150, 805))
letter_Z = croppedImage.crop((155,730, 210, 805))
letter_X = croppedImage.crop((220,730, 275, 805))
letter_C = croppedImage.crop((280,730, 335, 805))
letter_V = croppedImage.crop((345,730, 395, 805))
letter_B= croppedImage.crop((405,730, 460, 805))
letter_N = croppedImage.crop((465,730, 520, 805))
letter_M = croppedImage.crop((530,730, 585, 805))
letter_canc = croppedImage.crop((590,730, 670, 805))
letter_canc.show()