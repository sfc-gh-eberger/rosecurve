import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to generate rose curve data
def rose_curve(n, d):
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(n * theta) ** d
    return theta, r

# Streamlit app
def main():
    st.title('Rose Curves Generator')

    n = st.slider('Value of n', 1, 20, 2)
    d = st.slider('Value of d', 1, 20, 2)

    theta, r = rose_curve(n, d)

    # Plotting the rose curve
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(r * np.cos(theta), r * np.sin(theta))
    ax.set_aspect('equal')
    ax.set_title(f'Rose Curve with n={n}, d={d}')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
