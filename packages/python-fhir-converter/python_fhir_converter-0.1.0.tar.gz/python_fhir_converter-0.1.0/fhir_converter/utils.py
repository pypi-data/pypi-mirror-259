from os import remove as os_remove
from os import walk as os_walk
from pathlib import Path
from re import Pattern
from re import compile as re_compile
from typing import IO, Any, AnyStr, Dict, Final, Generator, List, Tuple, Union

from liquid import Undefined
from pyjson5 import loads as json_loads
from xmltodict import parse as xmltodict_parse

DataIn = Union[IO, AnyStr]

line_endings_pattern: Final[Pattern] = re_compile(r"\r\n?|\n")


def is_undefined_none_or_blank(obj: Any) -> bool:
    """is_undefined_none_or_blank returns whether the object is undefined,
    none or blank

    Will return True for the following::
        - Undefined
        - None
        - '' (empty string)
        - ' ' (blank string)
        - [] (empty list)
        - () (empty tuple)
        - {} (empty dict)

    Args:
        obj (Any): the object to check

    Returns:
        bool: returns True if the object is undefined, none or empty, otherwise, False
    """
    if isinstance(obj, Undefined):
        return True
    elif type(obj) in (int, float, bool):
        return False
    elif isinstance(obj, str):
        obj = blank_str_to_empty(obj)
    return not obj


def to_list_or_empty(obj: Any) -> List[Any]:
    """to_list_or_empty returns the object as a list if its a list or not empty
    or none, otherwise, []

    Args:
        obj (Any): the object to check

    Returns:
        list[Any]: returns the object as a list if its a list or not empty or none,
        otherwise, []
    """
    if isinstance(obj, list):
        return obj
    elif is_undefined_none_or_blank(obj):
        return []
    return [obj]


def blank_str_to_empty(obj: str) -> str:
    """blank_str_to_empty returns the given string if it's not blank, otherwise, empty

    Args:
        obj (str): the string to check

    Returns:
        str: returns the given string if it's not blank, otherwise, empty
    """
    return obj if obj and not obj.isspace() else ""


def merge_dict(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[Any, Any]:
    """merge_dict Merges the key/value pair mappings similarly to
    newtonsoft Merge.

    See https://www.newtonsoft.com/json/help/html/MergeJson.htm

    Args:
        a (Dict[Any, Any]): the mappings to merge into
        b (Dict[Any, Any]): the mappings to merge

    Returns:
        Dict[Any, Any]: the merged mappings
    """
    for bk, bv in b.items():
        if bv is None:
            continue

        if bk not in a:
            a[bk] = bv
        else:
            av = a[bk]
            if type(av) != type(bv):
                a[bk] = bv
            elif isinstance(bv, dict):
                merge_dict(av, bv)
            elif isinstance(bv, list):
                for v in bv:
                    if v not in av:
                        av.append(v)
            else:
                a[bk] = bv
    return a


def _remove_empty_json_list(obj: List[Any]) -> List[Any]:
    """remove_empty_json_list Removes any empty values from the JSON list

    See is_none_or_empty and remove_empty_json for more info

    Args:
        obj (List[Any]): the JSON list to check

    Returns:
        List[Any]: the JSON list with non empty values. May be empty if all values
        were empty
    """
    new_list = []
    for val in obj:
        val = _remove_empty_json(val)
        if not is_undefined_none_or_blank(val):
            new_list.append(val)
    return new_list


def _remove_empty_json_dict(obj: Dict[Any, Any]) -> Dict[Any, Any]:
    """remove_empty_json_dict Removes any empty JSON key/value mappings from
    the supplied key/value pairs

    See is_none_or_empty and remove_empty_json for more info

    Args:
        obj (Dict[Any, Any]): the JSON key/value pairs to check

    Returns:
        Dict[Any, Any]: the non empty key/value pairs, May be empty if
        all key/value pairs were empty
    """
    for key in list(obj.keys()):
        val = _remove_empty_json(obj[key])
        if not is_undefined_none_or_blank(val):
            obj[key] = val
        else:
            del obj[key]
    return obj


def _remove_empty_json(obj: Any) -> Any:
    """remove_empty_json Removes empty JSON

    Removes from the JSON object as follows::

        - '', ' ' strings will be converted to ''. See blank_str_to_empty
        - Lists with empty elements will be removed. See remove_empty_json_list
        - Dicts with empty key/value mappings will be removed. See remove_empty_json_dict

    Args:
        obj (Any): the JSON to check

    Returns:
        Any: the non empty JSON, or empty
    """
    if isinstance(obj, dict):
        return _remove_empty_json_dict(obj)
    elif isinstance(obj, list):
        return _remove_empty_json_list(obj)
    elif isinstance(obj, str):
        return blank_str_to_empty(obj)
    return obj


def _read_text(data: DataIn, encoding: str = "utf-8") -> str:
    """read_text Reads the given data using the supplied encoding if the data
    is not already a string

    Args:
        data (DataIn): the data to read
        encoding (str, optional): The character encoding to use. Defaults to "utf-8"

    Returns:
        str: the text content
    """
    if isinstance(data, str):
        return data

    content = data
    if not isinstance(content, bytes):
        content = content.read()
        if isinstance(content, str):
            return content
    return str(content, encoding=encoding)


def parse_json(
    json_in: DataIn, encoding: str = "utf-8", ignore_empty_fields: bool = True
) -> Any:
    """parse_json Parses the JSON string using a JSON 5 compliant decoder

    Any empty JSON will be removed from decoded output. See remove_empty_json

    Args:
        json_in (DataIn): the json to decode
        encoding (str, optional): The character encoding to use. Defaults to "utf-8"
        ignore_empty_fields (bool): Whether to ignore empty fields. Defaults to True

    Returns:
        Any: the decoded output
    """

    json = json_loads(_read_text(json_in, encoding))
    return _remove_empty_json(json) if ignore_empty_fields else json


def parse_xml(xml_in: DataIn, encoding: str = "utf-8") -> Dict[str, Any]:
    """parse_xml Parses the xml imput string or text/binary IO

    Wraps xmltodict customizing the output as follows::
        - Sets _originalData key with the original xml string with line endings removed
        - Forces cdata along with settng the key to _
        - Disables the prepanding of @ to attribute keys
        - Replaces any : characters in keys with _

    Args:
        xml_in (DataIn): the xml input
        encoding (str, optional): The character encoding to use. Defaults to "utf-8"

    Returns:
        Dict[str, Any]: the parsed xml
    """
    xml = line_endings_pattern.sub("", _read_text(xml_in))
    data = xmltodict_parse(
        xml,
        encoding=encoding,
        force_cdata=True,
        attr_prefix="",
        cdata_key="_",
        postprocessor=lambda _, key, value: (
            (key.replace(":", "_") if ":" in key else key, value) if value else None
        ),
    )
    data["_originalData"] = xml
    return data


def join_subpath(path: Path, parent: Path, child: Path) -> Path:
    """join_subpath Joins the parts from the child relative to the parent
    path to the supplied path. The final file part from child will be
    excluded if child is a file

    Args:
        path (Path): the path to join the parts to
        parent (Path): the parent path
        child (Path): the child within the parent path

    Returns:
        Path: the new path
    """
    if not parent.is_dir():
        raise ValueError("parent must be a directory")
    child_parts = list(child.parts if child.is_dir() else child.parts[:-1])
    for parent_part in parent.parts:
        child_part = child_parts.pop(0) if child_parts else None
        if parent_part != child_part:
            raise ValueError("child must be a subdirectory of parent")
    return path.joinpath(*child_parts)


def del_empty_dirs_quietly(path: Path) -> None:
    """del_empty_dirs_quietly Quietly deletes any empty sub directories within
    the path ignoring any errors that may have occurred

    Args:
        path (Path): the path to scan
    """
    for dir, dirs, filenames in walk_path(path):
        if not dirs and not filenames and dir != path:
            del_path_quietly(dir)


def del_path_quietly(path: Path) -> None:
    """del_path_quietly Quietly deletes a path ignoring any errors that
    may have occurred

    Allows callers to attempt to delete a path while not having to worry
    about file system errors

    Args:
        path (Path): the path to delete
    """
    try:
        if path.is_dir():
            path.rmdir()
        else:
            os_remove(path)
    except OSError:
        pass


def mkdir(path: Path, **kwargs) -> bool:
    """mkdir wrapper around Path.mkdir forwarding additional keyword args

    Allows callers to discern between a directory existing, an actual error
    while creating the directory and a successful creation aka the directory
    didn't exist previously

    Args:
        path (Path): the path

    Returns:
        bool: True if the directory was created, otherwise, False to indicate the
        directory already exists
    """
    if not path.is_dir():
        path.mkdir(**kwargs)
        return True
    return False


def walk_path(
    path: Path,
) -> Generator[Tuple[Path, List[str], List[str]], Any, None]:
    """walk_path wrapper around os.walk to semi bridge the gap of path.walk
    added in 3.12.

    Args:
        path (Path): the path to walk

    Yields:
        Generator[Tuple[Path, List[str], List[str]], Any, None]: The directory
        tree generator
    """
    for dir, dirs, filenames in os_walk(path):
        yield (Path(dir), dirs, filenames)


def tail(buffer: IO, last_n: int = 25, encoding: str = "utf-8") -> str:
    """tail Reads the tail from the given file like object

    Args:
        buffer (IO): the file like object to read from
        last_n (int, optional): The last n to read up to. Defaults to 25.
        encoding (str, optional): The character encoding to use. Defaults to "utf-8"

    Returns:
        str: up to the last n from the file like object or empty string if
        the object is empty
    """
    pos = buffer.tell()
    if pos <= 0:
        return ""
    buffer.seek(pos - min(pos, last_n))
    return _read_text(buffer, encoding)
