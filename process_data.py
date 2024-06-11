import pandas as pd
import os

# Define the directory where the CSV files are located
data_dir = 'data'

# Define the list of CSV files
csv_files = ['data1.csv', 'data2.csv', 'data3.csv']

# Initialize an empty DataFrame to hold the combined data
combined_data = pd.DataFrame()

# Process each CSV file
for file in csv_files:
    file_path = os.path.join(data_dir, file)
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Filter for Pink Morsels
    df = df[df['product'] == 'Pink Morsel']
    
    # Calculate sales
    df['sales'] = df['quantity'] * df['price']
    
    # Select relevant columns
    df = df[['sales', 'date', 'region']]
    
    # Append to the combined DataFrame
    combined_data = combined_data.append(df, ignore_index=True)

# Save the combined data to a new CSV file
output_file = os.path.join(data_dir, 'processed_sales_data.csv')
combined_data.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
