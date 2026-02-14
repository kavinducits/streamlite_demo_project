import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Kavindu Dashboard", page_icon="📊")

st.title("Kavindu Dashboard")
st.caption("Quick interactive walkthrough tailored for the Kavindu showcase.")

with st.sidebar:
    st.header("Controls")
    sample_size = st.slider("Sample size", min_value=10, max_value=200, value=50, step=10)
    noise_level = st.select_slider("Noise", options=[0.1, 0.2, 0.5, 1.0], value=0.2)
    show_table = st.toggle("Show raw data", value=True)

x = np.linspace(0, 2 * np.pi, sample_size)
y = np.sin(x) + np.random.normal(scale=noise_level, size=sample_size)

data = pd.DataFrame({
    "x": x,
    "signal": np.sin(x),
    "noisy": y,
})

st.subheader("Signal vs Noise")
st.line_chart(data.set_index("x")[["signal", "noisy"]])

st.subheader("Insights")
st.metric("Max noisy value", f"{data['noisy'].max():.2f}")
st.metric("Min noisy value", f"{data['noisy'].min():.2f}")
st.metric("Std dev", f"{data['noisy'].std():.2f}")

if show_table:
    st.subheader("Sample Data")
    st.dataframe(data.head(10))

st.markdown("---")
st.write("Try tweaking the sliders to see how the visual updates live. That's the core Streamlit experience behind Kavindu.")
