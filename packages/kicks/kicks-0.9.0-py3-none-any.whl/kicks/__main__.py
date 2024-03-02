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
t.add_row("1", "firefox windows 64")
t.add_row("2", "chrome windows 64")
t.add_row("3", "docker windows")
t.add_row("4", "process explorer")
t.add_row("5", "vc_redist")
t.add_row("6", "virtualbox")
t.add_row("7", "grml small iso")

CONSOLE.print(t)

x = CONSOLE.input('# ')

if x == "1":
    outfile = os.path.join(OP, "firefox-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "2":
    outfile = os.path.join(OP, "chrome.zip")
    outzipdir = os.path.join(OP, "chrome")
    cmd = 'curl -C - -L -o "%s" "https://dl.google.com/chrome/install/GoogleChromeEnterpriseBundle64.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""%s""" % os.path.join(outzipdir, "Installers", "GoogleChromeStandaloneEnterprise64.msi"), shell=True)
        #subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "3":
    outfile = os.path.join(OP, "docker-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://desktop.docker.com/win/main/amd64/Docker%%20Desktop%%20Installer.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "4":
    #https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
    outfile = os.path.join(OP, "pe.zip")
    outzipdir = os.path.join(OP, "pe")
    cmd = 'curl -C - -L -o "%s" "https://download.sysinternals.com/files/ProcessExplorer.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "5":
    outfile = os.path.join(OP, "vc_redist.exe")
    cmd = 'curl -C - -L -o "%s" "https://aka.ms/vs/17/release/vc_redist.x64.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "6":
    #https://www.virtualbox.org/wiki/Downloads
    outfile = os.path.join(OP, "vbox-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://download.virtualbox.org/virtualbox/7.0.14/VirtualBox-7.0.14-161095-Win.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "7":
    #https://download.grml.org/grml64-small_2024.02.iso
    outfile = os.path.join(OP, "grml.iso")
    cmd = 'curl -C - -L -o "%s" "https://download.grml.org/grml64-small_2024.02.iso"' % outfile
    subprocess.call(cmd, shell=True)
    subprocess.call("""explorer %s""" % (OP), shell=True)
