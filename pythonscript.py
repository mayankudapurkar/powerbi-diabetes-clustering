from sklearn.cluster import KMeans
import pandas as pd

# Copy dataset from Power BI
df = dataset.copy()

#  Select the features for clustering
features = df[['Glucose', 'BMI']].fillna(0)

# Run K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(features)

#  Create a DataFrame for centroids
centroids = pd.DataFrame(
    kmeans.cluster_centers_,
    columns=['Glucose', 'BMI']
)
centroids['Cluster'] = centroids.index
centroids['Centroid'] = 1   # mark as centroid

# Mark normal rows
df['Centroid'] = 0

# Keep only needed columns
df_out = df[['Glucose', 'BMI', 'Cluster', 'Centroid']]
centroids_out = centroids[['Glucose', 'BMI', 'Cluster', 'Centroid']]

# Combine patients + centroids into SAME table
output = pd.concat([df_out, centroids_out], ignore_index=True)
