Problem Statement: Customer Segmentation for Targeted Marketing
Context: A company's marketing department aims to optimize its promotional strategies by moving away from a 'one-size-fits-all' approach. The provided dataset contains detailed customer profiles, including demographics, spending habits across various product categories (wine, meat, fruits, etc.), and responses to previous marketing campaigns.

The Problem: How can the company effectively categorize its diverse customer base into distinct groups (segments) based on shared traits and behaviors? Without clear segmentation, the company risks wasting resources on irrelevant marketing materials and failing to engage specific high-value or niche customer groups.

Objective:

Identify Segments: Use unsupervised machine learning (K-Means Clustering) to group customers based on features like income, age, total spending, and purchase frequency.
Profile Clusters: Define the characteristics of each group (e.g., 'High-Value Spenders' vs. 'Budget-Conscious Families').
Actionable Insights: Provide data-driven recommendations for the marketing team to tailor campaigns for each specific segment, thereby increasing the Return on Investment (ROI) and customer engagement.

_______________________________________________________________________________________________________________________________________________________________________________________________________________
Based on the cluster analysis of your marketing campaign dataset, here is a summary of the three distinct customer segments identified:

<img width="863" height="470" alt="download" src="https://github.com/user-attachments/assets/31acc7c2-cd77-4f52-90d9-fc1d80016400" />


<img width="844" height="624" alt="download" src="https://github.com/user-attachments/assets/24963f41-feba-49c9-bb96-9107c2d5811b" />


Cluster Analysis Summary
Segment 1: High-Value Spenders (Cluster 0)

Profile: Affluent customers with the highest average income (~$78k).
Behavior: They are the biggest spenders, particularly on wines and meat. They shop frequently across all channels, especially catalogs and the web.
Family: Mostly households with few or no children.
Segment 2: Budget-Conscious Families (Cluster 1)

Profile: Customers with the lowest average income (~$35k).
Behavior: They have the lowest overall spending and make fewer purchases. They likely prioritize essentials and are sensitive to prices.
Family: This group has the highest average number of children (over 1.2 per household).
Segment 3: Middle-Market Shoppers (Cluster 2)

Profile: Middle-income earners (~$57k).
Behavior: They show moderate spending habits. Interestingly, they make a high total number of purchases (comparable to the high-value group) but at a lower total cost, suggesting frequent, value-driven shopping.
Family: Typically have one or more children at home.
Key Process Steps:
Preprocessing: Handled missing income values and converted birth years into 'Age'.
Feature Engineering: Created aggregate metrics like 'TotalSpending' and 'TotalPurchases'.
Clustering: Used K-Means clustering (K=3) validated by the Elbow Method and Silhouette scores.
Visualization: Applied PCA (Principal Component Analysis) to visualize the distinct separation between these groups in a 2D space.
