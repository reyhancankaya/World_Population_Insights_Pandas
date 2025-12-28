import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- STEP 1: **Initial Analysis with BRICS Countries** ---
# **Using Dictionaries to store raw data**
my_data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa", "Turkey", "Germany"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria", "Ankara", "Berlin"],
    "population": [214, 144, 1408, 1412, 60, 85, 83],
    "area": [8.51, 17.1, 3.28, 9.59, 1.22, 0.78, 0.35]
}

# **Converting Dictionary to Pandas DataFrame**
countries = pd.DataFrame(my_data)
countries.index = ["BR", "RU", "IN", "CH", "SA", "TR", "GE"]

# **Logic & Filtering: Countries with population > 100M and large area**
is_huge = countries["population"] > 100
is_large_area = countries["area"] > 2
selected_countries = countries[is_huge & is_large_area]

print("**Selected Large & Populous Countries:**")
print(selected_countries)

# **Visualization 1: Area vs Population (Scatter Plot)**
plt.scatter(countries["area"], countries["population"], s=countries["population"]*0.5, alpha=0.5)
plt.title("**Global Analysis: Area vs Population**")
plt.xlabel("Area (Million km2)")
plt.ylabel("Population (Millions)")
plt.grid(True)
plt.show()

# --- STEP 2: **Advanced Population Density Analysis** ---
# **Expanded data for more insights**
pop_data = {
    "country": ["China", "India", "United States", "Indonesia", "Brazil", "Turkey", "Germany"],
    "continent": ["Asia", "Asia", "Americas", "Asia", "Americas", "Europe", "Europe"],
    "population": [1412, 1408, 331, 273, 214, 85, 83],
    "area": [9.59, 3.28, 9.83, 1.90, 8.51, 0.78, 0.35]
}

df = pd.DataFrame(pop_data)
df.index = ["CH", "IN", "US", "ID", "BR", "TR", "GE"]

# **Filtering European countries with less than 100M population**
# **Logic:** (continent == 'Europe') **AND** (population < 100)
europe_small = df[(df["population"] < 100) & (df["continent"] == "Europe")]
print("\n**Small Population European Countries:**")
print(europe_small)

# **Loops: Calculating Population Density using iterrows()**
# **Formula:** density = population / area
for lab, row in df.iterrows():
    density = row["population"] / row["area"]
    df.loc[lab, "density"] = density

print("\n**Final DataFrame with Density Analysis:**")
print(df)

# **Visualization 2: Population Density (Bar Chart)**
plt.figure(figsize=(10, 6))
plt.bar(df["country"], df["density"], color='salmon')
plt.title("**Population Density by Country (People per km²)**")
plt.xlabel("Countries")
plt.ylabel("Density (Population/Area)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- STEP 4: Advanced Visualization with Seaborn ---
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Subplot 1: Population by Country (Categorized by Continent)
plt.subplot(1, 2, 1)
sns.barplot(data=df, x="country", y="population", hue="continent")
plt.title("**Population by Continent (2025)**")
plt.xticks(rotation=45)

# Subplot 2: Population Density Comparison
plt.subplot(1, 2, 2)
sns.barplot(data=df, x="country", y="density", palette="viridis")
plt.title("**Population Density Analysis**")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
