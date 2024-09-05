import math

def caudal_manning(B, h, n, S):
  """Calcula el caudal en un canal rectangular utilizando la ecuación de Manning.

  Args:
    B: Ancho del canal (m)
    h: Profundidad del flujo (m)
    n: Coeficiente de rugosidad de Manning
    S: Pendiente del canal

  Returns:
    Caudal en m³/s
  """

  Q = ((B*h)**(5/3) / (n * (B+2*h)**(2/3) )* math.sqrt(S))
  return Q

# Datos del problema
B = 20  # Ancho del canal (m)
h = 0.3  # Profundidad del flujo (m)
n = 0.03  # Coeficiente de rugosidad nominal
S = 0.0003  # Pendiente nominal

# Rango de incertidumbre para n y S
delta_n = 0.1 * n
delta_S = 0.1 * S

# Cálculo del caudal nominal y sus derivadas parciales
dn=-(B*h*math.sqrt(S)*(B**2/3)*(h**2/3))/((n**2)*((B+2*h)**2/3))
ds=((B*h)**(5/3))/((2*(n))*(math.sqrt(S))*(B+(2*h))**(2/3))

# Propagación de errores
eQ=dn*delta_n+ds*delta_S
print("dQ/dn=",dn)
print("dQ/ds=",ds)
print("Q-eQ= ",caudal_manning(B,h,n,S)-eQ)
print("Q+eQ= ",caudal_manning(B,h,n,S)+eQ)

print("se deberia intentar medir la pendiente para tener mejorar la precision")