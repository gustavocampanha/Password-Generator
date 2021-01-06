from random import sample, choice, random, seed
import time
import sys
import string
from itertools import combinations_with_replacement 
from datetime import timedelta 
from time import sleep
print('='*140)
sleep(0.5)
print('{} {:^140} {}'.format('\033[33m', 'Bem Vindo ao Gerador de Senhas!','\033[m'))
sleep(0.5)
print('='*140)
sleep(0.5)
print('{0}A OPÇÃO PERSONALIZADA RETORNARÁ COMBINAÇÕES DE UMA SENHA DEFINIDA ANTERIORMENTE, ENQUANTO A ALEATÓRIA IRÁ GERAR UMA SENHA TOTALMENTE NOVA BASEADA NAS  SUAS PREFERÊNCIAS.{1}'.format('\033[7:40m', '\033[m'))
sleep(1.5)
while True:
    escolha = str(input('Deseja um código Personalizado ou Aleatório? [P/A] '))

    if escolha in 'Pp':
        password = input('Digite sua Senha: ')
        p = sample(password,len(password))
        s=''.join(p)
        sleep(0.5)
        print(s)
        break
    
    elif escolha in 'Aa':
        b=list()
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        simbols = ['@','#','$','&','*','(',')','-','_','+','=','^','~',':']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        print('Responda com [S] ou [N], por favor.')
        sleep(0.5)
        n = str(input('A senha incluirá números? [S/N] '))
        sleep(0.5)
        s = str(input('A senha incluirá símbolos? [S/N] '))
        sleep(0.5)
        li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        sleep(0.5)
        la = str(input('A senha incluirá letras maiúsculas? [S/N] ')) 
        sleep(0.5)

        if n in 'Ss':
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + simbols + letters + LETTERS
                    else:
                        b = numbers + simbols + letters
                else:
                    if la in 'Ss':
                        b = numbers + simbols + LETTERS
                    else:
                        b = numbers + simbols
            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + letters + LETTERS
                    else:
                        b = numbers + letters
                else:
                    if la in 'Ss':
                        b = numbers + LETTERS
                    else:
                        b = numbers 
        elif n in 'Nn':
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = simbols + letters + LETTERS
                    else:
                        b = simbols + letters
                else:
                    if la in 'Ss':
                        b = simbols + LETTERS
                    else:
                        b = simbols 
            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = letters + LETTERS
                    else:
                        b = letters
                else:
                    if la in 'Ss':
                        b = LETTERS
                    else:
                        print('Por favor, não foda e meta o pé')
                        sleep(2)
                        sys.exit()

        q = int(input('Quantos dígitos a senha deve conter? '))
        sleep(0.5)
        password=sample(b,q)
        senha=''.join(password)
        print('A sua senha é: {0}.'.format(senha))
        break
    
    else:
        print('Por favor escreva sua escolha da mesma forma como foi apresentado.')