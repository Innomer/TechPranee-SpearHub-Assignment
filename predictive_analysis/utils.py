import os

def save_file(file, upload_folder):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, 'sample.csv')
    file.save(file_path)
    return file_path