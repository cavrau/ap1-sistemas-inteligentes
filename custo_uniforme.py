from copy import deepcopy

class Nodo:
    def __init__(self, _nodo, estado, vazio, numero_pais, custo=0):
        self.nodo_pai = _nodo
        self.estado = estado
        self.vazio = vazio
        self.numero_pais = numero_pais
        self.total_custo = custo + self.custo() + numero_pais
        self.solucao = (_nodo.solucao if _nodo else "")+ "------------------\n" + str(self)

    def __str__(self):
        return f"{self.estado[0]}\n{self.estado[1]}\n{self.estado[2]}\n"

    def custo(self):
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.estado[i][j] is None:
                    counter += abs((2-i) + (2-j))
                else:
                    counter += abs(((self.estado[i][j] // 3) - i) + (((self.estado[i][j] % 3) -1 )- j)) 
        return counter * 10


class CustoUniforme:

    def __init__(self, matriz):
        self.matriz = matriz
        for i, linha  in enumerate(matriz):
            for j, valor in enumerate(linha):
                if valor is None:
                    self.vazio = [i, j]
        self.estado_final = [
            [1,2,3], 
            [4,5,6], 
            [7,8,None]
        ]
        self.visitados = []
        self.nodo_solucao = None
        
    
    def gera_nodo(self, tar_1,tar_2, des_1,des_2):
        estado = deepcopy(self.nodo.estado)
        estado[tar_1][tar_2] = estado[des_1][des_2]
        estado[des_1][des_2] = None 
        return Nodo(self.nodo, estado, [des_1,des_2], self.nodo.numero_pais + 1, self.nodo.total_custo)


    def possiveis(self):
        if self.vazio[0] == 0:
            if self.vazio[1] == 0:
                possiveis = [
                    self.gera_nodo(0,0,1,0),
                    self.gera_nodo(0,0,0,1)
                ]
            if self.vazio[1] == 1:
                possiveis = [
                    self.gera_nodo(0,1,1,1),
                    self.gera_nodo(0,1,0,0),
                    self.gera_nodo(0,1,0,2),
                ]
            if self.vazio[1] == 2:
                possiveis = [
                    self.gera_nodo(0,2,1,2),
                    self.gera_nodo(0,2,0,1),
                ]
                
        elif self.vazio[0] == 1:
            if self.vazio[1] == 0:
                possiveis = [
                    self.gera_nodo(1,0,0,0),
                    self.gera_nodo(1,0,1,1),
                    self.gera_nodo(1,0,2,0),
                ]
            if self.vazio[1] == 1:
                possiveis = [
                    self.gera_nodo(1,1,0,1),
                    self.gera_nodo(1,1,1,0),
                    self.gera_nodo(1,1,1,2),
                    self.gera_nodo(1,1,2,1),
                ]
            if self.vazio[1] == 2:
                
                possiveis = [
                    self.gera_nodo(1,2,0,2),
                    self.gera_nodo(1,2,1,1),
                    self.gera_nodo(1,2,2,2),
                ]
        elif self.vazio[0] == 2:
            if self.vazio[1] == 0:
                possiveis = [
                    self.gera_nodo(2,0,1,0),
                    self.gera_nodo(2,0,2,1)
                ]
            if self.vazio[1] == 1:
                possiveis = [
                    self.gera_nodo(2,1,1,1),
                    self.gera_nodo(2,1,2,0),
                    self.gera_nodo(2,1,2,2),
                ]
            if self.vazio[1] == 2:
                possiveis = [
                    self.gera_nodo(2,2,1,2),
                    self.gera_nodo(2,2,2,1),
                ]
        
        return possiveis
                

    

    def busca(self):
        self.nodo = Nodo(None, self.matriz, self.vazio, 0)
        nodos_possiveis = self.possiveis()
        nodos_possiveis.sort(key=lambda x: x.total_custo)
        _nodo = nodos_possiveis.pop(0) 
        counter = 0
        fronteira = 0
        while _nodo:
            counter +=1
            self.nodo = _nodo
            if self.nodo_solucao and self.nodo.numero_pais > self.nodo_solucao.numero_pais:
                break
            if _nodo.estado == self.estado_final:
                if self.nodo_solucao:
                    if _nodo.numero_pais >= self.nodo_solucao.numero_pais:
                        _nodo = nodos_possiveis.pop(0)
                        continue
                    
                self.nodo_solucao = _nodo
                _nodo = nodos_possiveis.pop(0)
                continue
            if _nodo.estado in self.visitados:
                _nodo = nodos_possiveis.pop(0)
                continue
            if len(nodos_possiveis) > fronteira:
                fronteira = len(nodos_possiveis)
            self.vazio = _nodo.vazio
            filhos = self.possiveis()
            self.visitados.append(_nodo.estado)
            nodos_possiveis += [filho for filho in filhos if filho.estado not in self.visitados]
            nodos_possiveis.sort(key=lambda x: x.total_custo)
            _nodo = nodos_possiveis.pop(0)
        print("busca terminada")
        print(self.nodo_solucao.solucao)
        print(f"Foram visitados {counter} nodos")
        print(f"Foram criados {counter + len(nodos_possiveis)} nodos")
        print(f"A maior fronteira foi de {fronteira} nodos")
        print(f"O tamanho do caminho foi de {self.nodo_solucao.numero_pais} nodos")
        
            
CustoUniforme([[6,2,8], [1,7,None], [ 4,5, 3]]).busca()
