import random
import tkinter as tk
from tkinter import messagebox

vitorias = 0
derrotas= 0
empates = 0

def quem_ganha(JOGADOR, bot):
    global vitorias, derrotas, empates
    if (JOGADOR == bot):
        empates += 1
        return "Empatou!"
    
    elif (JOGADOR == "Pedra" and bot == "Tesoura") or \
         (JOGADOR == "Tesoura" and bot == "Papel") or \
         (JOGADOR == "Papel" and bot == "Pedra"):
            vitorias += 1
            return "Você venceu!"
    else:
        derrotas += 1
        return "Você perdeu!"
    
def escolher_opcao(opcao_jogador):
     bot = random.choice(["Pedra", "Papel", "Tesoura"])
     resultado = quem_ganha(opcao_jogador, bot)
     resultado_label.config (text= f"Eu escolhi: {bot}\n{resultado}")
     placar_label.config (text= f"Vitorias: {vitorias} \n Derrotas: {derrotas} \n Empates: {empates}")

janela = tk.Tk()
janela.title ("Pedra, Papel e Tesoura")
janela.config (bg='#f5e6ca')

label = tk.Label(janela, text=" Pedra, Papel ou Tesoura?", font= ("Arial", 16, "bold"),bg='#f5e6ca', compound="center", relief="solid",borderwidth=3 )
label.pack(pady=12)

resultado_label = tk.Label(janela, text=" ", font= ("Arial", 15, "bold"), bg='#f5e6ca')
resultado_label.pack(pady=20) 

placar_label = tk.Label (janela, text= f"Vitorias: {vitorias} \n Derrotas: {derrotas} \n Empates: {empates}", font=("Arial", 13, "bold"), bg='#f4f1de', fg='black', padx=20, relief="solid", borderwidth=2)
placar_label.pack(pady=13)

btn_pedra = tk.Button(janela, text="Pedra", font=("Arial", 15,"bold"), command= lambda: escolher_opcao("Pedra"), bg='#e07a5f', activebackground='#d1664a', fg='white', relief="raised")
btn_pedra.pack(side=tk.LEFT, padx=10)

btn_papel = tk.Button(janela, text="Papel", font= ("Arial", 15,"bold"), command= lambda: escolher_opcao("Papel"), bg='#e07a5f', activebackground='#d1664a', fg='white', relief="raised")
btn_papel.pack(side=tk.LEFT, padx=10)

btn_tesoura = tk.Button(janela, text="Tesoura", font=("Arial", 15,"bold"), command= lambda: escolher_opcao("Tesoura"), bg='#e07a5f', activebackground='#d1664a', fg='white', relief="raised")
btn_tesoura.pack(side=tk.LEFT, padx=10)

janela.mainloop()