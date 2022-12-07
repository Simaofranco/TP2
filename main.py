evento_1 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}
evento_2 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}
evento_3 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}

bancadas = ['A','B','C','D']




while True:
    utilizador = input('É gerente(g) ou cliente(c):')
    if utilizador == 'g':
        print("""
            #############################################
            #                Menu Gerente               #
            #############################################
            |                                           |
            |              1-Criar evento               |
            |              2- Editar evento             |
            |              3- Eliminar evento           |
            |                                           |
            |                  4-sair                   |
            |                                           |                                                    
            |                                           |
            #############################################
        """)
        opcao = int(input('\nInsira uma opção:'))
        if(opcao == 1):
            pass
        elif(opcao == 2):
            pass
        elif(opcao == 3):
            pass
        elif(opcao == 4):
            exit()

    elif utilizador == 'c':
        pass
    else:
        print('Insira um utilizador valido(g/c)')
        