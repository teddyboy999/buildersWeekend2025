# push to SupaBase Test.py
from supabase import create_client, Client
import pandas as pd

# Supabase credentials
SUPABASE_URL = 'SECRET_URL'  # Replace with your URL
SUPABASE_KEY = 'SECRET_KEY'      # Replace with your key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

testCsvFile = "/Users/bhushithgh/University/BuildersWeekend2025/TestData/test_restock_data.csv"

# Function to upload CSV to Supabase table
def upload_csv_to_supabase(csv_file_path, table_name):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file_path)

        # Validate columns
        expected_columns = ['product_id', 'restock_date']
        if not all(col in df.columns for col in expected_columns):
            raise ValueError(f"CSV must contain columns: {', '.join(expected_columns)}")

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')

        # Insert data into Supabase table
        response = supabase.table(table_name).insert(data).execute()

        # Check for errors
        if hasattr(response, 'error') and response.error:
            raise Exception(response.error.message)

        print(f"Successfully uploaded {len(data)} rows to '{table_name}'")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    tableName = "predicted_restock_data"
    upload_csv_to_supabase(testCsvFile, tableName)



