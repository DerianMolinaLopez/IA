import tkinter as tk
from tkinter import ttk, messagebox
from CiudadesObj import Ciudad
import math
import pandas as pd
from itertools import permutations
def seleccionar_ciudades():
    ciudades_disponibles = {
        1: "Kiev, Ucrania",
        2: "Sofia, Bulgaria",
        3: "Atenas, Grecia",
        4: "Viena, Austria",
        5: "Lisboa, Portugal",
        6: "Bucarest, Romania",
        7: "Berlin, Germany",
        8: "Zagreb, Croatia",
        9: "Amsterdam, Netherlands",
        10: "Bruselas, Belgium",
        11: "Berna, Switzerland",
        12: "Andorra la Vella, Andorra"
    }

    ciudades_seleccionadas = []  # Lista para almacenar ciudades seleccionadas
    """
     def actualizar_combobox_8(var_primero):
        # Actualizar ComboBox 8 con el valor del ComboBox 1
        comboboxes[-1].set(var_primero.get())   
    """


    def realizar_accion():
        nonlocal ciudades_seleccionadas
        # Obtiene los valores seleccionados de los ComboBox
        ciudades_seleccionadas = [combobox.get() for combobox in comboboxes[:7]]

        # Validar que no haya ciudades repetidas en los ComboBox del 1 al 7
        ciudades_set = set(ciudades_seleccionadas)
        if len(ciudades_set) == len(ciudades_seleccionadas):
            # No hay ciudades repetidas
            print("Ciudades seleccionadas:", ciudades_seleccionadas)
            root.destroy()  # Cierra la ventana cuando todo está bien
        else:
            # Hay ciudades repetidas, mostrar mensaje de advertencia
            ciudades_repetidas = [ciudad for ciudad in ciudades_set if ciudades_seleccionadas.count(ciudad) > 1]
            mensaje = f"No puedes seleccionar ciudades repetidas. Ciudad repetida: {', '.join(ciudades_repetidas)}"
            messagebox.showwarning("Ciudades Repetidas", mensaje)

    root = tk.Tk()
    root.title("Viaje por Europa")
    root.geometry("400x400")

    # Título en la ventana
    titulo_label = tk.Label(root, text="Selecciona tu destino XV en Europa", font=("Helvetica", 16))
    titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

    comboboxes = []

    # Variable de seguimiento para el ComboBox 1
    var_primero = tk.StringVar()
    #var_primero.trace_add("write", lambda *args: actualizar_combobox_8(var_primero))

    for i, (num, ciudad) in enumerate(list(ciudades_disponibles.items())[:8]):
        numero_label = tk.Label(root, text=str(num))
        numero_label.grid(row=i+1, column=0, padx=5, pady=5)

        text_variable = var_primero if i == 0 else None
        combobox = ttk.Combobox(root, values=list(ciudades_disponibles.values()), state="readonly", textvariable=text_variable)
        combobox.set(ciudades_disponibles[i+1])  # Valores iniciales diferentes
        combobox.grid(row=i+1, column=1, padx=5, pady=5)

        comboboxes.append(combobox)

    """
    # ComboBox 8
    numero_label_8 = tk.Label(root, text="8")
    numero_label_8.grid(row=8, column=0, padx=5, pady=5)
    combobox_8 = ttk.Combobox(root, values=list(ciudades_disponibles.values()), state="readonly", textvariable=var_primero)
    combobox_8.set(ciudades_disponibles[1])  # Reflejará dinámicamente el valor del ComboBox 1
    
    combobox_8.configure(state="readonly", takefocus=False)
    combobox_8.grid(row=8, column=1, padx=5, pady=5)
    comboboxes.append(combobox_8)
    """


    seleccionar_button = tk.Button(root, text="Realizar Acción", command=realizar_accion)
    seleccionar_button.grid(row=9, column=0, columnspan=2, pady=10)

    root.mainloop()

    return ciudades_seleccionadas


# Llamamos al método principal y almacenamos las ciudades seleccionadas
ciudades_seleccionadas = seleccionar_ciudades()
primer_valor = ciudades_seleccionadas[0]

# Agregar el primer valor al final de la lista
ciudades_seleccionadas.append(primer_valor)
# Ahora puedes trabajar con la lista de ciudades seleccionadas
print("Ciudades seleccionadas fuera de la función:", ciudades_seleccionadas )

gx = pd.read_csv("Aceptados\\U3\\XVaneras\\tabla_costos.csv")
gx = gx.set_index('Ciudad')
def getDistanciaAS(ori, fin):
    r =gx.loc[ori,fin]

    return r

def distancia(X1,Y1,X2,Y2):
  return abs(math.sqrt(((X2 - X1)**2) + ((Y2 - Y1)**2)))

def permutList(l):
  if not l:
    return [[]]
  l.append(l[0])
  subciudades = l[1:8]
  return list(permutations(subciudades))

Kiev = Ciudad("Kiev, Ucrania",    50.467981379817815, 30.527779407460397)
Sofia = Ciudad("Sofia, Bulgaria",    42.69985582624216, 23.31775344745848)
Atenas = Ciudad("Atenas, Grecia",    37.972675434696434, 23.719077070526172)
Viena = Ciudad("Viena, Austria",    48.206825617973095, 16.37674883580833)
Lisboa = Ciudad("Lisboa, Portugal",    38.72235565217588, -9.132939181769217)
Bucarest = Ciudad("Bucarest, Romania",    44.426763958980914, 26.105621291454796)
Berlin = Ciudad("Berlin, Germany",    52.519683845446124, 13.393824044940256)
Zagreb = Ciudad("Zagreb, Croatia",    45.815233909185984, 15.984274198017319)
Amsterdam = Ciudad("msterdam, Netherlands",    52.36922271743421, 4.900299838856)
Bruselas = Ciudad("Bruselas, Belgium",    50.84763858612332, 4.352281687217245)
Berna = Ciudad("Berna, Switzerland",    46.94778973905876, 7.446261829815972)
Andorra = Ciudad("Andorra la Vella, Andorra",    42.50643748395003, 1.5219176066786817)


Lisboa.setVecinos([Andorra])
Andorra.setVecinos([Lisboa, Berna])
Berna.setVecinos([Andorra, Bruselas, Viena])
Bruselas.setVecinos([Amsterdam, Berlin, Berna])
Amsterdam.setVecinos([Berlin, Bruselas])
Berlin.setVecinos([Amsterdam, Bruselas, Kiev])
Kiev.setVecinos([Berlin, Bucarest])
Bucarest.setVecinos([Sofia, Kiev, Zagreb])
Sofia.setVecinos([Zagreb, Bucarest])
Zagreb.setVecinos([Atenas, Bucarest, Sofia, Viena])
Viena.setVecinos([Berna, Zagreb])
Atenas.setVecinos([Zagreb])
resultado = [] #formato [fx, permutacion]
permutaciones =permutList(ciudades_seleccionadas)
#print(permutaciones)
for i in range(len(permutaciones)):
    permutacionActual = list(permutaciones[i])
    permutacionActual.append(primer_valor)
    permutacionActual.insert(0, primer_valor)
    acumulado = 0
    #pares_con_segundo_valor = []

    for j in range(len(permutacionActual) - 1):
        tupla_actual = (permutacionActual[j], permutacionActual[j + 1])
        ciudadActual = permutacionActual[j]
        ciudadSiguiente = permutacionActual[j+1]
        acumulado += int(getDistanciaAS(ciudadActual, ciudadSiguiente))
        #pares_con_segundo_valor.append(tupla_actual)

    resultado.append([acumulado,permutacionActual])

    resultado.append([acumulado,permutacionActual])
#ordena para sacar el mejor costo
resultado.sort()

print("**************************************")
print("La mejor ruta es:" + str(resultado[0][1]))
print("con un coste de :" + str(resultado[0][0]))

#Para graficar
#********************************************************

# Importar la librería gmplot
import gmplot
import googlemaps

ciudades = {
"Kiev, Ucrania": (50.467981379817815, 30.527779407460397),
"Sofia, Bulgaria": (42.69985582624216, 23.31775344745848),
"Atenas, Grecia": (37.972675434696434, 23.719077070526172),
"Viena, Austria": (48.206825617973095, 16.37674883580833),
"Lisboa, Portugal": (38.72235565217588, -9.132939181769217),
"Bucarest, Romania": (44.426763958980914, 26.105621291454796),
"Berlin, Germany": (52.519683845446124, 13.393824044940256),
"Zagreb, Croatia": (45.815233909185984, 15.984274198017319),
"Amsterdam, Netherlands": (52.36922271743421, 4.900299838856),
"Bruselas, Belgium": (50.84763858612332, 4.352281687217245),
"Berna, Switzerland": (46.94778973905876, 7.446261829815972),
"Andorra la Vella, Andorra": (42.50643748395003, 1.5219176066786817)
}
solucion = resultado[0][1]

key = 'AIzaSyD6Sg3csJVzgI6RxNS_m1NsZxdblPzshWY'

gmaps = googlemaps.Client(key=key)

nombres = [ciudad for ciudad in solucion]

ruta = gmaps.directions(nombres[0], nombres[-1], waypoints=nombres[1:-1], mode='driving', language='es')[0]
latitudes = []
longitudes = []
for leg in ruta['legs']:
    for step in leg['steps']:
        start = step['start_location']
        end = step['end_location']
        latitudes.append(start['lat'])
        longitudes.append(start['lng'])
        latitudes.append(end['lat'])
        longitudes.append(end['lng'])

gmap = gmplot.GoogleMapPlotter(48.8566, 2.3522, 4, apikey=key)

gmap.plot(latitudes, longitudes, 'red', edge_width=3)
gmap.draw('Aceptados\\U3\\XVaneras\\mapa.html')