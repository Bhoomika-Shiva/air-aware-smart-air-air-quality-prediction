 # =====================================================
# AIRAWARE SMART - FINAL MILESTONE
# AQI Prediction Dashboard using Streamlit
# =====================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# 1. PAGE TITLE
# -----------------------------------------------------

st.title("🌍 AirAware Smart Dashboard")
st.write("Air Quality Prediction System")

# -----------------------------------------------------
# 2. SAMPLE AQI DATA
# -----------------------------------------------------

data = {
    "Date": [
        "2024-01-11",
        "2024-01-12",
        "2024-01-13",
        "2024-01-14",
        "2024-01-15"
    ],

    "Predicted_AQI": [85,120,175,220,45]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------------------------------
# 3. AQI CATEGORY FUNCTION
# -----------------------------------------------------

def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"

df["Category"] = df["Predicted_AQI"].apply(get_aqi_category)

# -----------------------------------------------------
# 4. ALERT SYSTEM
# -----------------------------------------------------

def generate_alert(aqi):

    if aqi > 200:
        return "🚨 HIGH ALERT! Avoid outdoor activities"

    elif aqi > 150:
        return "⚠ Warning! Wear a mask outside"

    elif aqi > 100:
        return "⚠ Moderate pollution"

    else:
        return "✅ Air quality is safe"

df["Alert"] = df["Predicted_AQI"].apply(generate_alert)

# -----------------------------------------------------
# 5. SHOW GRAPH
# -----------------------------------------------------

st.subheader("📊 Predicted AQI Trend")

fig, ax = plt.subplots()

ax.plot(df["Date"], df["Predicted_AQI"], marker="o")

ax.set_title("Predicted AQI Trend")

ax.set_xlabel("Date")

ax.set_ylabel("AQI Level")

plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------------------------------
# 6. SHOW LATEST AQI
# -----------------------------------------------------

latest_aqi = df["Predicted_AQI"].iloc[-1]

st.subheader("Predicted AQI (Next Day)")

st.write(round(latest_aqi))

# -----------------------------------------------------
# 7. AQI CATEGORY
# -----------------------------------------------------

category = get_aqi_category(latest_aqi)

st.subheader("AQI Category")

st.write(category)

# -----------------------------------------------------
# 8. ALERT MESSAGE
# -----------------------------------------------------

if latest_aqi > 200:

    st.error("🚨 HIGH ALERT! Avoid outdoor activities")

elif latest_aqi > 150:

    st.warning("⚠ Warning! Wear a mask outside")

elif latest_aqi > 100:

    st.warning("⚠ Moderate pollution")

else:

    st.success("✅ Air quality is safe")

# -----------------------------------------------------
# 9. SHOW DATA TABLE
# -----------------------------------------------------

st.subheader("Historical AQI Data")

st.write(df)