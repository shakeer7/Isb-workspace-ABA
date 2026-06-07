
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# 1. Load data
df = pd.read_csv('/content/marketing_campaign_Module 9_Data set.csv')

# 2. Preprocessing
df.dropna(subset=['Income'], inplace=True)
current_year = 2023
df['Age'] = current_year - df['Year_Birth']
df.drop(columns=['Masked_ID', 'Year_Birth'], inplace=True)

# 3. Feature Engineering & Encoding
df = pd.get_dummies(df, columns=['Education', 'Marital_Status'], drop_first=False)
df['TotalSpending'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
df['TotalPurchases'] = df['NumDealsPurchases'] + df['NumWebPurchases'] + df['NumCatalogPurchases'] + df['NumStorePurchases']
df['Children'] = df['Kidhome'] + df['Teenhome']
df.drop(columns=['Kidhome', 'Teenhome'], inplace=True)

# 4. Scaling
features_for_clustering = df.select_dtypes(include=['int64', 'float64', 'uint8']).columns.tolist()
X = df[features_for_clustering]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=features_for_clustering, index=df.index)

# 5. Clustering
k = 3
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled_df)

# 6. Visualization (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled_df)
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
pca_df['Cluster'] = df['Cluster']

# 7. Summary
cluster_summary = df.groupby('Cluster').mean(numeric_only=True)
print(cluster_summary)
