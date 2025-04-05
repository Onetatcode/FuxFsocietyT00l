### 5. **log_utils.py (logging functions)**
```python
import os
from datetime import datetime

def save_log(tool_name, content):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/{tool_name}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(content)