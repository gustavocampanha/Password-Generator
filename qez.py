z = 3
q = int(input('Quantos dígitos a senha deve conter? '))
while True:
    if z > q:
        print('Impossível ter mais tipos de caracteres na senha do que tamanho')
        sleep(1)
        while True:
            novamente = str(input('Deseja escolher novamente o tamanho de sua senha? [S/N] '))
            while novamente not in 'SsNn':
                print('Não entendi, digite novamente por favor!')
                sleep(0.5)
                novamente = str(input('Deseja escolher novamente o tamanho de sua senha? [S/N] '))
            if novamente in 'Nn':
                sys.exit()
            elif novamente in 'Ss':
                q = int(input('Quantos dígitos a senha deve conter? '))
                break            
    else: 
        break        