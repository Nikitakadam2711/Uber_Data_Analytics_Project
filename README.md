# Uber Data Analytics Project

## Project Overview

This project analyzes Uber ride data using Python and SQL.

The main objective is to identify ride patterns, peak hours, revenue trends, and perform fare prediction using Machine Learning.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- Scikit-Learn
- Jupyter Notebook
- VS Code

---

## Project Structure

```text
Uber_Analytics_Project/
│
├── data/
│   ├── uber.csv
│   └── cleaned_uber_data.csv
│
├── notebooks/
│   └── uber_analysis.ipynb
│
├── sql/
│   ├── uber.db
│   └── uber_queries.sql
│
├── dashboard/
│
├── images/
│
└── README.md
```

---

## Data Cleaning

The following data cleaning operations were performed:

- Removed missing values
- Removed duplicate records
- Converted datetime columns
- Created new features:
  - Hour
  - Day
  - Month
  - Year

---

## Exploratory Data Analysis

Analysis performed:

- Total Ride Analysis
- Average Fare Analysis
- Maximum Fare Analysis
- Minimum Fare Analysis
- Peak Hour Analysis
- Day Wise Ride Analysis
- Monthly Revenue Analysis
- Fare Distribution Analysis
- Correlation Analysis

---

## SQL Analysis

SQL queries were used to calculate:

- Total Rides
- Average Fare
- Maximum Fare
- Minimum Fare
- Total Revenue
- Peak Ride Hours
- Monthly Revenue

---

## Machine Learning

Model Used:

- Linear Regression

Target Variable:

- Fare Amount

Features Used:

- Hour
- Month

Evaluation Metrics:

- Mean Absolute Error (MAE)
- R² Score

---

## Results

Key insights obtained:

- Identified peak ride hours
- Analyzed monthly revenue trends
- Studied fare distribution patterns
- Predicted fare amount using Machine Learning

---

## Future Improvements

- Power BI Dashboard
- Interactive Reporting
- Advanced Machine Learning Models
- Demand Forecasting

---

## Author

Data Analytics Project created using Python, SQL, and Machine Learning.

1. Peak ride demand observed during specific hours.
2. Revenue distribution varied across months.
3. Average fare remained stable.
4. Ride activity showed day-wise patterns.