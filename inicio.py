##Made by Kleber Povoacao
##GPL V.2 Licensed

import amostragem as am

print am.definir_qtd_n(am.confianca(.95),15000,100,am.desvpad_a([1000,0,500]))
exit()

print "Digite valor de S, desvio padrao de 1 amostra"
S = float(raw_input())
print "Digite valor de N, tamanho da populacao"
N = float(raw_input())
print "Digite valor de n, elementos amostrais"
n = float(raw_input())
print "Digite valor de n, elementos amostrais"
n = float(raw_input())
am.desv_pad_media_amostral_infinita(S, N, n)