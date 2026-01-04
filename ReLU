import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")
st.write("f(x) = max(0, x)")

x = np.linspace(-10, 10, 400)
y = np.maximum(0, x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.set_title("ReLU Function")

st.pyplot(fig)
