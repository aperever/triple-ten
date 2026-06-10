from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Vehicle Advertisement Dashboard",
    layout="wide",
)

DATA_PATH = Path(__file__).resolve().parent / "vehicles_us.csv"
ODOMETER_LIMIT = 100_000


@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    """Load the vehicle dataset and convert chart columns to numeric."""
    data = pd.read_csv(file_path)

    for column in ["price", "odometer"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    return data


st.header("Vehicle Advertisement Dashboard")

st.write(
    "This web app explores a dataset of used vehicle advertisements "
    "in the US market."
)

try:
    df = load_data(str(DATA_PATH))
except FileNotFoundError:
    st.error(f"Data file was not found: {DATA_PATH.name}")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("The data file is empty.")
    st.stop()
except pd.errors.ParserError:
    st.error("The data file could not be parsed as a valid CSV file.")
    st.stop()
except OSError as error:
    st.error(f"Could not read the data file: {error}")
    st.stop()


st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.subheader("Basic Dataset Information")

col_1, col_2, col_3 = st.columns(3)

col_1.metric("Total rows", f"{df.shape[0]:,}")
col_2.metric("Columns", df.shape[1])
col_3.metric(
    "Missing odometer values",
    f"{df['odometer'].isna().sum():,}",
)


show_filtered_data = st.checkbox(
    f"Show only vehicles with a known odometer below "
    f"{ODOMETER_LIMIT:,} miles"
)

if show_filtered_data:
    filter_mask = (
        df["odometer"].notna()
        & df["odometer"].lt(ODOMETER_LIMIT)
    )
    filtered_df = df.loc[filter_mask].copy()

    st.caption(
        "Rows with missing or invalid odometer values are excluded "
        "when this filter is enabled."
    )
else:
    filtered_df = df.copy()


st.metric(
    "Rows after filtering",
    f"{len(filtered_df):,}",
)

st.subheader("Filtered Dataset")
st.dataframe(filtered_df.head(), use_container_width=True)


st.subheader("Vehicle Price Distribution")

price_data = filtered_df.dropna(subset=["price"])

if price_data.empty:
    st.warning("There are no valid price values to display.")
else:
    fig_hist = px.histogram(
        price_data,
        x="price",
        nbins=50,
        title="Distribution of Vehicle Prices",
    )

    fig_hist.update_layout(
        xaxis_title="Price (USD)",
        yaxis_title="Number of vehicles",
    )

    st.plotly_chart(fig_hist, use_container_width=True)


st.subheader("Price vs Odometer")

scatter_data = filtered_df.dropna(
    subset=["price", "odometer"]
)

if scatter_data.empty:
    st.warning(
        "There are no valid price and odometer values "
        "to display."
    )
else:
    fig_scatter = px.scatter(
        scatter_data,
        x="odometer",
        y="price",
        title="Vehicle Price vs Odometer",
        opacity=0.5,
    )

    fig_scatter.update_layout(
        xaxis_title="Odometer (miles)",
        yaxis_title="Price (USD)",
    )

    st.plotly_chart(fig_scatter, use_container_width=True)