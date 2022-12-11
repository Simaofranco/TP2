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
        print(i+" ")
        if i == 'A5':
            print('\n')
        elif i == 'B5':
            print('\n')
        elif i == 'C5':
            print('\n')
        elif i == 'D5':
            print('\n')

def preço_bancadas(bancadas):
    '''
    Função para atribuit«r um preço a cada bancada
    '''
    for keys in bancadas.keys():
        bancadas[keys] = input("Insira o preço da bancada" + bancadas[keys] + ":")
    return bancadas

def eliminar_eventos(dic):
    """
    Elimina os items de um evento
    """
    del dic['name']
    del dic['artista']
    del dic['data']
    del dic['hora']
    del dic['local']
    return dic

def eliminar_bancadas(dic):
    """
    Elimina os preços das bancadas do evento 
    """
    del dic['A']
    del dic['B']
    del dic['C']
    del dic['D']
    return dic

def editar_evento(dic):
    """
    Edita um evento, atribui novos items ao dic do evento
    """
    dic['name'] = input("Insira um novo nome do evento:")
    dic['artista'] = input("Insira um novo nome do artista:")
    dic['data'] = input("Insira uma nova data do evento:")
    dic['hora'] = input("Insira uma nova hora do evento:")
    dic['local'] = input("Insira um novo nome do local do evento:")    
    return dic


def editar_bancadas(bancadas):
    '''
    Função para editar os preços de cada bancada
    '''
    for keys in bancadas.keys():
        bancadas[keys] = input("Insira um novo preço da bancada" + bancadas[keys] + ":")
    return bancadas



    

    