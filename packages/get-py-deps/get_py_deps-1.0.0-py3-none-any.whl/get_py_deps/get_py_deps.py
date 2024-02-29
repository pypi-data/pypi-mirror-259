import pkg_resources
import argparse
import logging
from prettytable import PrettyTable


def _get_pkg_license(pkg):
    try:
        lines = pkg.get_metadata_lines("METADATA")
    except Exception:
        lines = pkg.get_metadata_lines("PKG-INFO")

    for line in lines:
        if line.startswith("License:"):
            return line[9:]
    return "(License not found)"


def _get_pkg_home_page(pkg):
    try:
        lines = pkg.get_metadata_lines("METADATA")
    except Exception:
        lines = pkg.get_metadata_lines("PKG-INFO")

    for line in lines:
        if line.startswith("Home-page:"):
            return line[11:]
    return "(Homepage not found)"


def get_py_deps(package_name: str) -> PrettyTable:
    """Print all dependencies which are required with their licenses and home page."""
    pkg_requires = pkg_resources.working_set.by_key[package_name].requires()
    logging.debug(f"Package {package_name} requires {pkg_requires}")
    table = PrettyTable(["Package", "License", "Url"])

    for pkg in sorted(pkg_resources.working_set, key=lambda x: str(x).lower()):
        logging.debug(f"Processing package {pkg}")
        if pkg.project_name in [pkg.project_name for pkg in pkg_requires]:
            logging.debug(f"Package {pkg} is a dependency")
            logging.debug(f"Package {pkg} has license {_get_pkg_license(pkg)}")
            logging.debug(f"Package {pkg} has home page {_get_pkg_home_page(pkg)}")
            logging.debug(f"Adding package {pkg} to table")
            table.add_row((str(pkg), _get_pkg_license(pkg), _get_pkg_home_page(pkg)))

    return table

# Cli function, use argparse to parse the argument package_name and call get_py_deps
def _cli():
    import argparse
    parser = argparse.ArgumentParser(description="Print all dependencies for a python package with their licenses and home page.")
    parser.add_argument("package_name", help="The package name to get dependencies from.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    print(get_py_deps(args.package_name))

if __name__ == "__main__":
    _cli()