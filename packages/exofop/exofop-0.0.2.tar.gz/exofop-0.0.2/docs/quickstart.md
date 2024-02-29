# QuickStart

Welcome to the quick start tutorial for the ExoFOP package! 
This tutorial will guide you through the basic steps of using ExoFOP to download and extract light curve data for your astronomical system of interest.


## Downloading Data

To begin, import the necessary modules and specify the directory where you want to store the downloaded data:

```python
from exofop.download import System, SystemDownloader

# Path to directory that should store the downloaded files
data_dir = "./tmp"
```

Next, create a `System` object by providing the name of your target system and 
initialize a SystemDownloader object by passing the system and data directory:
```python
system = System("TOI 1130")  # or system = System("TIC 12345678")
system_loader = SystemDownloader(
    system=system,
    data_dir=data_dir,
)
```

You can now download the tags associated with the system:

```python
tags = system_loader.time_series.tags
system_loader.download(tags[:5], unzip=True)
```

## Extracting Light Curve Data

Once you have downloaded the data, you can proceed to extract the light curve information.
Load the downloaded data into a `LightCurveTableList` object:

```python
from exofop.extract import LightCurveTableList

target_dir = system_loader.target_dir
lctl = LightCurveTableList.load_exofop_data(
    target_dir=target_dir,
)

# Standardize the column names for consistency and apply time correction if needed
lctl.standardise_column_names()
lctl.apply_time_correction_in_case_of_discrepancy()

# Check if some of the extracted light curves could not be standardised successfully
lctl.incomplete
```

Now you can view summary information about the extracted light curves:

```python
lctl.info_df
```

Save all extracted measurement files as single ECSV files for future use.

```python
lctl.save('path/to/save/files/as/ecsv')
```

--- 
## Conclusion
You're now familiar with the basic steps to download and extract light curve data using the ExoFOP package. Feel free to explore further functionality and customize your analysis as needed. Happy researching!


All the code used in this tutorial at a glance:

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