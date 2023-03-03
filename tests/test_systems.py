import pytest
from src.systems import TypedList, Size, Coordinate


class TestForCoordinate:
    def test_OnInstantiation_NoParameters_ReturnsOriginCoordinate(self):
        origin = Coordinate()
        assert origin.x == 0 and origin.y == 0 and origin.z == 0

    def test_OnInstantiation_AnyParameter_ReturnsACoordinate(self):
        location = Coordinate(1, 2, 3)
        assert isinstance(location, Coordinate)

    def test_IsEqual_SameCoordinateValues_ReturnsTrue(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(1, 2, 3)
        assert a == b

    def test_IsEqual_DifferentCoordinateValues_ReturnsFalse(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(4, 5, 6)
        assert a != b

    def test_IsEqual_DifferentType_ReturnsFalse(self):
        a = Coordinate(1, 2, 3)
        b = (1, 2, 3)
        assert a != b


class TestForSize:
    def test_OnInstantiation_NoParameters_RetusnsMinimumSize(self):
        minimum = Size()
        assert minimum.length == 1 and minimum.height == 1 and minimum.width == 1

    def test_OnInstantiation_AnyParameterIsPositive_ReturnsASize(self):
        location = Size(1, 2, 3)
        assert isinstance(location, Size)

    @pytest.mark.parametrize("parameters", [(-1, 0, 0), (0, -2, 0), (0, 0, -3)])
    def test_OnInstantiation_AnyParameterIsNegative_RaisesValueError(self, parameters):
        with pytest.raises(ValueError):
            Size(*parameters)

    def test_IsEqual_SameSizeValues_ReturnsTrue(self):
        a = Size(1, 2, 3)
        b = Size(1, 2, 3)
        assert a == b

    def test_IsEqual_DifferentSizeValues_ReturnsFalse(self):
        a = Size(1, 2, 3)
        b = Size(4, 5, 6)
        assert a != b

    def test_IsEqual_DifferentType_ReturnsFalse(self):
        a = Size(1, 2, 3)
        b = (1, 2, 3)
        assert a != b

    def test_IsLonger_InstanceIsSmaller_ReturnsFalse(self):
        this = Size(2, 8, 8)
        than_this = Size(8, 2, 2)
        assert not this.is_longer(than_this)

    def test_IsLonger_InstanceIsBigger_ReturnsTrue(self):
        this = Size(8, 2, 2)
        than_this = Size(2, 8, 8)
        assert this.is_longer(than_this)

    def test_IsLonger_TypeMismatch_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Size().is_longer(9)

    def test_IsWhider_InstanceIsSmaller_ReturnsFalse(self):
        this = Size(4, 1, 4)
        than_this = Size(4, 9, 4)
        assert not this.is_whider(than_this)

    def test_IsWhider_InstanceIsBigger_ReturnsTrue(self):
        this = Size(4, 9, 4)
        than_this = Size(4, 1, 4)
        assert this.is_whider(than_this)

    def test_IsWhider_TypeMismatch_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Size().is_whider(9)

    def test_IsTaller_InstanceIsSmaller_ReturnsFalse(self):
        this = Size(1, 1, 2)
        than_this = Size(1, 1, 6)
        assert not this.is_taller(than_this)

    def test_IsTaller_InstanceIsBigger_ReturnsTrue(self):
        this = Size(1, 1, 6)
        than_this = Size(1, 1, 2)
        assert this.is_taller(than_this)

    def test_IsTaller_TypeMismatch_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Size().is_taller(9)

    def test_SetLength_NegativeValue_RaisesValurError(self):
        size = Size()
        with pytest.raises(ValueError):
            size.length = -2

    def test_SetWidth_NegativeValue_RaisesValurError(self):
        size = Size()
        with pytest.raises(ValueError):
            size.width = -2

    def test_SetHeigth_NegativeValue_RaisesValurError(self):
        size = Size()
        with pytest.raises(ValueError):
            size.height = -2


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
