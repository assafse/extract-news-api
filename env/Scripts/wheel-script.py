#!e:\devtest\extract-news-api\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wheel==0.34.2','console_scripts','wheel'
__requires__ = 'wheel==0.34.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wheel==0.34.2', 'console_scripts', 'wheel')()
    )
