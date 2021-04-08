
# prod = open('Produto', 'r', encoding="utf8")
# produto_nome = input('Por favor digite o seu nome do produto: ')
# rod_nome = produto_nome.readlines()
# prod_nome.append(produto_nome)
# print('O nome do produto é: ', produto_nome.format())



file = open("Produtos", 'r', encoding="utf8")
produto_nome = str(input('Por favor digite o seu nome do produto: '))

for line in file:
    if produto_nome in line:
        line.append(produto_nome)
        #print('line: ', produto_nome.format())
        break
file.close() 

leitura = open("Produtos", 'a', encoding="utf8")
leitura.writelines(produto_nome)
print('line: ', produto_nome.format())
file.close()  