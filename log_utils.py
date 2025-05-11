import os
from datetime import datetime
from pathlib import Path
import re

def save_log(tool_name, content, verbose=True):
    # Create reports directory if it doesn't exist
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Clean tool name for filename safety
    safe_tool = re.sub(r'\W+', '_', tool_name.lower())
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = reports_dir / f"{safe_tool}_{timestamp}.txt"

    # Write formatted content to file
    try:
        with filename.open("w", encoding="utf-8") as f:
            f.write(f"=== Log from {tool_name} ===\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write("="*40 + "\n\n")
            f.write(content)
        if verbose:
            print(f"[+] Log saved to: {filename}")
    except Exception as e:
        print(f"[!] Failed to save log: {e}")
