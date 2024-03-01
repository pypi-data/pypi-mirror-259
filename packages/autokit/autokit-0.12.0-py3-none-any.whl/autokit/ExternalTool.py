"""
A framework for managing and executing downloadable tools.
"""

import platform
import shlex
import subprocess
import sys
from abc import ABC, abstractmethod
from pathlib import Path

from . import ToolConfig, PlatformData
from .downloader import download
from .progressBar import print_progress_bar


class ExternalTool(ABC):
    def __init__(self, base_dir: Path = "./third-party", progress_bar: bool = False, lazy_setup: bool = False):
        self.base_dir = Path(base_dir)

        if not lazy_setup:
            self.setup(progress_bar)

    @property
    @abstractmethod
    def config(self) -> ToolConfig:
        pass

    @property
    def tool_name(self) -> str:
        """
        Returns the name of the tool.
        """
        return self.config.tool_name

    @property
    def python(self) -> bool:
        return self.config.python

    @property
    def tool_directory(self) -> Path:
        """
        Returns the directory where the tool is installed.
        """
        return Path(self.base_dir) / Path(self.tool_name)

    def setup(self, use_progress_bar=False) -> bool:
        """
        Sets up the tool by downloading and extracting it.
        """
        if self.calculate_path().exists():
            return True

        self.tool_directory.mkdir(parents=True, exist_ok=True)
        url = self.get_platform_data().url

        # check if the tool is already downloaded
        if self.calculate_path().exists():
            return True

        if use_progress_bar:
            download(self.tool_directory, url, progress_callback=print_progress_bar)
        else:
            download(self.tool_directory, url)

        if self.python:
            requirements = (self.calculate_dir() / "requirements.txt")

            if requirements.exists():
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "-r",
                     requirements.resolve()])

        return True

    def get_platform_data(self) -> PlatformData:
        """
        Returns the platform data for the current operating system.

        Raises:
            ValueError: If the operating system is not supported.
        """
        system = platform.system()

        platform_data = self.config.platform_data

        for key in platform_data:
            if key.lower() == system.lower():
                system = key
                break

        if system not in platform_data:
            raise ValueError(f"Unsupported operating system: {system}")
        return platform_data[system]

    def run_command(self, cmd: str, stdout=None, stderr=None, stdin=None) -> int:
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

        with subprocess.Popen(command_args, stdout=stdout, stderr=stderr, stdin=stdin, bufsize=1,
                              universal_newlines=True) as p:

            if p.stdout:
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
        path = directory / platform_data.executable
        return path

    def calculate_dir(self) -> Path:
        """
        Calculates the directory path of the tool based on the operating system.
        """
        subdir = self.get_platform_data().subdir
        if subdir:
            directory = self.tool_directory / subdir
        else:
            directory = self.tool_directory
        return directory
