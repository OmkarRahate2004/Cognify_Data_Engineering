import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Cognify Railway Intelligence", page_icon="🚆", layout="wide")
DAY_ORDER = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

@st.cache_data
def load_data():
    df = pd.read_csv("Railway_info.csv")
    for c in ["Train_Name","Source_Station_Name","Destination_Station_Name","days"]:
        df[c] = df[c].fillna("UNKNOWN").astype(str).str.strip().str.upper()
    df["days"] = df["days"].str.replace(r"D$", "", regex=True)
    df["days"] = pd.Categorical(df["days"], categories=DAY_ORDER, ordered=True)
    df["Service_Category"] = np.where(df["days"].isin(["SATURDAY","SUNDAY"]), "Weekend", "Weekday")
    return df

df = load_data()
st.title("🚆 Cognify Railway Intelligence Dashboard")
st.caption("Data Engineering Internship | Exploration • Transformation • Advanced Analysis • Reporting")

st.sidebar.header("Filters")
days = st.sidebar.multiselect("Operating Days", DAY_ORDER, default=DAY_ORDER)
sources = st.sidebar.multiselect("Source Stations", sorted(df["Source_Station_Name"].unique()), default=[])
filtered = df[df["days"].isin(days)].copy()
if sources:
    filtered = filtered[filtered["Source_Station_Name"].isin(sources)]

a,b,c,d = st.columns(4)
a.metric("Train Records", f"{len(filtered):,}")
b.metric("Unique Trains", f"{filtered['Train_No'].nunique():,}")
c.metric("Source Stations", f"{filtered['Source_Station_Name'].nunique():,}")
d.metric("Destination Stations", f"{filtered['Destination_Station_Name'].nunique():,}")

st.divider()

day_counts = filtered["days"].value_counts().reindex(DAY_ORDER, fill_value=0).rename_axis("Day").reset_index(name="Train_Count")
st.subheader("📊 Weekly Operating Pattern")
st.plotly_chart(px.bar(day_counts, x="Day", y="Train_Count", text="Train_Count", title="Train Records by Day"), use_container_width=True)

l,r = st.columns(2)
with l:
    x = filtered["Source_Station_Name"].value_counts().head(15).sort_values().rename_axis("Station").reset_index(name="Train_Count")
    st.plotly_chart(px.bar(x, x="Train_Count", y="Station", orientation="h", title="Top 15 Source Stations"), use_container_width=True)
with r:
    x = filtered["Destination_Station_Name"].value_counts().head(15).sort_values().rename_axis("Station").reset_index(name="Train_Count")
    st.plotly_chart(px.bar(x, x="Train_Count", y="Station", orientation="h", title="Top 15 Destination Stations"), use_container_width=True)

st.subheader("🔥 Source Station × Operating Day")
top20 = filtered["Source_Station_Name"].value_counts().head(20).index
heat = filtered[filtered["Source_Station_Name"].isin(top20)].groupby(["Source_Station_Name","days"], observed=True).size().unstack(fill_value=0).reindex(columns=DAY_ORDER, fill_value=0)
st.plotly_chart(px.imshow(heat, text_auto=True, aspect="auto", labels={"x":"Day","y":"Source Station","color":"Train Count"}, title="Operating Concentration by Station and Day"), use_container_width=True)

st.subheader("🛤️ Most Frequent Routes")
routes = filtered.groupby(["Source_Station_Name","Destination_Station_Name"]).size().reset_index(name="Train_Count").sort_values("Train_Count", ascending=False).head(15)
routes["Route"] = routes["Source_Station_Name"] + " → " + routes["Destination_Station_Name"]
st.plotly_chart(px.bar(routes.sort_values("Train_Count"), x="Train_Count", y="Route", orientation="h", title="Top 15 Source-Destination Routes"), use_container_width=True)

st.subheader("🗓️ Weekday vs Weekend")
cat = filtered["Service_Category"].value_counts().rename_axis("Category").reset_index(name="Train_Count")
st.plotly_chart(px.pie(cat, names="Category", values="Train_Count", hole=.45, title="Service Category Distribution"), use_container_width=True)

st.subheader("🔎 Filtered Data Preview")
st.dataframe(filtered.head(100), use_container_width=True)
st.download_button("⬇️ Download Filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_railway_data.csv", "text/csv")
st.info("Data note: the supplied file has one operating-day value per record, so the dashboard describes the recorded service-day distribution.")
