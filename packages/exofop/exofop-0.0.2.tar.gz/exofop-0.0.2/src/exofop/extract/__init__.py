"""
This sub-package  provides functionality for extracting data downloaded from the ExoFOP website
into a uniform format facilitating further analysis.

Outline
-------
:class:`exofop.extract.LightCurveTableList` : class
    A list of LightCurveTable instances with additional functionalities.

:class:`exofop.extract.LightCurveTable` : class
    A class representing a light curve table extracted from ExoFOP.

:class:`exofop.extract.SynonymMap` : class
    A class for handling the standardisation of column names.

:class:`exofop.extract.SynonymMapLc` : class
    A class for handling the standardisation of column names, with additional functionalities for
    the essential light curve attributes 'time', 'flux', and 'flux_err'.

Example
-------
The following is a basic example of how to use the class :class:`exofop.extract.LightCurveTableList`
to extract data downloaded from ExoFOP:

>>> from exofop.extract import LightCurveTableList
>>> target_dir = "path/to/your/directory/with/downloaded/measurements"
>>> lctl = LightCurveTableList.load_exofop_data(target_dir=target_dir)
>>> lctl.standardise_column_names()
>>> lctl.apply_time_correction_in_case_of_discrepancy()
>>> print(lctl.info_df)
>>> lctl_complete = lctl.complete
>>> lctl_complete.save()

For a more detailed introduction, consult the tutorial :doc:`notebooks/2_extract_and_standardise_time_series_data`.

Classes
-------
"""

from .extractor import LightCurveTableList, LightCurveTable
from .synonym_map import SynonymMap, SynonymMapLc

__all__ = ["LightCurveTableList", "LightCurveTable", "SynonymMap", "SynonymMapLc"]
