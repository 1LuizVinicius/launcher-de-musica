# importando Tkinter
from tkinter import*

# importando pillow
from PIL import Image, ImageTk
from click import command

''' importando
import pygame
from pygame import mixer
import os'''

# cores
co0 = "#f0f3f5" # cinzento / grey
co1 = "#feffff" # branca
co2 = "#3fb5a3" # verde
co3 = "#2e2d2c" # preta / black
co4 = "#403d3d" # preta / black
co5 = "#4a88e8" # azul / blue


# criando janela -----------

janela = Tk ()
janela.title ("")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


# Frames

frame_esquerda = Frame(janela,width=140, height=140,bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela,width=270, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

# configurando o frame esquerda
img_1 = Image.open('interface.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=3, y=9)

# configuracao o frame direita

lista = ['joao','futi','muanda']

listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('aria 9 bold'), bg=co3, fg=co1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, strick=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

for i in lista:
    listbox.insert(END, i)





janela.mainloop ()