# PyTools_QOL
Python tools that I use for quality of life programming

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/MicahBest/PyTools_QOL/.github%2Fworkflows%2FPyTools_QOL.yml?logo=github)

## Features and Capabilities

### Program Execution Time:
Example usage:
```python
import time
from PyTools_QOL import print_execution_time

def main():
    time.sleep(3) # waits for 3 seconds

if __name__ == "__main__":
    start_time = time.time()
    main()
    print_execution_time(start_time) # > Program executed in 3 seconds.
```
