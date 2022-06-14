from random import *
from colorama import Fore as color
from os import system, name
import pygame as game

# Music ===============================
game.mixer.init()
game.mixer.music.load('music.wav')
game.mixer.music.set_volume(0.4)
game.mixer.music.play(-1)


def clear():
    system('cls' if name == 'nt' else 'clear')


def pedircor():
    clear()
    global num_cor
    num_cor = input(
        f'''Digite o número de uma cor:
{color.RED}1. Vermelho{color.RESET}
{color.GREEN}2. Verde{color.RESET}
{color.YELLOW}3. Amarelo{color.RESET}
{color.BLUE}4. Azul{color.RESET}
{color.MAGENTA}5. Magenta{color.RESET}
{color.BLACK}6. Preto{color.RESET}
{color.RESET}
'''
    )
    if (
        num_cor == '1'
        or num_cor == '2'
        or num_cor == '3'
        or num_cor == '4'
        or num_cor == '5'
        or num_cor == '6'
    ):
        num_cor = int(num_cor)
    else:
        print('Entrada inválida! Tente novamente')
        input()
        pedircor()
    clear()


def lore():
    print(
        '''
Você acorda em uma sala e não se lembra de nada,
sequer o seu nome, quando você se leventa enxerga
um botão vermelho, na sala a frente há 5 pessoas,
cada uma vestindo uma roupa de uma cor só,
estranhamente a única coisa que você se lembra é que 
a cada vez que você apertar o botão você irá ganhar
uma boa quantia de dinheiro, porém aleatoriamente alguém morre.'''
    )


def cor():
    pedircor()
    if num_cor == 1:
        print(f'Você escolheu {color.RED}Vermelho{color.RESET}!')
    elif num_cor == 2:
        print(f'Você escolheu {color.GREEN}Verde{color.RESET}!')
    elif num_cor == 3:
        print(f'Você escolheu {color.YELLOW}Amarelo{color.RESET}!')
    elif num_cor == 4:
        print(f'Você escolheu {color.BLUE}Azul{color.RESET}!')
    elif num_cor == 5:
        print(f'Você escolheu {color.MAGENTA}Magenta{color.RESET}!')
    elif num_cor == 6:
        print(f'Você escolheu {color.BLACK}Preto{color.RESET}!')
    input()


def perguntar():
    desejo = input('\nDeseja apertar? [s/n]\n').lower()
    if desejo == 's':
        clear()
        atirar()
        perguntar()
    elif desejo == 'n':
        print(
            'Você começa a ficar tonto, e acorda, percebendo que talvez tenha sido tudo um sonho, talvez...'
        )
        input()
        exit()
    else:
        clear()
        print('Entrada inválida! Tente novamente')
        perguntar()


vermelho, verde, amarelo, azul, magenta, preto = True, True, True, True, True, True
quantia = 0


def atirar():
    global quantia, vermelho, verde, amarelo, azul, magenta, preto
    tiro = randint(1, 6)
    if tiro == num_cor:
        print(f'{color.RED}VOCÊ MORREU!{color.RESET}')
        print(f'Quantia ganha: R${quantia}')
        exit()
    elif tiro == 1:
        if vermelho:
            print(f'{color.RED}Vermelho{color.RESET} morreu')
            print('+R$1000')
            vermelho = False
            quantia += 1000
        else:
            atirar()
    elif tiro == 2:
        if verde:
            print(f'{color.GREEN}Verde{color.RESET} morreu')
            print('+R$1000')
            verde = False
            quantia += 1000
        else:
            atirar()
    elif tiro == 3:
        if amarelo:
            print(f'{color.YELLOW}Amarelo{color.RESET} morreu')
            print('+R$1000')
            amarelo = False
            quantia += 1000
        else:
            atirar()
    elif tiro == 4:
        if azul:
            print(f'{color.BLUE}Azul{color.RESET} morreu')
            print('+R$1000')
            azul = False
            quantia += 1000
        else:
            atirar()
    elif tiro == 5:
        if magenta:
            print(f'{color.MAGENTA}Magenta{color.RESET} morreu')
            print('+R$1000')
            magenta = False
            quantia += 1000
        else:
            atirar()
    elif tiro == 6:
        if preto:
            print(f'{color.BLACK}Preto{color.RESET} morreu')
            print('+R$1000')
            preto = False
            quantia += 1000
        else:
            atirar()


def jogar():
    cor()
    lore()
    perguntar()


if __name__ == '__main__':
    jogar()
