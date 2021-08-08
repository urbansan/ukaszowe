import json
import shutil
from datetime import datetime as dt
import sys

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def copy_file(from_file, to_file, logfile):
    try:
        shutil.copyfile('index.html', "C:\Users\LK\Desktop\index.html")
        print("Skopiowano")

        log_file = open("C:\Users\LK\Desktop\log.txt", "a")
        log_file.write("\nSuccess: %s" % (dt.now()))
        log_file.close()

    except (FileNotFoundError, PermissionError):
        print("Nieskopiowano")
        log_file = open(r"C:\Users\LK\Desktop\log.txt", "a")
        log_file.write("\nERROR: %s" % (dt.now()))
        log_file.close()


class LogFile:
    def __init__(self, filename=None):
        self._filename = filename

    def log(self, txt):
        now = dt.now()
        if self._filename:
            with open(self._filename, "a") as f:
                f.write(txt)
        else:
            print(txt, file=sys.stderr)

