import Nodo as Nodo
from AradBucarestGrafica import MapaCiudades
from diccionarioGrafico import puntos, lines
import tkinter as tk
from tkinter import ttk

# Definicion de la clase Nodo
nodo = Nodo.Nodo

# Nodos
arad = nodo('Arad')
bucarest = nodo('Bucarest')
craiova = nodo('Craiova')
dobreta = nodo('Dobreta')
eforie = nodo('Eforie')
fagaras = nodo('Fagaras')
giurgiu = nodo('Giurgiu')
hirsova = nodo('Hirsova')
iasi = nodo('Iasi')
lugoj = nodo('Lugoj')
mehadia = nodo('Mehadia')
neamt = nodo('Neamt')
oradea = nodo('Oradea')
pitesti = nodo('Pitesti')
rimnicu_vilcea = nodo('Rimnicu Vilcea')
sibiu = nodo('Sibiu')
timisoara = nodo('Timisoara')
urziceni = nodo('Urziceni')
vaslui = nodo('Vaslui')
zerind = nodo('Zerind')

# Lista de Adyacentes
arad.agregar_adyacente(sibiu, 140)
arad.agregar_adyacente(timisoara, 118)
arad.agregar_adyacente(zerind, 75)

bucarest.agregar_adyacente(fagaras, 211)
bucarest.agregar_adyacente(giurgiu, 90)
bucarest.agregar_adyacente(pitesti, 101)
bucarest.agregar_adyacente(urziceni, 85)

craiova.agregar_adyacente(dobreta, 120)
craiova.agregar_adyacente(pitesti, 138)
craiova.agregar_adyacente(rimnicu_vilcea, 146)

dobreta.agregar_adyacente(craiova, 120)
dobreta.agregar_adyacente(mehadia, 75)

eforie.agregar_adyacente(hirsova, 86)

fagaras.agregar_adyacente(bucarest, 211)
fagaras.agregar_adyacente(sibiu, 99)

giurgiu.agregar_adyacente(bucarest, 90)

hirsova.agregar_adyacente(eforie, 86)
hirsova.agregar_adyacente(urziceni, 98)

iasi.agregar_adyacente(neamt, 87)
iasi.agregar_adyacente(vaslui, 92)

lugoj.agregar_adyacente(mehadia, 70)
lugoj.agregar_adyacente(timisoara, 111)

mehadia.agregar_adyacente(dobreta, 75)
mehadia.agregar_adyacente(lugoj, 70)

neamt.agregar_adyacente(iasi, 87)

oradea.agregar_adyacente(sibiu, 151)
oradea.agregar_adyacente(zerind, 71)

pitesti.agregar_adyacente(bucarest, 101)
pitesti.agregar_adyacente(craiova, 138)
pitesti.agregar_adyacente(rimnicu_vilcea, 97)

rimnicu_vilcea.agregar_adyacente(craiova, 146)
rimnicu_vilcea.agregar_adyacente(pitesti, 97)
rimnicu_vilcea.agregar_adyacente(sibiu, 80)

sibiu.agregar_adyacente(arad, 140)
sibiu.agregar_adyacente(fagaras, 99)
sibiu.agregar_adyacente(oradea, 151)
sibiu.agregar_adyacente(rimnicu_vilcea, 80)

timisoara.agregar_adyacente(arad, 118)
timisoara.agregar_adyacente(lugoj, 111)

urziceni.agregar_adyacente(bucarest, 85)
urziceni.agregar_adyacente(hirsova, 98)
urziceni.agregar_adyacente(vaslui, 142)

vaslui.agregar_adyacente(iasi, 92)
vaslui.agregar_adyacente(urziceni, 142)

zerind.agregar_adyacente(arad, 75)
zerind.agregar_adyacente(oradea, 71)

# Tabla de Heuristica
tablaValores = dict()
tablaValores = {'Arad': 366,
                'Bucarest': 0,
                'Craiova': 160,
                'Dobreta': 242,
                'Eforie': 161,
                'Fagaras': 176,
                'Giurgiu': 77,
                'Hirsova': 151,
                'Iasi': 226,
                'Lugoj': 244,
                'Mehadia': 241,
                'Neamt': 234,
                'Oradea': 380,
                'Pitesti': 100,
                'Rimnicu Vilcea': 193,
                'Sibiu': 253,
                'Timisoara': 329,
                'Urziceni': 80,
                'Vaslui': 199,
                'Zerind': 374}

# Algoritmo A*
frontera = []
acumulado = 0
total = 0

listaYaVisitados = []
listAux = []


def algoritmoAestrella(frontera):
    if frontera == []:
        print("No hay solucion")
        return
    else:
        valor = frontera.pop(0)
        print(valor[1].getNombre())
        if valor[1].getNombre() in listaYaVisitados:  # el proble es en como estas haciendo el pop, el orden
            listAux.append(valor[1].getNombre())
            valor = frontera.pop(0)

            listAux.append(valor[1].getNombre())
            print(listAux)

        print(valor)
        print(valor[1].getNombre())
        listAux.append(valor[1].getNombre())
        estadoActual = valor[1]  # Como regresa una tupla, se obtiene el segundo elemento de la tupla que es el nodo
        listaYaVisitados.append(estadoActual.getNombre())

        if estadoActual == bucarest:  # goalTest
            print("Solucion encontrada")
            return

        else:
            sucesor = estadoActual.obtener_adyacentes()  # expand
            sucesor = evaluacion(acumulado, sucesor, estadoActual)  # evaluate
            frontera = frontera + sucesor
            frontera.sort()  # el sort que se haga con este metodo
            print(f"ListasVisitaods:{listaYaVisitados}")
            print(f"ListaAux:{listAux}")

            algoritmoAestrella(frontera)


def evaluacion(acumulado, sucesores, anterior):
    listaTemp = []
    for sucesor in sucesores:
        gn = acumulado + anterior.getCosto(sucesor)
        hn = tablaValores.get(sucesor.getNombre())
        total = gn + hn
        print(f"nodo;{sucesor.getNombre()}  {gn}----{hn}----{total}")
        listaTemp.append((total, sucesor, gn))
    # print(f"Lista Temporal{listaTemp[1]}")
    return listaTemp


###########################VENTANA EMERGENTE##########################33

def seleccionar_ciudad():
    ciudad_seleccionada = ciudad_var.get()
    # Obtener el nodo correspondiente al nombre de la ciudad seleccionada
    nodo_seleccionado = None
    for nodo in [arad, bucarest, craiova, dobreta, eforie, fagaras, giurgiu, hirsova, iasi, lugoj, mehadia, neamt,
                 oradea, pitesti, rimnicu_vilcea, sibiu, timisoara, urziceni, vaslui, zerind]:
        if nodo.getNombre() == ciudad_seleccionada:
            nodo_seleccionado = nodo
            break

    if nodo_seleccionado:
        frontera.append((0, nodo_seleccionado, 0))
        ventana.destroy()
        # Llamar al algoritmo A* con la nueva frontera
        algoritmoAestrella(frontera)


####################################################################
# Crear una ventana emergente
ventana = tk.Tk()
ventana.title("Seleccionar Ciudad para Frontera")

# Lista de nombres de ciudades
ciudades = list(puntos.keys())

# Variable de control para la lista desplegable
ciudad_var = tk.StringVar()
ciudad_var.set(ciudades[0])  # Valor predeterminado

# Crear una lista desplegable
etiqueta = tk.Label(ventana, text="Selecciona una ciudad:")
etiqueta.pack(padx=10, pady=10)
lista_desplegable = ttk.Combobox(ventana, textvariable=ciudad_var, values=ciudades)
lista_desplegable.pack(padx=10, pady=10)

# Botón para confirmar la selección
boton_confirmar = tk.Button(ventana, text="Agregar a Frontera", command=seleccionar_ciudad)
boton_confirmar.pack(padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
##################################################################################

''''''
mapeado = MapaCiudades(puntos, lines)
# mapa = MapaCiudades(puntos, lines)
mapeado.dibujar_ciudades()
mapeado.dibujar_lineas()

print(f"Nodos:{listaYaVisitados}")
mapeado.resaltar_ruta(listaYaVisitados)