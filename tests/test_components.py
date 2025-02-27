import pytest
from src.components import Area, Maze, Coordinate



class TestForArea:

    def test_new_area_position_is_not_coordinate_raises_type_error(self):
        with pytest.raises(TypeError):
            Area((1, 2, 3))

    def test_repr_no_portal_returns_position(self):
        area = Area(Coordinate(1, 2, 3))
        assert repr(area) == f"Area at {area.position}"

    def test_repr_with_portal_includes_portal_details(self):
        area = Area(Coordinate(1, 2, 3), with_portal=True)
        assert repr(area) == f"Area at {area.position} with portal"


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_ocupied_spaces_returns_coordinates_of_maze_areas(self):
        self.test_maze.areas[Coordinate(1, 2, 3)] = Area(Coordinate(1, 2, 3))
        assert all(isinstance(c, Coordinate) for c in self.test_maze.occupied_spaces)

    def test_portals_returns_empty_list_when_no_portals(self):
        assert self.test_maze.portals == []
    
    @pytest.mark.parametrize("expected", [1, 3, 12])
    def test_portals_returns_areas_maked_as_having_portals(self, expected):
        for i in range(expected):
            self.test_maze.areas[Coordinate(i, 2, 3)] = Area(Coordinate(i, 2, 3), with_portal=True)
            
        assert all(isinstance(a, Area) for a in self.test_maze.portals)
        assert len(self.test_maze.portals) == expected
