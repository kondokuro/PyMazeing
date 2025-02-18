import pytest
from src.core import Size, Coordinate


class TestForCoordinate:
    def test_new_coordinate_default_returns_origin_cordinates(self):
        origin = Coordinate()
        assert origin.x == 0 and origin.y == 0 and origin.z == 0

    def test_equality_both_have_same_values_returns_true(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(1, 2, 3)
        assert a == b

    def test_equality_any_value_difference_returns_false(self):
        a = Coordinate(1, 2, 3)
        b = Coordinate(4, 5, 6)
        assert a != b

    def test_equality_different_types_returns_false(self):
        a = Coordinate(1, 2, 3)
        b = (1, 2, 3)
        assert a != b


class TestForSize:
    def test_OnInstantiation_NoParameters_RetusnsMinimumSize(self):
        minimum = Size()
        assert minimum.length == 1 and minimum.height == 1 and minimum.width == 1

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
            Size().is_longer(9) # type: ignore
            
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
            Size().is_whider(9)  # type: ignore
            
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
            Size().is_taller(9)  # type: ignore
            
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
