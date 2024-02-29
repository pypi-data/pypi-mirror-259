import copy

from collections import defaultdict
from typing import Dict, List, NamedTuple, Optional, Set, Tuple, Union


class EssentialLightcurveAttributes(NamedTuple):
    """
    Represents essential attributes of a lightcurve.

    Attributes
    ----------
    time : str
        The primary alias for the time attribute.
    flux : str
        The primary alias for the flux attribute.
    flux_err : str
        The primary alias for the flux error attribute.

    Methods
    -------
    update_primary_alias(old_primary_alias, new_primary_alias)
        Rename a primary alias and update its synonyms accordingly.
    __deepcopy__(memo)
        Create a deep copy of the instance.

    """

    time: str = "time"
    flux: str = "flux"
    flux_err: str = "flux_err"

    def update_primary_alias(self, old_primary_alias, new_primary_alias):
        """
        Rename a primary alias and update its synonyms accordingly.

        Parameters
        ----------
        old_primary_alias : str
            The primary alias to be renamed.
        new_primary_alias : str
            The new primary alias to replace the old one.

        Raises
        ------
        KeyError
            If the old primary alias does not exist in the mapping.
        """
        if old_primary_alias in self:
            return EssentialLightcurveAttributes(
                **{
                    key: (value if value != old_primary_alias else new_primary_alias)
                    for key, value in self._asdict().items()
                }
            )
        else:
            raise KeyError(
                f"The primary alias '{old_primary_alias}' does not exist in the mapping."
            )

    def __deepcopy__(self, memo):
        """Create a deep copy of the instance.

        Parameters
        ----------
        memo : dict
            A dictionary that keeps track of already copied objects to avoid infinite recursion.

        Returns
        -------
        EssentialLightcurveAttributes
            A deep copy of the instance.

        Notes
        -----
        This method is called by the `copy.deepcopy` function.
        EssentialLightcurveAttributes is a NamedTuple, so we use the `_make` method.
        """
        return self._make(self)


class SynonymMap(defaultdict):
    """
    A dictionary-like class that allows the association of synonyms with a primary alias.

    This class plays a pivotal role in achieving consistent column naming across ExoFOP
    (Exoplanet Follow-up Observing Program) data files. With a wide range of
    observatories and processing pipelines contributing to ExoFOP, there are cases
    where different column names are used to denote the same underlying concept.
    For instance, the column representing time may be labelled as
    'BJD TBD', 'time', 'TIME', and so on.

    This class addresses this complexity by facilitating the organization of mappings between
    a primary concept alias and its corresponding synonyms. This systematic approach ensures
    that a consistent and intuitive nomenclature can be achieved, regardless of the original source.

    Parameters
    ----------
    None

    Examples
    --------
    Initialise the synonym map

    >>> synonym_map = SynonymMap()
    >>> synonym_map['time'] = ('Time', 'TIME', 'BJD TBD', 'another_synonym')
    >>> synonym_map.get_rename_dict('time')
    {'Time': 'time', 'TIME': 'time', 'BJD TBD': 'time', 'another_synonym': 'time'}

    Add a new primary alias and its synonyms

    >>> synonym_map['flux'] = ('flux', 'FLUX', 'rel_flux')

    Add a new synonym to an existing primary alias

    >>> synonym_map.add_synonyms('flux', 'rel_flux_T1')

    Rename a primary alias and update its synonyms accordingly

    >>> synonym_map.rename_primary_alias('flux', 'FLUX')
    >>> synonym_map.keys()
    dict_keys(['time', 'FLUX'])

    See Also
    --------
    exofop.extract.SynonymMapLc
    """

    def __init__(self) -> None:
        super().__init__(tuple)
        self._primary_alias_to_synonyms: Dict[str, Dict[str, str]] = {}

    @property
    def primary_alias_to_synonyms(self) -> Dict[str, Dict[str, str]]:
        """A dictionary mapping primary aliases to their synonyms."""
        if len(self) != len(self._primary_alias_to_synonyms) or any(
            len(self[key]) != len(self._primary_alias_to_synonyms[key]) for key in self
        ):
            self.rebuild_synonym_mapping()

        return self._primary_alias_to_synonyms

    @primary_alias_to_synonyms.setter
    def primary_alias_to_synonyms(self, value):
        self._primary_alias_to_synonyms = value

    def get_rename_dict(self, primary_alias) -> Dict[str, str]:
        """
        Retrieve a dictionary for renaming synonyms to their primary alias.

        Parameters
        ----------
        primary_alias : str
            The primary alias for which to retrieve the renaming dictionary

        Returns
        -------
        dict
            Rename dict.
        """
        return self.primary_alias_to_synonyms.get(primary_alias, {})

    def get_primary_alias(self, synonym: str) -> Union[str, None]:
        """Retrieve the primary alias associated with a synonym, if it is contained."""
        for primary_alias, rename_dict in self.primary_alias_to_synonyms.items():
            if synonym in rename_dict:
                return primary_alias

        return None

    def add_synonyms(self, primary_alias: str, synonym: Union[tuple, str]) -> None:
        """Add synonyms to an existing primary alias."""
        if isinstance(synonym, str):
            synonym = (synonym,)
        elif isinstance(synonym, (list, set)):
            synonym = tuple(synonym)

        self[primary_alias] = self[primary_alias] + tuple(
            item for item in synonym if item not in self[primary_alias]
        )

    def remove_synonym(self, primary_alias: str, synonym: str) -> None:
        self[primary_alias] = tuple(item for item in self[primary_alias] if item != synonym)

    def __setitem__(
        self, primary_alias: str, alias: Union[str, Set[str], List[str], Tuple[str, ...]]
    ) -> None:
        """
        Tuple a primary alias and their synonyms.

        Parameters
        ----------
        primary_alias : str
            The primary alias to tuple.
        alias : Tuple[str, ...]
            The tuple of synonyms associated with the primary alias.
        """
        if isinstance(alias, str):
            alias = (alias,)
        elif isinstance(alias, set):
            alias = tuple(alias)
        elif isinstance(alias, (list, tuple)):
            seen = set()
            alias = tuple(item for item in alias if item not in seen and not seen.add(item))

        if primary_alias not in self:
            # Check if the suggested primary alias already exists as a synonym
            existing_primary_alias = self.get_primary_alias(primary_alias)
            if existing_primary_alias is not None:
                raise KeyError(
                    f"The primary alias '{primary_alias}' already exists as a synonym for '{existing_primary_alias}'."
                )

        super().__setitem__(primary_alias, alias)
        self._update_primary_alias_to_synonyms(primary_alias, alias)

    def update(
        self, synonym_map: Dict[str, Union[str, Set[str], List[str], Tuple[str, ...]]]
    ) -> None:
        """
        Update the synonym map with a dictionary of primary aliases and their synonyms.

        Parameters
        ----------
        synonym_map : Dict[str, Tuple[str, ...]]
            A dictionary of primary aliases and their synonyms.
        """

        for primary_alias, synonyms in synonym_map.items():
            self[primary_alias] = synonyms

    def _update_primary_alias_to_synonyms(self, primary_alias: str, alias: Tuple[str, ...]) -> None:
        """
        Update the primary alias to synonyms mapping.
        """
        synonyms_dict = {}
        for synonym in alias:
            self._check_existing_aliases(synonym, primary_alias)
            synonyms_dict[synonym] = primary_alias
        self.primary_alias_to_synonyms[primary_alias] = synonyms_dict

    def _check_existing_aliases(self, synonym: str, new_primary_alias: str) -> None:
        """
        Check if a synonym is already associated with a different primary alias.

        Parameters
        ----------
        synonym : str
            The synonym to check.
        new_primary_alias : str
            The new primary alias to which the synonym is being associated.

        Raises
        ------
        KeyError
            If the synonym is already associated with a different primary alias.
        """
        existing_primary_alias = self.get(synonym)
        if any(synonym in synonyms for key, synonyms in self.items() if key != new_primary_alias):
            raise KeyError(
                f"The synonym '{synonym}' is already associated with the primary alias "
                f"'{existing_primary_alias}'. It cannot be used as a synonym for '{new_primary_alias}'."
            )

    def rebuild_synonym_mapping(self):
        """
        Update the synonym_to_primary_mapping dictionary based on the current state of the SynonymMap.
        """
        self._primary_alias_to_synonyms = {}
        for primary_alias, synonyms in self.items():
            self._primary_alias_to_synonyms[primary_alias] = {
                synonym: primary_alias for synonym in synonyms
            }

    def rename_primary_alias(self, old_primary_alias, new_primary_alias):
        """
        Rename a primary alias and update its synonyms accordingly.

        Parameters
        ----------
        old_primary_alias : str
            The primary alias to be renamed.
        new_primary_alias : str
            The new primary alias to replace the old one.

        Raises
        ------
        KeyError
            If the old primary alias does not exist in the mapping.
        """
        if old_primary_alias not in self:
            raise KeyError(
                f"The primary alias '{old_primary_alias}' does not exist in the mapping."
            )

        # Get the synonyms for the old primary alias
        synonyms_dict = self.primary_alias_to_synonyms[old_primary_alias]

        # Remove the old primary alias and its synonyms
        del self[old_primary_alias]
        del self._primary_alias_to_synonyms[old_primary_alias]

        # Add the new primary alias and its synonyms
        self[new_primary_alias] = (*tuple(synonyms_dict.keys()), old_primary_alias)

        self._primary_alias_to_synonyms[new_primary_alias] = synonyms_dict

    @classmethod
    def from_dict(cls, data: dict):
        instance = cls()
        instance.update(data)
        return instance

    def save_to_yaml(self, file_path):
        import yaml

        with open(file_path, "w") as file:
            yaml.dump(dict(self), file)

    @classmethod
    def load_from_yaml(cls, file_path):
        data = cls._load_yaml_content(file_path)
        return cls.from_dict(data)

    @staticmethod
    def _load_yaml_content(file_path):
        import yaml

        def tuple_constructor(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode) -> tuple:
            string_list = loader.construct_sequence(node)
            string_tuple = tuple(map(str, string_list))
            return string_tuple

        yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/tuple", tuple_constructor)

        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        return data


class SynonymMapLc(SynonymMap):
    """
    A subclass of SynonymMap specifically tailored for handling light curve attributes,
    with the ability to manipulate primary aliases and their synonyms.

    Parameters
    ----------
    light_curve_attributes : Optional[EssentialLightcurveAttributes], optional
        An instance of EssentialLightcurveAttributes defining primary aliases for time,
        flux, and flux error. If None, default aliases will be used.
    time : str, optional
        Primary alias for time attribute. Default is "BJD_TDB".
    flux : str, optional
        Primary alias for flux attribute. Default is "rel_flux_T1_n".
    flux_err : str, optional
        Primary alias for flux error attribute. Default is "rel_flux_err_T1_n".

    Attributes
    ----------
    light_curve_attributes : EssentialLightcurveAttributes
        The primary aliases for the essential light curve attributes.

    Example
    -------
    >>> synonym_map_lc = SynonymMapLc(time="BJD_TDB", flux="flux", flux_err="flux_err")
    >>> synonym_map_lc["BJD_TDB"] = ["time", "BJD", "BJD_TDB_MOBS", "#BJD_TDB"]
    >>> synonym_map_lc["flux"] = ["flux", "FLUX", "rel_flux", "rel_flux_T1"]
    >>> synonym_map_lc["flux_err"] = ["flux_err", "ERRFLUX", "rel_flux_err_T1"]
    >>> synonym_map_lc["cbv_0"] = ["cbv_0_synonym_0", "cbv_0_synonym_1"]

    You can access the primary aliases and their synonyms as attributes

    >>> synonym_map_lc.light_curve_attributes
    EssentialLightcurveAttributes(time='BJD_TDB', flux='flux', flux_err='flux_err')

    For convenience, you can access the primary aliases of the light curve attributes as properties
    >>> synonym_map_lc.time
    ('time', 'BJD', 'BJD_TDB_MOBS', '#BJD_TDB')
    >>> synonym_map_lc.rename_primary_alias("BJD_TDB", "time")
    >>> synonym_map_lc.keys()
    dict_keys(['flux', 'flux_err', 'cbv_0', 'time'])

    See Also
    --------
    exofop.extract.SynonymMap
    exofop.extract.EssentialLightcurveAttributes
    """

    def __init__(
        self,
        light_curve_attributes: Optional[EssentialLightcurveAttributes] = None,
        time: str = "BJD_TDB",
        flux: str = "rel_flux_T1_n",
        flux_err="rel_flux_err_T1_n",
    ) -> None:
        super().__init__()
        if light_curve_attributes is None:
            primary_alias_list = [time, flux, flux_err]
            self.light_curve_attributes = EssentialLightcurveAttributes(*primary_alias_list)
        else:
            if not isinstance(light_curve_attributes, EssentialLightcurveAttributes):
                raise TypeError(
                    "light_curve_attributes must be an instance of EssentialLightcurveAttributes."
                )
            self.light_curve_attributes = light_curve_attributes

    @property
    def cbv_names(self) -> List[str]:
        """List of primary aliases for the cotrending basis vectors (CBVs)."""
        return [key for key in self if key not in self.light_curve_attributes]

    @property
    def time(self) -> Tuple[str, ...]:
        """Tuple of synonyms for the time attribute."""
        return self[self.light_curve_attributes.time]

    @time.setter
    def time(self, value):
        self[self.light_curve_attributes.time] = value

    @property
    def flux(self) -> Tuple[str, ...]:
        """Tuple of synonyms for the flux attribute."""
        return self[self.light_curve_attributes.flux]

    @flux.setter
    def flux(self, value):
        self[self.light_curve_attributes.flux] = value

    @property
    def flux_err(self) -> Tuple[str, ...]:
        """Tuple of synonyms for the flux error attribute."""
        return self[self.light_curve_attributes.flux_err]

    @flux_err.setter
    def flux_err(self, value):
        self[self.light_curve_attributes.flux_err] = value

    def rename_primary_alias(self, old_primary_alias, new_primary_alias):
        """
        Rename a primary alias and update its synonyms accordingly.

        Parameters
        ----------
        old_primary_alias : str
            The primary alias to be renamed.
        new_primary_alias : str
            The new primary alias to replace the old one.

        Raises
        ------
        KeyError
            If the old primary alias does not exist in the mapping.
        """
        if old_primary_alias in self.light_curve_attributes:
            self.light_curve_attributes.update_primary_alias(old_primary_alias, new_primary_alias)

        super().rename_primary_alias(old_primary_alias, new_primary_alias)

    def __copy__(self) -> "SynonymMapLc":
        new = SynonymMapLc(light_curve_attributes=self.light_curve_attributes)
        for key, value in self.items():
            new[key] = value
        return new

    def __deepcopy__(self, memo) -> "SynonymMapLc":
        new = SynonymMapLc(light_curve_attributes=copy.deepcopy(self.light_curve_attributes))
        memo[id(self)] = new
        for key, value in self.items():
            new[copy.deepcopy(key, memo)] = copy.deepcopy(value, memo)
        return new

    def copy(self) -> "SynonymMapLc":
        return copy.copy(self)

    def deepcopy(self) -> "SynonymMapLc":
        return copy.deepcopy(self)

    def save_to_yaml(self, file_path):
        import yaml

        data = {
            "light_curve_attributes": self.light_curve_attributes._asdict(),
            "synonyms": dict(self),
        }
        with open(file_path, "w") as file:
            yaml.dump(data, file)

    @classmethod
    def load_from_yaml(cls, file_path) -> "SynonymMapLc":
        """
        Load the synonym map from a YAML file.

        Parameters
        ----------
        file_path : str
            The path to the YAML file.
        """
        data = cls._load_yaml_content(file_path)

        light_curve_attributes_data = data.get("light_curve_attributes", {})
        synonyms_data = data.get("synonyms", {})

        light_curve_attributes = EssentialLightcurveAttributes(**light_curve_attributes_data)
        synonyms = cls.from_dict(synonyms_data)

        instance = cls(light_curve_attributes=light_curve_attributes)
        instance.update(synonyms)

        return instance

    @classmethod
    def load_from_config(cls, reset=False) -> "SynonymMapLc":
        """
        Load the synonym map from the local config directory.

        Parameters
        ----------
        reset : bool, optional
            If True, the synonym map is reset to the default configuration.
            If False, the synonym map is loaded from the local config directory.
            Default is False.

        Returns
        -------
        SynonymMapLc
            The synonym map instance.

        Examples
        --------
        Load the user-modified default synonym map from the local config directory

        >>> synonym_map_lc = SynonymMapLc.load_from_config()

        Load the default synonym map from the local config directory as shipped with the package

        >>> synonym_map_lc = SynonymMapLc.load_from_config(reset=True)
        """
        import os
        from exofop.utils.paths import CONFIG_DIR

        config_content = os.listdir(CONFIG_DIR)

        if "synonym_map_lc_local.yaml" in config_content and not reset:
            file_path = os.path.join(CONFIG_DIR, "synonym_map_lc_local.yaml")
        elif "synonym_map_lc.yaml" in config_content:
            file_path = os.path.join(CONFIG_DIR, "synonym_map_lc.yaml")
        else:
            raise FileNotFoundError(
                "No synonym_map_lc.yaml or synonym_map_lc_local.yaml found in config directory."
                "Reinstall the package to restore the default config files."
            )

        instance = cls.load_from_yaml(file_path)

        if not os.path.exists(os.path.join(CONFIG_DIR, "synonym_map_lc_local.yaml")) or reset:
            instance.save_to_config()

        return instance

    def save_to_config(self):
        """
        Save the synonym map to the local config directory.

        The synonym map is saved to the local config directory as 'synonym_map_lc_local.yaml'.
        """
        import os
        from exofop.utils.paths import CONFIG_DIR

        file_path = os.path.join(CONFIG_DIR, "synonym_map_lc_local.yaml")

        self.save_to_yaml(file_path)
