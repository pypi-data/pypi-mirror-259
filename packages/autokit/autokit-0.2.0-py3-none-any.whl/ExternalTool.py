"""
A framework for managing and executing downloadable tools.
"""

import platform
import shlex
import subprocess
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict

from downloader import download


class ExternalTool(ABC):
    def __init__(self, base_dir: Path = "./third-party", lazy_setup: bool = False):
        self.base_dir = Path(base_dir)

        if not lazy_setup:
            self.setup()


    @property
    @abstractmethod
    def tool_name(self) -> str:
        """
        Returns the name of the tool.
        """
        return self.tool_name

    @property
    @abstractmethod
    def platform_data(self) -> Dict[str, dict]:
        """
        Returns the platform data for the tool.
        """
        # throw error if not implemented
        raise NotImplementedError("Platform data not implemented")

    @property
    @abstractmethod
    def tool_directory(self) -> Path:
        """
        Returns the directory where the tool is installed.
        """
        return Path(self.base_dir) / Path(self.tool_name)

    @property
    @abstractmethod
    def python(self) -> bool:
        return False

    def setup(self) -> bool:
        """
        Sets up the tool by downloading and extracting it.
        """
        if self.calculate_path().exists():
            return True

        self.tool_directory.mkdir(parents=True, exist_ok=True)
        url = self.get_platform_data()['url']
        download(url)

        if self.python:

            requirements = (self.calculate_dir() / "requirements.txt")

            if requirements.exists():
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "-r",
                     requirements.resolve()])

        return True

    def get_platform_data(self) -> dict:
        """Retrieves platform-specific data from the dictionary."""
        system = platform.system()
        if system not in self.platform_data:
            raise ValueError(f"Unsupported operating system: {system}")
        return self.platform_data[system]

    def run_command(self, cmd: str, stdout=None, stdin=None) -> int:
        """
        Run a command in a subprocess.

        Args:
            cmd: The command to run as a string.
            stdout: The file-like object to use as stdout.
            stdin: The file-like object to use as stdin.

        Returns:
            The exit code of the subprocess.
        """

        if not self.setup():
            raise ValueError(f"Could not set up {self.tool_name}")

        if self.python:
            cmd = f'{sys.executable} "{self.calculate_path().resolve()}" {cmd}'
        else:
            cmd = f'{self.calculate_path().resolve()} {cmd}'

        command_args = shlex.split(cmd, posix=False)

        for i, arg in enumerate(command_args):
            if arg.startswith('"') and arg.endswith('"'):
                command_args[i] = arg[1:-1]

        with subprocess.Popen(command_args, stdout=stdout, stderr=subprocess.PIPE, stdin=stdin, bufsize=1,
                              universal_newlines=True) as p:
            while True:
                line = p.stdout.readline()
                if not line:
                    break

            exit_code = p.wait()
        return exit_code

    def calculate_path(self) -> Path:
        """
        Calculates the path of the tool based on the operating system.
        """
        directory = self.calculate_dir()
        platform_data = self.get_platform_data()
        extension = platform_data.get('extension', "")
        path = directory / f'{self.tool_name}{extension}'
        return path

    def calculate_dir(self) -> Path:
        """
        Calculates the directory path of the tool based on the operating system.
        """
        platform_data = self.get_platform_data()
        subdir = platform_data.get('subdir', "")
        if subdir:
            directory = self.tool_directory / subdir
        else:
            directory = self.tool_directory
        return directory
