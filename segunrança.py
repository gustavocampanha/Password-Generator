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