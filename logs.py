from pathlib import Path
from datetime import datetime
import re

def save_log(tool_name, content, verbose=True):
    # Ensure reports directory exists
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Sanitize tool name for filename
    safe_tool = re.sub(r'\W+', '_', tool_name.lower())
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = reports_dir / f"{safe_tool}_{timestamp}.txt"

    try:
        with filename.open("w", encoding="utf-8") as f:
            f.write(f"[Tool] {tool_name}\n")
            f.write(f"[Time] {timestamp}\n")
            f.write("=" * 40 + "\n\n")
            f.write(content)
        if verbose:
            print(f"[✓] Log saved to: {filename}")
    except Exception as e:
        print(f"[!] Failed to save log: {e}")
