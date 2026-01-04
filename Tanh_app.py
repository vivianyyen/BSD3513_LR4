import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Hyperbolic Tangent (Tanh)")
st.latex(r"f(x) = \tanh(x)")

# Controls
x_min, x_max = st.slider("Select input range", -20.0, 20.0, (-10.0, 10.0))
x_value = st.slider("Select an input value x", x_min, x_max, 0.0)

x = np.linspace(x_min, x_max, 400)
y = np.tanh(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter([x_value], [np.tanh(x_value)], s=80)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.set_title("Tanh Function")

st.pyplot(fig)

st.write("For x =", x_value, ", Tanh(x) =", np.tanh(x_value))
