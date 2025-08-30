from xai_components.base import InArg, InCompArg, OutArg, Component, xai_component
import pandas as pd
import os

@xai_component
class CSVReader(Component):
    '''
    @xai_component: This decorator marks the class as a Xircuits component.
    InArg, InCompArg, and OutArg: These define the input and output ports for the component. InCompArg is used for compulsory inputs.
    execute method: This is where the main logic of the component is implemented.
    '''

    fileName: InCompArg[str]
    out: OutArg[dict]

    def execute(self, ctx) -> None:
        # Read the CSV file using pandas
        try:
            print("Current working directory:", os.getcwd())
            print(self.fileName.value)
            df = pd.read_csv(self.fileName.value)
            self.out.value = df.to_dict()
            print("CSV file read successfully!")
        except Exception as e:
            print(f"Error reading CSV file: {e}")



