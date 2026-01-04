import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Animated ReLU Activation Function")
st.latex(r"f(x) = \max(0, x)")

placeholder = st.empty()

# Animate x-range expansion
for xmax in np.linspace(1, 10, 30):
    x = np.linspace(-xmax, xmax, 400)
    y = np.maximum(0, x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Input (x)")
    ax.set_ylabel("Output")
    ax.set_title("ReLU Curve Growing")

    placeholder.pyplot(fig)
    time.sleep(0.05)

st.success("Animation complete. You can now interact below.")

# Interactive controls after animation
x_value = st.slider("Select x", -10.0, 10.0, 0.0)
st.write("ReLU(x) =", max(0, x_value))
