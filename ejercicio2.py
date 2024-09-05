import math

def factorial(n):
  """Función factorial"""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def taylor_ln(x, a, n):
  """
  Calcula la aproximación de ln(x) usando la serie de Taylor de orden n centrada en a
  """
  approx = 0
  for i in range(1, n+1):
    dy= (-1)**(i+1)*factorial(i-1) / a**i
    print((-1)**(i+1)*factorial(i-1)," /" ,"a^",i)
    print("la derivada es:" ,dy)
    approx += ((dy)/factorial(i))*(x-a)**i
    print(approx)
  return approx

# Parámetros
a = 1  # Centro de la serie de Taylor
x = 2.5
n = 4  # Orden de la serie de Taylor

# Cálculo de la aproximación
approx_ln = taylor_ln(x, a, n)

# Valor exacto (usando la biblioteca math)
exact_ln = math.log(x)

# Error absoluto
error_absoluto = abs(exact_ln - approx_ln)

# Error relativo porcentual
error_relativo = (error_absoluto / exact_ln) * 100

# Imprimir resultados
print("Aproximación de ln(2.5) usando la serie de Taylor:", approx_ln)
print("Valor exacto de ln(2.5):", exact_ln)
print("Error absoluto:", error_absoluto)
print("Error relativo porcentual:", error_relativo, "%")