import pyautogui as py
import time as t
import threading
import tkinter as tk

py.PAUSE = 0  # Remove a pausa entre os comandos para acelerar o bot

executar_bot = False

def usar_habilidades():
    imagens_habilidades = ['skils/skil1.png', 'skils/skil2.png', 'skils/skil3.png', 'skils/skil4.png', 'skils/skil5.png', 'skils/skil6.png', 'skils/skil7.png']
    
    for imagem in imagens_habilidades:
        habilidade = py.locateCenterOnScreen(imagem, confidence=0.7)
        py.click(habilidade)
    
def fechar_partida():
    
    continuar = py.locateCenterOnScreen('skils/continuar.png', confidence=0.7)
    py.click(continuar)

    imagens = [
        'skils/continuar.png', 'skils/continuar1.png', 'skils/continuar2.png', 'skils/continuar3.png',
        'skils/x3.png', 'skils/x4.png', 'skils/x5.png', 'skils/x6.png', 'skils/x7.png', 'skils/x8.png', 'skils/x9.png', 
        'skils/x10.png', 'skils/x11.png', 'skils/x12.png', 'skils/x13.png', 'skils/x14.png', 'skils/x14.png', 'skils/x15.png', 'skils/x16.png', 'skils/x17.png',
        'skils/x18.png', 'skils/x19.png', 'skils/x20.png', 'skils/x21.png', 'skils/x23.png'
    ]

    for imagem in imagens:
        posicao = py.locateCenterOnScreen(imagem, confidence=0.7)
        py.click(posicao)


def iniciar_jungle():
    jugg = py.locateCenterOnScreen('skils/jugg.png', confidence=0.7)
    py.click(jugg)

def iniciar_batalhar():
    global executar_bot
    while executar_bot:
        try:
            #estourar_bomba()
            iniciar_jungle()
            usar_habilidades()
            fechar_partida()
            #impecilhos()
            py.moveTo(951, 160)
        except Exception as e:
            print(f"Ocorreu um erro: {e}, continuando...")

def start_bot():
    global executar_bot
    executar_bot = True
    bot_thread = threading.Thread(target=iniciar_batalhar)
    bot_thread.start()

# Função para parar o bot
def stop_bot():
    global executar_bot
    executar_bot = False
    print("Bot parado.")

def cancelar_bot(event):
    stop_bot()

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Bot Control")
janela.geometry("400x200")
janela.configure(bg="black")  # Define o fundo preto

# Estilo dos botões
botao_estilo = {"width": 30, "height": 2, "bg": "blue", "fg": "white", "font": ("Helvetica", 12, "bold")}

# Botão para iniciar o bot
botao_comecar = tk.Button(janela, text="Start Bot", command=start_bot, **botao_estilo)
botao_comecar.pack(pady=20)

# Botão para parar o bot
botao_parar = tk.Button(janela, text="Stop Bot", command=stop_bot, **botao_estilo)
botao_parar.pack(pady=10)

# Tecla F10 para cancelar o bot
janela.bind('<F10>', cancelar_bot)

# Inicia o loop da interface gráfica
janela.mainloop()