''' 
Create a script that will print each key - value pair 
to the terminal in format: "Key: <value> | Value: <value>" 
'''

film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump is
                    the same house used in The Patriot
                    (2000). Some paneling was changed
                    for interior shots  in the latter
                    film.'''}

keys = list(film.keys())

while keys:
    first_key = keys.pop(0)
    print(f'Key: {first_key} | Value: {film.get(first_key)} ')

