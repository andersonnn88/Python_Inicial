print("ola, mundo!")
#o Python, os comentários de uma única linha começam com o símbolo #, enquanto os comentários de várias linhas são delimitados por três aspas """ . Por exemplo:

#aula 2

ead = 17

if ead < 18:
    print("Eh menor")

#estrutura for 
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

#estrutura while 
contador = 0
while contador < 5:

    print(contador)
    contador += 1   

#while com break 
contador = 0
while True:

    print(contador)
    contador += 1
    if contador == 5:
        break 
#PASS A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.
for i in range(5):
    pass

#lISTA
print("-----------------Metodos de lista ----------------------------------------------------------")
# Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.

frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"



#Metodos de lista 
#Métodos de listas
#As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

#append(elemento): adiciona um elemento ao final da lista.
#insert(indice, elemento): insere um elemento em uma posição específica da lista.
#remove(elemento): remove a primeira ocorrência de um elemento na lista.
#pop(indice): remove e retorna o elemento em uma posição específica da lista.
#sort(): ordena os elementos da lista em ordem ascendente.
#reverse(): inverte a ordem dos elementos na lista.

frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

#As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]

# Tuplas
#Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.
ponto = (3, 4)
print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4
#Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.
#As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.

#Métodos de tuplas
#count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
#index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
#len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2))   # Saída: 1
print (minha_tupla.index(2, 2))   #Saída: 3
print (minha_tupla.index(2, 2, 4))   #Saída: 3

# Dicionários
#Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário 
# consiste em uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}
print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"

"""Métodos de dicionários
Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

keys(): retorna uma visualização de todas as chaves do dicionário.
values(): retorna uma visualização de todos os valores do dicionário.
items(): retorna uma visualização de todos os pares chave-valor do dicionário.
update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
"""

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}


print("-----------------Conjuntos (set)----------------------------------------------------------")
#Conjuntos (set)
#Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

#Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
print("conjuntos")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

print("--------------------------Métodos de conjuntos-----------------------------------------------")
"""
Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

add(elemento): adiciona um elemento ao conjunto.
remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
clear(): remove todos os elementos do conjunto.
"""
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()