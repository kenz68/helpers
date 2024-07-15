import os


def rename_files_in_folder(folder_path, old_string, new_string):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Loop through all files in the folder
    for filename in files:
        # Check if the file contains the old_string
        if old_string in filename:
            # Form the new filename by replacing the old_string with the new_string
            new_filename = filename.replace(old_string, new_string)

            # Get the full paths of the old and new filenames
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')


# Example usage
folder_path = 'D:\\cp\\working\\CP-QRCode-API\\src\\CPAPI.Script\\Migrations\\002'
old_string = '.StoredProcedure.'
new_string = '.'

rename_files_in_folder(folder_path, old_string, new_string)
