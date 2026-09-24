# Cognify Internship - Railway Data Engineering

## Run
```bash
pip install -r requirements.txt
python railway_analysis.py
streamlit run dashboard.py
```

## Included
- Level 1: loading, inspection, statistics, missing-value handling, station standardization
- Level 2: Saturday filtering, source filtering, grouping, average-per-day metric, weekday/weekend enrichment
- Level 3: weekly pattern analysis, source/destination patterns, route analysis, heatmap
- Level 4: professional PNG charts, CSV outputs, Markdown report and interactive Streamlit dashboard

## Data note
The supplied `days` column contains variants such as `Mondayd`. The trailing `d` is normalized to the weekday.
