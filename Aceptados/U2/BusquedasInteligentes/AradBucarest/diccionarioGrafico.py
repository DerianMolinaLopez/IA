import matplotlib.pyplot as plt

# Coordenadas de ciudades
puntos = {
    'Arad': (1, 4),
    'Zerind': (1.2, 6),
    'Sibiu': (2.6, 2),
    'Oradea': (1.5, 8),
    'Timisoara': (1, 1),
    'Lugoj': (2, -1),
    'Mehadia': (2, -3),
    'Dobreta': (1.8, -5),
    'Craiova': (3, -5.5),
    'Rimnicu Vilcea': (3, 0),
    'Fagaras': (4, 3),
    'Pitesti': (4, -2),
    'Bucarest': (6, -4),
    'Guirguiu': (5.5, -6),
    'Urziceni': (7, -3),
    'Vaslui': (8.5, 1),
    'Iasi': (8, 5),
    'Neamt': (6.5, 6.5),
    'Hirsova': (9, -3),
    'Eforie': (10, -5)
}

# Líneas entre las ciudades y sus distancias
lines = {
    ('Arad', 'Zerind'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Arad', 'Timisoara'): 118,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Dobreta'): 75,
    ('Dobreta', 'Craiova'): 120,
    ('Craiova', 'Pitesti'): 138,  # Nueva línea de Craiova a Pitesti con distancia 138
    ('Oradea', 'Sibiu'): 151,
    ('Sibiu', 'Arad'): 140,
    ('Rimnicu Vilcea', 'Sibiu'): 80,
    ('Sibiu', 'Fagaras'): 99,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Fagaras', 'Bucarest'): 211,
    ('Pitesti', 'Bucarest'): 101,
    ('Bucarest', 'Guirguiu'): 90,
    ('Bucarest', 'Urziceni'): 85,
    ('Urziceni', 'Vaslui'): 142,
    ('Vaslui', 'Iasi'): 92,
    ('Iasi', 'Neamt'): 87,
    ('Urziceni', 'Hirsova'): 98,
    ('Hirsova', 'Eforie'): 86
}
'''
#!dibujamos los puntos
for punto, coordenadas in puntos.items():
    plt.plot(coordenadas[0], coordenadas[1], marker='o', markersize=8, color='blue')
    plt.text(coordenadas[0], coordenadas[1], punto, fontsize=12, ha='right')
#!dibujamos las lineas
for (city1, city2), distance in lines.items():
    plt.plot([puntos[city1][0], puntos[city2][0]], [puntos[city1][1], puntos[city2][1]], color='red', linestyle='-', linewidth=2)
    plt.text((puntos[city1][0] + puntos[city2][0]) / 2, (puntos[city1][1] + puntos[city2][1]) / 2, str(distance), fontsize=10, color='green')



ciudades_a_resaltar = ['Arad', 'Sibiu', 'Fagaras']


# Dibujamos las lineas y resaltamos las líneas entre las ciudades especificadas
for i in range(len(ciudades_a_resaltar) - 1):
    city1, city2 = ciudades_a_resaltar[i], ciudades_a_resaltar[i + 1]
    # Intenta encontrar la distancia en el diccionario lines
    if (city1, city2) in lines:
        distance = lines[(city1, city2)]
    elif (city2, city1) in lines:  # Intenta la tupla en el orden inverso
        distance = lines[(city2, city1)]
    else:
        print(f"No se encontró la distancia entre {city1} y {city2}")
        continue  # Salta esta iteración si no se encuentra la distancia

    # Dibuja la línea resaltada
    plt.plot([puntos[city1][0], puntos[city2][0]], [puntos[city1][1], puntos[city2][1]], color='blue', linestyle='-', linewidth=4)
  #  plt.text((puntos[city1][0] + puntos[city2][0]) / 2, (puntos[city1][1] + puntos[city2][1]) / 2, str(distance), fontsize=12, color='green')



#!esto es para el zoom de la imagen
plt.xlim(0, 10) 
plt.ylim(-7, 10) 

#ocultamos los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis('off')


plt.show()

'''
