import os
import polars as pl
from .files_source import FilesDataSource

class JsonSource(FilesDataSource):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'json_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.json')]

        if new_files:
            print(f'New JSON files detected: {new_files}')
            self.previous_files = current_files
        else:
            print('No new JSON files detected')
            self.get_data()

    def get_data(self):
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pl.read_json(path)
                data_frames.append(data)
            except Exception as e:
                print("An error occurred while reading the JSON file:", e)
        if data_frames:
            self.combined_data = pl.concat(data_frames)
            return self.combined_data
        else:
            return None
