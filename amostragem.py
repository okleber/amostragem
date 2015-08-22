##Made by Kleber Povoacao
##GPL V.2 Licensed


import math
import scipy.stats as st
import numpy as np

# retorna o p_valor de Z em % cumulativa na distribuicao normal
def p_valor(Z,media=0,desvpad=1):
    P = st.norm(media, desvpad).cdf(Z)
    return round(P, 4)


# retorna o valor de Z na distribuicao normal - P e a probabilidade
def z_valor(P,media=0,desvpad=1):
    Z = st.norm(media, desvpad).ppf(P)
    return raiz((round(Z, 2)) ** 2)  # eleva ao quadrado e tira raiz para sempre ser positivo o resultado


#retorna valores de Z no intervalo de confianca de X%
def confianca(percentagem):
    Z = (1 - percentagem) / 2
    return z_valor(Z)

###tira raiz quadrada ou outra qualquer
def raiz(n, y=2):
    return math.sqrt(n)

####desvio padrao da media amostral finita
def desv_pad_media_amostral_finita(S, N, n):
    return (S / raiz(n)) * raiz((N - n) / (N - 1))


####desvio padrao da media amostral infinita
def desv_pad_media_amostral_infinita(S, N, n):
    return (S / raiz(n))


####desvio padrao populacional
def desvpad_p(lista):
    return np.array([lista]).std()

####desvio padrao amostral
def desvpad_a(lista):
    return np.array([lista]).std(ddof=1)

# definir o valor de n(n amostral) ideal
def definir_qtd_n(Z,N,ME,S):
    # o resultado tem que ser maior que o valor ja retirado. caso o valor retirado seja menor vc tem que tirar de novo
    #Z = valor de Z confianca
    #N = tamanho da populacao
    #S = desvio padrao da amostra piloto
    #ME = margem de erro
    A=(Z**2*S**2*N)
    B=(ME**2)*(N-1)+Z**2*S**2
    n=A/B
    return int(n)

#retorna tupla com margem de erro esquerda e margem de erro direita
def margems_de_erro(Z,S,N,n):
    esquerda=+Z*desv_pad_media_amostral_finita(S,N,n)
    direita=-Z*desv_pad_media_amostral_finita(S,N,n)
    return (esquerda,direita)