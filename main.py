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

def write(msg):
    pgui.write(msg)

def fechaJanela():
    pgui.hotkey('alt', 'f4')

def alert(msg):
    pgui.alert(msg)

def press(button):
    pgui.press(button)

def startDialogs():
    loadingScreen()
    thinkingBox(3, 4)
    alert('Unknown voice: W-Who are you?')
    sleep(1)
    alert('Unknown voice: I`m lost. Can you help me?')
    sleep(1)
    alert("You can't see nothing, everything is dark, just hearing that strange and cute voice...")
    sleep(1)
    alert('You: Who are you? Where am I?')
    sleep(1)
    alert('You hear nothing, everything is silence...')
    alert('Until...')
    sleep(1)
    alert('WHAT')
    alert('THE')
    alert('HELL')

def notepadStartPart():
    pgui.hotkey('winleft', 'd')
    sleep(1)
    press('winleft')
    sleep(0.5)
    write('notepad')
    sleep(1)
    press('enter')
    sleep(1)
    write('hey')
    sleep(2)
    press('enter')
    sleep(1)
    write(f'how are you {nome}?')
    sleep(0.5)
    press('enter')
    sleep(0.5)
    write("ACTUALLY, don't answer it, i don't care")
    sleep(2)
    press('enter')
    sleep(1)
    write(f"And please {nome}, don't think we're still locked in that game")
    sleep(2)
    press('enter')
    sleep(1)
    write('now is just you and me :)')
    sleep(2)
    press('enter')
    sleep(2)
    write('-cyberHeat34')
    sleep(2)
    fechaJanela()
    sleep(1)
    press('right')
    press('enter')

def startChapterOne():
    alert('What just happened? Am i crazy or something?')
    alert('Well, maybe if I should try to CONTROL the computer too...')
    alert('It is not that hard i think...')
    press('win')
    sleep(1)
    write('chrome')
    sleep(1)
    press('enter')
    sleep(2)
    write('https://pt.wikipedia.org/wiki/Cognato')
    sleep(1)
    press('enter')
    sleep(4)
    fechaJanela()
    alert("Well, it's easy, but, who are the owner of this COMPUTER?")

#Código do jogo abaixo
while True:
    menuModel() 
    verification = int(input('O que deseja fazer? '))
    nome = str(input('Antes de tudo, qual seu nome? '))

    pgui.PAUSE = 0.8
    if verification == 1:
        
        startDialogs()
        notepadStartPart()
        startChapterOne()
        
    elif verification == 2:
        listaPersonagens()
    elif verification == 3:
        break
        #implementar créditos
    elif verification == 4:
        fraseAdeusRandom()
        sleep(0.5)
        break
