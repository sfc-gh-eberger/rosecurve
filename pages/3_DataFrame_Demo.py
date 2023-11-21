import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to generate rhodonea curve data
def rhodonea_curve(n, d, theta_values):
    r = np.cos(n * theta_values) + np.sin(d * theta_values)
    return r

# Streamlit app
def main():
    st.title('Rhodonea Curve Graphing')

    n = st.slider('Value of n', -20.0, 20.0, 5.0, step=0.25)
    d = st.slider('Value of d', -20.0, 20.0, 7.0, step=0.25)

    color = 'red'

    # Radio button for filling the center with red color
    fill_color = st.radio("Fill the center with red color", ('Yes', 'No'))

    theta_min = 0
    theta_max = 2 * np.pi

    theta_values = np.linspace(theta_min, theta_max, 1000)
    r_values = rhodonea_curve(n, d, theta_values)

    # Plotting the rhodonea curve
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.plot(theta_values, r_values, color=color)

    if fill_color == 'Yes':
        ax.fill(theta_values, r_values, color='red', alpha=0.3)

    ax.set_title(f'Rhodonea Curve with n={n}, d={d}')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
