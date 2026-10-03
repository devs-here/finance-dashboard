# Finance Dashboard

A simple personal finance dashboard built with **Streamlit**. Upload your income and expense data (CSV or Excel) and see where your money goes.

🚀 **Live Demo:** [Open the app](https://finance-dashboard-gaurav.streamlit.app)

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


<img width="1808" height="853" alt="Screenshot 2026-10-03 172545" src="https://github.com/user-attachments/assets/e550a35e-3b46-4651-a843-4bdb8e748a28" />
<img width="1782" height="682" alt="Screenshot 2026-10-03 172558" src="https://github.com/user-attachments/assets/a6426d3a-aadf-4f17-8119-1238a6fb1bf0" />


## Author

Built by [Gaurav](https://github.com/devs-here) as part of my data science learning journey.
