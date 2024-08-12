import os
import json
from datetime import datetime

folder = "files"
files_list = []

for root, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path) / (1024 * 1024)  # size in MB
        last_modified = datetime.utcfromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

        files_list.append({
            "folder": root,
            "name": file,
            "path": file_path,
            "lastModified": last_modified,
            "size": round(size, 2)
        })

with open("database.json", "w") as f:
    json.dump(files_list, f, indent=4)
