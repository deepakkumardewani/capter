import os
import subprocess
import random
import string
from pathlib import Path
import pwd

DEFAULT_FILE_NAME = "output.png"


def get_user_name():
    return pwd.getpwuid(os.getuid()).pw_name


def file_exists(name):
    file = f"/Users/deepakdewani1/Documents/screenshots/{name}"
    screenshot_file = Path(file)
    if screenshot_file.is_file():
        return True


def create_screenshots_directory():
    Path(f"/Users/{get_user_name()}/Documents/screenshots").mkdir(
        parents=True, exist_ok=True
    )


def run():
    file = f"/Users/deepakdewani1/Documents/screenshots/{DEFAULT_FILE_NAME}"

    if file_exists(DEFAULT_FILE_NAME):
        random_str = "".join(
            random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)
        )
        file_name = f"output-{random_str}.png"
        file = f"/Users/deepakdewani1/Documents/screenshots/{file_name}"
    SCREENSHOT_CMD = f"screenshot -w on_screen_only Terminal -f {file}"
    COPY_CMD = ["osascript", "-e"]

    create_screenshots_directory()

    clipboard = (
        'set the clipboard to (read (POSIX file "/Users/%s/Documents/screenshots/output.png") as {«class PNGf»})'
        % (get_user_name())
    )

    COPY_CMD.append(clipboard)
    os.system(SCREENSHOT_CMD)
    subprocess.run(COPY_CMD)
