#At the beginning we have dictionary with tram stations.
# Our goal is to identify which stations are included in each list.

tram_stations = {
'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska',
          'Sumavska', 'Hrnicrska', 'Pionyrska', 'Antoninska', 'Moravske nam.',
          'Malinovske nam', 'Hlavni nadr.', 'Nove sady', 'Hybesova',
          'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2',
          'Lipova', 'Pisarky'],
'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska',
          'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady',
          'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM',
          'Celni', 'Hluboka', 'Ustredni hrbitov'],
'No.3' : ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka',
          'Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.',
          'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska',
          'Komenskeho nam.', 'Obilni trh', 'Uvoz']
}

list1 = set(tram_stations.get('No.1'))
list2 = set(tram_stations.get('No.2'))
list3 = set(tram_stations.get('No.3'))

print(list1 & list2 & list3)

