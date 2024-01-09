from grafo import Grafo 
import random

def cria_gramatica(nome_arquivo):
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


gramatica = cria_gramatica('dicionario.txt')
grafo = Grafo()

def cria_grafo():
    for variavel in gramatica['variaveis']:
        grafo.adicionar_no(variavel)

    for variavel, producoes in gramatica['producoes'].items():
        for producao in producoes:
            if producao == '':
                grafo.adicionar_aresta(variavel,variavel,producao)
            else:
                for letra in producao:
                    if letra in gramatica['variaveis']:
                        grafo.adicionar_aresta(variavel,letra,producao)
                        break
                else:
                    grafo.adicionar_aresta(variavel,variavel,producao)



cria_grafo()

def modo_rapido(grafo, gramatica):
    array_cadeias_geradas = []
    
    while True:
        cadeia_atual = f"{gramatica['inicial']}"
        
        while True:  # Loop interno para gerar uma cadeia única
            no_atual = gramatica['inicial']
            
            while any(variavel in cadeia_atual for variavel in gramatica['variaveis']):
                if no_atual not in cadeia_atual:
                    for variavel in gramatica['variaveis']:
                        if variavel in cadeia_atual:
                            no_atual = variavel
                            break
                possiveis_escolhas = Grafo.obter_possiveis_escolhas(grafo, no_atual)
                
                
                if not possiveis_escolhas:
                    print(f"{no_atual} não possui vizinhos")
                    break
                
                escolha_index = random.randint(0, len(possiveis_escolhas) - 1)
                escolha_transicao = list(grafo.nos[no_atual].vizinhos.values())[escolha_index]
                cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)
                no_atual = list(grafo.nos[no_atual].vizinhos.keys())[escolha_index]
            
            if cadeia_atual not in array_cadeias_geradas:
                print(f"Cadeia Gerada: {cadeia_atual}")
                array_cadeias_geradas.append(cadeia_atual)
                break  # Sai do loop interno quando a cadeia é única
            else:
                print(f"A cadeia '{cadeia_atual}' já foi gerada. Gerando outra automaticamente.")
                cadeia_atual = f"{gramatica['inicial']}"  # Reseta para gerar uma nova cadeia
        print("1 - Sim")
        print("2 - Não")
        escolha = input('Deseja Gerar outra cadeia? ')
        if escolha != '1':
            for array in array_cadeias_geradas:
                print(array)
            break
def modo_lento(grafo, gramatica):
    no_atual = gramatica['inicial']
    cadeia_atual = f"{gramatica['inicial']}"
    array_cadeias=[]
    while any(variavel in cadeia_atual for variavel in gramatica['variaveis']):
        if no_atual not in cadeia_atual:
            for variavel in gramatica['variaveis']:
                if variavel in cadeia_atual:
                    no_atual = variavel
                    break
        possiveis_escolhas = Grafo.obter_possiveis_escolhas(grafo, no_atual)
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
            escolha_transicao = list(grafo.nos[no_atual].vizinhos.values())[escolha_index]
            print(f"Transição escolhida: {escolha_transicao}\n")
            cadeia_atual = cadeia_atual.replace(no_atual, escolha_transicao, 1)  # Substitui o nó atual pela escolha na cadeia atual
            no_atual = list(grafo.nos[no_atual].vizinhos.keys())[escolha_index]
        else:
            print("Escolha inválida. Por favor, digite um número válido ou 'sair'.\n")
        if cadeia_atual not in array_cadeias:
            array_cadeias.append(cadeia_atual)
    
    print(f"Cadeia final: {cadeia_atual}")
    
    for cadeias in array_cadeias:
        print(cadeias)


def gerencia(grafo,gramatica):
    while True:
        print("------------------ Selecione o modo desejado ------------------")
        print("1 - Modo Rápido")
        print("2 - Modo Lento")
        print("---------------------------------------------------------------")
        escolha = input("Escolha o Modo (digite 'sair' para encerrar) ")
        if escolha == "1":
            modo_rapido(grafo,gramatica)
        elif escolha == "2":
            modo_lento(grafo,gramatica)
        elif escolha.lower() == 'sair':
            break
gerencia(grafo,gramatica)



