import io

from pathlib import (
    Path, os
)

def fix_overviews():
    folder = Path.home().joinpath("Documents/EVE/Overview/")

    for n in os.listdir(folder):
        ov_file = folder.joinpath(n)

        # don't try to open subfolders
        if not ov_file.is_file():
            continue

        with io.open(ov_file, 'r+', encoding='utf8') as f:
            overview = f.read()
            print("Fixing {}".format(ov_file))
            overview = overview.replace('&lt;', '<')
            overview = overview.replace('&gt;', '>')
            f.write(overview)
    print("Done!")



if __name__ == '__main__':
    fix_overviews()
