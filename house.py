import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('extract_price.csv')

# Original DataFrame overview
print("Original Data Overview:")
print(data.head(15))
 
# Function to clean and extract price
def extract_price(price_str):
    price_str = price_str.replace('₹', '').strip()  # Remove ₹ symbol
    
    # Handle price ranges (e.g., '₹1.75 - 1.75 Cr')
    if '-' in price_str:
        price_range = price_str.split('-')
        # Take the average of the two prices in the range
        price_values = [convert_price(p.strip()) for p in price_range]
        return np.mean(price_values)
    else:
        # Single price value
        return convert_price(price_str)

# Function to convert the price from string to float considering "Cr" and "Lac"
def convert_price(price_str):
    if 'Cr' in price_str:
        # Convert Crores to numeric value
        return float(price_str.replace('Cr', '').replace(',', '').strip()) * 1e7
    elif 'Lac' in price_str:
        # Convert Lacs to numeric value
        return float(price_str.replace('Lac', '').replace(',', '').strip()) * 1e5
    else:
        # Handle prices without 'Cr' or 'Lac'
        return float(price_str.replace(',', '').strip())

# Apply the cleaning function to the Price column
data['Price'] = data['Price'].apply(extract_price)

# Function to clean and process the Area column
def clean_area(area_str):
    # Check if the area has a range like '1,880-1,884 sqft'
    if '-' in area_str:
        # Split the range, remove commas and convert to floats
        range_values = area_str.replace(' sqft', '').replace(',', '').split('-')
        # Average the two values
        area_value = (float(range_values[0]) + float(range_values[1])) / 2
    else:
        # Remove 'sqft' and commas, then convert to float
        area_value = float(area_str.replace(' sqft', '').replace(',', ''))
    return area_value

# Apply the cleaning function to the Area column
data['Area'] = data['Area'].apply(clean_area)

# Sort the data by Area for a more readable line plot
data = data.sort_values(by='Area')

# Display cleaned data (Price and Area)
print("\nCleaned Data - Price and Area:")
print(data[['Area', 'Price']])

# Plotting using Matplotlib - Line Plot for Area vs Price
plt.figure(figsize=(10,10))

# Line plot for Area vs Price
plt.plot(data['Area'], data['Price'], color='pink', linestyle='-', linewidth=2)

plt.title('House Price by Area')
plt.xlabel('Area (sqft)')
plt.ylabel('Price (₹)')
plt.grid(True)

plt.show()
