from math import exp

'''
/**
* todo Eficiência de tração (TE)
* * MR = Resistência ao rolamento
* * NT = Força no eixo (pneu): É proveniente da interação solo-pneu entre as
* * forças GT e MR
* | NT = Força líquida = GT - MR
* * Força no implemento -> P = Pv (vertical) + Ph (horizontal)
* ? Para que haja o movimento
* | NT >= Ph 

* * GT = Tração total (eixo)
* * MR = Força de resistência ao movimento
* * wd = Carga dinâmica no pneu
* * TRR = Taxa de redução da viagem
* * Índice de mobilidade
* ? Cálculo do TE
* | TE (ratio) = OutputPower/InputPower = (NT * va)/AxlePower
* |              = (NT * va)/(GTR * vt) =
* |              = ((NT/wd) * va)/((GT/wd) * vt) = 
* |              = (NTR/GTR) * (va/vt)

* ? Cálculo do GTR - Coeficiente de tração
* | GTR = (NTR/TE) * (va/vt) = (NRT/TE) * (1 - TRR)
* * Outra forma de obter o GTR (Equação empírica)
* | GTR = Q/(r * wd) = 0.88 * (1 - exp(-0.1 * Bn)) * (1 - exp(-7.5 * S)) + 0.04
* * Bn = Índice de mobilidade - Curva vermelha
* ? Para cada Bn há uma eficiência TE associada.
* todo Visando aumentar a eficiência, a melhor alternativa é modificar
* todo a carga dinâmica (wd), logo
* | wd = wr + wl (wl, lastro)
* * S = Patinagem
* | Bn = (CI * b * d)/wd * (1 + 5 * (add/h)) / (1 + 3 * (b/d))
* * add = Deformação
* * W = Carga dinâmica
* * h = Altura do rodado
* * b = Largura do pneu
* * Diâmetro do pneu
* * CI = Índice de cone (característica do solo) -> Resistência do solo à penetração
* * de um cone.
* | MRR = GTR - NTR
*/
'''

add = float(input('Deformação do pneu: '))
b = float(input('Largura do pneu sem deformação: '))
h = float(input('Altura do pneu, medido a partir do topo da roda (sem deformação): '))
d = float(input('Diâmetro do pneu - a partir do solo - com deformação: '))
hDeform = float(input('Altura do pneu na parte deformada: '))
ci = float(input('Índice de cone: '))
wd = float(input('Carga dinâmica: '))

add = h - hDeform # * h será sempre maior que hDeform, já que o pneu
# * é comprimido na parte em contato com o solo.

Bn = (ci * b * d)/wd * (1 + 5 * (add/h)) / (1 + 3 * (b/d))

S = float(input("Patinagem: "))
r = float(input("Raio da roda traseira: "))

gtr = Q/(r * wd) = 0.88 * (1 - exp(-0.1 * Bn)) * (1 - exp(-7.5 * S)) + 0.04