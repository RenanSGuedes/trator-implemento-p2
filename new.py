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

if question == 'Vf':
  w = float(input("Massa do trator (w, em kg): "))
  x = float(input("Distância entre eixos medida no plano (x, em m): "))
  xl = float(input("Distância horizontal que vai do eixo traseiro a CG do implemento (xl, em m): "))
  yl = float(input("Distância vertical do solo ao eixo inclinado (yl, em m): "))
  r = float(input("Raio da roda traseira (r, em m): "))
  p = float(input("Força de tração no implemento (p, em N): "))
  yg = float(input("Distãncia vertical do solo ao CG do trator (yg, em m): "))
  xr = float(input("Distância horizontal entre o eixo traseiro e o CG do trator (xr, em m): "))
  theta = float(input("Ângulo de inclinação da força p (theta, em graus): "))
  alpha = float(input("Ângulo de inclinação do terreno (alpha, em graus): "))

  y = r - yl

  t1 = w * 9.81 * cos(radians(alpha)) * (xr/x)
  t2 = w * 9.81 * sin(radians(alpha)) * (r + yg/x)
  t3 = p * cos(radians(theta)) * (r - y)/x
  t4 = p * sin(radians(theta)) * xl/x

  vf = t1 - t2 - t3 - t4  

  print("{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}\n".format(t1, t2, t3, t4))
  print("vf = {:.2f}N".format(vf))
else:
  w = float(input("Massa do trator (w, em kg): "))
  vf = float(input("Tração requerida com o solo (vf, em N): "))
  x = float(input("Distância entre eixos medida no plano (x, em m): "))
  xl = float(input("Distância horizontal que vai do eixo traseiro a CG do implemento (xl, em m): "))
  yl = float(input("Distância vertical do solo ao eixo inclinado (yl, em m): "))
  r = float(input("Raio da roda traseira (r, em m): "))
  p = float(input("Força de tração no implemento (p, em N): "))
  yg = float(input("Distãncia vertical do solo ao CG do trator (yg, em m): "))
  xr = float(input("Distância horizontal entre o eixo traseiro e o CG do trator (xr, em m): "))
  theta = float(input("Ângulo de inclinação da força p (theta, em graus): "))
  alpha = float(input("Ângulo de inclinação do terreno (alpha, em graus): "))

  y = r - yl

  K = cos(radians(theta)) * (r - y)/x + sin(radians(theta)) * xl/x
  L = cos(radians(alpha)) * (xr/x) - sin(radians(alpha)) * (r + yg/x)

  p = (w * 9.81 * L - vf)/K

  print("p = {}N = {}kg".format(p, p/9.81))