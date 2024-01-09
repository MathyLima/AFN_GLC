class No:
    def __init__(self, dado):
        self.dado = dado
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, valor_transicao):
        if vizinho not in self.vizinhos:
            self.vizinhos[vizinho] = valor_transicao


class Grafo:
    def __init__(self):
        self.nos = {}

    def adicionar_no(self, valor):
        if valor not in self.nos:
            novo_no = No(valor)
            self.nos[valor] = novo_no

    def adicionar_aresta(self, origem, destino, valor_transicao):
        if origem in self.nos and destino in self.nos:
            self.nos[origem].adicionar_vizinho(destino, valor_transicao)
        if valor_transicao == " ":
            self.nos[origem].adicionar_vizinho(origem," ")

    def mostrar_grafo(self):
        for valor, no in self.nos.items():
            vizinhos = ', '.join([f"{vizinho} ({valor_transicao})" for vizinho, valor_transicao in no.vizinhos.items()])
            print(f"{valor} -> {vizinhos}")

    def transitar(self,origem,destino):
        if origem in self.nos and destino in self.nos:
            if destino in self.nos[origem].vizinhos:
                print(f"Transicao de {origem} para destino realizada com sucesso. Valor da tansição: {self.nos[origem].vizinhos[destino]}")
            else:
                print(f"Não há uma transição direta de {origem} para {destino}")
        else:
            print("Nós não foram encontrados no grafo")
    

    def obter_possiveis_escolhas(grafo, no_atual):
        possiveis_escolhas = []
        if no_atual in grafo.nos:
            vizinhos = grafo.nos[no_atual].vizinhos
            if vizinhos:
                for vizinho, valor_transicao in vizinhos.items():
                    possiveis_escolhas.append(f"Vizinho: {vizinho}, Valor da transição: {valor_transicao}")
        else:
            print("O nó atual não existe no grafo.")
        
        return possiveis_escolhas
        
        
