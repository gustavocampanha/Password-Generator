#Este é o programa final
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
        sleep(0.5)
        print('Por favor escreva sua escolha da mesma forma como foi apresentado.')
        escolha = str(input('Deseja um código Personalizado ou Aleatório? [P/A] '))
            
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
        simbols = ['@','#','$','&','*','(',')','-','_','+','=','^','~',':','.']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        print('Responda com [S] ou [N], por favor.')
        sleep(1)
                
        n = str(input('A senha incluirá números? [S/N] '))   
        while n not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            n = str(input('A senha incluirá números? [S/N] '))
        sleep(0.5)
                
        s = str(input('A senha incluirá símbolos? [S/N] '))
        while s not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            s = str(input('A senha incluirá símbolos? [S/N] '))
        sleep(0.5)
        
        li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        while li not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            li = str(input('A senha incluirá letras minúsculas? [S/N] '))
        sleep(0.5)
        
        la = str(input('A senha incluirá letras maiúsculas? [S/N] '))
        while la not in 'SsNn':
            print('Não entendi, digite novamente por favor!')
            la = str(input('A senha incluirá letras maiúsculas? [S/N] '))
        sleep(0.5)
       
        #SE DESEJA CARACTERE REPETIDO
        q = int(input('Quantos dígitos a senha deve conter? '))       

        if n in'Ss' and s in 'Nn' and li in 'Nn' and la in 'Nn':
            b=numbers
            
        elif s in 'Ss' and n in 'Nn' and li in 'Nn' and la in 'Nn':
            b=simbols
            
        elif li in 'Ss' and n in 'Nn' and s in 'Nn' and la in 'Nn':
            b=letters
                            
        elif la in 'Ss' and n in 'Nn' and s in 'Nn' and li in 'Nn':
            b=LETTERS
            
        elif n in 'Ss' and s in 'Ss' and li in 'Nn' and la in 'Nn':
            b=numbers+simbols
            while True:
                password=sample(b,q)
                if  numbers in password and simbols  in password:
                    break

        elif n in 'Ss' and li in 'Ss' and s in 'Ss' and la in 'Nn':
            b=numbers+letters
            while True:
                password=sample(b,q)
                if numbers in password and letters in password:
                    break
                
        elif n in 'Ss' and la in 'Ss' and s in 'Nn' and li in 'Nn':
            b=numbers+LETTERS
            while True:
                password=sample(b,q)
                if numbers in password and LETTERS in password:
                    break

        elif s in 'Ss' and li in 'Ss' and n in 'Nn' and la in 'Nn':
            b=simbols+letters
            while True:
                password=sample(b,q)
                if simbols in password and letters in password:
                    break

        elif s in 'Ss' and la in 'Ss' and n in 'Nn' and li in 'Nn':
            b=simbols+LETTERS
            while True:
                password=sample(b,q)
                if simbols in password and LETTERS in password:
                    break

        elif li in 'Ss' and la in 'Ss' and n in 'Nn' and s in 'Nn':
            b=letters+LETTERS
            while True:
                password=sample(b,q)
                if letters in password and LETTERS in password:
                    break

        elif n in 'Ss' and s in 'Ss' and li in 'Ss' and la in 'Nn':
            b=numbers+simbols+letters
            while True:
                password=sample(b,q)
                if numbers in password and simbols in password and letters in password:
                    break

        elif n in 'Ss' and s in 'Ss' and la in 'Ss' and li in 'Nn':
            b=numbers+simbols+LETTERS
            while True:
                password=sample(b,q)
                if numbers in password and simbols in password and LETTERS in password:
                    break

        elif n in 'Ss' and li in 'Ss' and la in 'Ss' and s in 'Nn':
            b=numbers+letters+LETTERS
            while True:
                password=sample(b,q)
                if numbers in password and letters in password and LETTERS in password:
                    break

        elif s in 'Ss' and li in 'Ss' and la in 'Ss' and n in 'Nn': 
            b=simbols+letters+LETTERS
            while True:
                password=sample(b,q)
                if simbols in password and letters in password and LETTERS in password:
                    break

        elif n in 'Ss' and s in 'Ss' and la in 'Ss' and li in 'Ss':
            b=numbers+simbols+letters+LETTERS
            while True:
                password=sample(b,q)
                if numbers in password and simbols in password and letters in password and LETTERS in password:
                    break
        else:
            print('Por favor, não foda e meta o pé')
            sleep(2)
            sys.exit()

        sleep(0.5)
        senha=''.join(password)
        print('Nova Senha: {0}'.format(senha))
        break

sleep(1)
print('{0}Muito obrigado por usar nossos serviços, estaremos aqui sempre que precisar de nós! Agora poderá proveitar sua vida online de uma forma mais segura!{1}'.format('\033[32m','\033[m'))