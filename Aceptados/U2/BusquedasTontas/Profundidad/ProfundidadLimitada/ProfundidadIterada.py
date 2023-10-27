from ProfundidadLimitada import ProfundidadLimitadaObj as Bl
def profundidadIterada():
    Limite = 2
    while True:
        Frontier = [[1, 1, 1, 1], 0]  # Inicializa el estado inicial y el nivel en Frontier
        resultado = Bl().profundidadLimitada([Frontier], Limite)  # Llama al método profundidadLimitada
        if resultado:
            print("Solución encontrada:", resultado)
            break  # Si encuentra una solución, termina el bucle
        Limite += 2

profundidadIterada()