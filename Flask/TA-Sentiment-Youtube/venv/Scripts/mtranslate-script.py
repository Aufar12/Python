#!c:\users\aufar\documents\ta-sentiment-youtube\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mtranslate==1.6','console_scripts','mtranslate'
__requires__ = 'mtranslate==1.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mtranslate==1.6', 'console_scripts', 'mtranslate')()
    )
