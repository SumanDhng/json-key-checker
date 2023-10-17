import json

# List of keys to check for presence and emptiness
required_keys = ['customer_address','inv_dt','inv_total']

# Checks JSON objects for required keys and empty values
def check_json(json_obj, current_path="", file_name=""):
    missing_keys = []
    empty_keys = []

    # Check if the JSON object is a dictionary
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_path = f"{current_path}.{key}" if current_path else key
            
            # Check for required keys and empty values
            if key in required_keys:
                if not value:
                    empty_keys.append(key)
            elif key not in json_obj:
                missing_keys.append(key)
            
            # Extract the file name if available
            if key == "file_name" and not file_name:
                file_name = value
            
            # Recursive call to check nested JSON objects
            file_name, missing, empty = check_json(value, new_path,file_name)
            missing_keys.extend(missing)
            empty_keys.extend(empty)

    # Check if the JSON object is a list
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            new_path = f"{current_path}[{i}]"
            file_name, missing, empty = check_json(item, new_path,file_name)
            missing_keys.extend(missing)
            empty_keys.extend(empty)

    return file_name, missing_keys, empty_keys
if __name__ == "__main__":
    missing_info = []

    file_path = input("Enter the json file path: ")
    
    # Load JSON data from the file path provided
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Iterate through each JSON object and check for missing and empty keys
    for json_obj in json_data:
        file_name, missing_keys, empty_keys = check_json(json_obj)
        missing_keys = list(set(missing_keys)) # Remove duplicate missing keys
        empty_keys = list(set(empty_keys)) # Remove duplicate empty keys
        
        # Append information about missing and empty keys to a list
        if missing_keys or empty_keys:
            missing_info.append(
                {
                    "file_name": file_name,
                    "missing_keys": missing_keys,
                    "empty_keys": empty_keys
                }
            )

    # Dump the data of missing and empty keys to a JSON file
    with open('missing.json', 'w') as json_file:
        json.dump(missing_info,json_file,indent=4)