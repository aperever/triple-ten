import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Vehicle Advertisement Dashboard")

st.write(
    "This web app explores a dataset of used vehicle advertisements in the US market."
)

df = pd.read_csv("vehicles_us.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Basic Dataset Information")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")

show_filtered_data = st.checkbox("Show only vehicles with odometer below 100,000 miles")

if show_filtered_data:
    filtered_df = df[df["odometer"] < 100000]
else:
    filtered_df = df

st.subheader("Filtered Dataset")
st.write(filtered_df.head())

st.subheader("Vehicle Price Distribution")

fig_hist = px.histogram(
    filtered_df,
    x="price",
    nbins=50,
    title="Distribution of Vehicle Prices"
)

st.plotly_chart(fig_hist, use_container_width=True)

st.subheader("Price vs Odometer")

fig_scatter = px.scatter(
    filtered_df,
    x="odometer",
    y="price",
    title="Vehicle Price vs Odometer",
    opacity=0.5
)

st.plotly_chart(fig_scatter, use_container_width=True)