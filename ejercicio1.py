def f(x):
  """Función original"""
  return 25*x**3 - 6*x**2 + 7*x - 88

def taylor_approx(x):
  """Aproximación de Taylor de tercer orden centrada en x=1"""
  return -62 + 70*(x-1) + (138/2)*(x-1)**2 + (150/6)*(x-1)**3

# Valor en el que queremos evaluar
x_value = 3

# Valor aproximado usando la serie de Taylor
approx_value = taylor_approx(x_value)

# Valor exacto de la función
exact_value = f(x_value)

# Error absoluto
error_absoluto = abs(exact_value - approx_value)

# Error relativo porcentual
error_relativo_porcentual = (error_absoluto / exact_value) * 100

# Imprimir resultados
print(f"Valor aproximado de f({x_value}) usando la serie de Taylor: {approx_value}")
print(f"Valor exacto de f({x_value}): {exact_value}")
print(f"Error absoluto: {error_absoluto}")
print(f"Error relativo porcentual: {error_relativo_porcentual:.2f}%")