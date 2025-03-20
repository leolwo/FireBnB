def parouimpar(n, par, impar):
  if n % 2 == 0:
    n = par
  else:
    n = impar

  if n == par:
    print(f'{n} é par')
  elif n == impar:
    print(f'{n} é ímpar')
