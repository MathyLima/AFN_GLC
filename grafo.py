class No:
    """
    Classe que representa um nó em um grafo.

    Attributes:
        dado: O dado armazenado no nó.
        vizinhos: Um dicionário que mapeia os nós vizinhos aos valores de transição.

    Methods:
        __init__(self, dado):
            Inicializa um objeto No com o dado fornecido e um dicionário vazio de vizinhos.

        adicionar_vizinho(self, vizinho, valor_transicao):
            Adiciona um vizinho ao nó com o valor de transição fornecido.

    """

    def __init__(self, dado):
        """
        Inicializa um objeto No com o dado fornecido e um dicionário vazio de vizinhos.

        Args:
            dado: O dado a ser armazenado no nó.

        Returns:
            None
        """
        self.dado = dado
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, valor_transicao):
        """
        Adiciona um vizinho ao nó com o valor de transição fornecido.

        Args:
            vizinho: O nó vizinho a ser adicionado.
            valor_transicao: O valor da transição para o vizinho.

        Returns:
            None
        """
        if vizinho not in self.vizinhos:
            self.vizinhos[vizinho] = valor_transicao


class Grafo:
    """
    Classe que representa um grafo.

    Attributes:
        nos: Um dicionário que mapeia os valores dos nós aos objetos No correspondentes.

    Methods:
        __init__(self):
            Inicializa um grafo com um dicionário vazio de nós.

        adicionar_no(self, valor):
            Adiciona um nó com o valor fornecido ao grafo, se ainda não estiver presente.

        adicionar_aresta(self, origem, destino, valor_transicao):
            Adiciona uma aresta direcionada do nó de origem para o nó de destino com o valor de transição fornecido.

        mostrar_grafo(self):
            Exibe uma representação visual do grafo na forma de pares de valores de nó e seus vizinhos.

        transitar(self, origem, destino):
            Verifica se há uma transição direta do nó de origem para o nó de destino e exibe o valor da transição, se existir.

        obter_possiveis_escolhas(grafo, no_atual):
            Obtém uma lista de possíveis escolhas (vizinhos) a partir do nó atual em um grafo.

    """

    def __init__(self):
        """
        Inicializa um grafo com um dicionário vazio de nós.

        Returns:
            None
        """
        self.nos = {}

    def adicionar_no(self, valor):
        """
        Adiciona um nó com o valor fornecido ao grafo, se ainda não estiver presente.

        Args:
            valor: O valor do nó a ser adicionado.

        Returns:
            None
        """
        if valor not in self.nos:
            novo_no = No(valor)
            self.nos[valor] = novo_no

    def adicionar_aresta(self, origem, destino, valor_transicao):
        """
        Adiciona uma aresta direcionada do nó de origem para o nó de destino com o valor de transição fornecido.

        Args:
            origem: O valor do nó de origem.
            destino: O valor do nó de destino.
            valor_transicao: O valor da transição da origem para o destino.

        Returns:
            None
        """
        if origem in self.nos and destino in self.nos:
            self.nos[origem].adicionar_vizinho(destino, valor_transicao)
        if valor_transicao == " ":
            self.nos[origem].adicionar_vizinho(origem, " ")

    def mostrar_grafo(self):
        """
        Exibe uma representação visual do grafo na forma de pares de valores de nó e seus vizinhos.

        Returns:
            None
        """
        for valor, no in self.nos.items():
            vizinhos = ', '.join([f"{vizinho} ({valor_transicao})" for vizinho, valor_transicao in no.vizinhos.items()])
            print(f"{valor} -> {vizinhos}")

    @staticmethod
    def obter_possiveis_escolhas(grafo, no_atual):
        """
        Obtém uma lista de possíveis escolhas (vizinhos) a partir do nó atual em um grafo.

        Args:
            grafo: O grafo do qual obter as escolhas.
            no_atual: O valor do nó atual.

        Returns:
            possiveis_escolhas (list): Uma lista de possíveis escolhas (vizinhos) a partir do nó atual.
        """
        possiveis_escolhas = []
        if no_atual in grafo.nos:
            vizinhos = grafo.nos[no_atual].vizinhos
            if vizinhos:
                for vizinho, valor_transicao in vizinhos.items():
                    possiveis_escolhas.append(f"Vizinho: {vizinho}, Valor da transição: {valor_transicao}")
        else:
            print("O nó atual não existe no grafo.")

        return possiveis_escolhas

        
