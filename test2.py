import pandas as pd

# Load the dataset
file_path = 'imdb_top_1000.csv'
data = pd.read_csv(file_path)

# Add a new column with id starting from 1
data.insert(0, 'id', range(1, len(data) + 1))

# Save the updated dataframe to a new csv file
updated_file_path = './new_imdb_top_1000.csv'
data.to_csv(updated_file_path, index=False)
