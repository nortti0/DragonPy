# coding: utf-8

"""
    DragonPy - Dragon 32 emulator in Python
    =======================================

    :created: 2014 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2014-2015 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""


import hashlib
import logging
import os
import sys
import zipfile

import dragonpy


PY3 = sys.version_info[0] == 3
if PY3:
    from urllib.request import urlopen
    from zipfile import BadZipFile
else:
    from urllib.request import urlopen
    from zipfile import BadZipfile as BadZipFile


ARCHIVE_EXT_ZIP = ".zip"

log = logging.getLogger(__name__)


class ROMFileNotFound(Exception):
    pass


class ROMFile(object):
    ROM_PATH = os.path.normpath(
        os.path.join(os.path.abspath(os.path.dirname(dragonpy.__file__)), "..", "roms")
    )
    URL = None  # download location
    DOWNLOAD_SHA1 = None  # Hash of the downloaded file
    ARCHIVE_EXT = ARCHIVE_EXT_ZIP  # archive type of the download
    FILE_COUNT = None  # how many files are in the archive?
    RENAME_DATA = None  # save the files with different names from archive

    SHA1 = None  # Hash of the extracted ROM file
    FILENAME = None  # filename of the ROM file, e.g.: "d32.rom"

    def __init__(self, address, max_size=None):
        self.address = address
        self.max_size = max_size

        if not os.path.isdir(self.ROM_PATH):
            os.makedirs(self.ROM_PATH)
            print(f"ROM path created here: {self.ROM_PATH!r}")
        else:
            log.debug(f"Use ROM path: {self.ROM_PATH!r}")

        self.archive_filename = self.FILENAME + self.ARCHIVE_EXT  # used to download
        self.archive_path = os.path.join(self.ROM_PATH, self.archive_filename)
        self.rom_path = os.path.join(self.ROM_PATH, self.FILENAME)

    def get_data(self):
        if not os.path.isfile(self.rom_path):
            self.download()
            if self.ARCHIVE_EXT == ".zip":
                self.extract_zip()

        print(f"Read ROM file {self.rom_path!r}...")
        with open(self.rom_path, "rb") as f:
            data = f.read()

        # Check SHA hash:
        current_sha1 = hashlib.sha1(data).hexdigest()
        assert current_sha1 == self.SHA1, f"ROM sha1 value is wrong! SHA1 is: {current_sha1!r}"
        print(f"ROM SHA1: {current_sha1!r}, ok.")

        if self.max_size:
            filesize = os.stat(self.rom_path).st_size
            if filesize > self.max_size:
                log.critical("Load only $%04x (dez.: %i) Bytes - file size is $%04x (dez.: %i) Bytes",
                             self.max_size, self.max_size, filesize, filesize
                             )
            data = data[:self.max_size]

        return data

    def file_rename(self, filename):
        if not self.RENAME_DATA:
            return filename

        try:
            return self.RENAME_DATA[filename]
        except KeyError:
            raise RuntimeError(
                "Filename %r in archive is unknown! Known names are: %s" %
                list(
                    self.RENAME_DATA.keys()))

    def extract_zip(self):
        assert self.FILE_COUNT > 0
        try:
            with zipfile.ZipFile(self.archive_path, "r") as zip:
                namelist = zip.namelist()
                print("namelist():", namelist)
                if len(namelist) != self.FILE_COUNT:
                    msg = (
                        "Wrong archive content?!?"
                        " There exists %i files, but it should exist %i."
                        "Existing names are: %r"
                    ) % (len(namelist), self.FILE_COUNT, namelist)
                    log.error(msg)
                    raise RuntimeError(msg)

                for filename in namelist:
                    content = zip.read(filename)
                    dst = self.file_rename(filename)

                    out_filename = os.path.join(self.ROM_PATH, dst)
                    with open(out_filename, "wb") as f:
                        f.write(content)

                    if dst == filename:
                        print(f"{out_filename!r} extracted")
                    else:
                        print(f"{filename!r} extracted to {out_filename!r}")

                    self.post_processing(out_filename)

        except BadZipFile as err:
            msg = f"Error extracting archive {self.archive_path!r}: {err}"
            log.error(msg)
            raise BadZipFile(msg)

    def post_processing(self, out_filename):
        pass

    def download(self):
        """
        Request url and return his content
        The Requested content will be cached into the default temp directory.
        """
        if os.path.isfile(self.archive_path):
            print(f"Use {self.archive_path!r}")
            with open(self.archive_path, "rb") as f:
                content = f.read()
        else:
            print(f"Request: {self.URL!r}...")
            # Warning: HTTPS requests do not do any verification of the server's certificate.
            f = urlopen(self.URL)
            content = f.read()
            with open(self.archive_path, "wb") as out_file:
                out_file.write(content)

        # Check SHA hash:
        current_sha1 = hashlib.sha1(content).hexdigest()
        assert current_sha1 == self.DOWNLOAD_SHA1, f"Download sha1 value is wrong! SHA1 is: {current_sha1!r}"
        print(f"Download SHA1: {current_sha1!r}, ok.")
