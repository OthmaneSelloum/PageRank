import tkinter as tk
from tkinter import messagebox

def load_matrix():
    messagebox.showinfo("Load Matrix", "Loading matrix...")

def load_xml():
    messagebox.showinfo("Load XML", "Loading XML...")

def load_dictionary():
    messagebox.showinfo("Load Dictionary", "Loading dictionary...")

def calculate_pagerank():
    messagebox.showinfo("PageRank Score", "Calculating PageRank score...")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Data Loader Interface")
root.geometry("600x400")

# Cadre principal pour organiser les widgets
main_frame = tk.Frame(root)
main_frame.pack(pady=20, padx=20)

# Zone de dessin agrandie
draw_frame = tk.Frame(main_frame)
draw_frame.grid(row=0, column=0, rowspan=5, padx=10)

draw_label = tk.Label(draw_frame, text="Draw a Graph", font=("Arial", 12))
draw_label.pack()

draw_area = tk.Canvas(draw_frame, width=300, height=300, bg="white")
draw_area.pack()

draw_button = tk.Button(draw_frame, text="DRAW", command=lambda: messagebox.showinfo("Draw", "Drawing..."))
draw_button.pack(pady=10)

# Cadre pour les boutons alignés verticalement
button_frame = tk.Frame(main_frame)
button_frame.grid(row=0, column=1, padx=20)

# Boutons pour charger les fichiers et calculer le score PageRank
load_matrix_button = tk.Button(button_frame, text="Load a Matrix", width=20, command=load_matrix)
load_matrix_button.pack(pady=5)

load_xml_button = tk.Button(button_frame, text="Load a XML", width=20, command=load_xml)
load_xml_button.pack(pady=5)

load_dict_button = tk.Button(button_frame, text="Load a Dictionary", width=20, command=load_dictionary)
load_dict_button.pack(pady=5)

pagerank_button = tk.Button(button_frame, text="PageRank Score", width=20, command=calculate_pagerank)
pagerank_button.pack(pady=5)

root.mainloop()
