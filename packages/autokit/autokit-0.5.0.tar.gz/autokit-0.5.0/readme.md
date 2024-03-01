# autokit version 0.5.0



A framework for effortlessly integrating external tools into your Python projects.

## Installation

```bash
pip install autokit 
```

## Basic Usage

```python
import autokit

class MyTool(autokit.ExternalTool):
    @property
    def tool_name(self):
        return "MyTool"

    @property
    def platform_data(self):
        return {
            'Windows': {
                'url': "example.com/downloads/windows.zip",
                'subdir': "",
                'extension': ".exe"
            },
            'Darwin': {
                'url': "example.com/downloads/osx-x64.zip",
                'subdir': "",
                'extension': ""
            },
            'Linux': {
                'url': "example.com/downloads/linux.zip",
                'subdir': "",
                'extension': ""
            },
        }

    @property
    def python(self):
        return False


tool = MyTool(base_dir="./third-party")
tool.run_command("--help")
```

## Features
- Automatic download and configuration of external tools on first use.
- Define tools and their commands in a configuration file.
- Streamlined execution of tool commands from within your Python code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


Contact: olson@student.ubc.ca