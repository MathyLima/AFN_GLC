from grafo import Grafo 


class GerenciadorGramatica:
    def __init__(self,nome_arquivo):
        self.gramatica = self.cria_gramatica(nome_arquivo)
        self.grafo = Grafo()
        self.cria_grafo()


    def cria_gramatica(self,nome_arquivo):
        gramatica={'producoes':{}}
        with open(nome_arquivo,'r') as arquivo:
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
        for variavel in self.gramatica['variaveis']:
            self.grafo.adicionar_no(variavel)

        for variavel, producoes in self.gramatica['producoes'].items():
            for producao in producoes:
                if producao == '':
                    self.grafo.adicionar_aresta(variavel,variavel,producao)
                else:
                    for letra in producao:
                        if letra in self.gramatica['variaveis']:
                            self.grafo.adicionar_aresta(variavel,letra,producao)
                            break
                    else:
                        self.grafo.adicionar_aresta(variavel,variavel,producao)