import json

def jsonToReadable(jsonFilename, readable_output):
    """take difficult to read file and change it to human readable"""
    with open(jsonFilename) as f:
        all_data = json.load(f)

    # create a file to write the data in a more readable format.
    with open(readable_output, 'w') as f:
        json.dump(all_data, f, indent=4)
