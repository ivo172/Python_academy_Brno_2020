# Vytvořte program, který uživateli umožní provádět následující akce:
# 1. Vytvořte tabulku
# 2. Vložte nový řádek do dané tabulky
# 3. Vložte nový sloupec do dané tabulky
# 4. Aktualizujte buňku v tabulce
# 5. Vypočítat součet pro vybraný sloupec
# 6. Vypočítat součet pro vybraný řádek
# 7. Tisk celé tabulky nebo vybraných řádků
# 8. Export tabulky do slovníku
# Program by měl běžet ve smyčce, dokud mu uživatel neřekne ukončení. 

while True:
    print(80 * '_')
    print('''What do we want to do?
    1-Create table  | 2-Insert new row | 3-Insert new column |
    4-Update a cell | 5-Column Total   | 6-Row Total         |
    7-Print Table   | 8-Export do List of Dicts              |''')
    your_choice = input('Enter the number: ')

    if your_choice == 1:
        print('OPTION 1')    
        print(80 * '_')
        header_names = input('Enter header names separated by comma (e.g. Name,Age,Email): ')
