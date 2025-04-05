# progress.py
from rich.progress import Progress
import time

def loading_bar(task_name="Initializing fsociety..."):
    with Progress() as progress:
        task = progress.add_task(f"[purple]{task_name}", total=100)
        while not progress.finished:
            progress.update(task, advance=3)
            time.sleep(0.05)
