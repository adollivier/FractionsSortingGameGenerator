import sys
import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
from tkinter.filedialog import askdirectory


def create_pdf(jeu, nbrIntervalleMax, nbrDenominateur, outputFolder):
    c = canvas.Canvas(outputFolder + "/" + jeu, pagesize=letter)

    # Dimensions de la page A4
    page_width, page_height = letter

    # Nombre de cartes par ligne et par colonne
    cards_per_row = 3
    cards_per_col = 4

    # Calcul des dimensions de chaque carte pour remplir la page
    card_width = (page_width - (cards_per_row - 1)) / cards_per_row
    card_height = (page_height - (cards_per_col - 1)) / cards_per_col

    # Taille de la police
    font_size = 40

    # Nombre de cartes par ligne
    cards_per_row = 3
    fractions = []
    for _ in range(12):
        B = random.randint(2, nbrDenominateur)
        A = random.randint(1, int(nbrIntervalleMax * B))
        fractions.append([A, B])

    for i, fraction in enumerate(fractions):
        row = i // cards_per_row
        col = i % cards_per_row
        x = col * card_width
        y = letter[1] - (row % (letter[1] // card_height) + 1) * card_height

        # Dessine le rectangle de la carte
        c.rect(x, y, card_width, card_height)

        # Définit la taille de la police
        c.setFont("Helvetica", font_size)

        # Ajoute la fraction au centre de la carte
        c.drawCentredString(x + 1 * card_width / 2, y + 2 * card_height / 7, str(fraction[1]))
        c.drawCentredString(x + 1 * card_width / 2, y + 3 * card_height / 7, "——")
        c.drawCentredString(x + 1 * card_width / 2, y + 4 * card_height / 7, str(fraction[0]))

    c.save()


def get_output_folder():
    root = tk.Tk()
    root.iconify()
    root.attributes("-topmost", True)
    folder_selected = tk.filedialog.askdirectory()
    if folder_selected:
        print(f"Dossier sélectionné : {folder_selected}")
    else:
        print("Aucun dossier sélectionné.")
    return folder_selected


def askParametreUser():
    listParametre = []
    try:
        listParametre.append(int(input("Choisissez le nombre de grilles de jeux souhaité : ")))
        listParametre.append(int(input("Choisissez la valeur maximale que pourra prendre une fraction : ")))
        listParametre.append(int(input("Choisissez la valeur maximale du dénominateur : ")))
        for j in listParametre:
            if j <= 0:
                raise ValueError()
    except ValueError:
        print("Vous devez entrer uniquement des entiers positifs.")
        sys.exit()

    try:
        print("Choisissez le dossier où vous voulez enregistrer les grilles de jeux : ")
        listParametre.append(get_output_folder())
    except NameError:
        print("Vous devez choisir un dossier valide.")
        sys.exit()
    return listParametre


if __name__ == "__main__":
    parametreUser = askParametreUser()
    for i in range(parametreUser[0]):
        jeu = "jeu " + str(i + 1) + ".pdf"
        create_pdf(jeu, parametreUser[1], parametreUser[2], parametreUser[3])
