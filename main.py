from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import players_by_position
from football_dictionaries.assignment_3 import players_by_country_and_position

from rich.console import Console
from rich.table import Table
from rich.style import Style
import random
from typing import List, Dict, Any, Union

CONSOLE = Console()
COLORS = ["bright_blue", "bright_green", "bright_cyan", "bright_magenta", "bright_yellow", "bright_red"]

def get_random_color() -> str:
    """Returns a randomly chosen color from the defined list."""
    return random.choice(COLORS)

def _display_list_of_dicts(data: List[Dict[str, Any]]) -> None:
    """Displays a list of dictionaries as a colored table."""
    if not data:
        CONSOLE.print("[yellow]No data to display.[/yellow]")
        return

    keys = data[0].keys()
    table = Table(title="Data")
    column_styles = {key: get_random_color() for key in keys}
    for key in keys:
        table.add_column(key, style=column_styles[key])

    for item in data:
        row = [str(item.get(key, "")) for key in keys]
        table.add_row(*row)
    CONSOLE.print(table)

def _display_dict_of_lists(data: Dict[str, List[Dict[str, Any]]]) -> None:
    """Displays a dictionary where values are lists of dictionaries as colored tables."""
    if not data:
        CONSOLE.print("[yellow]No data to display.[/yellow]")
        return

    for category, items in data.items():
        if not items:
            CONSOLE.print(f"[bold magenta]{category}[/bold magenta]: [yellow]No data.[/yellow]")
            continue

        keys = items[0].keys()
        table = Table(title=f"[bold magenta]{category}[/bold magenta]")
        column_styles = {key: get_random_color() for key in keys}
        for key in keys:
            table.add_column(key, style=column_styles[key])

        for item in items:
            row = [str(item.get(key, "")) for key in keys]
            table.add_row(*row)
        CONSOLE.print(table)

def _display_nested_dict(data: Dict[str, Dict[str, Union[List[Dict[str, Any]], Any]]]) -> None:
    """Displays a nested dictionary as colored tables."""
    if not data:
        CONSOLE.print("[yellow]No data to display.[/yellow]")
        return

    for top_category, sub_data in data.items():
        CONSOLE.print(f"\n[bold green]{top_category}[/bold green]")
        for sub_category, items in sub_data.items():
            if isinstance(items, list) and items:
                keys = items[0].keys()
                table = Table(title=f"[magenta]{sub_category}[/magenta]")
                column_styles = {key: get_random_color() for key in keys}
                for key in keys:
                    table.add_column(key, style=column_styles[key])
                for item in items:
                    row = [str(item.get(key, "")) for key in keys]
                    table.add_row(*row)
                CONSOLE.print(table)
            elif not items:
                CONSOLE.print(f"[magenta]{sub_category}[/magenta]: [yellow]No data.[/yellow]")
            else:
                CONSOLE.print(f"[magenta]{sub_category}[/magenta]: [yellow]Unexpected data format.[/yellow]")

def display_as_table(data: Union[List[Dict[str, Any]], Dict[str, Any]]) -> None:
    """
    Displays a list of dictionaries or a dictionary (including nested) as colored tables
    with random colors for each column.

    Args:
        data (list or dict): The data to display.
                           If a list of dictionaries, each dictionary represents a row.
                           If a dictionary:
                             - If the values are lists of dictionaries, the keys are
                               treated as main categories.
                             - If the values are dictionaries themselves (and not lists),
                               the keys of the outer dictionary are top-level categories,
                               and the keys of the inner dictionaries are sub-categories
                               that will be displayed as separate tables.
    """
    if isinstance(data, list):
        _display_list_of_dicts(data)
    elif isinstance(data, dict):
        first_value = next(iter(data.values()), None)
        if isinstance(first_value, list):
            _display_dict_of_lists(data)
        elif isinstance(first_value, dict):
            _display_nested_dict(data)
        else:
            CONSOLE.print("[bold red]Error:[/bold red] Unexpected dictionary format.")
    else:
        CONSOLE.print("[bold red]Error:[/bold red] Input must be a list of dictionaries or a dictionary.")

if __name__ == "__main__":
    squad_data = players_as_dictionaries(SQUADS_DATA)
    CONSOLE.print("[bold underline bright_cyan]Displaying players as dictionaries:[/bold underline bright_cyan]")
    display_as_table(squad_data)

    players_by_pos = players_by_position(squad_data)
    CONSOLE.print("\n[bold underline bright_cyan]Displaying players by position:[/bold underline bright_cyan]")
    display_as_table(players_by_pos)

    players_by_country_pos = players_by_country_and_position(squad_data)
    CONSOLE.print("\n[bold underline bright_cyan]Displaying players by country and position:[/bold underline bright_cyan]")
    display_as_table(players_by_country_pos)