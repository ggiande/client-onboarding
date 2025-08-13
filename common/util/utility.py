import os
import shutil
from stat import S_IWRITE

"""
DO NOT IMPORT ANYTHING FROM ANOTHER MODEL UNLESS IT'S A 3RD PARTY
CONSTANT IS THE EXCEPTION -- CIRUCLAR DEPENDENCIES WILL FORM
"""
class Utility:
    """
    Utility stores functions used for logging, extracting, printing, and additional items
    """

    def __init__(self) -> None:
        """
        Special method that replaces a constructor/__new()__
        """


    @classmethod
    def check_if_dirs_exist(cls, dir: str, create: bool = True, verbose: bool = False, delete: bool = False) -> bool:
        exists = True if os.path.isdir(dir) or os.path.isfile(dir) else False
        path_type = "file" if os.path.splitext(dir)[1] else "directory"

        if create and not exists:
            if path_type == "file":
                fd = os.open(dir, os.O_CREAT | os.O_WRONLY)
                os.close(fd)
                if verbose:
                    print(f"{path_type}: {dir} created")
                return False
            elif path_type == "directory":
                os.makedirs(dir)
                if verbose:
                    print(f"{path_type}: {dir} created")
                return False

        if create and exists:
            if verbose:
                print(f"{path_type}: {dir} exists")
            return True

        if not delete and exists:
            if verbose:
                print(f"{path_type}: {dir} exists")
            return True

        if delete and exists:
            cls.assign_write_to_subdirs(dir)
            if verbose:
                print(f"{path_type}: {dir} deleted")
            if path_type == "directory":
                shutil.rmtree(dir)
                return True
            elif path_type == "file":
                os.remove(dir)
                return True

        if delete and not exists:
            if verbose:
                print(f"{path_type}: {dir} marked for deletion but does not exist")
            return False


    @staticmethod
    def assign_write_to_subdirs(root_dir:str) -> None:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    os.chmod(file_path, S_IWRITE)
                except Exception as e:
                    print(f"[ERROR] changing perms to writeable {file_path, filename}")
