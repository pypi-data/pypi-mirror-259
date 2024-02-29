import doctest

import exofop
import pytest
from exofop.extract.synonym_map import SynonymMap, SynonymMapLc


@pytest.fixture
def synonym_map():
    return SynonymMap()


def test_setitem(synonym_map):
    synonym_map["time"] = ["Time", "BJD TBD"]
    assert synonym_map["time"] == ("Time", "BJD TBD")


def test_setitem_existing_synonym(synonym_map):
    synonym_map["time"] = ["Time", "TIME", "BJD TBD"]
    with pytest.raises(KeyError):
        synonym_map["new_time"] = ["TIME"]


def test_setitem_existing_synonym_different_primary_alias(synonym_map):
    synonym_map["time"] = ["Time", "TIME", "BJD TBD"]
    with pytest.raises(KeyError):
        synonym_map["new_time"] = ["Time"]


def test_get_rename_dict_inexistent(synonym_map):
    assert synonym_map.get_rename_dict("new_primary_alias") == {}


def test_get_rename_dict(synonym_map):
    synonym_map["time"] = ["Time", "BJD TBD"]
    assert synonym_map.get_rename_dict("time") == {"Time": "time", "BJD TBD": "time"}


def test_get_rename_dict_not_found(synonym_map):
    assert synonym_map.get_rename_dict("inexistent") == {}


def test_add_synonyms(synonym_map):
    synonym_map["time"] = ["Time", "BJD TBD"]
    synonym_map.add_synonyms("time", ["UTC", "UTC TBD"])
    assert synonym_map.get_rename_dict("time") == {
        "Time": "time",
        "BJD TBD": "time",
        "UTC": "time",
        "UTC TBD": "time",
    }


def test_remove_alias(synonym_map):
    # Add a primary alias and its synonyms
    synonym_map["time"] = ["Time", "BJD TBD", "UTC"]

    # Remove the primary alias
    del synonym_map["time"]

    # Ensure that the primary alias and its synonyms are no longer present
    assert "time" not in synonym_map
    assert synonym_map.get_rename_dict("time") == {}

    for synonym in ["Time", "BJD TBD", "UTC"]:
        assert synonym not in synonym_map


def test_remove_synonym(synonym_map):
    # Add a primary alias and its synonyms
    synonym_map["time"] = ["Time", "BJD TBD", "UTC"]

    # Remove one of the synonyms
    synonym_map.remove_synonym("time", "UTC")

    # Ensure that the synonym is no longer associated with the primary alias
    assert synonym_map.get_rename_dict("time") == {"Time": "time", "BJD TBD": "time"}

    # Ensure that the removed synonym is no longer present in the synonym map
    assert "UTC" not in synonym_map


def test_rename_primary_alias(synonym_map):
    synonym_map["time"] = ["Time", "BJD TBD"]
    synonym_map.rename_primary_alias("time", "TIME_RENAMED")
    assert "time" not in synonym_map
    assert "TIME_RENAMED" in synonym_map
    assert synonym_map.get_rename_dict("TIME_RENAMED") == {
        "Time": "TIME_RENAMED",
        "BJD TBD": "TIME_RENAMED",
        "time": "TIME_RENAMED",
    }


def test_update(synonym_map):
    synonym_map.update({"flux": ["Flux", "FLUX", "flux_value"], "temperature": ("Temp",)})
    assert "flux" in synonym_map
    assert "temperature" in synonym_map
    assert synonym_map.get_rename_dict("flux") == {
        "Flux": "flux",
        "FLUX": "flux",
        "flux_value": "flux",
    }
    assert synonym_map.get_rename_dict("temperature") == {"Temp": "temperature"}


def test_save_load_to_yaml(tmp_path):
    file_path = tmp_path / "synonym_map.yaml"
    synonym_map = SynonymMap()
    synonym_map["time"] = ["Time", "BJD TBD"]
    synonym_map.save_to_yaml(file_path)
    loaded_synonym_map = SynonymMap.load_from_yaml(file_path)
    assert loaded_synonym_map == synonym_map


@pytest.fixture
def synonym_map_lc():
    return SynonymMapLc()


def test_initialization_and_attribute_access(synonym_map_lc):
    assert isinstance(synonym_map_lc, SynonymMapLc)
    assert synonym_map_lc.light_curve_attributes.time == "BJD_TDB"
    assert synonym_map_lc.light_curve_attributes.flux == "rel_flux_T1_n"
    assert synonym_map_lc.light_curve_attributes.flux_err == "rel_flux_err_T1_n"


def test_add_synonyms_lc(synonym_map_lc):
    synonym_map_lc["BJD_TDB"] = ["time", "BJD", "BJD_TDB_MOBS", "#BJD_TDB"]
    assert synonym_map_lc.time == ("time", "BJD", "BJD_TDB_MOBS", "#BJD_TDB")


def test_remove_alias_and_synonym(synonym_map_lc):
    synonym_map_lc["time"] = ["Time", "BJD", "BJD_TDB", "#BJD_TDB"]
    del synonym_map_lc["time"]
    assert "time" not in synonym_map_lc
    assert synonym_map_lc.get_rename_dict("time") == {}

    synonym_map_lc.remove_synonym("BJD_TDB", "BJD")
    assert "BJD" not in synonym_map_lc.get_rename_dict("BJD_TDB")


def test_rename_alias(synonym_map_lc):
    synonym_map_lc["time"] = ["Time", "BJD", "BJD_TDB", "#BJD_TDB"]
    synonym_map_lc.rename_primary_alias("time", "time_renamed")
    assert synonym_map_lc.get_rename_dict("time_renamed") == {
        'Time': 'time_renamed',
        'BJD': 'time_renamed',
        'BJD_TDB': 'time_renamed',
        '#BJD_TDB': 'time_renamed',
        'time': 'time_renamed'
    }
    assert "time" not in synonym_map_lc

def test_yaml_serialization_deserialization(tmp_path):
    file_path = tmp_path / "synonym_map_lc.yaml"
    synonym_map_lc = SynonymMapLc(
        time="BJD_TDB", flux="rel_flux_T1_n", flux_err="rel_flux_err_T1_n"
    )
    synonym_map_lc.save_to_yaml(file_path)
    loaded_synonym_map_lc = SynonymMapLc.load_from_yaml(file_path)
    assert loaded_synonym_map_lc == synonym_map_lc


def test_load_from_default_config():
    synonym_map_lc = SynonymMapLc.load_from_config()
    assert isinstance(synonym_map_lc, SynonymMapLc)
    
    synonym_map_lc = SynonymMapLc.load_from_config(reset=True)
    assert isinstance(synonym_map_lc, SynonymMapLc)


def test_doctest():
    failures, _ = doctest.testmod(exofop.extract.synonym_map)  # type: ignore
    assert failures == 0
