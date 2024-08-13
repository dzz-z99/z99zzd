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
        
        # Get the creation time (when the file was originally created)
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

        # Append file details to the list
        files_list.append({
            "folder": root,
            "name": file,
            "path": file_path.replace("\\", "/"),  # Convert backslashes to slashes
            "created": creation_date,
            "size": round(size, 2)
        })

# Write the list to a JSON file
with open("database.json", "w") as f:
    json.dump(files_list, f, indent=4)

print("database.json generated successfully!")
