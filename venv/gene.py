import copy
# import math
import random

import matplotlib.pyplot as plt
import numpy as np


def calcula_peso(populacao_test):
    soma = 0
    for index_test in range(len(objetos)):
        (valor, peso) = objetos[index_test]
        soma += populacao_test[index_test] * peso
    return soma


def fn_adapta(populacao_test):
    soma = 0
    for test_index in range(len(objetos)):
        (valor, peso) = objetos[test_index]
        soma += populacao_test[test_index] * valor

    test_peso = calcula_peso(populacao_test)
    if test_peso > capMochila:
        return 0
    else:
        return soma


def reproduz(pai_escolhido, mae_escolhida):
    c = random.randrange(0, n)
    filho_escolhido = pai_escolhido[0:c] + mae_escolhida[c:n]
    if random.random() < prob_mutacao:
        gene = random.randrange(0, n)
        filho_escolhido[gene] = 1 - filho_escolhido[gene]
    return filho_escolhido


def selecao_aleatoria(populacao_draw, ranking_populacao):
    sorteio = copy.deepcopy(random.choices(populacao_draw, weights=ranking_populacao, k=1))
    return sorteio[0]


def atualiza_ranking(populacao_rank):
    ranking_populacao = []
    for indexP in range(qnt_populacao):
        ranking_populacao.append(fn_adapta(populacao_rank[indexP]))
    return ranking_populacao


def algoritmo_genetico(populacao_inicial):
    populacao_iter = copy.deepcopy(populacao_inicial)
    melhores_individuos = copy.deepcopy(populacao_inicial)

    for i in range(geracoes):
        atualiza_results(populacao_iter, populacao_results, i)
        ranking = atualiza_ranking(populacao_iter)

        nova_populacao = []
        print("----------------------- Geração ", i + 1, " iniciada -----------------------")
        for j in range(qnt_populacao):
            pai = selecao_aleatoria(populacao_iter, ranking)
            # print("Pai:   ", pai)
            mae = selecao_aleatoria(populacao_iter, ranking)
            # print("Mãe:   ", mae)
            filho = reproduz(pai, mae)
            # print("Filho: ", filho)
            nova_populacao.append(filho)
        atualiza_melhores(melhores_individuos, nova_populacao)
        populacao_iter = copy.deepcopy(nova_populacao)
        printa_populacao(nova_populacao)
        print("-----------------------------------------------------------------------")
    plota_grafico(populacao_results)
    return melhores_individuos


def atualiza_melhores(populacao_cand, proximo):
    populacao_retorno = copy.deepcopy(populacao_cand)

    for individuo_cand in range(qnt_populacao):
        if fn_adapta(populacao_retorno[individuo_cand]) < fn_adapta(proximo[individuo_cand]):
            populacao_cand[individuo_cand] = proximo[individuo_cand]


def atualiza_results(populacao_, pop_results, tempo_t):
    for index_z in range(qnt_populacao):
        pop_results[index_z][tempo_t] = fn_adapta(populacao_[index_z])


def printa_populacao(populacao_test):
    for individuo_i in populacao_test:
        print(individuo_i, " Valor: ", fn_adapta(individuo_i),
              " Peso: ", calcula_peso(individuo_i))


def plota_grafico(populacao_r):
    x1 = np.arange(1, geracoes + 1, 1)
    for indexT in range(qnt_populacao):
        plt.plot(x1, populacao_r[indexT])


# n = int(input("Digite um número de pecas: "))
# valorMin = input("Digite um valor máximo para as pecas: ")
# valorMax = input("Digite um valor mínimo para as pecas: ")
# pesoMin = input("Digite um peso máximo para as pecas: ")
# pesoMax = input("Digite um peso máximo para as pecas: ")
# capMochila = input("Digite a capacidade máxima da mochila: ")

# n = 6
# capMochila = 10


n = 10
valorMax = 5
valorMin = 1
pesoMax = 5
pesoMin = 2
capMochila = 20
prob_mutacao = 0.10
qnt_populacao = 3
geracoes = 15

populacao = []
objetos = []

for indexI in range(qnt_populacao):
    individuo = []
    for indexJ in range(n):
        individuo.append(random.randint(0, 1))
    populacao.append(individuo)

for indexI in range(n):
    tupla = (random.randint(valorMin, valorMax),
             random.randint(pesoMin, pesoMax))
    objetos.append(tupla)

# objetos.append((20,1))            #exemplo fixo para testes
# objetos.append((5,2))
# objetos.append((10,3))
# objetos.append((40,8))
# objetos.append((15,7))
# objetos.append((25,4))


populacao_results = []
for index_populacao in range(qnt_populacao):
    results = []
    for index in range(geracoes):
        results.append(0)
    populacao_results.append(results)

print("----------------------- VALORES INICIAIS DA POPULACAO --------------------")
printa_populacao(populacao)
print(objetos)
# print("------------------------- TESTE REPRODUÇÃO -----------------------------")
# print("PAI:   ", populacao[0])
# print("MAE:   ", populacao[1])
# filho = reproduz(populacao[0], populacao[1])
# print("FILHO: ", filho)
# print("--------------------------- TESTE RANKING ------------------------------")
# teste_ranking = atualiza_ranking(populacao)
# print("Teste ranking: ", teste_ranking)
# print("--------------------------- SORTEADO ------------------------------")
# printa_populacao(selecao_aleatoria(populacao, teste_ranking))

populacao_final = algoritmo_genetico(populacao)
print("--------------------------- MELHORES INDIVIDUOS ENCONTRADOS ------------------------------")
printa_populacao(populacao_final)
plt.show()
