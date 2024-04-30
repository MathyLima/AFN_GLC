from grafo import Grafo

class GerenciadorGramatica:
    """
    Classe responsável por gerenciar uma gramática e criar sua representação em forma de grafo.

    Attributes:
        gramatica (dict): Um dicionário que armazena informações sobre a gramática lida do arquivo.
                          Contém chaves 'terminais', 'variaveis', 'inicial' e 'producoes'.
        grafo (Grafo): Um objeto Grafo que representa a gramática, onde os nós são variáveis e
                       as arestas representam as produções.

    Methods:
        __init__(self, nome_arquivo):
            Inicializa o GerenciadorGramatica lendo uma gramática do arquivo especificado
            e criando a representação em grafo.

        cria_gramatica(self, nome_arquivo):
            Lê a gramática do arquivo especificado e a armazena em um dicionário.

        cria_grafo(self):
            Cria a representação em grafo da gramática, adicionando nós e arestas ao objeto Grafo.

        verificar_gramatica(self):
            Verifica se a gramática está corretamente formatada, incluindo se o símbolo inicial está
            entre as variáveis, se todos os símbolos das produções estão entre variáveis ou terminais,
            e se não há variáveis ou terminais duplicados.

    """

    def __init__(self, nome_arquivo):
        """
        Inicializa o GerenciadorGramatica lendo uma gramática do arquivo especificado
        e criando a representação em grafo.

        Args:
            nome_arquivo (str): O nome do arquivo que contém a definição da gramática.
                                O arquivo deve seguir um formato específico.

        Returns:
            None
        """
        self.gramatica = self.cria_gramatica(nome_arquivo)
        self.grafo = Grafo()
        self.cria_grafo()

    def cria_gramatica(self, nome_arquivo):
        """
        Lê a gramática do arquivo especificado e a armazena em um dicionário.

        Args:
            nome_arquivo (str): O nome do arquivo que contém a definição da gramática.

        Returns:
            dict: Um dicionário contendo informações sobre a gramática lida.
                  Contém chaves 'terminais', 'variaveis', 'inicial' e 'producoes'.
        """
        gramatica = {'producoes': {}}
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if 'terminais' in linha:
                    gramatica['terminais'] = [t for t in linha.split('=')[1].split(',') if t]
                elif 'variaveis' in linha:
                    gramatica['variaveis'] = [var for var in linha.split('=')[1].split(',') if var != 'epsilon']
                elif 'inicial' in linha:
                    gramatica['inicial'] = linha.split('=')[1].strip()
                elif linha == 'producoes':
                    for linha_producao in arquivo:
                        linha_producao = linha_producao.strip()
                        if not linha_producao:
                            break
                        variavel, producao = linha_producao.split('->')
                        producoes_variavel = gramatica['producoes'].get(variavel, [])
                        producoes_variavel.append(producao.replace('epsilon', '') if 'epsilon' in producao else producao)
                        gramatica['producoes'][variavel] = producoes_variavel
            return gramatica

    def cria_grafo(self):
        """
        Cria a representação em grafo da gramática, adicionando nós e arestas ao objeto Grafo.

        Args:
            None

        Returns:
            None
        """
        for variavel in self.gramatica['variaveis']:
            self.grafo.adicionar_no(variavel)

        for variavel, producoes in self.gramatica['producoes'].items():
            for producao in producoes:
                if producao == '':
                    self.grafo.adicionar_aresta(variavel, variavel, producao)
                else:
                    for letra in producao:
                        if letra in self.gramatica['variaveis']:
                            self.grafo.adicionar_aresta(variavel, letra, producao)
                            break
                    else:
                        self.grafo.adicionar_aresta(variavel, variavel, producao)


    def verificar_gramatica(self):
        """
        Verifica se a gramática está corretamente formatada.

        Args:
            None

        Returns:
            tuple: Uma tupla contendo um valor booleano indicando se a gramática está corretamente
                   formatada e uma mensagem de erro em caso contrário.
        """
        gramatica = self.gramatica
        # Verificar se o símbolo inicial está entre as variáveis
        if gramatica['inicial'] not in gramatica['variaveis']:
            return False, "O símbolo inicial não está entre as variáveis."

        # Verificar se todos os símbolos das produções estão entre as variáveis ou terminais
        for variavel, producoes in gramatica['producoes'].items():
            for producao in producoes:
                for simbolo in producao.split():
                    if simbolo not in gramatica['variaveis'] and simbolo not in gramatica['terminais'] and simbolo != 'epsilon':
                        return False, f"O símbolo '{simbolo}' nas produções de '{variavel}' não é uma variável, terminal ou 'epsilon'."

        # Verificar se todos os símbolos terminais e não-terminais são únicos
        if len(gramatica['variaveis']) != len(set(gramatica['variaveis'])):
            return False, "Existem variáveis duplicadas na lista de variáveis."
        if len(gramatica['terminais']) != len(set(gramatica['terminais'])):
            return False, "Existem terminais duplicados na lista de terminais."

        return True, "A gramática está corretamente formatada."
