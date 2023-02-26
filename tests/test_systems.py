import pytest
from src.systems import TypedList, Size, Coordinate


class TestForCoordinate:
    def test_OnInstantiation_AnyParameterIsPositive_ReturnsACoordinate(self):
        location = Coordinate(1, 2, 3)
        assert isinstance(location, Coordinate)

    def test_OnComparizon_SameCoordinateValues_ReturnsTrue(self):
        a = Coordinate(1,2,3)
        b = Coordinate(1,2,3)
        assert a == b

    def test_OnComparizon_DifferentCoordinateValues_ReturnsFalse(self):
        a = Coordinate(1,2,3)
        b = Coordinate(4,5,6)
        assert a != b

    def test_OnComparizon_DifferentType_ReturnsFalse(self):
        a = Coordinate(1,2,3)
        b = (1,2,3)
        assert a != b


class TestForSixe:
    def test_OnInstantiation_AnyParameterIsPositive_ReturnsASize(self):
        location = Size(1, 2, 3)
        assert isinstance(location, Size)

    @pytest.mark.parametrize("parameters", [(-1, 0, 0), (0, -2, 0), (0, 0, -3)])
    def test_OnInstantiation_AnyParameterIsNegative_RaisesValueError(self, parameters):
        with pytest.raises(ValueError):
            Size(*parameters)


class TestForTypedList:
    @pytest.mark.parametrize(
        "class_type, method, value, expected_result",
        [
            (int, "append", [1], [1]),
            (str, "append", ["a"], ["a"]),
            (int, "insert", [0, 1], [1]),
            (str, "insert", [0, "a"], ["a"]),
            (int, "extend", [[5, 6]], [5, 6]),
            (str, "extend", [["a", "b"]], ["a", "b"]),
        ],
    )
    def test_AnyInsertionMethod_ValidItem_ItemIsAdded(
        self, class_type, method, value, expected_result
    ):
        typed_list = TypedList(class_type)
        getattr(typed_list, method)(*value)
        assert typed_list == expected_result

    @pytest.mark.parametrize(
        "class_type, method, value",
        [
            (str, "append", [1]),
            (int, "append", ["a"]),
            (str, "insert", [0, 1]),
            (int, "insert", [0, "a"]),
            (str, "extend", [[5, 6]]),
            (int, "extend", [["a", "b"]]),
        ],
    )
    def test_AnyInsertionMethod_InvalidItem_RaisesTypeError(
        self, class_type, method, value
    ):
        typed_list = TypedList(class_type)
        with pytest.raises(TypeError):
            getattr(typed_list, method)(*value)
