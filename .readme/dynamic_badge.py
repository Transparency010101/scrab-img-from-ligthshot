"""Automatic change version in README file's shield.

This is module with some function for is not relation to project. README file has a shield that show
project version, when makes push to repository I'd like this version change automatic in shield(I have to
change project version only in pyproject.toml), so I did this module rewrite json file(project_version.json)
and when makes push to GitHub, automatically runs this script and change version in project_version.json, that
dynamic badge gets changes from json file.

Usage:
    Run the script:
        python3 .readme/dynamic_badge.py
"""

import tomllib as toml
import json


def get_project_version():
    """Get project's version from pyproject.toml file.

    Returns:
        str
    """
    with open("pyproject.toml", "rb") as file:
        data = toml.load(file)

    return data["tool"]["poetry"]["version"]


def insert_version_to_json_file(version):
    """Gets version and insert it in project_version.json

    Returns:
        None
    """
    data = {
        "version": version,
    }

    with open("project_version.json", "w") as file:
        file.write(json.dumps(data))


insert_version_to_json_file(get_project_version())
