import funcoes_gerente as fg
import funcoes_cliente as fc

evento_1 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}
evento_2 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}
evento_3 = {'nome':'', 'artista':'', 'data':'', 'hora':'', 'local':''}

bancadas_1 = {'A':0,'B':0,'C':0,'D':0}
bancadas_2 = {'A':0,'B':0,'C':0,'D':0}
bancadas_3 = {'A':0,'B':0,'C':0,'D':0} 

bilhetes_1 = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','D1','D2','D3','D4','D5',]
bilhetes_2 = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','D1','D2','D3','D4','D5',]
bilhetes_3 = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','D1','D2','D3','D4','D5',]


while True:
    utilizador = input('É gerente(g) ou cliente(c):')
    if utilizador == 'g':
        while True:
            print("""
                #############################################
                #                Menu Gerente               #
                #############################################
                |                                           |
                |              1-Criar evento               |
                |              2-Editar evento              |
                |              3-Eliminar evento            |
                |              4- Ver bilhetes              |
                |              5- Ver eventos               |
                |                 6-sair                    |
                |                 7-voltar                  |                                                    
                |                                           |
                #############################################
            """)
            opcao = int(input('\nInsira uma opção:'))
            if(opcao == 1):
                while True:
                    evento = int(input('\nInsira o evento que pretende criar(1/2/3):'))
                    if evento == 1:
                        evento_1 = fg.criar_evento(evento_1)
                        break
                    elif evento == 2:
                        evento_2 = fg.criar_evento(evento_2)
                        break
                    elif evento == 3:
                        evento_3 = fg.criar_evento(evento_3)
                        break
                    else:
                        print('Esse evento não existe!')
            elif(opcao == 2):
                pass
            elif(opcao == 3):
                pass
            elif(opcao == 4):
                pass
            elif(opcao == 5):
                fc.ver_eventos(evento_1, evento_2, evento_3)              
            elif(opcao == 6):
                exit()
            elif(opcao == 7):
                break
            else:
                print('\nInsira uma opção valida!')

    elif utilizador == 'c':
        while True:
            print('''
                *********************************************
                *                 Bem-Vindo                 *
                *********************************************
                |                                           |
                |                1-Ver eventos              |
                |              2-Comprar bilhetes           |            
                |                  3-sair                   |
                |                 4-voltar                  | 
                |                                           |
                |___________________________________________|                                         

        ''')
            opcao = int(input('\nInsira uma opção:'))
            if(opcao == 1):
                pass
            elif(opcao == 2):
                pass
            elif(opcao == 3):
                exit()
            elif(opcao == 4):
                break
            else:
                print('\nInsira uma opção valida!')
    else:
        print('Insira um utilizador valido(g/c)')