# autokit version 0.1.1



A framework for effortlessly integrating external tools into your Python projects.

## Installation

```bash
pip install autokit 
```

## Basic Usage
```python
import autokit 
from pathlib import Path

class MyToolManager:
    DOWNLOAD_URLS = {
        'Windows': "example.com/downloads/windows.zip",
        'Darwin': "example.com/downloads/osx-x64.zip",
        'Linux': "example.com/downloads/linux.zip",
    }

    def __init__(self, base_dir: Path = "./third-party"):
        self.tool = autokit.ExternalToolManager(
            tool_name="IRSSMediaTools",
            download_urls=self.DOWNLOAD_URLS,  # Pass URLs
            python=False,
            base_dir=base_dir)
        self.tool.setup()


    

    def run(self):
        self.tool.run_command("--help")    

example = MyToolManager()
example.run()
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