import sys
import argparse
from typing import Optional
from collections.abc import Sequence
from . import gitvenv



def main_cli(args: Optional[Sequence[str]] = None) -> int:
    rc = 0
    try:
        if args is None:
            args = sys.argv[1:]

        parser = argparse.ArgumentParser(
            prog="gitvenv",
            description="Creates virtual Git environments in the target directory.",
            epilog="Once an environment has been created, you may wish to activate it, e.g. by "
            "sourcing an activate script in its bin directory."
        )
        parser.add_argument(
            "dir", metavar="ENV_DIR",
            help="A directory to create the environment in."
        )
        parser.add_argument(
            "--clear", default=False, action="store_true", dest="clear",
            help="Delete the contents of the environment directory if it already exists, before "
            "environment creation."
        )
        parser.add_argument(
            "--copy", default=False, action="store_true", dest="copy",
            help="Copy the current config files to the new environment."
        )
        options = parser.parse_args(args)

        gitvenv.create(options.dir, clear=options.clear, copy_current=options.copy)
    except Exception as err:
        rc = 1
        print(f"Error: {err}", file=sys.stderr)

    return rc
