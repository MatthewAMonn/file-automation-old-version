"""
2nd version of the program. Flushes out exception use cases.
"""

# Provides a way for file and directory operations, such as copying and moving.
import shutil

# Hardcoded file to be moved and destination location
source_file = "C:/Users/13605/Downloads/MatthewMonnResume.pdf"
destination_location = "C:/Users/13605/Desktop/DL_Docs/"


# Potential issues that can occur:
# 1. File is missing from 'source_file'
# 2. Destination does not exist. Should it be created or just thrown an exception? This version will throw an error.
#       Without an error source file is 'destroyed' by becoming a simple file.
# 3. Permission issues with accessing file or destination


def move_file(file, location):
    """Moves a file from one location to another

    Args:
        file (string): File to be moved
        location (string): Location for file to be moved to
    """
    try:
        shutil.move(source_file, destination_location)
        print("File was successfully moved ")
    except FileNotFoundError:
        print("Source file does not exist")
    except PermissionError as e:
        print("Permissions error has occured. Please adjust permission settings for file/destination and that file is closed")
    except Exception as e:
        print(f"Unknown error has occured: {e}")


move_file(source_file, destination_location)
