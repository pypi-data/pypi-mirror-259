import doctest

import exofop
import pytest
from exofop.download.identifiers import (
    TIC,
    TOI,
    InvalidTICError,
    InvalidTOIError,
    System,
)


def test_system():
    system = System("TIC 123456789")
    assert system.target == "123456789"
    assert system.tic.id == "123456789"

    system = System("TOI 1234.01")
    assert system.target == "TOI1234.01"
    assert system.toi.id == "TOI1234.01"


def test_tic_from_string():
    tic = TIC("123456789")
    assert tic.id == "123456789"
    assert not tic.exists()

    tic = TIC("TIC 123456789")
    assert tic.id == "123456789"


def test_invalid_toi_string():
    with pytest.raises(InvalidTOIError):
        TOI("invalid_id")


def test_invalid_tic_string():
    with pytest.raises(InvalidTICError):
        TIC("invalid_id")


def test_toi_from_string():
    toi = TOI("1234.01")
    assert toi.id == "TOI1234.01"
    assert not toi.exists()

    toi = TOI("TOI 1234.01")
    assert toi.id == "TOI1234.01"


def test_toi_planet_and_system_property():
    toi = TOI("1234.01")
    assert toi.planet == "01"
    assert toi.system == "1234"


def test_tic_to_toi():
    tic = TIC(254113311)
    assert tic.to_toi().id == TOI(1130).id


def test_toi_to_tic():
    toi = TOI(1130)
    toi.to_tic()
    assert toi.to_tic().id == TIC(254113311).id


def test_system_lookup():
    system = System("TOI 1130")
    assert system.get_tic().id == "254113311"

    system = System("TIC 254113311")
    assert system.get_toi().id == "TOI1130"


def test_system_autocomplete():
    system = System("TOI 1130")
    assert system.autocomplete()

    system = System("TIC 254113311")
    assert system.autocomplete()


def test_doctest():
    failures, _ = doctest.testmod(exofop.download.identifiers)  # type: ignore
    assert failures == 0
