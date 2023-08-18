#!/usr/bin/env python3
from plexarr.utils import get_py_path
from pathlib import Path
from rich import print
import shutil


cwd = get_py_path()

files = [
    "package-lock.json",
    "package.json",
    "public/config.js",
    "public/config.php",
    "config_js.tpl",
    "config_php.tpl",
    "configs_setup.py",
    "configs_backup.py"
]

print("\n[cyan]Backing up config files...[/]")
for f in files:
    print(f'[green]\[+] {f}[/]')
    src = cwd.joinpath(f)
    dst = cwd.parent.joinpath('streamity_config_backup', f)
    shutil.copy(src, dst)
