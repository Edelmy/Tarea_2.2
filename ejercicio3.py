import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
def g(x):
    return (np.cos(x))#g(x)

# Criterio de convergencia
def g_prime(x): #
    return -(np.sin(x))  # Calcula g(x) usando la función exponencial de NumPy

# Error absoluto
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old) # Calcula la diferencia absoluta entre dos valores

# Error relativo
def error_relativo(x_new, x_old):
    return abs((x_new - x_old) / x_new)  # Calcula la diferencia relativa entre dos valores

# Error cuadrático
def error_cuadratico(x_new, x_old):
    return (x_new - x_old)**2 # Calcula el cuadrado de la diferencia entre dos valores

# Método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []

    x_old = x0 # Inicializa el valor anterior
    for i in range(max_iter):  # Itera hasta alcanzar el número máximo de iteraciones
        x_new = g(x_old) # Calcula el nuevo valor usando la función g(x)
        e_abs = error_absoluto(x_new, x_old)
        e_rel = error_relativo(x_new, x_old)
        e_cuad = error_cuadratico(x_new, x_old)

        iteraciones.append((i+1, x_new, e_abs, e_rel, e_cuad))  # Almacena los resultados de la iteración
        errores_abs.append(e_abs)
        errores_rel.append(e_rel)
        errores_cuad.append(e_cuad)

        if e_abs < tol:  # Verifica si el error absoluto es menor que la tolerancia
            break # Termina la iteración si se alcanza la tolerancia

        x_old = x_new # Actualiza el valor anterior

    return iteraciones, errores_abs, errores_rel, errores_cuad # Devuelve los resultados

# Parámetros iniciales SE CAMBIA
x0 = 0.5
iteraciones, errores_abs, errores_rel, errores_cuad = punto_fijo(x0) # Ejecuta el método de punto fijo

# Imprimir tabla de iteraciones
print("Iteración | x_n      | Error absoluto | Error relativo | Error cuadrático")
print("-----------------------------------------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e} | {it[3]:.6e} | {it[4]:.6e}")

# Graficar la convergencia
x_vals = np.linspace(-1, 3, 100)  # Genera un rango de valores para x
y_vals = g(x_vals) # Calcula los valores de g(x) para el rango de valores de x


plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$g(x) = (cos(x))$", color="blue")
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")

# Graficar iteraciones
x_points = [it[1] for it in iteraciones]  # Obtiene los valores de x_n de cada iteración
y_points = [g(x) for x in x_points]  # Calcula los valores de g(x) para los valores de x_n
plt.scatter(x_points, y_points, color="black", zorder=3) # Grafica los puntos de las iteraciones
plt.plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")

plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.title("Método de Punto Fijo")
plt.savefig("punto_fijo_convergencia.png")
plt.show()

# Graficar errores
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")
plt.plot(range(1, len(errores_rel) + 1), errores_rel, marker="s", label="Error relativo")
plt.plot(range(1, len(errores_cuad) + 1), errores_cuad, marker="^", label="Error cuadrático")

plt.xlabel("Iteración")
plt.ylabel("Error")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.title("Evolución de los Errores")
plt.savefig("errores_punto_fijo.png")
plt.show() # Muestra el gráfico