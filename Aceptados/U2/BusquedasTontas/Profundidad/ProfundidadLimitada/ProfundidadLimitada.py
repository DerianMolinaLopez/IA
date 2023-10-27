'''
PROGRAMA DE BUSQEUDA DE PROFUNDIDAD LIMITADA CON LAS MATRICES NIVELADAS
'''

class ProfundidadLimitadaObj:
    def __init__(self) -> None:
        pass
    
    def profundidadLimitada(self, Frontier, Limite, nivel=0):
        Edo_Actual = Frontier[0][0]
        Nivel_Edo_Actual = Frontier[0][1]
        print(Edo_Actual)
        Frontier.pop(0)
        if self.goalTest(Edo_Actual):
            return Edo_Actual  # retorna el estado meta
        else:
            if Nivel_Edo_Actual < Limite:
                OffSpring = self.expand(Edo_Actual)
                OffSpring = self.asignarNivel(OffSpring, Nivel_Edo_Actual + 1)
                print(OffSpring)
                Frontier = self.insertarAlPrincipio(OffSpring, Frontier)
                print(Frontier)
                return self.profundidadLimitada(Frontier, Limite, nivel=Nivel_Edo_Actual)
            else:
                return False
    
    def insertarAlPrincipio(self, OffSpring, Frontier):
        return OffSpring + Frontier
    
    def asignarNivel(self, nodo, nivel):
        nodos_con_nivel = []
        for estado in nodo:
            nodos_con_nivel.append([estado, nivel])
        return nodos_con_nivel

    def expand(self, a):
        N = len(a)
        resultados = []
        for i in range(N):
            copia = a.copy()
            if (copia[i] < N):
                copia[i] = copia[i] + 1
            resultados.append(copia)
        return resultados
        
    def goalTest(self, a):
        return self.ataques(a) == 0
    
    def ataques(self, v):
        n = len(v)
        total_ataques = 0
        for i in range(n):
            for j in range(i + 1, n):
                if v[i] == v[j] or abs(i - j) == abs(v[i] - v[j]):
                    total_ataques += 2
        return total_ataques

#objLimita = ProfundidadLimitadaObj()
#objLimita.profundidadLimitada([[[1,1,1,1], 0]], 3)
