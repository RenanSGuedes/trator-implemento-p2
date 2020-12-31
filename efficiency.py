from math import exp

'''
/**
* todo Eficiência de tração (TE)
* * NT = Tração trativa (pneu)
* * GT = Tração total (eixo)
* * MR = Força de resistência ao movimento
* * wd = Carga dinâmica no pneu
* * TRR = Taxa de redução da viagem
* * Índice de mobilidade
* ? Cálculo do TE
* | TE (ratio) = OutputPower/InputPower = (NT * va)/AxlePower
* |              = (NT * va)/(GT * vt) =
* |              = ((NT/wd) * va)/((GT/wd) * vt) = 
* |              = (NTR/GTR) * (va/vt)

* ? Cálculo do GTR
* | GTR = (NTR/TE) * (va/vt) = (NRT/TE) * (1 - TRR)
* * Outra forma de obter o GTR (Equação empírica)
* | GTR = Q/(r * W) = 0.88 * (1 - exp(-0.1 * Bn)) * (1 - exp(-7.5 * S)) + 0.04
* * Bn = Índice de mobilidade
* * S = Patinagem
* | Bn = (CI * b * d)/W * (1 + 5 * (add/h)) / (1 + 3 * (b/d))
* * add = Deformação
* * W = Carga dinâmica
* * h = Altura do rodado
* * b = Largura do pneu
* * Diâmetro do pneu
* * CI = Índice de cone (característica do solo) 
* | MRR = GTR - NTR
*/
'''

