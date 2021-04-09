def menu_opcoes():
    print("\n" * 100)
    while True:
        print("\n      OPÇÕES DISPONÍVEIS NO BD:\n          1 - INSERIR\n          2 - PESQUISAR\n          3 - ALTERAR\n          4 - EXCLUIR\n          5 - LISTAR\n          6 - SAIR\n")
        opcao = int(input("DÍGITE SUA OPÇÃO > "))
        if opcao == 1:
            inserir()
        elif opcao == 2:
            pesquisar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("\n" * 100)
            print("\n\n>>>>>>> VOCÊ SAIU DO BANCO DE DADOS! <<<<<<<")
        else:
            print("\nOpção inválida, escolhas uma das 6 opções disponíveis para continuar!\n")


def inserir():
    #print("\n"*100)
    #print("\n     --- INSERÇÃO DE NOVO PRODUTO NO BANCO DE DADOS ---\n")
    arquivo = open('produtos.txt','a+')
    nome = str(input("Digite o nome do Produto: ")).upper()

    arquivo.writelines("Produto.............: ")
    arquivo.writelines(str(nome) + "\n")

    arquivo.write("\n----------------------------------------------------\n")
    arquivo.close()
    print("\n----------------------------------------------------\n            PRODUTO CADASTRADO COM SUCESSO!\n----------------------------------------------------\n")
    continuar_cadastro = str(input("Desenha cadastrar outro produto (S/N)? >>> ")).upper()
    if continuar_cadastro == "S":
        inserir()
    elif continuar_cadastro == "N":
        continuar_programa()
    

def listar():
    arquivo = open('produtos.txt','r')
    a = arquivo.readlines()
    for linha in a:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

def pesquisar():
    arquivo = open('produtos.txt','r')
    a = arquivo.readlines()
    prod = input("\nDígite produto: ").upper()
    for line in a:
        if prod in line:
            posicao_prod = (a.index(line))
            print("\n" + a[posicao_prod].rstrip())
            print("Resultado da pesquisa: {}".format(a[posicao_prod].rstrip()))
            
    print("\nDeseja realizar uma nova pesquisa?") 
    cont = int(input("1 - SIM\n2 - MENU PRINCIPAL\nDigite sua escolha: "))              
    if cont == 1:
        pesquisar()
    elif cont == 2:
        menu_opcoes()
    else:
        print("Valor inválido, escolha uma das duas opções disponíveis")

def excluir():
    arquivo = open('produtos.txt', 'r+')
    a = arquivo.readlines()
    prod = str(input("Dígite o nome do produto que deseja excluir do banco de dados: ")).upper()
    for line in a:
        if prod in line:
            posicao_prod = (a.index(line))
            a[posicao_prod] = ""
            arquivo = open('produtos.txt','w')
            arquivo.writelines(a)
    arquivo.close()

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

def alterar():
    arquivo = open('produtos.txt','r+')
    a = arquivo.readlines()
    prod = str(input("Dígite o nome do produto que deseja fazer alterações: ")).upper()
    arquivo = open('produtos.txt', 'w')
    for line in a:
        if prod in line:
            posicao_prod = (a.index(line))
            novo_nome = str(input("Dígite o novo nome do produto que deseja incluir------------------------------------: ")).upper()
           
            a[posicao_prod] = (novo_nome)+"\n"
            arquivo.writelines(a)
    arquivo.close()
menu_opcoes()