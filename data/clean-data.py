import pandas as pd

def clean_data(file_path):
    # Load the data into a DataFrame
    df = pd.read_csv(file_path, sep='|', header=None, names=[
        'id', 'datetime', 'city', 'state', 'country', 'shape', 'duration_seconds', 
        'duration_hours_min', 'comments', 'date_posted', 'latitude', 'longitude'
    ])

    # Display the first few rows of the dataset
    print("Initial Data:")
    print(df.head())

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna({
        'state': 'unknown',
        'country': 'unknown',
        'shape': 'unknown',
        'duration_seconds': 0,
        'duration_hours_min': 'unknown',
        'comments': 'No comments',
        'latitude': 0.0,
        'longitude': 0.0
    }, inplace=True)

    # Convert 'datetime' and 'date_posted' to datetime objects
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')

    # Convert 'duration_seconds' to numeric, setting errors to NaN
    df['duration_seconds'] = pd.to_numeric(df['duration_seconds'], errors='coerce').fillna(0)

    # Display the cleaned data
    print("Cleaned Data:")
    print(df.head())

    # Save the cleaned data to a new file
    df.to_csv('cleaned_data.csv', index=False)

# Example usage
clean_data('data/ufo-scrubbed-geocoded-time-standardized.csv')
