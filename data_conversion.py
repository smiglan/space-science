import pandas as pd

# Load your CSV file
df = pd.read_csv(r'Meteorite Landings\Meteorite_Landings_20240430.csv')

# Selecting relevant columns for visualization
df = df[['name', 'id', 'mass (g)', 'year', 'reclat', 'reclong']]

# Handle missing values if necessary
df.dropna(inplace=True)

# Convert DataFrame to JSON
json_result = df.to_json(orient='records')

# Save the JSON output to a file
with open('data.js', 'w') as file:
    file.write('const meteoriteData = ')
    file.write(json_result)
    file.write(';')
