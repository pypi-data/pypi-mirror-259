# ExoFOP

A python-package to facilitate the download and standardization data from the Exoplanet Follow-up Observing Program (ExoFOP).
It streamlines the process of accessing ExoFOP data, making it easier for researchers and enthusiasts to work with this valuable collection of astronomical observations.

## Installation

The recommended method of installing ExoFOP is using pip:
```bash
pip install exofop
```
For more detailed installation instructions or troubleshooting, please refer to the [documentation](https://dgegen.github.io/exofop/).

## Documentation

Comprehensive documentation for ExoFOP Python package can be found [here](https://dgegen.github.io/exofop/).
It includes information about the package, installation instructions, tutorials, and API references.

## Example
Here's an example demonstrating how to use ExoFOP Python package to download and standardize data:
```python
from exofop.download import System, SystemDownloader
from exofop.extract import LightCurveTableList

# Specify the directory to store downloaded data
data_dir = "./tmp"

# Downloading Data
system = System("TOI 1130")
system_loader = SystemDownloader(
    system=system,
    data_dir=data_dir,
)

# Selecting tags and downloading them
tags = system_loader.time_series.tags
system_loader.download(tags[:5], unzip=True)

# Extracting Light Curve Data
target_dir = system_loader.target_dir
lctl = LightCurveTableList.load_exofop_data(
    target_dir=target_dir,
)
lctl.standardise_column_names()
lctl.apply_time_correction_in_case_of_discrepancy()

# Save the extracted data as a single ECSV file for future reference
lctl.save()
```
This example demonstrates how to download data for a specific target (in this case, "TOI 1130"),
extract light curve data, standardize column names, apply time corrections,
and save the extracted data for future reference.

# Contributing
Contributions to ExoFOP Python package are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please feel free to open an issue or submit a pull request on the GitHub repository.

# License
ExoFOP Python package is licensed under the MIT License. See the LICENSE file for details.
