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
    