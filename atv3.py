import tkinter as tk
from tkinter import messagebox

def botaoclick():
    messagebox.showinfo("Parabéns!!", "Botão clicado")

#Configurações da janela principal 
janela = tk.Tk()
janela.title("Interface Gráfica com Imagem")
janela.geometry("800x500")

#Imagem de fundo
imagem = tk.PhotoImage(file="ohmyga.gif")
rotulo = tk.Label(janela, image=imagem)
rotulo.pack()

#Rotulo com uma mensagem abaixo da imagem
rotuloMensagem = tk.Label(janela, text="Clique no botão")
rotuloMensagem.pack(pady=10)

#Configuração do botão
imagemBotão = tk.PhotoImage(file="click.png")#-- Definindo o caminho da imagem
botao = tk.Button(janela, image=imagemBotão, command=botaoclick).pack(pady=10) #-- Colocando a imagem no botão e dando a função "botaoclck"


janela.mainloop()