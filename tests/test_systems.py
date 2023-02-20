import pytest
from src.systems import TypedList


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
    def test_InsertionMethod_ValidItem_ItemIsAdded(
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
    def test_InsertionMethod_InvalidItem_RaisesTypeError(
        self, class_type, method, value
    ):
        typed_list = TypedList(class_type)
        with pytest.raises(TypeError):
            getattr(typed_list, method)(*value)
