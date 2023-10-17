# JSON Key Checker

This script checks JSON objects for the presence of required keys and empty values. It helps ensure that the specified keys are present and not empty, based on the provided JSON data. The script is useful for validating JSON data integrity and identifying missing or empty key fields.

## Requirements

- `json` module

## Usage

1. Clone the repository or download the script.
2. Ensure that the JSON data file is correctly formatted.
3. Run the script by executing the following command:

    ```
    py main.py
    ```

4. Input the JSON file path as prompted.

5. The script will analyze the JSON data and generate a report, `missing.json` containing information about any missing or empty keys.

## Customization

You can customize the list of required keys in the script by updating the `required_keys` variable.

## Note

Ensure that the JSON file follows the expected structure for accurate analysis. Verify the accuracy of the generated `missing.json` report to address any identified issues with the JSON data.