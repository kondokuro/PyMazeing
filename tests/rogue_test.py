"""
Test to define and verify the rouge skills behaviour
"""
import pytest
import rogue
import wizard


@pytest.mark.parametrize("maze_params, expexted"[()])
def test_find_paths_returns_existing_paths(self, maze_params, expected):
    labyrinth = wizard.conjure_maze()
    maze_paths = rogue.find_paths(labyrinth)
    assert len(maze_paths) is expected, "too many or few paths found"


@pytest.mark.parametrize("maze_params, expexted"[()])
def test_detect_branches_returns_branching_halls(self, maze_params, expected):
    labyrinth = wizard.conjure_maze()
    beanches = rogue.detect_branches(labyrinth)


@pytest.mark.parametrize("maze_params, expexted"[()])
def test_track_portals_returns_available_portal_areas(self, maze_params, expected):
    labyrinth = wizard.conjure_maze()
    portals = rogue.track_portals(labyrinth)


@pytest.mark.parametrize("hall_params, expexted"[()])
def test_gather_coordinates_returns_coordinates_list(sefl, hall_params, expected):
    hall = wizard.summon_hall()
    coordinates = rogue.gather_coordinaes(hall)
    assert len(coordinates) is len(
        hall.areas), "too many or few coordinates found"
    # and loop thgough the hall areas and coordinates exist in the new list
