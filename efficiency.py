from math import exp, sqrt 

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
  * * MRR = Coeficiente de resistência ao rolamento
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
  * | wd = wr (cte) + wl (wl, peso, lastro - pode ser modificado)
  * * S = Patinagem
  * | Bn = (CI * b * d)/wd * (1 + 5 * (add/h)) / (1 + 3 * (b/d))
  * * add = Deformação
  * * h = Altura do rodado
  * * b = Largura do pneu
  * * Diâmetro do pneu
  * * CI = Índice de cone (característica do solo) -> Resistência do solo à penetração
  * * de um cone.
  * | MRR = MR/wd = GTR - NTR = (1/Bn) + 0.4 + (0.5 * S)/sqrt(Bn)
*/
'''

add = float(input('Deflexão/Deformação do pneu (add, em m): '))
b = float(input('Largura do pneu sem deformação (b, em m): '))
h = float(input('Altura do pneu, medido a partir do topo da roda (sem deformação) (h, em m): '))
d = float(input('Diâmetro do pneu - a partir do solo - com deformação [subtrair] (d, em m): '))
ci = float(input('Índice de cone: '))
wd = float(input('Carga dinâmica: (wd, em N): ')) # * wd = vr
S = float(input('Patinagem (de 0 a 1): '))


Bn = (ci * b * d)/(wd/1000) * (1 + 5 * (add/h)) / (1 + 3 * (b/d))

print("Bn = {:.2f}".format(Bn))

mrr = 1/Bn + .04 + .5 * S/sqrt(Bn)

mr = mrr * (wd/1000)

print("(Coeficiente de resistência ao rolamento) MRR = {:.2f}\n(Força de resistência ao rolamento) MR = {:.2f} kN".format(mrr, mr))

# * gtr = Q/(r * wd) = 0.88 * (1 - exp(-0.1 * Bn)) * (1 - exp(-7.5 * S)) + 0.04

coefTracao = float(input('Coeficiente de tração: (de 0 a 1): '))

gtr = coefTracao
gt = gtr * (wd/1000)
nt = gt - mr

print("(Tração total/Força de tração máxima) [eixo] GT = {:.2f} kN".format(gt))
print("(Força no eixo/máxima força disponível) [pneu] NT = {:.2f} kN".format(nt))

'''
  /**
  * ? Fi = Tipo de solo (1, 2, 3)
  * ? S = Velocidade (S, em km/h)
  * ? W = Largura da máquina ou número de ferramentas (em, m)
  * ? T = Profundidade (T, em cm)
  */
'''

f = float(input("Textura do solo (inteiro): "))
a = float(input("Parâmetro A: "))
b = float(input("Parâmetro B: "))
c = float(input("Parâmetro C: "))
largura = float(input("Largura do implemento (em m)/Número de ferramentas: "))
profundidade = float(input("Profundidade de trabalho (t, em cm): "))
velocidade = float(input("Velocidade de operação (km/h): "))

D = f * (a + b * velocidade + c * velocidade**(2)) * largura * profundidade # * Em Newton

kwb = D * (velocidade/3.6)

print("D = {:.2f} kN".format(D/1000))
print("KWB = {:.2f} kN".format(kwb/1000))