# pull from SupaBase Test.py
from supabase import create_client, Client
import pandas as pd

# Supabase credentials
SUPABASE_URL = 'SECRET_URL'  # Replace with your URL
SUPABASE_KEY = 'SECRET_KEY'      # Replace with your key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to pull table and save as CSV
def pull_table_to_csv(table_name, output_file):
    try:
        # Fetch all data from the table
        response = supabase.table(table_name).select('*').execute()

        # Check for errors
        if hasattr(response, 'error') and response.error:
            raise Exception(response.error.message)

        # Extract data
        data = response.data
        if not data:
            print(f"No data found in table '{table_name}'")
            return

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"Table '{table_name}' saved as '{output_file}'")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    pull_table_to_csv('stock_data', 'stock_data_export.csv')