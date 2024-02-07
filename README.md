# Python Snobal

Python implementation of the Snobal model applied at either a point or over and image (iSnobal). This package conatains the C libraries of Snobal in a python wrapper for more flexibility and ease of interaction.

ipysnobal.py has functions for general interaction. More detailed and flexible functions can be found in the Automated Water Supply Model (AWSM).

### Building from source

In addition to the other dependencies, you will need to install `cython`, and you will need a c compiler on your machine. Windows users: install the latest Visual Studio community release with the "Universal Windows Platform" option checked during installation.
NOTE: This is meant for use on exclusively Linux, not windows

1. Use _cibuildwheel_ (note: if using Windows or Mac OS, docker is required if the platform option is set to `linux`):

`cibuildwheel --platform=linux --output-dir=dist`

2. Install the wheel file with `pip install dist/hgs_output-[version details].whl` or run `pip install .`.


#### Usage
For Linux systems when installing:
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

## Development Installation

To install the development environment:

```
pipenv install --dev
```