

file = open("Categoria", 'r', encoding="utf8")

categoria_nome = str(input('Por favor digite o seu nome do categoria: '))

for line in file:
    if categoria_nome in line:
        line.append(categoria_nome)
        print('line: ', categoria_nome.format())
        break
    print('line: ', categoria_nome.format())
file.close()

leitura = open("Categoria", 'w', encoding="utf8")
leitura.writelines(categoria_nome)

print('line: ', categoria_nome.format())
file.close()