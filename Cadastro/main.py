from Product.Product import menu_opcoes as product_options
from Category.Category import menu_opcoes as category_options
import sqlite3

def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Category (
            category_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(50) NOT NULL, 
            description VARCHAR(100) NOT NULL
        ); '''
    )
    cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
            product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(50)
        ); '''
    )
    cursor.execute('''CREATE TABLE IF NOT EXISTS ProductCategory (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            product_id INT NOT NULL,
            category_id INT NOT NULL,
            FOREIGN KEY (category_id) REFERENCES Category(category_id),
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
        ); '''
    )

def main():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    create_tables(cur)
    choice = input('Selecione se quer trabalhar com produtos ou categorias: (p/c)\n')

    if choice == 'p':
        product_options(cur, con)
    elif choice == 'c':
        category_options()
    else:
        print('Por favor seleciona uma das opções (produtos ou categorias)')
        main()

main()
