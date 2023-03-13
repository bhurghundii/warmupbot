import pandas as pd

class DataReader:
    def load_data_source(self, path: str, file_name: str):
        pass

class CSVReader(DataReader):
    def load_data_source(self, path: str, file_name: str):
        return pd.read_csv(path + file_name)
