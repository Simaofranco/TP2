def criar_evento(dic):
    '''
    função para criar evento
    '''
    dic['name'] = input("Insira o nome do evento:")
    dic['artista'] = input("Insira o nome do artista:")
    dic['data'] = input("Insira a data do evento:")
    dic['hora'] = input("Insira a hora do evento:")
    dic['local'] = input("Insira o nome do local do evento:")
    return dic

def ver_bilhetes(bilhetes):
    '''
    função para ver bilhetes
    '''
    for i in bilhetes:
        print(i" ")
        if i == 'A5':
            print('\n')
        elif i == 'B5':
            print('\n')
        elif i == 'C5':
            print('\n')
        elif i == 'D5':
            print('\n')