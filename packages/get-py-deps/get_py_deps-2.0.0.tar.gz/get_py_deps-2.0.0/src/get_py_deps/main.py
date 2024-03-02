import argparse
import logging
import sys

import pkg_resources
from prettytable import PrettyTable


def _get_pkg_license(pkg: pkg_resources.Distribution) -> str:
    try:
        lines = pkg.get_metadata_lines("METADATA")
    except Exception:
        lines = pkg.get_metadata_lines("PKG-INFO")

    for line in lines:
        if line.startswith("License:"):
            return line[9:]
    return "(License not found)"


def _get_pkg_home_page(pkg: pkg_resources.Distribution) -> str:
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
    try:
        pkg_requires = [pkg.key for pkg in pkg_resources.require(package_name)]
    except pkg_resources.DistributionNotFound:
        logging.error(
            f"Package '{package_name}' not found, "
            "is it really installed in the current environment?"
        )
        exit(1)

    logging.debug(f"Package {package_name} requires {pkg_requires}")
    table = PrettyTable(["Package", "License", "Url"])

    for pkg in sorted(pkg_resources.working_set, key=lambda x: str(x).lower()):
        logging.debug(f"Processing package {pkg}")
        if pkg.key in pkg_requires and pkg.key != package_name:
            logging.debug(f"Package {pkg} is a dependency")
            logging.debug(f"Package {pkg} has license {_get_pkg_license(pkg)}")
            logging.debug(f"Package {pkg} has home page {_get_pkg_home_page(pkg)}")
            logging.debug(f"Adding package {pkg} to table")
            table.add_row((str(pkg), _get_pkg_license(pkg), _get_pkg_home_page(pkg)))

    return table


def _parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print all dependencies for a python package "
        "with their licenses and home page."
    )
    parser.add_argument(
        "package_name", help="The package name to get dependencies from."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )
    return parser.parse_args(args)


# Cli function, use argparse to parse the argument package_name and call get_py_deps
def _cli(args: list[str] | None = None) -> None:
    args = sys.argv[1:] if args is None else args
    logging.debug(f"Received CLI arguments {args}")
    parsed_args = _parse_args(args)
    logging.debug(f"Parsed CLI arguments {parsed_args}")

    if parsed_args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    print(get_py_deps(parsed_args.package_name))


if __name__ == "__main__":
    _cli()
