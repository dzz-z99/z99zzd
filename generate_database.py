import os
import json
from datetime import datetime

# The folder containing your files
folder = "files"

# List to hold file details
files_list = []

# Walk through the files directory
for root, dirs, files in os.walk(folder):
    for file in files:
        # Get the full file path
        file_path = os.path.join(root, file)
        
        # Calculate the file size in MB
        size = os.path.getsize(file_path) / (1024 * 1024)
        
        # Get the last modified time (this will reflect the last commit date in GitHub)
        last_modified_time = os.path.getmtime(file_path)
        last_modified_date = datetime.utcfromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')

        # Append file details to the list
        files_list.append({
            "folder": root,
            "name": file,
            "path": file_path.replace("\\", "/"),  # Convert backslashes to slashes
            "lastModified": last_modified_date,  # Correctly naming the field
            "size": size  # Store size in MB for now
        })

# Write the list to a JSON file
with open("database.json", "w") as f:
    json.dump(files_list, f, indent=4)

print("database.json generated successfully!")
