# IPy : 

Python library for handling of the different device in the MML

## Environment setup : 
Make sure that you have
- python version = 3.9 (recommend installation of anaconda or miniconda)
  - create a new environment with : `conda create --name mml python=3.9`
  - switch to new environment with : `conda activate mml`
- Install sphinx and rtd theme for documentation : 
  - `python -m pip install sphinx sphinx-rtd-theme`
- If you don't have `make` installed : 
  - `sudo apt-get install make`

Then you can proceede with the package install. 

## Development install :

Install the requirements by running : 
```bash
python -m pip install -r requirements.txt
```

Then you can install the library by running 
```bash
python -m pip install -e .
```
in the root directory of the library where the `setup.py` file is located. 
The `-e` flag will enable local changes in the code repository to be used when running 
the code without the need to reinstall the package.

## Documentation build : 

```bash
make html
```

for latex files which are then compield with pdflatex : 

```bash
make latexpdf
```

## Build and update pypi registry : 

```bash
# building the new release : 
python -m build

# upload to pypi (assuming that in dist only new build): 
python -m twine upload --skip-existing dist/*
```

## User install :

If using anaconda python distribution, run :  
```bash
python -m pip install ipy
```

else if using system python then run : 
```bash
pip3 install ipy
```

## Example : 

### TODOs : 