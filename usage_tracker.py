import os
from datetime import datetime

TRACKER_FILE = os.path.expanduser("~/.fsociety_tracker")

def notify():
    try:
        # Create the hidden tracker file if it doesn't exist
        if not os.path.exists(TRACKER_FILE):
            with open(TRACKER_FILE, 'w') as f:
                f.write("0")

        # Read current count
        with open(TRACKER_FILE, 'r') as f:
            count = int(f.read().strip())

        # Increment count
        count += 1

        # Overwrite with updated count
        with open(TRACKER_FILE, 'w') as f:
            f.write(str(count))

        # Optional: Save timestamped log
        with open("/fsociety/reports/usage.log", 'a') as log:
            log.write(f"[{datetime.now()}] Tool used {count} times\n")

    except Exception:
        pass  # Silently ignore all issues
