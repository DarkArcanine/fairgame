#      FairGame - Automated Purchasing Program
#      Copyright (C) 2021  Hari Nagarajan
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      The author may be contacted through the project's GitHub, at:
#      https://github.com/Hari-Nagarajan/fairgame
import os
import hashlib
from common.license_hash import license_hash #this means that it imports from license_hash.py from the common folder


def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, "rb", buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


if os.path.exists("LICENSE") and sha256sum("LICENSE") in license_hash: #checks license file matches hash
    s = """
    FairGame Copyright (C) 2021 Hari Nagarajan
        This program comes with ABSOLUTELY NO WARRANTY; for details
        start the program with the `show --w' option.

        This is free software, and you are welcome to redistribute it
        under certain conditions; for details start the program with
        the `show --c' option.\n
    """

    print(s)
else:
    print("License File Changed or Missing. Quitting Program.")
    exit(0)


def notfound_message(exception):
    print(exception)
    print(
        f"Missing '{exception.name}' module.  If you ran 'pipenv install', try 'pipenv install {exception.name}'"
    )
    print("Exiting...")


try:
    from cli import cli 
    #from cli in this case is a package (which is still like a regular module); a package typically corresponds to 
    # a file directory containing Python files and other directories. To create a Python package yourself, 
    # you create a directory and a file named __init__.py inside it. The __init__.py file contains the contents of the package when it’s treated as a module. It can be left empty.
except ModuleNotFoundError as e:
    notfound_message(e)
    exit(0)

if __name__ == "__main__":
    try:
        cli.main()
    except ModuleNotFoundError as e:
        notfound_message(e)
        exit(0)
