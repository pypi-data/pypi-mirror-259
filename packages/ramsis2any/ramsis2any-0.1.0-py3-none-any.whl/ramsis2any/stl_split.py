import sys
import re

import rich

RE_ENDSOLID = re.compile(r'solid (?P<name>[^\n]+)\n(?P<content>.+?)endsolid', re.DOTALL)

def splitfile(filename: list[str]):
    """
    Split STL files into separate files based on the 'solid - endsolid' keywords.

    Args:
        filenames (list): List of file paths to the STL files.
    """
    with open(filename, 'r') as f:
        data = f.read()
    if data.count('endsolid') == 1:
        rich.print(f"[bold red]Skipping:[/bold red] [bold magenta]'{filename}'[/bold magenta] does not contain multiple solids.")
        return
    if data.count('solid') == 0:
        rich.print(f"[bold red]Skipping:[/bold red] [bold magenta]'{filename}'[/bold magenta] does not contain any solids.")
        return
    data = RE_ENDSOLID.findall(data)

    for name, content in data:
        with open(name + '.stl', 'w') as f:
            stl_content = f"solid {name}\n{content}endsolid {name}\n"
            f.write(stl_content)
            rich.print(f"[bold magenta]'{name}.stl'[/bold magenta] created")

if __name__ == '__main__':
    splitfile(sys.argv[1])
