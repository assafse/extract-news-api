#!e:\devtest\extract-news-api\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zappa==0.51.0','console_scripts','zappa'
__requires__ = 'zappa==0.51.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zappa==0.51.0', 'console_scripts', 'zappa')()
    )
