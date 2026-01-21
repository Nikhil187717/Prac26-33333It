import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ----------------------------------
# Step 1: Simulate Sensor Data
# ----------------------------------
temperature = []
humidity = []

for i in range(60):
    # Normal sensor readings
    if random.random() < 0.85:
        temperature.append(random.uniform(25, 35))
        humidity.append(random.uniform(40, 60))
    # Anomalous readings (fault / environment change)
    else:
        temperature.append(random.uniform(45, 55))
        humidity.append(random.uniform(10, 20))

data = pd.DataFrame({
    "Temperature": temperature,
    "Humidity": humidity
})

print("Sample Sensor Data:")
print(data.head())

# ----------------------------------
# Step 2: Feature Scaling
# ----------------------------------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# ----------------------------------
# Step 3: Apply K-Means Clustering
# ----------------------------------
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

data["Cluster"] = clusters

# ----------------------------------
# Step 4: Detect Anomalies
# ----------------------------------
# Distance from cluster center
distances = np.linalg.norm(
    scaled_data - kmeans.cluster_centers_[clusters],
    axis=1
)

threshold = np.percentile(distances, 90)  # top 10% as anomalies
data["Anomaly"] = distances > threshold

print("\nDetected Anomalies:")
print(data[data["Anomaly"] == True])

# ----------------------------------
# Step 5: Visualization
# ----------------------------------
plt.figure()
plt.scatter(
    data["Temperature"],
    data["Humidity"],
    c=data["Cluster"],
    label="Clusters"
)

# Highlight anomalies
plt.scatter(
    data[data["Anomaly"]]["Temperature"],
    data[data["Anomaly"]]["Humidity"],
    marker='x',
    label="Anomaly"
)

plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Sensor Data Clustering with Anomaly Detection")
plt.legend()
plt.tight_layout()
plt.show()

#Libraries required
#Unsupervised learning techniques like clustering group normal sensor behavior, while data points far from clusters are detected as anomalies.
