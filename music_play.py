# importando Tkinter
from tkinter import*

# importando pillow
from PIL import Image, ImageTk

# importando o pygame
import pygame
from pygame import mixer
import os

# cores
co0 = "#f0f3f5" # cinzento / grey
co1 = "#feffff" # branca
co2 = "#3fb5a3" # verde
co3 = "#2e2d2c" # preta / black
co4 = "#403d3d" # preta / black
co5 = "#4a88e8" # azul / blue


# criando janela -----------

janela = Tk ()
janela.title ("Player Music")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


# Frames

frame_esquerda = Frame(janela,width=145, height=140,bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela,width=250, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=404, height=120, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)


# configurando o frame esquerda

img_1 = Image.open('papel1.jpg')
img_1 = img_1.resize((152, 145))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=145, image=img_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=0, y=0)


# Criando funções ---------------------------------------


# tocar musica
def play_musica():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

# pausar musica
def pausar_musica():
    mixer.music.pause()

# continuar musica
def continuar_musica():
    mixer.music.unpause()

# parar musica
def parar_musica():
    mixer.music.stop()

# proxima musica
def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

# deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()


    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando


# musica anterior
def anterior_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

# deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()


    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando


# configuracao o frame direita

lista = ['joao', 'futi', 'muanda']

listbox = Listbox(frame_direita, width=29, height=9, selectmode=SINGLE, font=('aria 9 bold'), bg=co3, fg=co1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


# configurando o frame baixo ---------------------

l_rodando = Label(frame_baixo, text='Escola uma musica da lista', width=44, justify=LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4)
l_rodando.place(x=0, y=1)



# configurando o frame botao

img_2 = Image.open('voltar.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
b_voltar = Button(frame_baixo, command=anterior_musica, width=40, height=40, image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_voltar.place(x=38, y=35)

img_3 = Image.open('play.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo, command=play_musica, width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_play.place(x=84, y=35)

img_4 = Image.open('passar.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
b_passar = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_passar.place(x=130, y=35)

img_5 = Image.open('pause.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
b_pause = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_pause.place(x=176, y=35)

img_6 = Image.open('continuar(1).png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
b_continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_continuar.place(x=222, y=35)

img_7 = Image.open('stop-button.png')
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
b_stop = Button(frame_baixo, command=parar_musica, width=40, height=40, image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_stop.place(x=266, y=35)


os.chdir(r'C:\Users\User\Desktop\musicas')
musicas = os.listdir()


def mostrar():
    for i in musicas:
        listbox.insert(END, i)


mostrar()


# inicializando o mixer
mixer.init()

janela.mainloop ()