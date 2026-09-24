# Cognify Internship - Railway Data Engineering Report

## Dataset Summary
- Records: **11,113**
- Unique trains: **11,113**
- Unique source stations: **921**
- Unique destination stations: **924**
- Missing values after cleaning: **0**

## Data Cleaning
Text fields were trimmed and standardized to uppercase. The `days` field was
normalized by removing the trailing `D` found in values such as `MONDAYD`.
A `Service_Category` field was added for Weekday/Weekend classification.

## Key Findings
- Highest recorded day: **FRIDAY (1,649 records)**
- Lowest recorded day: **MONDAY (1,503 records)**
- Most common source: **CST-MUMBAI (513)**
- Most common destination: **CST-MUMBAI (514)**
- Most frequent recorded route: **TAMBARAM → CHENNAI BEACH (137)**

## Recommendations
1. Use day-wise counts for operational and timetable analysis.
2. Monitor high-volume source stations and routes.
3. Use the heatmap to identify day-specific concentration.
4. Combine timetable data with passenger demand, delays and cancellations
   before making real scheduling decisions.

## Assumption
Each row contains one operating-day value. Therefore this analysis describes
the distribution of records across days. Average trains per day is a simple
source-level record count divided by 7 and is not a verified timetable
frequency measure.
