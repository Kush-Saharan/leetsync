import json
import os

STATE_FILE = ".synced.json"


def load_last_synced():
    if not os.path.exists(STATE_FILE):
        return None

    with open(STATE_FILE, "r") as f:
        data = json.load(f)

    return data.get("last_synced_id")


def save_last_synced(submission_id):
    data = {
        "last_synced_id": submission_id
    }

    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=4)
