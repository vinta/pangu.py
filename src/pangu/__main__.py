"""Support ``python -m pangu``."""

import sys

from pangu._cli import cli

if __name__ == "__main__":
    sys.exit(cli())
