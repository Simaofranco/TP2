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
                #Criar eventos
                while True:
                    evento = int(input('\nQual o evento que pretende criar(1/2/3):'))
                    if evento == 1:
                        evento_1 = fg.criar_evento(evento_1)
                        bancadas_1 = fg.preço_bancadas(bancadas_1)
                        print('\nEvento criado com sucesso!')  
                        break
                    elif evento == 2:
                        evento_2 = fg.criar_evento(evento_2)
                        bancadas_2 = fg.preço_bancadas(bancadas_2)
                        print('\nEvento criado com sucesso!')  
                        break
                    elif evento == 3:
                        evento_3 = fg.criar_evento(evento_3)
                        bancadas_3 = fg.preço_bancadas(bancadas_3)
                        print('\nEvento criado com sucesso!')  
                        break
                    else:
                        print('Esse evento não existe!')
            elif(opcao == 2):
                while True:
                    evento = int(input('\nQual é o evento que pretende editar(1/2/3):'))
                    if evento == 1:
                        evento_1 = fg.editar_evento(evento_1)
                        bancadas_1 = fg.editar_bancadas(bancadas_1)
                        print('\nEvento editado com sucesso!')
                        break
                    elif evento == 2:
                        evento_2 = fg.editar_evento(evento_2)
                        bancadas_2 = fg.editar_bancadas(bancadas_2)
                        print('\nEvento editado com sucesso!')
                        break
                    elif evento == 3:
                        evento_2 = fg.editar_evento(evento_2)
                        bancadas_2 = fg.editar_bancadas(bancadas_3)
                        print('\nEvento editado com sucesso!')
                        break
                    else:
                        print('Esse evento não existe!')
            elif(opcao == 3):
                while True:
                    evento = int(input('\nQual é o evento que pretende eliminar(1/2/3):'))
                    if evento == 1:
                        evento_1 = fg.eliminar_eventos(evento_1)
                        bancadas_1 = fg.eliminar_bancadas(bancadas_1)
                        bilhetes_1 = fg.resetar_bilhetes(bilhetes_1)
                        print('\nEvento eliminado com sucesso!')
                        break
                    elif evento == 2:
                        evento_2 = fg.eliminar_eventos(evento_2)
                        bancadas_2 = fg.eliminar_bancadas(bancadas_2)
                        bilhetes_2 = fg.resetar_bilhetes(bilhetes_2)
                        print('\nEvento eliminado com sucesso!')
                        break
                    elif evento == 3:
                        evento_3 = fg.eliminar_eventos(evento_3)
                        bancadas_3 = fg.eliminar_bancadas(bancadas_3)
                        bilhetes_3 = fg.resetar_bilhetes(bilhetes_3)
                        print('\nEvento eliminado com sucesso!')
                        break
                    else:
                        print('Esse evento não existe!')
            elif(opcao == 4):
                while True:
                    evento = int(input('\nQual é o evento que pretende ver os bilhetes(1/2/3):'))
                    if evento == 1:
                        fg.ver_bilhetes(bilhetes_1)
                        break
                    elif evento == 2:
                        fg.ver_bilhetes(bilhetes_2)
                        break
                    elif evento == 3:
                        fg.ver_bilhetes(bilhetes_3)
                        break
                    else:
                        print('Esse evento não existe!')
            elif(opcao == 5):
                #Ver eventos
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
                fc.ver_eventos(evento_1, evento_2, evento_3)
            elif(opcao == 2):
                while True:
                    evento = int(input('\nQual é o evento que pretende comprar os bilhetes(1/2/3):'))
                    if evento == 1:
                        fc.comprar_bilhetes(bancadas_1, bilhetes_1)
                        break
                    elif evento == 2:
                        pass
                    elif evento == 3:
                        pass
                    else: 
                        print('Esse evento não existe!')

            elif(opcao == 3):
                exit()
            elif(opcao == 4):
                break
            else:
                print('\nInsira uma opção valida!')
    else:
        print('Insira um utilizador valido(g/c)')