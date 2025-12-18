# Provides a way for file and directory operations, such as copying and moving.
from pathlib import Path

# Hard coded file name and source/destination directories. Future update might change this to dynamic or more than 1 file.
source_file = "MatthewMonnResume.pdf"
source_directory = Path("C:/Users/13605/Downloads/")
destination_directory = Path("C:/Users/13605/Desktop/DL_Docs/")


def check_directory_is_valid(directory):
    """Checks if a directory exists or not

    Args:
        directory (string): Path of a directory

    Returns:
        boolean: Provides True or False if directory exists
    """
    if directory.is_dir():
        return True
    else:
        print("Directory of where the file is to be moved does not exist. Please create the directory first, then try again.")
        return False


def move_file(source_file: str, source_directory: Path, destination_directory: Path):
    """Moves a file from one directory to another if possible

    Args:
        source_file (str): Name of file to be moved
        source_directory (Path): Path of the directory that contains the source file
        destination_directory (Path): Path of the directory that the file is to be moved to
    """
    if check_directory_is_valid(destination_directory):
        source_full_path = source_directory / source_file
        destination_full_path = destination_directory / source_file

        try:
            source_full_path.rename(destination_full_path)
            print(
                f"Moved file '{source_file}' successfully to '{destination_directory}'.")
        except FileNotFoundError:
            print(
                f"Error: Source file '{source_file}' does not exist in directory '{source_directory}'.")
        except PermissionError as e:
            print("Permission error has occured. Please adjust permission settings for file/destination and that file is closed.")
        except Exception as e:
            print(f"Unknown error has occured: {e}")


move_file(source_file, source_directory, destination_directory)
