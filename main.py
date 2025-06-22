from time import sleep
from src.lib.classes.csv_source import CsvSource
from src.lib.classes.txt_source import TxtSource
# from lib.classes.excel_source import ExcelSource
# from lib.classes.json_source import JsonSource
# from lib.classes.parquet_source import ParquetSource

def check_for_new_files():
    csv_source.check_new_files()
    # excel_source.check_new_files()
    # json_source.check_new_files()
    # parquet_source.check_new_files()
    txt_source.check_new_files()

csv_source = CsvSource()
# excel_source = ExcelSource()
# json_source = JsonSource()
# parquet_source = ParquetSource()
txt_source = TxtSource()

if __name__ == "__main__":
    
    while True:
        check_for_new_files()
        sleep(2)
