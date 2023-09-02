import copy
import math
import random


def calcula_peso(mochila_test):
    soma = 0
    for index in range(len(objetos)):
        (valor, peso) = objetos[index]
        soma += mochila_test[index] * peso
    return soma


def calcula_valor(mochila_test):
    soma = 0
    for index in range(len(objetos)):
        (valor, peso) = objetos[index]
        soma += mochila_test[index] * valor

    test_peso = calcula_peso(mochila_test)
    if test_peso > capMochila:
        return 0
    else:
        return soma


def escalonamento(time):
    return fator_k ** (-fator_l * time)


# def gera_proximo(viajantes_test):
#     viajantes_retorno = copy.deepcopy(viajantes_test)
#     for ind_viajante in range(qnt_mochileiros):
#         mochila_escolhida = random.choice(viajantes_retorno[ind_viajante])
#         viajantes_retorno[ind_viajante][mochila_escolhida] = 1 - viajantes_retorno[ind_viajante][mochila_escolhida]
#     return viajantes_retorno

def gera_proximo(viajantes_test):
    viajantes_retorno = copy.deepcopy(viajantes_test)
    for viajante in range(qnt_mochileiros):
        for peca in range(n):
            if random.random() < 0.1:
                viajantes_retorno[viajante][peca] = 1 - viajantes_retorno[viajante][peca]
    return viajantes_retorno


def tempora_simulada(viajantes_iniciais):
    atual = copy.deepcopy(viajantes_iniciais)
    melhores_viajantes = copy.deepcopy(viajantes_iniciais)

    for tempo in range(tempo_limite):
        temperatura = escalonamento(t)
        proximo = gera_proximo(atual)
        atualiza_melhores(melhores_viajantes, proximo)

        for mochileiro_cand in range(qnt_mochileiros):
            delta_e = calcula_valor(proximo[mochileiro_cand]) - calcula_valor(atual[mochileiro_cand])
            if delta_e >= 0:
                atual[mochileiro_cand] = proximo[mochileiro_cand]
            else:
                if random.random() < math.exp(delta_e / temperatura):
                    atual[mochileiro_cand] = proximo[mochileiro_cand]
    return melhores_viajantes


def atualiza_melhores(viajantes_cand, proximo):
    viajantes_retorno = copy.deepcopy(viajantes_cand)

    for mochila_cand in range(qnt_mochileiros):
        if calcula_valor(viajantes_retorno[mochila_cand]) < calcula_valor(proximo[mochila_cand]):
            viajantes_cand[mochila_cand] = proximo[mochila_cand]


def printa_mochileiros(viajantes_test):
    for mochileiro in viajantes_test:
        print(mochileiro, " Valor: ", calcula_valor(mochileiro),
              " Peso: ", calcula_peso(mochileiro))


# n = int(input("Digite um número de pecas: "))
# valorMin = input("Digite um valor máximo para as pecas: ")
# valorMax = input("Digite um valor mínimo para as pecas: ")
# pesoMin = input("Digite um peso máximo para as pecas: ")
# pesoMax = input("Digite um peso máximo para as pecas: ")
# capMochila = input("Digite a capacidade máxima da mochila: ")
n = 10
valorMax = 100
valorMin = 20
pesoMax = 10
pesoMin = 1
capMochila = 20
qnt_mochileiros = 5
fator_k = 20  # parametro para escalonamento
fator_l = 0.005  # parametro para escalonamento
temperatura_inicial = 20
t = 1
tempo_limite = 1000

viajantes = []
mochila = []
objetos = []

for indexI in range(qnt_mochileiros):
    mochila = []
    for indexJ in range(n):
        mochila.append(random.randint(0, 1))
    viajantes.append(mochila)

for indexI in range(n):
    tupla = (random.randint(valorMin, valorMax),
             random.randint(pesoMin, pesoMax))
    objetos.append(tupla)

print("--------------- VALORES INICIAIS DE VIAJANTES E OBJETOS ----------------")
printa_mochileiros(viajantes)
print(objetos)
# print("----------------- COMPARAÇÃO GERA PRÓXIMO ------------------")
# print(viajantes)
# print(gera_proximo(viajantes))
# print("----------------- TESTE ESCALONAMENTO ------------------")
# for indexI in range(tempo_limite):
#     print(escalonamento(indexI))
# print("----------------- TESTE ATUALIZA MELHORES ------------------")
# for indexI in range(2):
#     proximo = gera_proximo(viajantes)
#     print("Proximo gerado:")
#     printa_mochileiros(proximo)
#     print("Antes da função, melhores:")
#     printa_mochileiros(viajantes)
#     atualiza_melhores(viajantes, proximo)
#     print("Melhores para comparação:")
#     printa_mochileiros(viajantes)
#     print("----------------- FIM ITERAÇÃO ------------------")
print("---------- MELHORES VIAJANTES TEMPORA SIMULADA -------------")
viajantes = tempora_simulada(viajantes)
printa_mochileiros(viajantes)
