import pytest
from src.components import SpatialContainer
from src.systems import Coordinate, Size


class TestForSpatialContainer:
    def test_Ininitalization_HolderIsNotSpatialContainer_RaisesTypeError(self):
        with pytest.raises(TypeError):
            SpatialContainer("invalid", Coordinate(1, 2, 3), Size(2, 2, 2), [])
