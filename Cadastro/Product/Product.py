def menu_opcoes(cursor, connection=None):
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
    nome = str(input("Digite o nome do Produto: ")).upper()
    cursor.execute(f"INSERT INTO Product (name) VALUES ('{nome}')")

    connection.commit()
    
    continuar_cadastro = str(input("Desenha cadastrar outro produto (S/N)? >>> ")).upper()
    if continuar_cadastro == "S":
        inserir(cursor)
    elif continuar_cadastro == "N":
        continuar_programa()
    

def listar(cursor):
    cursor.execute("SELECT * FROM Product")
    print(cursor.fetchall())

def pesquisar(cursor):
    prod = input("\nDígite produto: ").upper()
    cursor.execute(f"SELECT * FROM Product WHERE name='{prod}'")
    print(cursor.fetchall())

    print("\nDeseja realizar uma nova pesquisa?") 
    cont = int(input("1 - SIM\n2 - MENU PRINCIPAL\nDigite sua escolha: "))               
    if cont == 1:
        pesquisar(cursor)
    elif cont == 2:
        menu_opcoes(cursor)
    else:
        print("Valor inválido, escolha uma das duas opções disponíveis")

################
def excluir(cursor, connection):
    prod = str(input("Dígite o código (id) do produto que deseja excluir do banco de dados: "))
    
    cursor.execute(f"DELETE FROM Product WHERE product_id='{prod}'")
    connection.commit()
    print('PRODUTO EXCLUIDO COM SUCESSO')

    # for line in a:
    #     if prod in line:
    #         posicao_prod = (a.index(line))
    #         a[posicao_prod] = ""
    #         arquivo = open('produtos.txt','w')
    #         arquivo.writelines(a)
    # arquivo.close()

def alterar(cursor, connection):
    # arquivo = open('produtos.txt','r+')
    # a = arquivo.readlines()
    prod = str(input("Dígite o código (id) do produto que deseja fazer alterações: "))
    new_value = str(input("Dígite o novo nome do produto: "))

    cursor.execute(f"UPDATE Product SET name='{new_value}' WHERE product_id='{prod}'")
    connection.commit()
    print('PRODUTO ALTERADO COM SUCESSO')



    # for line in a:
    #     if prod in line:
    #         posicao_prod = (a.index(line))
    #         novo_nome = str(input("Dígite o novo nome do produto que deseja incluir: ")).upper()
           
    #         a[posicao_prod] = (novo_nome)+"\n"
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