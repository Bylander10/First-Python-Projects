AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        print()
        print('<<<<TODOS OS CONTATOS>>>>')
        print()
        for contato in AGENDA:
            print(contato)
        print('------------------')
        escolha = input('Digite 0 para voltar ao menu ou 1 para expandir os contatos: ')
        if escolha == '1':
            print()
            for contato in AGENDA:
                buscar_contato(contato)
                print('------------------')
    else:
        print('Agenda vazia')


def buscar_contato(contato):
    try:
        print(f'Nome: {contato}')
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereço'])
    except KeyError:
        print('Contato inexistente!')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)


def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco


def incluir_editar_contatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereço': endereco
    }
    salvar()
    print()
    print(f'>>>>Contato {contato} adicionado/editado com sucesso<<<<')
    buscar_contato(contato)
    print()


def remover_contatos(chave):
    try:
        AGENDA.pop(chave)
        salvar()
        print()
        print(f'>>>> Contato {chave} removido <<<<')
        print()
    except KeyError:
        print('Contato inexistente!')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereço']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print('Agenda exportada com sucesso!')
    except Exception as error:
        print('Algum erro ocorreu ao exportar contatos!')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contatos(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Algum erro ocorreu')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereço': endereco
                }
        print('Database carregado com sucesso')
        print(f'{len(AGENDA)} contatos carregados')
    except FileNotFoundError:
        print('Agenda Vazia')
    except Exception as error:
        print('Algum erro ocorreu')
        print(error)


def imprimir_menu():
    print('---------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print('---------------------------------------')


# INÍCIO DO PROGRAMA

carregar()
while True:

    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato que deseja buscar: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print(f'Editando contato: {contato}')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contatos(contato, telefone, email, endereco)
        except KeyError:
            print('Contato inexistente')
    elif opcao == '5':
        while True:
            print('SEUS CONTATOS:')
            for i, contato in enumerate(AGENDA):
                print(f'{i + 1} - {contato}')
            contato = int(input('Selecione um número para excluir: '))
            lista_chaves = list(AGENDA)
            chave = lista_chaves[contato - 1]
            escolha = input(f'Tem certeza que deseja excluir {chave} (s/n)? ')
            if escolha == 's':
                remover_contatos(chave)
                break
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('>>>> Fechando programa')
        break
    else:
        print('>>>> Opção inválida')