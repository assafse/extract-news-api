#!e:\devtest\extract-news-api\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip-tools==5.0.0','console_scripts','pip-sync'
__requires__ = 'pip-tools==5.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip-tools==5.0.0', 'console_scripts', 'pip-sync')()
    )
