import json
import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.trailnote_log.json")

def save_log(image_path, guesses):
    logs = get_logs()
    
    entry = {
        "date": datetime.now().isoformat(),
        "image": os.path.basename(image_path),
        "guesses": guesses
    }
    
    logs.append(entry)
    
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def get_logs():
    if not os.path.exists(LOG_FILE):
        return []
    
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
