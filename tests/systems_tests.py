import pytest
from src.systems import TypedList


class TestTypedList:
    @pytest.mark.parametrize(
        "type, method, value, expected_result",
        [
            (int, "append", 1, [1]),
            (str, "append", "a", ["a"]),
            (int, "insert", 0, [0]),
            (str, "insert", "a", ["a"]),
            (int, "extend", [5, 6], [5, 6]),
            (str, "extend", ["a", "b"], ["a", "b"]),
        ],
    )
    def test_InsertionMethod_ValidItem_ItemIsAdded(
        self, type, method, value, expected_result
    ):
        typed_list = TypedList(type)
        getattr(typed_list, method)(value)
        assert typed_list == expected_result

    @pytest.mark.parametrize(
        "type, method, value, expected_result",
        [
            (str, "append", 1),
            (int, "append", "a"),
            (str, "insert", 0),
            (int, "insert", "a"),
            (str, "extend", [5, 6]),
            (int, "extend", ["a", "b"]),
        ],
    )
    def test_InsertionMethod_InvalidItem_RaisesTypeError(self, type, method, value):
        typed_list = TypedList(type)
        with pytest.raises(TypeError):
            getattr(typed_list, method)(value)
