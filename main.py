from pickle import NONE
from time import sleep
from random import randint
import pyautogui as pgui

#Listas necessárias para o jogo
listaFrasesAdeus = ['OK! Espero que nos encontremos novamente!', 'Adeus, volte jogar outra hora!', 'Sinto que estaremos juntos sempre', 'Até mais meu consagrado!', 'Obrigado por tentar :)']
listaPersonagens = ['You', 'Unknown voice', 'Some Hacker', 'cyberHeat34']

nome = NONE

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
    sleep(3)
    print("The game you are playing is a demonstration version of the original(cz i was tired and didn't wanted to make more lmao), more chapters coming soon")
    sleep(5)

def thinkingBox(seconds, qtd):
    for i in range(qtd):
        print('...')
        sleep(seconds)

def write(msg):
    pgui.write(msg)

def fechaNotepad():
    fechaJanela()
    sleep(1)
    press('right')
    press('enter')

def fechaJanela():
    pgui.hotkey('alt', 'f4')

def alert(msg):
    pgui.alert(msg)

def press(button):
    pgui.press(button)

def prompt(msg, title):
    pgui.prompt(msg, title)

def startDialogs():
    loadingScreen()
    pgui.hotkey('winleft', 'd')
    alert('Chapter 1')
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
    fechaNotepad()
def startChapterOne():
    alert('What just happened? Am i crazy or something?')
    alert('Well, maybe if I should try to CONTROL the computer too...')
    alert('It is not that hard i think...')
    sleep(1)
    alert("Well, it's easy, but, who are the owner of this COMPUTER?")
    sleep(1)

def chapterTwoName():
    alert('Chapter 2')
    sleep(1)
    conf1 = pgui.confirm('Can you see or hear me?', 'Someone says', ['Yes', 'No'])
    if conf1 == "Yes":
        alert('Great, at least i am not alone')
        str(prompt('What is your name?', 'Someone says'))
        sleep(1)
        alert(f'Ok, hello')
    elif conf1 == "No":
        alert('How did you answered me so? Dumby')
        sleep(1)
        alert('Im not kidding')
        str(prompt('What is your name?', 'Someone says'))
        alert(f'Ok, hello')
    

def continuationChap2():
    alert('Well, whatever, we need to discover-')
    sleep(1)
    press('winleft')
    sleep(1)
    write('notepad')
    sleep(0.4)
    press('enter')
    sleep(1)
    write("it's me again c:")
    sleep(1)
    press('enter')
    write('i see there are two of you now ')
    sleep(1)
    press('enter')
    write("next time you try to stop me i will open cmd c:")
    sleep(2)
    fechaNotepad()

def chapter3():
    alert('WE WILL DO IT, WE CAN')
    sleep(1)
    press('winleft')
    sleep(0.5)
    write('cmd')
    sleep(0.5)
    press('enter')
    sleep(1)
    write('netstat')
    sleep(0.5)
    press('enter')
    sleep(2)
    fechaJanela()

def lastChap():
    sleep(1)
    alert('th- the end is coming...')
    alert('i can feel it...')
    alert('nobody can save us...')
    alert('nobody can save you...')
    alert('and this is not over...')
    alert('at least not yet...')
    alert(nome + '...')




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
        chapterTwoName()
        continuationChap2()
        chapter3()
        lastChap()
        
    elif verification == 2:
        listaPersonagens()
    elif verification == 3:
        break
        #implementar créditos
    elif verification == 4:
        fraseAdeusRandom()
        sleep(0.5)
        break

