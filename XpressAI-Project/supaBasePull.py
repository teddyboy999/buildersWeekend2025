# pull from SupaBase Test.py
from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component
from supabase import create_client, Client
import pandas as pd
import os

@xai_component
class supaBasePull(Component):
    '''
    @xai_component: This decorator marks the class as a Xircuits component.
    InArg, InCompArg, and OutArg: These define the input and output ports for the component. InCompArg is used for compulsory inputs.
    execute method: This is where the main logic of the component is implemented.
    '''

    tableName: InCompArg[str]
    out: OutArg[dict]
    
    def execute(self, ctx) -> None:
        # Supabase credentials
        SUPABASE_URL = 'https://hrluyuodioqpgcweprpn.supabase.co'  
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhybHV5dW9kaW9xcGdjd2VwcnBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxOTkyODQsImV4cCI6MjA1NTc3NTI4NH0.JRjGlqA75gyWelLVJdiDM_0-6Jxxnt46d8Bhm4BqXLg'      # DONT SHARE!!
        
        # Initialize Supabase client
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

        table_name = 'stock_data'
        output_file = 'xai_components/xai_myComponents/stock_data_export.csv'

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
            print(df)
    
            # Save to CSV
            df.to_csv(output_file, index=False)
            self.out.value = df.to_dict()
            print(f"Table '{table_name}' saved as '{output_file}'")
        except Exception as e:
            print(f"Error: {str(e)}")

