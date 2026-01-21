import time
import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Simulate Data Logging
# -------------------------------
timestamps = []
temperatures = []

print("Logging temperature data...\n")

for i in range(15):
    timestamps.append(datetime.now().strftime("%H:%M:%S"))
    temperatures.append(round(random.uniform(25, 35), 2))
    print(f"Time: {timestamps[-1]} | Temp: {temperatures[-1]} °C")
    time.sleep(0.5)

# -------------------------------
# Step 2: Create DataFrame
# -------------------------------
data = pd.DataFrame({
    "Time": timestamps,
    "Temperature": temperatures
})

# -------------------------------
# Step 3: Basic Data Analysis
# -------------------------------
print("\nBasic Analysis:")
print("Average Temperature:", data["Temperature"].mean())
print("Maximum Temperature:", data["Temperature"].max())
print("Minimum Temperature:", data["Temperature"].min())

# -------------------------------
# Step 4: Trend Visualization
# -------------------------------
plt.figure()
plt.plot(data["Time"], data["Temperature"], marker='o')
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Libraries Required
#pip install pandas matplotlib
