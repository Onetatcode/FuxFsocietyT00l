from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
import time

def loading_bar(task_name="Initializing fsociety...", total=100, speed=0.1):
    """
    Display a loading bar with enhanced visuals and smooth animations.

    Args:
        task_name (str): Name or description of the task.
        total (int): Total value representing the progress.
        speed (float): Speed at which the task advances (in seconds).
    """
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None, complete_style="bold green", finished_style="bold yellow"),
        TimeRemainingColumn(style="dim"),
        transient=True
    ) as progress:

        task = progress.add_task(f"[cyan]{task_name}", total=total)

        # Update the progress bar, with smoother animation
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(speed)

        # Print a completion message after the task finishes
        progress.console.print(f"\n[bold green]Task '{task_name}' completed successfully![/bold green]\n")

if __name__ == "__main__":
    loading_bar("Setting up fsociety tools...", total=50, speed=0.05)
