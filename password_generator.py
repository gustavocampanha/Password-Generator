from random import sample, choice, random, seed
import time
import sys
import string
from itertools import combinations_with_replacement 
from datetime import timedelta 
from time import sleep

print('{0} BEM VINDO AO GERADOR DE SENHAS! A OPÇÃO PERSONALIZADA RETORNARÁ COMBINAÇÕES DE UMA SENHA DEFINIDA ANTERIORMENTE, ENQUANTO A ALEATÓRIA IRÁ GERAR UMA SENHA TOTALMENTE NOVA BASEADA NAS SUAS PREFERÊNCIAS.{1}'.format('\033[7:40m', '\033[m'))

while True:
    escolha = str(input('Deseja um código personalizado ou aleatório? '))

    if escolha == 'personalizado':
        password = input('Digite sua Senha: ')
        p = sample(password,len(password))
        s=''.join(p)
        print(s)
        break
    
    elif escolha == 'aleatório':
        b=list()
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        simbols = ['@','#','$','&','*','(',')','-','_','+','=','^','~',':']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        print('Responda com [S] ou [N], por favor.')
        n = str(input('A senha incluirá números? [S/N] '))
        s = str(input('A senha incluirá símbolos? [S/N] '))
        li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        la = str(input('A senha incluirá letras maiúsculas? [S/N] ')) 

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
        print(b)
        password=sample(b,q)
        senha=''.join(password)
        print('A sua senha é: {0}.'.format(senha))
        break
    
    else:
        print('Por favor escreva sua escolha da mesma forma como foi apresentado.')


while True:
    segurança = str(input('Deseja saber o nível de segurança de sua senha baseado no tamanho dela? [S/N] '))
    if segurança in 'Ss':
        def main(args):

            valores = string.ascii_letters
            valores += string.digits
            valores += string.punctuation
            tamanho = int(input('Digite o tamanho da senha desejada: '))

            ini_t = time.time()
            gerar_senhas(valores, tamanho)
            fin_t = time.time()

            print("Tempo: " + str(fin_t - ini_t) + "s")

        def gerar_senhas(valores, tamanho):
            comb = combinations_with_replacement(valores, tamanho)
            print("Combinações: " + str(len(list(comb))))

        if __name__ == '__main__':
            main(sys.argv[1:])
        break
    elif segurança in 'Nn':
        print('Foi um prazer!')
        break
    else:
        print('Não entendi, por favor digite novamente: ')