# main.py
# Resolución analítica y aproximación numérica (Euler) de la EDO:
#   dy/dt = y,  y(0) = 1
#
# Solución exacta: y(t) = e^t

import math

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def f(t, y):
    """Función que define la EDO: dy/dt = y."""
    return y


def solucion_exacta(t):
    """Solución analítica de la EDO: y(t) = e^t."""
    return math.exp(t)


def euler(f, t0, y0, h, tf):
    """
    Método de Euler para aproximar la solución de una EDO de primer orden.

    f  : función f(t, y)
    t0 : tiempo inicial
    y0 : valor inicial y(t0)
    h  : tamaño de paso
    tf : tiempo final

    Regresa:
        listas (ts, ys) con los puntos (t_n, y_n) generados.
    """
    ts = [t0]
    ys = [y0]

    n_pasos = int((tf - t0) / h)

    for _ in range(n_pasos):
        t_n = ts[-1]
        y_n = ys[-1]
        y_siguiente = y_n + h * f(t_n, y_n)
        t_siguiente = t_n + h

        ts.append(t_siguiente)
        ys.append(y_siguiente)

    return ts, ys


def main():
    # Parámetros del problema
    t0 = 0.0
    y0 = 1.0
    tf = 1.0
    h = 0.2

    # Aproximación por Euler
    ts, ys = euler(f, t0, y0, h, tf)

    # Impresión de resultados en forma de tabla
    print("Aproximación de la EDO dy/dt = y,  y(0) = 1")
    print(f"Usando método de Euler en [0, {tf}] con h = {h}\n")

    print("{:>5s} | {:>8s} | {:>12s} | {:>12s} | {:>12s}".format(
        "n", "t_n", "Euler y_n", "Exacta y(t_n)", "Error |y - y_n|"
    ))
    print("-" * 62)

    for n, (t, y_n) in enumerate(zip(ts, ys)):
        y_exacta = solucion_exacta(t)
        error = abs(y_exacta - y_n)
        print("{:5d} | {:8.2f} | {:12.6f} | {:12.6f} | {:12.6f}".format(
            n, t, y_n, y_exacta, error
        ))

    # Gráfica opcional
    if HAS_MATPLOTLIB:
        # Datos exactos para la curva suave
        t_fino = [t0 + i * 0.01 for i in range(int((tf - t0) / 0.01) + 1)]
        y_fino = [solucion_exacta(t) for t in t_fino]

        plt.plot(t_fino, y_fino, label="Solución exacta y(t) = e^t")
        plt.scatter(ts, ys, label="Puntos método de Euler", zorder=3)

        plt.title("Comparación: solución exacta vs. método de Euler")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("\nNota: matplotlib no está instalado; no se generó la gráfica.")
        print("Si deseas graficar, instala con: pip install matplotlib")


if __name__ == "__main__":
    main()
