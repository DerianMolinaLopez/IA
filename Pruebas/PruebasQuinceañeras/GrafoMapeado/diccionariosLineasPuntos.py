puntos = {
            'Kiev': (10, -6.8),
            'Atenas': (7, -40),
            'Viena': (-6, -14),
            'Bucarest': (10, -20.5),
            'Berlin': (-9, -4),
            'Zagreb': (-5, -20),
            'Amsterdam': (-19, -2),
            'Brucelas': (-21, -6),
            'Andorra': (-28, -25.8),
            'Paris':(-23, -10),
            'Madrid':(-37,-30),
            'Berna':(-17, -17)  
        }

#orden de las lineas
'''
madrid-andorra
andorra-paris
paris-brucelas
brucelas-amsterdam
amsterdam-berlin
bruceslas-berlin
parus-berna
berna-viena
viean-zagreb
viena-zagreb
zagreb-bucarest
atenas-zagreb
bucarest-kiev
berlin-kiev

'''

lineas = {
    ('Madrid', 'Andorra'): { 'linestyle': '-'},
    ('Andorra', 'Paris'): {'linestyle': '-'},
    ('Paris', 'Brucelas'): {'linestyle': '-'},
    ('Brucelas', 'Amsterdam'): { 'linestyle': '-'},
    ('Amsterdam', 'Berlin'): { 'linestyle': '-'},
    ('Brucelas', 'Berlin'): { 'linestyle': '-'},
    ('Paris', 'Berna'): { 'linestyle': '-'},
    ('Berna', 'Viena'): { 'linestyle': '-'},
    ('Viena', 'Zagreb'): { 'linestyle': '-'},
    ('Viena', 'Zagreb'): { 'linestyle': '-'},
    ('Zagreb', 'Bucarest'): { 'linestyle': '-'},
    ('Atenas', 'Zagreb'): { 'linestyle': '-'},
    ('Bucarest', 'Kiev'): {'linestyle': '-'},
    ('Berlin', 'Kiev'): {'linestyle': '-'},
}

