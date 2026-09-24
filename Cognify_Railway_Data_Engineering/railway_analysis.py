# Cognify Internship Railway Analysis
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "Railway_info.csv"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)
DAY_ORDER = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
sns.set_theme(style="whitegrid", context="notebook")

df = pd.read_csv(DATA_PATH)
print("\nFIRST 10 ROWS")
print(df.head(10).to_string(index=False))
print("\nDATA TYPES")
print(df.dtypes)
print("\nMISSING VALUES BEFORE CLEANING")
print(df.isna().sum())

df = df.drop_duplicates().copy()
for c in ["Train_Name","Source_Station_Name","Destination_Station_Name","days"]:
    df[c] = df[c].fillna("UNKNOWN").astype(str).str.strip().str.upper()
df["days"] = df["days"].str.replace(r"D$", "", regex=True)
df["days"] = pd.Categorical(df["days"], categories=DAY_ORDER, ordered=True)
df["Service_Category"] = np.where(df["days"].isin(["SATURDAY","SUNDAY"]), "Weekend", "Weekday")

print("\nBASIC STATISTICS")
print("Number of train records:", len(df))
print("Unique trains:", df["Train_No"].nunique())
print("Unique source stations:", df["Source_Station_Name"].nunique())
print("Unique destination stations:", df["Destination_Station_Name"].nunique())
print("\nMost common source stations")
print(df["Source_Station_Name"].value_counts().head(10))
print("\nMost common destination stations")
print(df["Destination_Station_Name"].value_counts().head(10))

saturday = df[df["days"] == "SATURDAY"]
selected_station = df["Source_Station_Name"].value_counts().idxmax()
source_trains = df[df["Source_Station_Name"] == selected_station]
print("\nSATURDAY RECORDS:", len(saturday))
print("AUTO-SELECTED SOURCE:", selected_station)
print("RECORDS FROM SOURCE:", len(source_trains))

source_counts = df.groupby("Source_Station_Name").size().sort_values(ascending=False)
source_day = df.groupby(["Source_Station_Name","days"], observed=True).size().unstack(fill_value=0)
source_day = source_day.reindex(columns=DAY_ORDER, fill_value=0)
source_day["Average_Trains_Per_Day"] = source_day.sum(axis=1) / 7

df.to_csv(OUTPUT_DIR/"railway_cleaned.csv", index=False)
source_counts.rename("Train_Count").to_csv(OUTPUT_DIR/"source_station_counts.csv")
source_day.to_csv(OUTPUT_DIR/"source_average_trains_per_day.csv")

day_counts = df["days"].value_counts().reindex(DAY_ORDER, fill_value=0)
day_counts.rename("Train_Count").to_csv(OUTPUT_DIR/"day_wise_counts.csv")

# Day-wise plot
plt.figure(figsize=(10,6))
plt.bar(DAY_ORDER, day_counts.values)
plt.title("Railway Services by Day of Week", weight="bold")
plt.xlabel("Day"); plt.ylabel("Number of Train Records")
plt.xticks(rotation=25); plt.tight_layout()
plt.savefig(OUTPUT_DIR/"01_day_wise_distribution.png", dpi=180); plt.close()

# Top source stations
top = source_counts.head(15).sort_values()
plt.figure(figsize=(11,7))
plt.barh(top.index, top.values)
plt.title("Top 15 Source Stations by Train Count", weight="bold")
plt.xlabel("Number of Train Records"); plt.ylabel("Source Station")
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"02_top_source_stations.png", dpi=180); plt.close()

# Top destination stations
dest = df["Destination_Station_Name"].value_counts().head(15).sort_values()
plt.figure(figsize=(11,7))
plt.barh(dest.index, dest.values)
plt.title("Top 15 Destination Stations by Train Count", weight="bold")
plt.xlabel("Number of Train Records"); plt.ylabel("Destination Station")
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"03_top_destination_stations.png", dpi=180); plt.close()

# Weekday/weekend
cat = df["Service_Category"].value_counts()
plt.figure(figsize=(7,5))
plt.bar(cat.index, cat.values)
plt.title("Weekday vs Weekend Services", weight="bold")
plt.xlabel("Service Category"); plt.ylabel("Number of Train Records")
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"04_weekday_weekend.png", dpi=180); plt.close()

# Heatmap
top20 = source_counts.head(20).index
heat = df[df["Source_Station_Name"].isin(top20)].groupby(
    ["Source_Station_Name","days"], observed=True).size().unstack(fill_value=0)
heat = heat.reindex(columns=DAY_ORDER, fill_value=0).loc[top20[::-1]]
plt.figure(figsize=(12,9))
sns.heatmap(heat, annot=True, fmt="d", cmap="Blues")
plt.title("Train Operations: Top Source Stations vs Days", weight="bold")
plt.xlabel("Day of Week"); plt.ylabel("Source Station")
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"05_source_day_heatmap.png", dpi=180); plt.close()

# Routes
routes = df.groupby(["Source_Station_Name","Destination_Station_Name"]).size().reset_index(name="Train_Count")
routes = routes.sort_values("Train_Count", ascending=False)
routes.to_csv(OUTPUT_DIR/"all_route_counts.csv", index=False)
r = routes.head(15).copy()
r["Route"] = r["Source_Station_Name"] + " → " + r["Destination_Station_Name"]
r = r.sort_values("Train_Count")
plt.figure(figsize=(12,8))
plt.barh(r["Route"], r["Train_Count"])
plt.title("Top 15 Source-Destination Routes", weight="bold")
plt.xlabel("Number of Train Records"); plt.ylabel("Route")
plt.tight_layout(); plt.savefig(OUTPUT_DIR/"06_top_routes.png", dpi=180); plt.close()

print("\nAnalysis completed. Check the outputs folder.")
