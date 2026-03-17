# =====================================================
# AIRAWARE SMART - MILESTONE 3 DEMO
# AQI Category Classification + Alert System
# =====================================================

import pandas as pd
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from prophet import Prophet

# -----------------------------------------------------
# 1. SAMPLE PREDICTED AQI DATA (from ML model)
# -----------------------------------------------------

data = {
    "Date": [
        "2024-01-11",
        "2024-01-12",
        "2024-01-13",
        "2024-01-14",
        "2024-01-15"
    ],
    
    "Predicted_AQI": [85, 120, 175, 220, 45]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

print("Predicted AQI Data:")
print(df)

# -----------------------------------------------------
# 2. FUNCTION TO CLASSIFY AQI CATEGORY
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

# -----------------------------------------------------
# 3. APPLY CATEGORY FUNCTION
# -----------------------------------------------------

df["Category"] = df["Predicted_AQI"].apply(get_aqi_category)

print("\nAQI with Categories:")
print(df)

# -----------------------------------------------------
# 4. ALERT SYSTEM
# -----------------------------------------------------

def generate_alert(aqi):

    if aqi > 200:
        return "🚨 HIGH ALERT! Avoid outdoor activities."

    elif aqi > 150:
        return "⚠ Warning! Wear mask outside."

    elif aqi > 100:
        return "⚠ Moderate pollution. Sensitive people be careful."

    else:
        return "✅ Air quality is safe."

df["Alert"] = df["Predicted_AQI"].apply(generate_alert)

# -----------------------------------------------------
# 5. FINAL REPORT
# -----------------------------------------------------

print("\nFinal AirAware Alert Report:")
print(df)

# -----------------------------------------------------
# 6. VISUALIZATION
# -----------------------------------------------------

plt.figure()

plt.plot(df["Date"], df["Predicted_AQI"], marker="o")

plt.title("Predicted AQI Trend")

plt.xlabel("Date")

plt.ylabel("AQI Level")

plt.xticks(rotation=45)

plt.grid()

plt.show()