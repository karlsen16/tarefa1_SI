import math
import random

def calcula_Peso(mochila):
    soma = 0
    for index in range(len(objetos)):
        (valor, peso) = objetos[index]
        soma += mochila[index] * peso
    return soma

def calcula_Valor(mochila):
    soma = 0
    for index in range(len(objetos)):
        (valor, peso) = objetos[index]
        soma += mochila[index] * valor

    testPeso = calcula_Peso(mochila)
    if testPeso > capMochila:
        return 0
    else:
        return soma

def escalonamento(t):
   return k**(-l*t)

# def gera_Proximo(viajantes):
#
#     for indexI in range(mochileiros):
#         indexR = random.choice(viajantes[indexI])
#         viajantes[indexI][indexR] = 1 - viajantes[indexI][indexR]
#     return viajantes

def gera_Proximo(viajantes):

    for indexI in range(mochileiros):
        for indexJ in range(n):
            if random.random() < 0.1:
                viajantes[indexI][indexJ] = 1 - viajantes[indexI][indexJ]
    return viajantes


def tempora_Simulada(viajantes):

    atual = viajantes
    melhores_Viajantes = viajantes

    for indexI in range(tempo_limite):
        Temperature = escalonamento(t)
        proximo = gera_Proximo(atual)
        melhores_Viajantes = atualiza_melhores(melhores_Viajantes, proximo)

        for indexJ in range(mochileiros):
            delta_E = calcula_Valor(proximo[indexJ]) - calcula_Valor(atual[indexJ])
            if delta_E >= 0:
                atual[indexJ] = proximo[indexJ]
            else:
                if random.random() < math.exp(delta_E/Temperature):
                    atual[indexJ] = proximo[indexJ]
                    hitsT += 1

    print(melhores_Viajantes)
    return melhores_Viajantes

def atualiza_melhores(viajantes, proximo):

    for indexI in range(mochileiros):
        if calcula_Valor(viajantes[indexI]) < calcula_Valor(proximo[indexI]):
            viajantes[indexI] = proximo[indexI]
    return viajantes

# n = int(input("Digite um número de pecas: "))
# valorMin = input("Digite um valor máximo para as pecas: ")
# valorMax = input("Digite um valor mínimo para as pecas: ")
# pesoMin = input("Digite um peso máximo para as pecas: ")
# pesoMax = input("Digite um peso máximo para as pecas: ")
# capMochila = input("Digite a capacidade máxima da mochila: ")
n = 10
valorMax = 100
valorMin = 20
pesoMax = 5
pesoMin = 1
capMochila = 20
mochileiros = 5
k = 20              #parametro para escalonamento
l = 0.005           #parametro para escalonamento
Temperature = 20              #temperatura
t = 1
tempo_limite = 200
hitsT = 0

viajantes = []
mochila = []
objetos = []

for indexI in range(mochileiros):
    mochila = []
    for indexJ in range(n):
        mochila.append(random.randint(0,1))
    viajantes.append(mochila)

for indexI in range(n):
    tuple = (random.randint(valorMin, valorMax),
             random.randint(pesoMin, pesoMax))
    objetos.append(tuple)

print("--------------- VALORES VIAJANTES E OBJETOS ----------------")
print(viajantes)
print(objetos)
for indexK in range(mochileiros):
    print(calcula_Valor(viajantes[indexK]))
# print("------------------- VALORES MOCHILA 2 ----------------------")
# print(viajantes[2])
# print(calcula_Peso(viajantes[2], objetos))
# print(calcula_Valor(viajantes[2], objetos))
# print("----------------- COMPARAÇÃO GERA PRÓXIMO ------------------")
# print(viajantes)
# print(gera_Proximo(viajantes))
print("---------- MELHORES VIAJANTES TEMPORA SIMULADA -------------")
viajantes = tempora_Simulada(viajantes)
for indexK in range(mochileiros):
    print(calcula_Valor(viajantes[indexK]))

print(hitsT)
# mudei