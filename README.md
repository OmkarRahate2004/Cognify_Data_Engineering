# 🚆 Railway Data Engineering & Analytics

A complete **Data Engineering and Analytics project** developed as part of the **Cognify Internship**. The project analyzes railway train information to identify journey patterns, source and destination trends, day-wise train operations, and route-level insights.

The project includes data cleaning, exploratory analysis, statistical summaries, visualization, and an interactive **Streamlit dashboard**.

---

## 📌 Project Overview

The objective of this project is to transform raw railway data into meaningful and interactive insights.

The analysis focuses on:

* Railway train information
* Source and destination stations
* Day-wise train operations
* Weekday vs weekend patterns
* Popular source stations
* Popular destination stations
* Frequently occurring routes
* Weekly journey patterns
* Interactive data visualization

---

## 🎯 Objectives

1. Load and inspect the railway dataset.
2. Clean and preprocess the raw data.
3. Analyze train operations by day.
4. Identify the most common source and destination stations.
5. Analyze source-station-wise train counts.
6. Study weekday and weekend patterns.
7. Analyze frequently occurring railway routes.
8. Generate meaningful visualizations.
9. Build an interactive Streamlit dashboard.
10. Provide data-driven insights for railway stakeholders.

---

## 📂 Dataset

The project uses a railway train information dataset containing:

| Column                     | Description                     |
| -------------------------- | ------------------------------- |
| `Train_No`                 | Unique train number             |
| `Train_Name`               | Name of the train               |
| `Source_Station_Name`      | Starting station                |
| `Destination_Station_Name` | Destination station             |
| `days`                     | Day on which the train operates |

### Dataset Statistics

* **Total records:** 11,113
* **Columns:** 5
* **Unique train numbers:** 11,113
* **Unique source stations:** 921
* **Unique destination stations:** 924
* **Missing values:** 0 in the original dataset

The `days` field was normalized during preprocessing to standard weekday names.

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Streamlit
* Git
* GitHub

---

## 📁 Project Structure

```text
Cognify_Railway_Data_Engineering/
│
├── Railway_info.csv
├── railway_analysis.py
├── dashboard.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── outputs/
    ├── cleaned_railway_data.csv
    ├── source_station_summary.csv
    ├── destination_station_summary.csv
    ├── day_summary.csv
    ├── route_summary.csv
    ├── day_distribution.png
    ├── top_source_stations.png
    ├── top_destination_stations.png
    ├── weekday_weekend.png
    ├── source_day_heatmap.png
    ├── top_routes.png
    └── railway_analysis_report.txt
```

---

## 🔄 Data Processing Workflow

```text
Raw Railway Dataset
        ↓
Data Loading
        ↓
Data Inspection
        ↓
Data Cleaning
        ↓
Day Normalization
        ↓
Station Name Standardization
        ↓
Feature Creation
        ↓
Statistical Analysis
        ↓
Visualization
        ↓
Interactive Dashboard
        ↓
Insights & Recommendations
```

---

## 🧹 Data Cleaning

The following preprocessing operations are performed:

* Duplicate records are removed.
* Station names are converted to uppercase.
* Leading and trailing spaces are removed.
* Missing text values are handled.
* Train numbers are converted to numeric format.
* Day names are normalized.
* A `Service_Category` feature is created.

The service category contains:

```text
Weekday
Weekend
```

---

## 📊 Analysis Performed

### 1. Basic Dataset Analysis

The project analyzes:

* Dataset shape
* Column names
* Data types
* Missing values
* Descriptive statistics
* Number of trains
* Unique stations

### 2. Day-wise Analysis

Train operations are analyzed across:

```text
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```

### 3. Source Station Analysis

The project identifies stations with high numbers of originating train records.

### 4. Destination Station Analysis

Destination stations are analyzed to identify frequently occurring endpoints.

### 5. Route Analysis

Source-destination combinations are grouped to identify frequently occurring railway routes.

### 6. Weekday vs Weekend

Train records are classified into:

* Weekday
* Weekend

This provides a simple comparison of railway service patterns.

---

## 📈 Visualizations

The project generates multiple visualizations, including:

* Day-wise train distribution
* Top source stations
* Top destination stations
* Weekday vs weekend distribution
* Source station × day heatmap
* Top railway routes

---

## 📊 Interactive Streamlit Dashboard

The project includes an interactive dashboard developed using **Streamlit**.

The dashboard provides:

* KPI cards
* Day filters
* Source station filters
* Day-wise charts
* Source station analysis
* Destination station analysis
* Route analysis
* Weekday/weekend analysis
* Source-day heatmap
* Filtered railway data
* CSV download functionality

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/OmkarRahate2004/Cognify_Data_Engineering.git
```

### Step 2: Open the Project

```bash
cd Cognify_Data_Engineering
```

### Step 3: Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

### Step 4: Activate Virtual Environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 6: Run Data Analysis

```powershell
python railway_analysis.py
```

This generates the cleaned dataset, summary files, visualizations, and analysis report inside the `outputs` folder.

### Step 7: Launch Streamlit Dashboard

```powershell
python -m streamlit run dashboard.py
```

The dashboard will normally be available at:

```text
http://localhost:8501
```

---

## 📌 Key Findings

The analysis identified:

* **11,113 railway records** in the dataset.
* **921 unique source stations**.
* **924 unique destination stations**.
* The dataset contains records across all seven days of the week.
* **Friday** has the highest number of train records in the normalized day-wise analysis.
* **CST-MUMBAI** is the most frequently occurring source station in the dataset.
* Source and destination station distributions show that train activity is concentrated around several frequently occurring railway stations.
* Route-level grouping helps identify commonly occurring source-destination combinations.

---

## 💡 Business & Operational Insights

The analysis can support railway stakeholders in:

* Understanding day-wise train activity.
* Identifying stations with high train-originating activity.
* Studying frequently occurring routes.
* Comparing weekday and weekend operations.
* Supporting timetable and resource analysis.
* Identifying areas requiring further investigation.
* Creating interactive reports for non-technical stakeholders.

---

## ⚠️ Analytical Note

The dataset contains a `days` field representing the operating day associated with each record.

The project treats the dataset records as the basis for day-wise descriptive analysis. Any calculation of average trains per day should therefore be interpreted as a dataset-level analytical measure rather than a verified timetable frequency unless the underlying timetable structure confirms that interpretation.

---

## 🚀 Future Enhancements

Possible future improvements include:

* Real-time railway API integration.
* Delay and punctuality analysis.
* Passenger demand prediction.
* Train occupancy analysis.
* Geographic route mapping.
* Advanced time-series forecasting.
* Machine learning-based demand prediction.
* Automated stakeholder reporting.
* Deployment of the dashboard to Streamlit Cloud.

---

## 👨‍💻 Author

**Omkar S. Rahate**

MCA – First Year
DY Patil International University, Pune

### Internship

**Cognify Internship – Data Engineering**

---

## 📜 License

This project is developed for educational and internship purposes.
