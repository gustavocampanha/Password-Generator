from random import sample, choice
import sys
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
    while escolha not in 'PpAa':
            print('Por favor escreva sua escolha da mesma forma como foi apresentado.')
            escolha = str(input('Deseja um código Personalizado ou Aleatório? [P/A] '))
            sleep(0.5)
    sleep(1)
    if escolha in 'Pp':
        password = input('Digite sua Senha: ')
        p = sample(password,len(password))
        s=''.join(p)
        sleep(0.5)
        print(f'Nova Senha: {s}')
        break
    
    else:
        b=list()
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        simbols = ['@','#','$','&','*','(',')','-','_','+','=','^','~',':']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        print('Responda com [S] ou [N], por favor.')
        sleep(1)
        z = 0
        
        n = str(input('A senha incluirá números? [S/N] '))   
        while n not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            n = str(input('A senha incluirá números? [S/N] '))
        sleep(0.5)
        if n in 'Ss':
            z += 1
        
        s = str(input('A senha incluirá símbolos? [S/N] '))
        while s not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            s = str(input('A senha incluirá símbolos? [S/N] '))
        sleep(0.5)
        if s in 'Ss':
            z += 1

        li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        while li not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            li = str(input('A senha incluirá letras minúsculas? [S/N] '))

        sleep(0.5)
        if li in 'Ss':
            z += 1

        la = str(input('A senha incluirá letras maiúsculas? [S/N] '))
        while la not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            la = str(input('A senha incluirá letras maiúsculas? [S/N] '))

        sleep(0.5)
        if la in 'Ss':
            z += 1

        #SE DESEJA CARACTERE REPETIDO

        if n in 'Ss':
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + simbols + letters + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                        
                        
                                
                        
                            #problema de não ter todos os caracteres desejados e com isso deve ser refeita a senha pelo programa



                    else:
                        b = numbers + simbols + letters
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                else:
                    if la in 'Ss':
                        b = numbers + simbols + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = numbers + simbols
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = numbers + letters + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = numbers + letters
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                else:
                    if la in 'Ss':
                        b = numbers + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = numbers
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q) 
        elif n in 'Nn':
            if s in 'Ss':
                if li in 'Ss':
                    if la in 'Ss':
                        b = simbols + letters + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = simbols + letters
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                else:
                    if la in 'Ss':
                        b = simbols + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = simbols
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q) 
            else:
                if li in 'Ss':
                    if la in 'Ss':
                        b = letters + LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        b = letters
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                else:
                    if la in 'Ss':
                        b = LETTERS
                        q = int(input('Quantos dígitos a senha deve conter? '))
                        if z > q:
                            print('Impossível ter mais tipos de caracteres na senha do que tamanho')
                            sleep(1)
                            sys.exit()
                        password=sample(b,q)
                    else:
                        print('Por favor, não foda e meta o pé')
                        sleep(2)
                        sys.exit()

        sleep(0.5)
        senha=''.join(password)
        print('Nova Senha: {0}.'.format(senha))
        break
    
sleep(1)
print('{0}Muito obrigado por usar nossos serviços, estaremos aqui sempre que precisar de nós! Agora poderá proveitar sua vida online de uma forma mais segura!{1}'.format('\033[32m','\033[m'))
print()