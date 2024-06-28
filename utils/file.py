import os
import json

def read_json_file():
    # Define the folder and file paths
    filename='result.json'
    folder_path = os.path.join(os.getcwd(), 'output')
    file_path = os.path.join(folder_path, filename)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"The file {file_path} is not a valid JSON.")
        return None

def write_dict_to_json(data, filename='result.json'):
    # Define the folder and file paths
    folder_path = os.path.join(os.getcwd(), 'output')
    file_path = os.path.join(folder_path, filename)
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")
    
    # Write the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Dictionary written to '{file_path}'.")

# Example dictionary to write to JSON
example_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
