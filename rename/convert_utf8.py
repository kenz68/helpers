import os
import chardet


def convert_to_utf8(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for filename in files:
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Read the file and detect its encoding
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            original_encoding = result['encoding']

        # Skip if the encoding is already UTF-8
        if original_encoding.lower() == 'utf-8':
            print(f'Skipping {filename}, already UTF-8.')
            continue

        # Read the file with the detected encoding
        with open(file_path, 'r', encoding=original_encoding) as file:
            content = file.read()

        # Write the file back in UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f'Converted {filename} to UTF-8.')


# Example usage
# folder_path = 'D:\\cp\\working\\CP-QRCode-API\\src\\CPAPI.Script\\Migrations\\002'
folder_path = 'D:\\cp\\working\\CP-QRCode-API\\src\\CPAPI.Script\\StoreProcedures'
convert_to_utf8(folder_path)

