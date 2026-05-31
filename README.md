# Vehicle Advertisement Dashboard

This project is a Streamlit web application for exploring a dataset of used vehicle advertisements in the US market.

The app allows users to view the dataset, explore basic information, and visualize vehicle price patterns using interactive Plotly charts.

## Project Description

The application analyzes vehicle advertisement data from `vehicles_us.csv`.

It includes:

- a dataset preview;
- basic dataset information;
- a checkbox filter for vehicles with odometer values below 100,000 miles;
- a histogram of vehicle prices;
- a scatter plot showing the relationship between price and odometer.

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly Express
- Jupyter Notebook

## Project Structure

```text
triple-ten/
│
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
├── notebooks/
│   └── EDA.ipynb
└── .gitignore

## Deployed Application

The deployed app is available here:

https://triple-ten-ampg.onrender.com
