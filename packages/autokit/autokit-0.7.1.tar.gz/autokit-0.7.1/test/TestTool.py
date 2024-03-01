from pathlib import Path


import autokit
from autokit import ExternalTool, ToolConfig, PlatformData


class TestTool(ExternalTool):
    def __init__(self, base_dir: str = "./third-party", progress_bar: bool = True, lazy_setup: bool = False):
        super().__init__(Path(base_dir), progress_bar, lazy_setup)

    @property
    def config(self) -> ToolConfig:
        return ToolConfig(
            tool_name="test-tool",
            platform_data={
                "windows": PlatformData(
                    url="https://github.com/IRSS-UBC/MediaTools/releases/download/latest/win-x64.zip",
                    subdir=Path(""),
                    executable=Path("IRSSMediaTools.exe")
                ),
            },
            python=False,
        )

    def help(self):
        self.run_command("help")


if __name__ == "__main__":
    test = TestTool()
    test.help()
