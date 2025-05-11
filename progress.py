from rich.console import Console
from rich.progress import Progress
import time

def loading_bar(task_name="Initializing fsociety..."):
    console = Console()

    # Create a Progress object with specific task
    with Progress() as progress:
        # Adding task without style argument
        task = progress.add_task(f"[purple]{task_name}", total=100)

        # Update the progress bar with a smooth transition
        while not progress.finished:
            progress.update(task, advance=3)
            time.sleep(0.05)

# Calling the function to show the progress bar
loading_bar()
