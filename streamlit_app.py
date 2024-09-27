import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Funciones importadas del archivo odes.py (simplificadas)
def euler(f, x0, t):
    x = np.zeros(len(t))
    x[0] = x0
    xs = [[t[0], x[0]]]
    for n in range(len(t) - 1):
        x[n + 1] = x[n] + f(x[n], t[n]) * (t[n + 1] - t[n])
        xs.append([t[n + 1], x[n + 1]])
    return np.round(np.array(xs), 4)

def euler2(f1, f2, y0, x0, t):
    y = np.zeros(len(t))
    x = np.zeros(len(t))
    y[0] = y0
    x[0] = x0
    yx = [[y[0], x[0]]]
    for n in range(len(t) - 1):
        y[n + 1] = y[n] + f1(y[n], x[n], t[n]) * (t[n + 1] - t[n])
        x[n + 1] = x[n] + f2(y[n], x[n], t[n]) * (t[n + 1] - t[n])
        yx.append([y[n + 1], x[n + 1]])
    return np.round(np.array(yx), 4)

# Ejemplo de funciones para resolver
def example_func(x, t):
    return -0.5 * x

def example_func1(y, x, t):
    return y - x

def example_func2(y, x, t):
    return x - y

# Configurar la interfaz con Streamlit
st.title("Solución de Ecuaciones Diferenciales con Métodos Numéricos")

# Entrada de datos
x0 = st.number_input("Condición inicial x0", value=1.0)
t = np.linspace(0, 10, 100)

# Botones para ejecutar las funciones
if st.button("Ejecutar Método de Euler para una ODE"):
    resultado = euler(example_func, x0, t)
    st.write("Resultado:", resultado)
    fig, ax = plt.subplots()
    ax.plot(resultado[:, 0], resultado[:, 1], label="Euler")
    ax.set_title("Método de Euler")
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    st.pyplot(fig)

if st.button("Ejecutar Método de Euler para un Sistema de 2 EDOs"):
    y0 = st.number_input("Condición inicial y0", value=1.0)
    resultado = euler2(example_func1, example_func2, y0, x0, t)
    st.write("Resultado:", resultado)
    fig, ax = plt.subplots()
    ax.plot(t, resultado[:, 0], label="y(t)")
    ax.plot(t, resultado[:, 1], label="x(t)")
    ax.set_title("Método de Euler para Sistema de 2 EDOs")
    ax.set_xlabel("t")
    ax.legend()
    st.pyplot(fig)
