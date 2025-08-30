# pull from SupaBase Test.py
from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component
from supabase import create_client, Client
import pandas as pd
import os

@xai_component
class supaBasePush(Component):
    '''
    @xai_component: This decorator marks the class as a Xircuits component.
    InArg, InCompArg, and OutArg: These define the input and output ports for the component. InCompArg is used for compulsory inputs.
    execute method: This is where the main logic of the component is implemented.
    '''

    csvFile: InCompArg[str]
    tableName: InCompArg[str]
    
    def execute(self, ctx) -> None:
        # Supabase credentials
        SUPABASE_URL = 'https://hrluyuodioqpgcweprpn.supabase.co'  # Replace with your URL
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhybHV5dW9kaW9xcGdjd2VwcnBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxOTkyODQsImV4cCI6MjA1NTc3NTI4NH0.JRjGlqA75gyWelLVJdiDM_0-6Jxxnt46d8Bhm4BqXLg'      # Replace with your key
        
        # Initialize Supabase client
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

        csv_file_path = "readingCSVTest/test_restock_data_2.csv"
        table_name = "predicted_restock_data"
        
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

