import pandas as pd
import geopandas as gpd
import folium
import os

# Load the updated dataset
file_path = r'C:\Users\Akshay\Desktop\pyhtonCA\updated_dataset.csv'
df = pd.read_csv(file_path)

# Drop rows where country code or species is missing
df_geo = df.dropna(subset=['countryCode', 'scientificName'])

# Load the built-in world map (low-resolution dataset)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge species data with the world map based on the country code
merged = world.merge(df_geo, left_on='iso_a2', right_on='countryCode', how='inner')

# Create a Folium map centered around a global location
m = folium.Map(location=[20, 0], zoom_start=2)

# Function to visualize each country where a species was found
for _, row in merged.iterrows():
    species = row['scientificName']
    country_name = row['name']  # Country name from world dataset

    # Add a marker for each country with species found
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],  # Country center
        popup=f"{species} found in {country_name}",
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(m)

# Define the path where the HTML file will be saved
output_dir = r'C:\Users\Akshay\Desktop\pyhtonCA'
output_file = os.path.join(output_dir, 'species_distribution_map.html')

# Save the map to an HTML file
m.save(output_file)

print(f"Map has been saved as '{output_file}'. Open it in a browser to view the interactive map.")
