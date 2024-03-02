import os
import rich
import subprocess
from rich.console import Console
from rich.table import Table

CONSOLE = Console()


OP="_kicks"
OD=os.makedirs(OP, exist_ok=True)

t = Table()
t.add_column("#")
t.add_column("File")
t.add_row("1", "ff")

CONSOLE.print(t)

x = CONSOLE.input('# ')

if x == "1":
    outfile = os.path.join(OP, "firefox-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)
