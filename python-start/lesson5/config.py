import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FILES_FOLDER_NAME = "files"
FILES_DIR = os.path.join(BASE_DIR, FILES_FOLDER_NAME)

DEFAULT_FILE_NAME = "test.txt"


def full_filename(filename): return os.path.join(FILES_DIR, filename)
