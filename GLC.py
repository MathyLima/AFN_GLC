"""
Este script oferece funcionalidades para gerar cadeias a partir de uma gramática fornecida, utilizando dois modos: rápido e lento.

Ele contém as seguintes classes e métodos:

- GerenciadorGramatica: Uma classe para gerenciar uma gramática e criar sua representação em forma de grafo.
- Gerador_Cadeias: Uma classe para gerar cadeias a partir da gramática utilizando os modos rápido e lento.

Exemplo de Uso:
--------------
# Inicialize um gerenciador de gramática com um arquivo de gramática
gramatica = GerenciadorGramatica('dicionario.txt')

# Inicialize um gerador de cadeias com o grafo da gramática e o dicionário da gramática
gerador = Gerador_Cadeias(gramatica.grafo, gramatica.gramatica)

# Gerencie o processo de geração de cadeias
gerador.gerencia()
"""
import time

from gerenciador_gramatica import GerenciadorGramatica
import random
from grafo import Grafo

class Gerador_Cadeias:
    def __init__(self, grafo, gramatica):
        """
        Inicializa o gerador de cadeias com o grafo da gramática e o dicionário da gramática.

        Args:
            grafo (Grafo): O grafo representando a gramática.
            gramatica (dict): O dicionário contendo as informações da gramática.

        Returns:
            None
        """
        self.grafo = grafo
        self.gramatica = gramatica


    def get_proxima_derivacao(self, no_atual, cadeia_atual):
        """
        Obtém o próximo nó a ser derivado na cadeia.

        Args:
            no_atual (str): O nó atual na cadeia.
            cadeia_atual (str): A cadeia atual.

        Returns:
            str: O próximo nó a ser derivado.
        """
        no_atual = None
        for variavel in self.grafo.get_variaveis():
            if variavel in cadeia_atual:
                no_atual = variavel
                break

        return no_atual

    def modo_rapido(self, array_cadeias_geradas=None, cadeia_anterior=None, no_anterior=None, derivacao_escolhida=None):
        """
        Método para gerar cadeias rapidamente a partir da gramática.

        Retorna:
            None
        """
        no_atual = ''
        cadeia_atual = ''
        if array_cadeias_geradas is None:
            array_cadeias_geradas = []
        if cadeia_anterior is None:
            no_atual = self.gramatica['inicial']
            cadeia_atual = f"{no_atual}"
        else:
            no_atual = no_anterior
            cadeia_atual = cadeia_anterior
            print(f"Cadeia anterior a que foi repetida anteriormente {cadeia_atual}, com o no {no_atual}")

        while any(variavel in cadeia_atual for variavel in self.grafo.get_variaveis()):
            if no_atual not in cadeia_atual:
                no_atual = self.get_proxima_derivacao(no_atual, cadeia_atual)
                if no_atual is None:
                    break

            possiveis_escolhas = self.grafo.obter_possiveis_transicoes(no_atual)
            if derivacao_escolhida is not None:
                possiveis_escolhas.pop(derivacao_escolhida)
            derivacao_escolhida = None

            if not possiveis_escolhas:
                print(f"{no_atual} não possui vizinhos")
                print("------FINALIZANDO------")
                time.sleep(0.2)
                break

            escolha_index = random.randint(0, len(possiveis_escolhas) - 1)
            escolha_transicao = possiveis_escolhas[escolha_index]
            estado_escolhido = self.grafo.transitar(no_atual, escolha_transicao)

            # Salvando o estado atual para a próxima iteração
            cadeia_anterior = cadeia_atual
            no_anterior = no_atual

            # Atualizando o estado atual para a próxima iteração
            cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)
            no_atual = estado_escolhido

        if cadeia_atual not in array_cadeias_geradas:
            print(f"Cadeira Gerada: {cadeia_atual}")
            array_cadeias_geradas.append(cadeia_atual)
            print("1 - Sim")
            print("2 - Não")
            escolha = input('Deseja Gerar outra cadeia? ')
            if escolha == '1':
                # Chamada recursiva passando o estado atual para a próxima iteração
                self.modo_rapido(array_cadeias_geradas)
            else:
                for array in array_cadeias_geradas:
                    print(array)
        else:
            print(f"A cadeia '{cadeia_atual}' já foi gerada. Gerando outra automaticamente.")
            derivacao_escolhida = escolha_index
            # Chamada recursiva passando o estado atual para a próxima iteração
            self.modo_rapido(array_cadeias_geradas, cadeia_anterior, no_anterior, derivacao_escolhida)

    def modo_lento(self):
        """
        Método para gerar cadeias lentamente a partir da gramática.

        Retorna:
            None
        """
        no_atual = self.gramatica['inicial']
        cadeia_atual = f"{self.gramatica['inicial']}"
        array_cadeias = []

        while any(variavel in cadeia_atual for variavel in self.gramatica['variaveis']):
            if no_atual not in cadeia_atual:
                self.get_proxima_derivacao(no_atual, cadeia_atual)
            possiveis_escolhas = self.grafo.obter_possiveis_transicoes(no_atual)
            
            print(f"No atual: {no_atual}")
            print(f"Cadeia atual: {cadeia_atual}")
            array_cadeias.append(cadeia_atual)
            
            if not possiveis_escolhas:
                print("Não há vizinhos neste nó.")
                break
            
            print("Possíveis escolhas:")
            for i, escolha in enumerate(possiveis_escolhas, start=1):
                print(f"{i}. {escolha}")

            escolha = input("Escolha a transição (digite o número correspondente ou 'sair' para encerrar): ")
            
            if escolha.lower() == 'sair':
                print("Encerrando a caminhada.")
                break
            
            if escolha.isdigit() and 1 <= int(escolha) <= len(possiveis_escolhas):
                escolha_index = int(escolha) - 1

                escolha_transicao = possiveis_escolhas[escolha_index]
                estado_escolhido = self.grafo.transitar(no_atual, escolha_transicao)
                print(f"Transição escolhida: {escolha_transicao}\n")
                cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)
                no_atual = estado_escolhido
            else:
                print("Escolha inválida. Por favor, digite um número válido ou 'sair'.\n")
                
            if cadeia_atual not in array_cadeias:
                array_cadeias.append(cadeia_atual)
        
        print(f"Cadeia final: {cadeia_atual}")
        
        for cadeias in array_cadeias:
            print(cadeias)

    def gerencia(self):
        """
        Método para gerenciar o processo de geração de cadeias.

        Retorna:
            None
        """
        while True:
            print("------------------ Selecione o modo desejado ------------------")
            print("1 - Modo Rápido")
            print("2 - Modo Lento")
            print("---------------------------------------------------------------")
            escolha = input("Escolha o Modo (digite 'sair' para encerrar) ")
            if escolha == "1":
                self.modo_rapido()
            elif escolha == "2":
                self.modo_lento()
            elif escolha.lower() == 'sair':
                break

# Inicializa o gerenciador de gramática com um arquivo de gramática
gramatica = GerenciadorGramatica('dicionario.txt')
if gramatica.verificar_gramatica():
    # Inicializa o gerador de cadeias com o grafo da gramática e o dicionário da gramática
    cadeia = Gerador_Cadeias(gramatica.grafo, gramatica.gramatica)

    # Gerencia o processo de geração de cadeias
    cadeia.gerencia()
