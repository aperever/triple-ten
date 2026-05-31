import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.title("Triple Ten Project")

st.write("My first Streamlit app")

data = pd.DataFrame({
    "month": ["January", "February", "March", "April"],
    "sales": [100, 150, 130, 180]
})

st.subheader("Data")
st.dataframe(data)

st.subheader("Plotly chart")
fig = px.line(data, x="month", y="sales", markers=True)
st.plotly_chart(fig)

st.subheader("Altair chart")
chart = alt.Chart(data).mark_bar().encode(
    x="month",
    y="sales"
)
st.altair_chart(chart, use_container_width=True)