#!C:\Users\Jahiro\PycharmProjects\Final\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'GitGitlab==1.16','console_scripts','git-lab'
__requires__ = 'GitGitlab==1.16'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('GitGitlab==1.16', 'console_scripts', 'git-lab')()
    )
