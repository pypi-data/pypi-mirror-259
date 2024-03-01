# Cloud Free Image Downloader

A small tool to download cloud free images from GEE. Also serves as an example that projects in the
DLR MF-DAS organization should follow. You should copy the CI/CD set-up and other practices for your repository.

## Installation

This tool relies on Google Earth Engine's Python API which cannot be installed automatically as a
dependency. You need to install it from conda-forge in your conda environment:

```
conda install -c conda-forge earthengine-api
```

This is assuming you already have a conda environment activated. To install from source code you can
do the following:

```
git clone git@github.com:DLR-MF-DAS/gee_downloader.git
cd gee_downloader
pip install -e .
```
Or if you don't want the source code you can do:

```
pip install git+git@github.com:DLR-MF-DAS/gee_downloader.git
```

## Usage

Authenticate to Google Earth Engine (note that authentication mode should be set to notebook)

```
earthengine authenticate --auth_mode notebook
```

Then you can run the script by executing the module with the -m flag.

```
python3 -m gee_downloader --help
```

Which will tell you what the options for the script are.

```
Usage: python -m gee_downloader [OPTIONS]

Options:
  -i, --geojson TEXT      Area of interest in the GeoJSON format  [required]
  -s, --start-date TEXT   Starting date for the composite (yyyy-mm-dd)
                          [required]
  -e, --end-date TEXT     End date for the composite (yyyy-mm-dd)  [required]
  -o, --output-file TEXT  File to write the results to  [required]
  --help                  Show this message and exit.
```

For designing command line interfaces I recomment the click library for Python - https://click.palletsprojects.com/. 
The implementation of the script can be found under `src/gee_downloader/__main__.py`. Please consider following this 
structure if your project requires you to provide an executable script.

To download some actual data you can try the following arguments from inside the repository file structure of this 
project.

```
python3 -m gee_downloader -i test/munich.json -s 2019-01-01 -e 2019-04-01 --output-file test.tiff
```

Which should result in a 13 band image part of which looks like this.

![munich](test/munich.png)

## CI/CD Setup

### Testing

For testing you should use https://docs.pytest.org/. The GitHub Actions workflow file that runs the tests
is located under gee_downloader/.github/workflows/python-app.yml. Use it and the tests under the test/
subdirectory as an example for your own projects.

### Documentation

The documentation for this library is automatically built and uploaded to GitHub Pages on each commit.
The workflow responsible for this is defined at gee_downloader/.github/workflows/pdoc.yml. I prefer
to use pdoc for documentation building (over sphinx which is in my view an outdated abomination) but
if you prefer to use something more complex the idea behind building and publishing it stays the same.

You can find the documentation here: https://dlr-mf-das.github.io/gee_downloader/

### Publishing
