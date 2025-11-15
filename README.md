# solAnaliticasyNumericas
# Ecuación diferencial separable y método de Euler

Este repositorio contiene un ejemplo sencillo de cómo resolver una ecuación diferencial
separable de forma analítica y cómo aproximar su solución usando el método de Euler en Python.

## Planteamiento del problema

Consideramos la ecuación diferencial ordinaria (EDO):

\[
\frac{dy}{dt} = y, \quad y(0) = 1
\]

Esta EDO es separable, ya que podemos escribir:

\[
\frac{1}{y} \, dy = dt
\]

Integramos ambos lados:

\[
\int \frac{1}{y} \, dy = \int dt \quad \Rightarrow \quad \ln|y| = t + C
\]

Despejando:

\[
y = Ce^{t}
\]

Usando la condición inicial \(y(0) = 1\):

\[
1 = C e^{0} \Rightarrow C = 1
\]

Por lo tanto, la **solución exacta** es:

\[
y(t) = e^{t}
\]

## Método de Euler

Para aproximar la solución numéricamente usamos el método de Euler:

\[
y_{n+1} = y_n + h\,f(t_n, y_n)
\]

Con:

- \(f(t,y) = y\)
- Intervalo: \(t \in [0,1]\)
- Paso: \(h = 0.2\)
- Condición inicial: \(y(0) = 1\)

Los puntos de la malla son:
\(t = 0, 0.2, 0.4, 0.6, 0.8, 1.0\)

El programa en Python calcula la aproximación en estos puntos y la compara con la
solución exacta \(y(t) = e^{t}\), mostrando el error \(|y(t_n) - y_n|\).

## Contenido del repositorio

- `main.py`: código en Python que:
  - Define la EDO.
  - Calcula la solución exacta.
  - Aplica el método de Euler.
  - Imprime una tabla con las aproximaciones y el error.
  - (Opcional) genera una gráfica si `matplotlib` está instalado.
- `README.md`: explicación del problema, la solución analítica
  y la implementación del método de Euler.

## Requisitos

- Python 3.x
- (Opcional) `matplotlib` para la gráfica

Para instalar `matplotlib`:

```bash
pip install matplotlib

