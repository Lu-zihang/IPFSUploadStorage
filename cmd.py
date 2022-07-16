import docopt
import pkg
import os
"""
Usage:
    clidemo cmdA <valueA>
    clidemo cmdB paramB <valueB>

Options:
    -h --help       Show Help doc.
    -v --version    Show Version.
"""

def cmd():
    args = docopt(__doc__, version=pkg.__version__)
    if args.get("cmdA"):
        os.system("tree")

if __name__ == '__main__':
    cmd()