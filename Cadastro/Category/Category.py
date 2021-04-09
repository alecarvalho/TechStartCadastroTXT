
def menu_opcoes(cursor, connection):
    print("\n" * 100)
    while True:
        print("\n      OPÇÕES DISPONÍVEIS NO BD:\n          1 - INSERIR\n          2 - PESQUISAR\n          3 - ALTERAR\n          4 - EXCLUIR\n          5 - LISTAR\n          6 - SAIR\n")
        opcao = int(input("DÍGITE SUA OPÇÃO > "))
        if opcao == 1:
            inserir(cursor, connection)
        elif opcao == 2:
            pesquisar(cursor)
        elif opcao == 3:
            alterar(cursor, connection)
        elif opcao == 4:
            excluir(cursor, connection)
        elif opcao == 5:
            listar(cursor)
        elif opcao == 6:
            print("\n" * 100)
            print("\n\n>>>>>>> VOCÊ SAIU DO BANCO DE DADOS! <<<<<<<")
        else:
            print("\nOpção inválida, escolhas uma das 6 opções disponíveis para continuar!\n")


def inserir(cursor, connection):
    #print("\n"*100)
    #print("\n     --- INSERÇÃO DE NOVA CATEGORIA NO BANCO DE DADOS ---\n")
    #arquivo = open('categoria.txt','a+')
    nome = str(input("Digite o nome da categoria "))
    descricao = str(input("Digite a descrição da categoria "))

    cursor.execute(f'INSERT INTO Category (name, description) VALUES ("{nome}", "{descricao}")')
    connection.commit()
    

    # arquivo.writelines(str(nome) + "\n")
    # arquivo.writelines("Categoria.............: ")

    # arquivo.writelines("Descrição.............: ")
    # arquivo.writelines(str(descricao) + "\n")

    # arquivo.write("\n----------------------------------------------------\n")
    # arquivo.close()

    print('CATEGORIA CADASTRADA COM SUCESSO!')
    continuar_cadastro = str(input("Deseja cadastrar outra categoria (S/N)? >>> ")).upper()
    if continuar_cadastro == "S":
        inserir(cursor, connection)
    elif continuar_cadastro == "N":
        continuar_programa()
    

def listar(cursor):
    # arquivo = open('categoria.txt','r')
    # a = arquivo.readlines()
    # for linha in a:
    #     linha = linha.rstrip()
    #     print(linha)
    # arquivo.close()

    cursor.execute('SELECT * FROM Category')
    print(cursor.fetchall())

def pesquisar(cursor):
    # arquivo = open('categoria.txt','r')
    # a = arquivo.readlines()
    prod = input("Dígite a categoria: ")
    cursor.execute(f'SELECT * FROM Category WHERE name = "{prod}"')
    print(cursor.fetchall())
    # for line in a:
    #     if prod in line:
    #         posicao_prod = (a.index(line))
    #         print("\n" + a[posicao_prod].rstrip())
    #         print("Resultado da pesquisa: {}".format(a[posicao_prod].rstrip()))
            
    print("\nDeseja realizar uma nova pesquisa?") 
    cont = int(input("1 - SIM\n2 - MENU PRINCIPAL\nDigite sua escolha: "))              
    if cont == 1:
        pesquisar()
    elif cont == 2:
        menu_opcoes()
    else:
        print("Valor inválido, escolha uma das duas opções disponíveis")

def excluir(cursor, connection):
    # arquivo = open('categoria.txt', 'r+')
    # a = arquivo.readlines()
    prod = str(input("Dígite o nome da código (id) que deseja excluir do banco de dados: "))
    cursor.execute(f'DELETE FROM Category WHERE category_id = "{prod}"')
    connection.commit()
    # for line in a:
    #     if prod in line:
    #         posicao_prod = (a.index(line))
    #         a[posicao_prod] = ""
    #         arquivo = open('categoria.txt','w')
    #         arquivo.writelines(a)
    # arquivo.close()

def continuar_programa():
    while True:
        print("\n>>> Dígite 1 para ir para o menu principal.")
        print(">>> Dígite 2 para sair do Banco de dados.")
        continuar = int(input("Dígite sua opção: "))
        if continuar == 1:
            print("\n"*100)
            menu_opcoes()
        elif continuar == 2:
            print("\n"*100)
            print("\n\n>>>>>>> VOCÊ SAIU DO BANCO DE DADOS! <<<<<<<")
            break
        else:
             print("Valor inválido, digite 1 = Sim ou 2 = Não.")

def alterar(cursor, connection):
    # arquivo = open('categoria.txt','r+')
    # a = arquivo.readlines()
    prod = str(input("Dígite o nome da categoria que deseja fazer alterações: "))
    novo_nome = str(input("Dígite o novo nome da categoria que deseja incluir: "))
    cursor.execute(f'UPDATE Category SET name = "{novo_nome}" WHERE category_id "{prod}"')
    connection.commit()
    print('CATEGORIA ALTERADA COM SUCESSO')


    # arquivo = open('categoria.txt', 'w')
    # for line in a:
    #     if prod in line:
    #         posicao_prod = (a.index(line))
           
    #         a[posicao_prod] = (novo_nome)+"\n"
    #         arquivo.writelines(a)
    # arquivo.close()