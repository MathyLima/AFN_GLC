class No:
    """
    Classe que representa um nó em um grafo.

    Attributes:
        dado: O dado armazenado no nó.
        vizinhos: Um dicionário que mapeia os nós vizinhos aos valores de transição.

    Methods:
        __init__(self, dado):
            Inicializa um objeto No com o dado fornecido e um dicionário vazio de vizinhos.

        adicionar_vizinho(self, vizinho, transicao):
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

    def adicionar_vizinho(self, vizinho, transicao):
        """
        Adiciona um vizinho ao nó com o valor de transição fornecido.

        Args:
            vizinho: O nó vizinho a ser adicionado.
            transicao: O valor da transição para o vizinho.

        Returns:
            None
        """
        if vizinho not in self.vizinhos:
            self.vizinhos[vizinho] = transicao


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

        adicionar_aresta(self, origem, destino, transicao):
            Adiciona uma aresta direcionada do nó de origem para o nó de destino com o valor de transição fornecido.

        mostrar_grafo(self):
            Exibe uma representação visual do grafo na forma de pares de valores de nó e seus vizinhos.

        transitar(self, origem, transicao):
            Transita do nó de origem para o nó destino usando a transição especificada.

        obter_possiveis_transicoes(grafo, no_atual):
            Obtém uma lista de possíveis transições (vizinhos) a partir do nó atual em um grafo, incluindo os valores das transições.
    """

    def __init__(self):
        """
        Inicializa um grafo com um dicionário vazio de nós.

        Returns:
            None
        """
        self.nos = {}
        self.variaveis = []

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
            self.variaveis.append(valor)

    def get_variaveis(self):
        """
        Obtém uma lista de variáveis presentes no grafo.

        Returns:
            list: Lista contendo as variáveis presentes no grafo.
        """
        return self.variaveis

    def adicionar_aresta(self, origem, destino, transicao):
        """
        Adiciona uma aresta direcionada do nó de origem para o nó de destino com o valor de transição fornecido.

        Args:
            origem: O valor do nó de origem.
            destino: O valor do nó de destino.
            transicao: O valor da transição da origem para o destino.

        Returns:
            None
        """
        self.adicionar_no(origem)
        self.adicionar_no(destino)
        self.nos[origem].adicionar_vizinho(destino, transicao)

    def mostrar_grafo(self):
        """
        Exibe uma representação visual do grafo na forma de pares de valores de nó e seus vizinhos, incluindo os valores das transições.

        Returns:
            None
        """
        for no, vizinhos in self.nos.items():
            vizinhos_formatados = ', '.join([f"{vizinho} (Transicao: {transicao})" for vizinho, transicao in vizinhos.vizinhos.items()])
            print(f"{no} -> {vizinhos_formatados}")

    def transitar(self, origem, transicao):
        """
        Transita do nó de origem para o nó destino usando a transição especificada.

        Args:
            origem: O valor do nó de origem.
            transicao: O valor da transição a ser usada para transitar.

        Returns:
            destino (str): O valor do nó de destino, se encontrado. Caso contrário, retorna None.
        """
        vizinhos = self.nos.get(origem, {}).vizinhos
        for destino, valor_transicao in vizinhos.items():
            if valor_transicao == transicao:
                return destino
        return None

    def obter_possiveis_transicoes(self, no_atual):
        """
        Obtém uma lista de possíveis transições (vizinhos) a partir do nó atual em um grafo, incluindo os valores das transições.

        Args:
            no_atual: O valor do nó atual.

        Returns:
            possiveis_transicoes (list): Uma lista de possíveis transições (vizinhos) a partir do nó atual, incluindo os valores das transições.
        """
        possiveis_transicoes = []
        if no_atual in self.nos:
            vizinhos = self.nos[no_atual].vizinhos
            if vizinhos:
                for vizinho, transicao in vizinhos.items():
                    possiveis_transicoes.append(transicao)
        else:
            print("O nó atual não existe no grafo.")

        return possiveis_transicoes
