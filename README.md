# Finance Dashboard

A simple personal finance dashboard built with **Streamlit**. Upload your income and expense data (CSV or Excel) and see where your money goes.

## Features

- Upload your own data as **CSV or Excel**
- **Spend by category** chart and category breakdown table
- **Monthly income vs expense** bar chart
- **Running balance** over time
- Sample datasets included in `sample_data/` so you can try it right away

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- openpyxl

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/devs-here/finance-dashboard.git
cd finance-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python -m streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

On Windows you can also double-click `run.bat`.

## Try It With Sample Data

Upload any file from the `sample_data/` folder (for example `seed_data.csv`) to see the dashboard in action.

## Project Structure

```
finance-dashboard/
├── app.py            # Streamlit app
├── requirements.txt  # Python dependencies
├── run.bat           # One-click launcher (Windows)
└── sample_data/      # Example CSV files
```

## Screenshots

_Add a screenshot of the dashboard here._

## Author

Built by [Gaurav](https://github.com/devs-here) as part of my data science learning journey.
