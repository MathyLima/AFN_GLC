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
        
    def modo_rapido(self):
        """
        Método para gerar cadeias rapidamente a partir da gramática.

        Retorna:
            None
        """
        array_cadeias_geradas = []
        
        while True:
            cadeia_atual = f"{self.gramatica['inicial']}"
            
            while True:  # Loop interno para gerar uma cadeia única
                no_atual = self.gramatica['inicial']
                
                while any(variavel in cadeia_atual for variavel in self.gramatica['variaveis']):
                    if no_atual not in cadeia_atual:
                        for variavel in self.gramatica['variaveis']:
                            if variavel in cadeia_atual:
                                no_atual = variavel
                                break
                    possiveis_escolhas = Grafo.obter_possiveis_escolhas(self.grafo, no_atual)
                    
                    if not possiveis_escolhas:
                        print(f"{no_atual} não possui vizinhos")
                        break
                    
                    escolha_index = random.randint(0, len(possiveis_escolhas) - 1)
                    escolha_transicao = list(self.grafo.nos[no_atual].vizinhos.values())[escolha_index]
                    cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)
                    no_atual = list(self.grafo.nos[no_atual].vizinhos.keys())[escolha_index]
                
                if cadeia_atual not in array_cadeias_geradas:
                    print(f"Cadeia Gerada: {cadeia_atual}")
                    array_cadeias_geradas.append(cadeia_atual)
                    break  # Sai do loop interno quando a cadeia é única
                else:
                    print(f"A cadeia '{cadeia_atual}' já foi gerada. Gerando outra automaticamente.")
                    cadeia_atual = f"{self.gramatica['inicial']}"  # Reseta para gerar uma nova cadeia
            print("1 - Sim")
            print("2 - Não")
            escolha = input('Deseja Gerar outra cadeia? ')
            if escolha != '1':
                for array in array_cadeias_geradas:
                    print(array)
                break
                
    def modo_lento(self):
        """
        Método para gerar cadeias lentamente a partir da gramática.

        Retorna:
            None
        """
        no_atual = self.gramatica['inicial']
        cadeia_atual = f"{self.gramatica['inicial']}"
        array_cadeias=[]
        
        while any(variavel in cadeia_atual for variavel in self.gramatica['variaveis']):
            if no_atual not in cadeia_atual:
                for variavel in self.gramatica['variaveis']:
                    if variavel in cadeia_atual:
                        no_atual = variavel
                        break
            possiveis_escolhas = Grafo.obter_possiveis_escolhas(self.grafo, no_atual)
            
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
                escolha_transicao = list(self.grafo.nos[no_atual].vizinhos.values())[escolha_index]
                print(f"Transição escolhida: {escolha_transicao}\n")
                cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)
                no_atual = list(self.grafo.nos[no_atual].vizinhos.keys())[escolha_index]
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
