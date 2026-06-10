# Vehicle Advertisement Dashboard

This project is a Streamlit web application for exploring a dataset of used vehicle advertisements in the US market.

The app allows users to view the dataset, explore basic information, filter vehicle advertisements, and visualize vehicle price patterns using interactive Plotly charts.

## Project Description

The application analyzes vehicle advertisement data from `vehicles_us.csv`.

It includes:

* a dataset preview;
* basic dataset information;
* a checkbox filter for vehicles with known odometer values below 100,000 miles;
* the number of records remaining after filtering;
* a histogram of vehicle prices;
* a scatter plot showing the relationship between price and odometer.

## Technologies Used

* Python
* Pandas
* Streamlit
* Plotly Express
* Jupyter Notebook

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
```

## Running the App Locally

1. Clone the repository and open the project folder.

```bash
git clone <https://github.com/aperever/triple-ten>
cd triple-ten
```

2. Create a virtual environment.

```bash
python -m venv .venv
```

3. Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

5. Run the Streamlit application.

```bash
python -m streamlit run app.py
```

6. Open the local URL displayed in the terminal, for example:

```text
http://localhost:10000
```

## Exploratory Data Analysis

The exploratory data analysis is available in:

```text
notebooks/EDA.ipynb
```

The notebook includes:

* initial data inspection;
* analysis and processing of missing values;
* data type validation;
* descriptive statistics;
* visual analysis of price, mileage, and model year.

## Deployed Application

The deployed app is available here:

https://triple-ten-ampg.onrender.com
