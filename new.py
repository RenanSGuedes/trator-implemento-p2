from math import cos, tan, atan, radians

# todo Carga Dinâmica - Em movimento com solo em determinada inclinação (alpha)

'''
/**
* * Primeira parte: Posição do CG em x:
* ? Peso do trator: w
* ? Distância entre eixos: x
* todo Relação:
* | w * xf = wf * xr
* ? xr = distância horizontal do CG ao eixo traseiro
* ? xf = distância horizontal do CG ao eixo dianteiro
*/
'''

print(10 * "-","Parte 1", 10 * "-")
w = float(input("Peso do trator (w, kg): "))
x = float(input("Distância entre eixos (x, m): "))
wf = float(input("Peso do eixo dianteiro apoiado (wf, kg): "))
wr = float(input("Peso do eixo traseiro apoiado (wr, kg): "))

'''
/**
* | Exemplo Numérico 1
* * x = 88.94 mm
* * w = 1006.57 g
* * wf = 468.25 g
* * wr = 534.57 g
* ? O peso pode ser adicionado tanto ao eixo traseiro quanto 
* ? na parte dianteira do trator
*/
'''

xf = (wf/w) * x
xr = x - xf
print("(Distância do CG ao eixo dianteiro) xf = {:.2f}m\n(Distância do CG ao eixo traseiro) xr = {:.2f}m".format(xf, xr)) 

'''
/**
* * Segunda parte: Posição do CG em y
* ? rr = raio da roda traseira
* ? rf = raio da roda dianteira
* ? yl = distância vertical do solo ao eixo da roda inclinada
* ? wfl = peso da roda dianteira inclinada
* ? xll = distância entre eixos com o trator inclinado
* ? yg = Altura y do CG
*/
'''

'''
/**
* | Exemplo numérico 2
* * rf = 23 mm
* * rr = 32 mm
* * Peso dianteiro inclinado wfl = 438.8 g
* * projeção: xll = 84.6 mm 
* * altura do apoio: h = 27.6 mm
*/
'''
print(10 * "-","Parte 2", 10 * "-")

wfl = float(input("Peso inclinado da parte dianteira apoiada (wfl, em kg): "))
xll = float(input("Distância entre eixos com o trator inclinado (xll, em m): "))
rf = float(input("Raio dianteiro (rf, em m): "))
rr = float(input("Raio traseiro (rr, em m): "))
h = float(input("Altura do apoio para o trator inclinado (h, em m): "))

yl = rf + h
beta = atan((rr - rf)/x) + atan((yl - rr)/xll) # ? Valor em radianos

xrl = wfl * xll / w
z = xrl/cos(beta)
yg = (xf - z)/tan(beta)


print("(Em relação à roda traseira) yg = {:.2f}m\n=> (Em relação ao solo) ygt = {:.2f}\nz = {:.2f}m\nxrl = {:.2f}m".format(yg, yg + rr,z, xrl))

# todo Resumo de cargas estáticas

questionAboutTheta = input("Theta é nulo? [S]im ou [N]ão: ")
questionAboutP = input("P é nula? [S]im ou [N]ão: ")
questionAboutAlpha = input("Alpha é nulo? [S]im ou [N]ão: ")

if questionAboutTheta == "S":
  theta = 0

if questionAboutP == "S":
  p = 0

if questionAboutAlpha == "S":
  alpha = 0

# * Quando theta = 0°
  # | A força do implemento é paralela ao solo, logo

if theta == 0:
  vf = w * cos(radians(alpha)) * (xr/x) - w * sin(radians(alpha)) * (rr + yg/x) - p * (yl/x)
  vr = w * cos(radians(alpha)) * (xf/x) - w * sin(radians(alpha)) * (rr + yg/x) + p * (yl/x)
elif alpha == 0:
  vf = wf - (P * yl)/x
  vr = wf + (P * yl)/x
else: # * Quando p = 0 
  vf = wf
  vr = wf

