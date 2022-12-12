def ver_eventos(dic1, dic2, dic3):    
    """
    Percorre os dicionarios dos eventos e mostra os seu items
    """
    print("Evento 1:\n")
    for keys in dic1.keys():
        print(keys+": "+dic1[keys])

    print("\nEvento 2:\n")
    for keys in dic2.keys():
        print(keys+": "+dic2[keys])

    print("\nEvento 3:\n")
    for keys in dic3.keys():
        print(keys+": "+dic3[keys])


def comprar_bilhetes(bancadas, list):
    """
    Mostra o preço de cada bancada, guarda o bilhete que o cliente quer comprar, 
    verifica se o bilhete está disponivel, adiciona a mensagem vendido à lista
    dos bilhetes, e diz que o bilhete foi comprado
    """
    print('Preços:\n')
    for keys in bancadas.keys():
        print('Bancada '+keys+': '+str(bancadas[keys])+'$\n')
    
    while True:
        bilhete = input('Qual o bilhete que quer comprar(A1-A5):')
        if bilhete in list:
            break
        else:
            print('O bilhete já esta vendido ou não existe!\n')
    
    for i in range(len(list)):
        if list[i] == bilhete:
            list[i] = str(list[i]+'- vendido')

    print('\nComprou o bilhete '+bilhete)


    