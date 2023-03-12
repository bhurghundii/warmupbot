from data_reader import CSVReader
from output_data import OutputData
from config_enums import FileConfig

def generate_markdown():
    csv_reader = CSVReader()
    data_source_path = FileConfig.filePath.value
    data_source = FileConfig.dataSource.value
    data_frame = csv_reader.load_data_source(data_source_path, data_source)
    output_data = OutputData(data_frame)
    output_data.output_data()

if __name__ == "__main__":
    generate_markdown()