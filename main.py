import tkinter as tk
import math

# Fonction pour traiter les entrées
def bouton_click(bouton):
    current = entry.get()
    entry.delete(0, tk.END)  # Efface l'entrée actuelle
    entry.insert(tk.END, current + str(bouton))

# Fonction pour calculer le résultat
def calculer():
    try:
        expression = entry.get()
        # Remplacer ^ par ** pour le calcul des puissances
        expression = expression.replace("^", "**")
        result = eval(expression)  # Utilise eval pour calculer l'expression mathématique
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur: Div. par 0")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

# Fonction pour effacer l'entrée
def effacer():
    entry.delete(0, tk.END)

# Fonction pour calculer la racine carrée
def racine_carre():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

# Fonction pour calculer le pourcentage
def pourcentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

# Fonction trigonométrique (sin, cos, tan)
def trig_function(func):
    try:
        angle = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(angle))  # Convertir l'angle en radians
        elif func == "cos":
            result = math.cos(math.radians(angle))
        elif func == "tan":
            result = math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Calculatrice Scientifique Rose")

# Configurer la couleur de fond et la taille de la fenêtre
root.config(bg="#F8BBD0")
root.geometry("320x460")  # Ajuster la taille pour être plus proche d'une calculatrice réelle

# Zone de texte pour afficher l'entrée et les résultats
entry = tk.Entry(root, width=16, font=("Arial", 18), borderwidth=2, relief="solid", bg="#FFF0F6", fg="#D5006D", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Liste des boutons de la calculatrice (ajout de fonctions avancées)
boutons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('%', 5, 2), ('^', 5, 3),
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2),
]

# Créer les boutons et les placer sur la grille
for (text, row, col) in boutons:
    if text == "=":
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculer, bg="#F48FB1", fg="#D5006D")
    elif text == "C":
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=effacer, bg="#F48FB1", fg="#D5006D")
    elif text == "√":
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=racine_carre, bg="#F48FB1", fg="#D5006D")
    elif text == "%":
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=pourcentage, bg="#F48FB1", fg="#D5006D")
    elif text == "^":
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda b=text: bouton_click(b), bg="#F48FB1", fg="#D5006D")
    elif text in ["sin", "cos", "tan"]:
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda f=text: trig_function(f), bg="#F48FB1", fg="#D5006D")
    else:
        bouton = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda b=text: bouton_click(b), bg="#F48FB1", fg="#D5006D")
    
    bouton.grid(row=row, column=col, padx=5, pady=5)

# Lancer l'interface graphique
root.mainloop()