from math import sin, cos, tan, atan, radians
'''
/**
* * Terceira parte: Cálculo de vf e vr
* ? r = rr (Raio da roda traseira)
* ? alpha = Inclinação do terreno com a horizontal, em graus
* ? theta = Ângulo da força trativa P medido em relação à horizontal
* ? y = Distância vertical do ponto onde se conecta o implemento ao eixo traseiro
* ? xl = Distância horizontal que vai do eixo traseiro a CG do implemento
*/
'''

question = input("Calcular a carga [P] ou a força de tração [V]f: ")

w = float(input("Massa do trator (w, em kg): "))
x = float(input("Distância entre eixos medida no plano (x, em m): "))
xl = float(input("Distância horizontal que vai do eixo traseiro a CG do implemento (xl, em m): "))
yl = float(input("Distância vertical do solo ao ponto de conexão do implemento (yl, em m): "))
r = float(input("Raio da roda traseira (r, em m): "))
yg = float(input("Distãncia vertical do eixo traseiro ao CG do trator (yg, em m): "))
xr = float(input("Distância horizontal entre o eixo traseiro e o CG do trator (xr, em m): "))
theta = float(input("Ângulo de inclinação da força p (theta, em graus): "))
alpha = float(input("Ângulo de inclinação do terreno (alpha, em graus): "))

wr = float(input("Massa com eixo traseiro apoiado (wr, em kg): "))
wf = float(input("Massa com eixo dianteiro apoiado: (wf, em kg): "))

y = r - yl

if question == 'V':
  p = float(input("Força de tração no implemento (p, em N): "))

  # * t1 = w * 9.81 * cos(radians(alpha)) * (xr/x) # * wf
  t2 = w * 9.81 * sin(radians(alpha)) * (r + yg)/x
  t3 = p * cos(radians(theta)) * (r - y)/x
  t4 = p * sin(radians(theta)) * xl/x

  # * t5 = w * 9.81 * cos(radians(alpha)) * (1 - xr/x) # * wr
  t7 = p * cos(radians(theta)) * (yl/x) 
  t8 = p * sin(radians(theta)) * (x + xl)/x


  vf = wf * 9.81 - t2 - t3 - t4  
  vr = wr * 9.81 + t2 + t7 + t8

  print("vf = wf (novo) = {:.2f} N = {:.2f} kg".format(vf, vf/9.81))
  print("vr = {:.2f} N = {:.2f} kg".format(vr, vr/9.81))
  print("Comparar o vf obtido com o wf do trator no plano para ver o quanto é preciso adicionar ou tirar de massa.")
else:
  vf = float(input("Tração requerida com o solo (vf, em N): "))

  A = 9.81 * w * (cos(radians(alpha)) * xr - sin(radians(alpha)) * (r + yg)) - vf * x
  B = cos(radians(theta)) * yl + sin(radians(theta)) * xl

  p = A/B

  print("p = {:.2f} N = {:.2f} kg".format(p, p/9.81))