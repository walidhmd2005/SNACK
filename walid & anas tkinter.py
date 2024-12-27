import tkinter as tk
from tkinter import messagebox


menu = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}


commande = {}


def calculer_total():
    total = 0
    texte_commande = ""
    for item, quantite in commande.items():
        prix = menu[item] * quantite
        total += prix
        texte_commande += f"{item} x{quantite}: {prix:.2f} DH\n"
    texte_commande += f"\nTotal: {total:.2f} DH"
    return texte_commande


def ajouter_article():
    article = var_article.get()
    quantite = var_quantite.get()
    if quantite > 0:
        if article in commande:
            commande[article] += quantite
        else:
            commande[article] = quantite
        messagebox.showinfo("Succès", f"{quantite} x {article} ajouté à votre commande !")
    else:
        messagebox.showerror("Erreur", "La quantité doit être supérieure à 0.")


def afficher_commande():
    if commande:
        messagebox.showinfo("Votre Commande", calculer_total())
    else:
        messagebox.showwarning("Attention", "t'as na pas fait aucune commende")


def reinitialiser_commande():
    commande.clear()
    messagebox.showinfo("Réinitialisation", "Votre commande a été réinitialisée.")


fenetre = tk.Tk()
fenetre.title("Snack Étudiant")
fenetre.geometry("300x300")
fenetre.config(bg="lightyellow")


tk.Label(fenetre, text="Choisissez un article :", bg="lightblue").pack(pady=5)
var_article = tk.StringVar(value="Pizza")
menu_deroulant = tk.OptionMenu(fenetre, var_article, *menu.keys())
menu_deroulant.pack(pady=5)


tk.Label(fenetre, text="Quantité :", bg="lightblue").pack(pady=5)
var_quantite = tk.IntVar(value=1)
selecteur_quantite = tk.Spinbox(fenetre, from_=1, to=100, textvariable=var_quantite)
selecteur_quantite.pack(pady=5)


btn_ajouter = tk.Button(fenetre, text="Ajouter à la commande", command=ajouter_article, bg="lightblue")
btn_ajouter.pack(pady=5)


btn_afficher = tk.Button(fenetre, text="Afficher la commande", command=afficher_commande, bg="lightblue")
btn_afficher.pack(pady=5)


btn_reset = tk.Button(fenetre, text="Réinitialiser", command=reinitialiser_commande, bg="lightblue")
btn_reset.pack(pady=5)


btn_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit, bg="lightblue", fg="black")
btn_quitter.pack(pady=5)


fenetre.mainloop()
