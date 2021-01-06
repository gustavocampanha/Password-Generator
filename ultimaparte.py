#tenho o valor de z
#pessoa escolhe o valor de q
q = int(input('Quantos dígitos a senha deve conter? '))

while True:
    if q < z:
        print('Impossível ter mais tipos de caracteres na senha do que tamanho')
        novamente = str(input('Deseja escolher novamente o tamanho de sua senha? [S/N] '))
        #Perguntar se deseja continuar no código escrevendo mais uma vez o tamanho que deseja na senha ou se deseja terminar o código
            while novamente not in 'SsNn':
                print('Não entendi, digite novamente por favor!')
                novamente = str(input('Deseja escolher novamente o tamanho de sua senha? [S/N] '))
            if novamente in 'Ss': #Caso deseje continuar no código:
                while True:
                    q = int(input('Quantos dígitos a senha deve conter? '))
                #se escreveu um q menor que z, deve reescrever o q e ser perguntado novamente se deseja continuar ou sair
                    if q >= z:
                        break#se escreveu um q maior ou igual a z, ok vida que segue

            else: #Caso deseje terminar o código:
                sys.exit()

    #se q >= z:
        #ok, vida q segue
    else:
    #caso contrário:
        break