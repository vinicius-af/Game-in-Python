from time import sleep
from random import randint
import pyautogui as pgui

#Listas necessárias para o jogo
listaFrasesAdeus = ['OK! Espero que nos encontremos novamente!', 'Adeus, volte jogar outra hora!', 'Sinto que estaremos juntos sempre', 'Até mais meu consagrado!', 'Obrigado por tentar :)']
listaPersonagens = ['Personagem principal', 'Unknown voice', 'Some Hacker', 'cyberHeat34']


#Funções do jogo
def fraseAdeusRandom():
    print(listaFrasesAdeus[randint(0, len(listaFrasesAdeus) - 1)])

def listaPersonagens():
    print('A lista de personagens segue a baixo: ')
    for i in range(len(listaPersonagens) - 1):
        print(listaPersonagens[i])
        sleep(1)

def menuModel():
    print('-'*10 + 'The Cognates' + '-' * 10)
    print('Seja bem vindo ao jogo!')
    print('[1]Jogar')
    print('[2]Personagens')
    print('[3]Créditos')
    print('[4]Sair')

def loadingScreen():
    print('Loading...')
    sleep(2)
    print('Fetching DataBase')
    sleep(5)
    print('Starting ms-Speech and AI-Talks')
    sleep(3)
    print('AI activated')

def thinkingBox(seconds, qtd):
    for i in range(qtd):
        print('...')
        sleep(seconds)

#Código do jogo abaixo
while True:
    menuModel() 
    verification = int(input('O que deseja fazer? '))
    nome = str(input('Antes de tudo, qual seu nome? '))

    pgui.PAUSE = 0.8
    if verification == 1:
        loadingScreen()
        thinkingBox(3, 4)
        pgui.alert('Unknown voice: W-Who are you?')
        sleep(1)
        pgui.alert('Unknown voice: I`m lost. Can you help me?')
        sleep(1)
        pgui.alert("You can't see nothing, everything is dark, just hearing that strange and cute voice...")
        sleep(1)
        pgui.alert('You: Who are you? Where am I?')
        sleep(1)
        pgui.alert('You hear nothing, everything is silence...')
        pgui.alert('Until...')
        sleep(1)
        pgui.alert('WHAT')
        pgui.alert('THE')
        pgui.alert('F**K')

        pgui.hotkey('winleft', 'd')
        sleep(1)
        pgui.press('winleft')
        sleep(0.5)
        pgui.write('notepad')
        sleep(1)
        pgui.press('enter')
        sleep(1)
        pgui.write('hey')
        sleep(2)
        pgui.press('enter')
        sleep(1)
        pgui.write(f'how are you {nome}?')
        sleep(0.5)
        pgui.press('enter')
        sleep(0.5)
        pgui.write("ACTUALLY, don't answer it, i don't care")
        sleep(2)
        pgui.press('enter')
        sleep(1)
        pgui.write(f"And please {nome}, don't think we're still locked in that game")
        sleep(2)
        pgui.press('enter')
        sleep(1)
        pgui.write('now is just you and me :)')
        sleep(2)
        pgui.press('enter')
        sleep(2)
        pgui.write('-cyberHeat34')
        sleep(2)
        pgui.hotkey('alt', 'f4')
        sleep(1)
        pgui.press('right')
        pgui.press('enter')
        
        
    elif verification == 2:
        listaPersonagens()
    elif verification == 3:
        break
        #implementar créditos
    elif verification == 4:
        fraseAdeusRandom()
        sleep(0.5)
        break
