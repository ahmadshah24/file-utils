import shutil
import os




def create_file(file_path):
    """
    Create a new file at the given file path.
    """
    with open(file_path, 'w') as file:
        pass

def copy_file(source, destination):
    """
    Copy a file from the source path to the destination path.
    """
    shutil.copy2(source, destination)

def move_file(source, destination):
    """
    Move a file from the source path to the destination path.
    """
    shutil.move(source, destination)

def rename_file(old_name, new_name):
    """
    Rename a file from the old name to the new name.
    """
    os.rename(old_name, new_name)

def delete_file(file_path):
    """
    Delete a file at the given file path.
    """
    os.remove(file_path)
