import pytest
from pathlib import Path
from src import file_automation

file_test_data = "RealFile.pdf"
source_directory_test_data = Path("C:/Users/13605/Downloads/Temp_path")
destination_directory_test_data = Path(
    "C:/Users/13605/Desktop/DL_Docs/Temp_path")
expected_results_test_data = f"Moved file '{file_test_data}' successfully to '{destination_directory_test_data}'."


@pytest.mark.parametrize(
    "source_file, source_directory, destination_directory, expected_result",
    [
        (file_test_data, source_directory_test_data,
         destination_directory_test_data, expected_results_test_data,)
    ]
)
def test_move_file_valid_permission(source_file: str, source_directory: Path, destination_directory: Path, expected_result: str, tmp_path):
    """Test for move file function, assuming valid permission

    Args:
        source_file (str): File to be moved
        source_directory (Path): Location of file to be moved
        destination_directory (Path): Destination of file to be moved
        expected_result (str): Message that should be generated if the function works correctly
        tmp_path (Path): Temporary directory
    """
    temp_source_directory: Path = tmp_path / str(source_directory)
    temp_destination_directory: Path = tmp_path / str(destination_directory)
    temp_file_source = temp_source_directory / "RealFile.pdf"
    temp_file_destination = temp_destination_directory / "RealFile.pdf"

    temp_source_directory.mkdir()
    temp_destination_directory.mkdir()
    temp_file_source.write_text("test content")

    result = file_automation.move_file(
        source_file, temp_source_directory, temp_destination_directory)

    if temp_file_source.exists():
        temp_file_source.unlink()
    if temp_file_destination.exists():
        temp_file_destination.unlink()
    if temp_source_directory.is_dir():
        temp_source_directory.rmdir()
    if temp_destination_directory.is_dir():
        temp_destination_directory.rmdir()

    assert result == expected_result


@pytest.mark.parametrize(
    "directory_path, expected_result",
    [
        (Path("C:/Users/13605/Desktop/DL_Docs/"), True),
        (Path("C:/Users/13605/Downloads/"), True),
        (Path("C:/Uuuusers"), False),
        (Path(''), False),
        (Path(), False),
    ],
)
def test_check_directory_is_valid(directory_path, expected_result):
    """Test to determine if a directory exists

    Args:
        directory_path (Path): Location of directory to be tested
        expected_result (bool): Boolean value to check directory against
    """
    result = file_automation.check_directory_is_valid(directory_path)
    assert result == expected_result
