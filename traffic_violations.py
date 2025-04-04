# traffic_violations.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load sample traffic violation dataset (replace with your city dataset or use a public one)
data_url = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit=50000"
df = pd.read_csv(data_url)

# Preview the data
print(df[['violation_code', 'issue_date', 'vehicle_body_type', 'vehicle_make', 'violation_location', 'longitude', 'latitude']].head())

# Clean and prepare data
df['issue_date'] = pd.to_datetime(df['issue_date'], errors='coerce')
df = df.dropna(subset=['longitude', 'latitude'])

# Top 10 Violation Codes
top_violations = df['violation_code'].value_counts().head(10)
sns.barplot(x=top_violations.values, y=top_violations.index, palette='viridis')
plt.title('Top 10 Traffic Violation Codes')
plt.xlabel('Number of Violations')
plt.ylabel('Violation Code')
plt.tight_layout()
plt.savefig("top_violations.png")
plt.show()

# Violations by vehicle body type
top_bodies = df['vehicle_body_type'].value_counts().head(10)
sns.barplot(x=top_bodies.values, y=top_bodies.index, palette='coolwarm')
plt.title('Top Vehicle Body Types Involved in Violations')
plt.xlabel('Number of Violations')
plt.ylabel('Vehicle Body Type')
plt.tight_layout()
plt.savefig("top_body_types.png")
plt.show()

# Heatmap of violations
m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)  # NYC center
heat_data = [[row['latitude'], row['longitude']] for index, row in df.iterrows() if not pd.isnull(row['latitude']) and not pd.isnull(row['longitude'])]
HeatMap(heat_data[:1000]).add_to(m)
m.save("traffic_violation_heatmap.html")
print("Heatmap saved as traffic_violation_heatmap.html")
