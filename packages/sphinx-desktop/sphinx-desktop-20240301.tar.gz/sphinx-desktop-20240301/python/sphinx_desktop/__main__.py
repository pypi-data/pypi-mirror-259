#!/bin/env python3

import logging
import os
import pkgutil
import subprocess
import sys
from argparse import ArgumentParser
from os.path import expandvars

from dataclasses import dataclass
from pathlib import Path
from shutil import which
from urllib.parse import urlparse

import toml


@dataclass
class Project:
    name: str
    path: Path
    release: str


def main():
    root_parser = ArgumentParser(
        prog="sphinx-desktop",
        description="""Open sphinx:// links on your desktop.""",
        epilog="""""",
    )

    subparsers = root_parser.add_subparsers(
        dest='command',
        title="commands",
        description="Valid commands",
        help="Commands you may enter.",
        required=True,
    )

    parser = subparsers.add_parser("open")
    parser.add_argument("url")

    parser = subparsers.add_parser("install-xdg")
    args = root_parser.parse_args()

    commands = {
        "open": main_open,
        "install-xdg": main_install_xdg,
    }

    commands[args.command](args)


def error(message):
    print(message)


def main_open(args):
    url = urlparse(args.url)

    path = url.path

    print(path)
    path = Path(path)

    project_name = url.netloc
    release = Path(path.parts[1])
    source_path = Path(*path.parts[2:])

    print(project_name)

    config = Path("~/.config/sphinx-desktop.toml").expanduser()

    if not config.exists():
        print(f"Config doesn't exist at {config}")
        sys.exit(-1)

    with config.open("r") as f:
        doc = toml.load(f)

    main = doc.get("sphinx", {})

    projects = main.get("projects", [])

    project_map = {}

    environ = os.environ

    for project in projects:
        if not project:
            continue

        name = project.get("name", None)
        path = project.get("path", None)
        release = project.get("release", "*")

        if not name and not path:
            continue

        if isinstance(path, dict):
            expand = path.get("expand", None)
            if expand:
                path = expandvars(expand)
            else:
                print(f"Invalid path config at {config}.")
                sys.exit(-1)

        key = (name, release)
        project_map[key] = Project(name, Path(path.format(**environ)).expanduser(), release)

    project = project_map.get((project_name, release), None)
    project_any = project_map.get((project_name, "*"), None)

    if project is None and project_any is None:
        error(f"No path for project {project_name} {project}")
        sys.exit(-1)

    project = project or project_any

    if not project.path.exists():
        error(f"Project {project_name}  at path {project.path} doesn't exist.")
        sys.exit(-1)

    file_path = project.path / source_path

    if not file_path.exists():
        error(f"File to edit {file_path} doesn't exist.")
        sys.exit(-1)

    subprocess.run(["xdg-open", file_path])


def main_install_xdg(args):
    # Install sphinx desktop
    xdgm = which("xdg-mime")
    udd = which("update-desktop-database")

    if xdgm is None:
        print("Error! xdg-mime can not be found.")
        sys.exit(-1)

    if udd is None:
        print("Error! xdg-mime can not be found.")
        sys.exit(-1)

    dest = Path.home() / ".local/share/applications" / "sphinx-desktop.desktop"
    print(f"Installing desktop file {dest}")
    #desktop-file-install --dir=$HOME/.local/share/applications source/sphinx-desktop.desktop
    with dest.open("w") as f:
        data = pkgutil.get_data("sphinx_desktop.xdg", "sphinx-desktop.desktop").decode("utf-8")

        f.write(data)

    #xdg-mime default sphinx-desktop.desktop x-scheme-handler/sphinx
    print("Set default scheme handler for sphinx://...")
    subprocess.run([xdgm, "default", "sphinx-desktop.desktop", "x-scheme-handler/sphinx"])

    #update-desktop-database
    print("Update desktop database...")
    subprocess.run([udd])
    #cp source/python/sphinx_desktop.py ~/.local/bin/sphinx-desktop
    #chmod +x ~/.local/bin/sphinx-desktop


def main_uninstall_xdg(args):
    xdgm = which("xdg-mime")
    udd = which("update-desktop-database")

    if xdgm is None:
        print("Error! xdg-mime can not be found.")
        sys.exit(-1)

    if udd is None:
        print("Error! update-desktop-database can not be found.")
        sys.exit(-1)

    dest = Path.home() / ".local/share/applications" / "sphinx-desktop.desktop"
    dest.unlink(missing_ok=True)

    #print("Set default scheme handler for sphinx://...")
    #subprocess.run([xdgm, "uninstall", "sphinx-desktop.desktop", "x-scheme-handler/sphinx"])

    print("Update desktop database...")
    subprocess.run([udd])


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        logging.exception(e)
        sys.exit(-1)
