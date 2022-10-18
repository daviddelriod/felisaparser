import pandas as pd
class parser:
    def __init__(self, path):
        self.path = path

    def excel_to_csv(self):
        df = pd.read_excel(self.path)
        df.to_csv(str(self.path[:-5])+'.csv', index=False)
        print("Done!")