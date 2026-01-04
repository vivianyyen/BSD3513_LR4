import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")
st.write("f(x) = 1 / (1 + e⁻ˣ)")

x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Function")

st.pyplot(fig)
