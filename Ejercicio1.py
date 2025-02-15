import numpy as np  # Importa la biblioteca NumPy para operaciones matemáticas
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para graficar

# Definir la función g(x) para el método de punto fijo
def g(x): 
    return(3*x-1)**(1/2)  # Calcula g(x) usando la función exponencial de NumPy

# Criterio de convergencia
def g_prime(x):  
    return (3/2) * (3*x-1)**(-1/2)  # Derivada de la función exponencial

# Error absoluto
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)  # Calcula la diferencia absoluta entre dos valores

# Error relativo
def error_relativo(x_new, x_old):
    return abs((x_new - x_old) / x_new)  # Calcula la diferencia relativa entre dos valores

# Error cuadrático
def error_cuadratico(x_new, x_old):
    return (x_new - x_old)**2  # Calcula el cuadrado de la diferencia entre dos valores

# Método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []  
    errores_abs = []  
    errores_rel = []  
    errores_cuad = []  

    x_old = x0  # Inicializa el valor anterior
    for i in range(max_iter):  # Itera hasta alcanzar el número máximo de iteraciones
        x_new = g(x_old)  # Calcula el nuevo valor usando la función g(x)
        e_abs = error_absoluto(x_new, x_old)  # Calcula el error absoluto
        e_rel = error_relativo(x_new, x_old)  # Calcula el error relativo
        e_cuad = error_cuadratico(x_new, x_old)  # Calcula el error cuadrático

        iteraciones.append((i+1, x_new, e_abs, e_rel, e_cuad))  # Almacena los resultados de la iteración
        errores_abs.append(e_abs)  
        errores_rel.append(e_rel)  
        errores_cuad.append(e_cuad)  

        if e_abs < tol:  # Verifica si el error absoluto es menor que la tolerancia
            break  # Termina la iteración si se alcanza la tolerancia

        x_old = x_new  # Actualiza el valor anterior

    return iteraciones, errores_abs, errores_rel, errores_cuad  # Devuelve los resultados

# Parámetros iniciales
x0 = 1.5 # Define el valor inicial (se cambia)
iteraciones, errores_abs, errores_rel, errores_cuad = punto_fijo(x0)  # Ejecuta el método de punto fijo

# Imprimir tabla de iteraciones
print("Iteración | x_n      | Error absoluto | Error relativo | Error cuadrático")
print("-----------------------------------------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e} | {it[3]:.6e} | {it[4]:.6e}")

# Graficar la convergencia
x_vals = np.linspace(-1, 3, 100)  # Genera un rango de valores para x
y_vals = g(x_vals)  # Calcula los valores de g(x) para el rango de valores de x

plt.figure(figsize=(8, 5))  # Crea una figura para el gráfico
plt.plot(x_vals, y_vals, label=r"$g(x) = (3x-1)^{1/2}$", color="blue")  # Grafica la función g(x)
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")  # Grafica la línea y = x
# Graficar iteraciones
x_points = [it[1] for it in iteraciones]  # Obtiene los valores de x_n de cada iteración
y_points = [g(x) for x in x_points]  # Calcula los valores de g(x) para los valores de x_n
plt.scatter(x_points, y_points, color="black", zorder=3)  # Grafica los puntos de las iteraciones
plt.plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")  

plt.xlabel("x")  
plt.ylabel("g(x)")  
plt.legend()  
plt.grid(True)  
plt.title("Método de Punto Fijo")  
plt.savefig("punto_fijo_convergencia.png")  
plt.show()  

# Graficar errores
plt.figure(figsize=(8, 5))  # Crea una figura para el gráfico
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")  # Grafica el error absoluto
plt.plot(range(1, len(errores_rel) + 1), errores_rel, marker="s", label="Error relativo")  # Grafica el error relativo
plt.plot(range(1, len(errores_cuad) + 1), errores_cuad, marker="^", label="Error cuadrático")  # Grafica el error cuadrático

plt.xlabel("Iteración")  # Etiqueta del eje x
plt.ylabel("Error")  
plt.yscale("log")  
plt.legend()  
plt.grid(True) 
plt.title("Evolución de los Errores") 
plt.savefig("errores_punto_fijo.png")  
plt.show()  # Muestra el gráfico