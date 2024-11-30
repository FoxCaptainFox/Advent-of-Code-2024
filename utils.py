from typing import Any, List, Optional, TypeVar, Union, Literal, Callable, overload
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DIRECTORY_NAME = "Data"

T = TypeVar('T')  # Define 'T' as a generic type variable

def _convert_value(value: str, output_type: Any) -> Optional[T]:
    """
    Convert the given value to the specified type. Returns None if conversion fails.
    """
    try:
        return output_type(value)
    except ValueError:
        return None

def read_file(file_number: int) -> str:
    """
    Reads a file based on the given file number from the specified directory.
    Returns the file content as a string.
    """
    file_path = os.path.join(__location__, DIRECTORY_NAME, f"{file_number:02}.txt")
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

@overload
def read_data(file_number: int, as_separate_characters: Literal[False] = False, output_type: Callable[[str], T] = str, filter_none: bool = False) -> List[T]: ...
    
@overload
def read_data(file_number: int, as_separate_characters: Literal[True], output_type: Callable[[str], T] = str, filter_none: bool = False) -> List[List[T]]: ...

def read_data(file_number: int, as_separate_characters: bool = False, output_type: Callable[[str], T] = str, filter_none: bool = False) -> Union[List[T], List[List[T]]]:
    """
    Reads data from a file and converts each line or character to the specified output type.
    Filters out None values if filter_none is True.
    Returns a list of converted values or a list of lists of converted values.
    """
    lines = read_file(file_number).split("\n")
    if as_separate_characters:
        return [[_convert_value(ch, output_type) for ch in line if not (filter_none and _convert_value(ch, output_type) is None)] for line in lines]
    else:
        return [_convert_value(line, output_type) for line in lines if not (filter_none and _convert_value(line, output_type) is None)]