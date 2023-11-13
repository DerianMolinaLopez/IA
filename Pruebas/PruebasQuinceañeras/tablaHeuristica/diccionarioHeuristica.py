'''
DEFINCIION GLOBAL DEL DICCIONARIO DE TABLA DE EURISTICAS
'''
lineasRectas = {
    'Kiev': {
        'Kiev': 0, 'Sofia': 968, 'Atenas': 1430, 'Viena': 1100, 'Lisboa': 3124,
        'Bucarest': 660, 'Berlín': 1100, 'Zagreb': 1232, 'Ámsterdam': 1650,
        'Bruselas': 1782, 'Berna': 1694, 'Andorra la vieja': 2244
    },
    'Sofia': {
        'Kiev': 968, 'Sofia': 0, 'Atenas': 528, 'Viena': 770, 'Lisboa': 2574,
        'Bucarest': 286, 'Berlín': 1232, 'Zagreb': 660, 'Ámsterdam': 1628,
        'Bruselas': 1606, 'Berna': 1254, 'Andorra la vieja': 1672
    },
    'Atenas': {
        'Kiev': 1430, 'Sofia': 528, 'Atenas': 0, 'Viena': 1210, 'Lisboa': 2706,
        'Bucarest': 704, 'Berlín': 1683, 'Zagreb': 1056, 'Ámsterdam': 2013,
        'Bruselas': 1938, 'Berna': 1550, 'Andorra la vieja': 1848
    },
    'Viena': {
        'Kiev': 1100, 'Sofia': 770, 'Atenas': 1210, 'Viena': 0, 'Lisboa': 2145,
        'Bucarest': 816, 'Berlín': 490, 'Zagreb': 253, 'Ámsterdam': 880,
        'Bruselas': 847, 'Berna': 836, 'Andorra la vieja': 1454
    },
    'Lisboa': {
        'Kiev': 3124, 'Sofia': 2574, 'Atenas': 2706, 'Viena': 2145, 'Lisboa': 0,
        'Bucarest': 3036, 'Berlín': 2200, 'Zagreb': 2068, 'Ámsterdam': 1793,
        'Bruselas': 1584, 'Berna': 1492, 'Andorra la vieja': 946
    },
    'Bucarest': {
        'Kiev': 660, 'Sofia': 286, 'Atenas': 704, 'Viena': 816, 'Lisboa': 3036,
        'Bucarest': 0, 'Berlín': 1199, 'Zagreb': 748, 'Ámsterdam': 1650,
        'Bruselas': 1650, 'Berna': 1353, 'Andorra la vieja': 1868
    },
    'Berlín': {
        'Kiev': 1100, 'Sofia': 1232, 'Atenas': 1683, 'Viena': 490, 'Lisboa': 2200,
        'Bucarest': 1199, 'Berlín': 0, 'Zagreb': 715, 'Ámsterdam': 517,
        'Bruselas': 600, 'Berna': 700, 'Andorra la vieja': 1320
    },
    'Zagreb': {
        'Kiev': 1232, 'Sofia': 660, 'Atenas': 1056, 'Viena': 253, 'Lisboa': 2068,
        'Bucarest': 748, 'Berlín': 715, 'Zagreb': 0, 'Ámsterdam': 990,
        'Bruselas': 935, 'Berna': 847, 'Andorra la vieja': 1144
    },
    'Ámsterdam': {
        'Kiev': 1650, 'Sofia': 1628, 'Atenas': 2013, 'Viena': 880, 'Lisboa': 1793,
        'Bucarest': 1650, 'Berlín': 517, 'Zagreb': 990, 'Ámsterdam': 0,
        'Bruselas': 154, 'Berna': 583, 'Andorra la vieja': 1034
    },
    'Bruselas': {
        'Kiev': 1782, 'Sofia': 1606, 'Atenas': 1938, 'Viena': 847, 'Lisboa': 1584,
        'Bucarest': 1650, 'Berlín': 600, 'Zagreb': 935, 'Ámsterdam': 154,
        'Bruselas': 0, 'Berna': 440, 'Andorra la vieja': 880
    },
    'Berna': {
        'Kiev': 1694, 'Sofia': 1254, 'Atenas': 1550, 'Viena': 836, 'Lisboa': 1492,
        'Bucarest': 1353, 'Berlín': 700, 'Zagreb': 847, 'Ámsterdam': 583,
        'Bruselas': 440, 'Berna': 0, 'Andorra la vieja': 627
    },
    'Andorra la vieja': {
        'Kiev': 2244, 'Sofia': 1672, 'Atenas': 1848, 'Viena': 1454, 'Lisboa': 946,
        'Bucarest': 1868, 'Berlín': 1320, 'Zagreb': 1144, 'Ámsterdam': 1034,
        'Bruselas': 880, 'Berna': 627, 'Andorra la vieja': 0
    }
}
