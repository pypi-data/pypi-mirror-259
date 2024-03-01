from pathlib import Path
from typing import Dict, NamedTuple


class PlatformData(NamedTuple):
    """
    A class to represent the data for a platform.

    Attributes
    ----------
    url : str
        The URL to download the tool from.
    subdir : Path
        The subdirectory to extract the tool to.
    executable : Path
        The path to the executable, relative to the subdir.
    """
    url: str
    subdir: Path
    executable: Path


class ToolConfig(NamedTuple):
    """
    A class to represent the configuration for a tool.

    Attributes
    ----------
    tool_name : str
        The name of the tool.
    platform_data : Dict[str, PlatformData]
        The platform data for the tool.
    python : bool
        Whether the tool should be executed by the Python interpreter.
    """
    tool_name: str
    platform_data: Dict[str, PlatformData]
    python: bool
