"""
Test to define and verify the rouge skills behaviour
"""
import pytest
from src.characters import rogue
from src.characters import wizard
from src.pymaze import sections


def _create_areas(count=1) -> list[sections.Area]:
    return [sections.Area((0, i)) for i in count]


@pytest.mark.parametrize("expected, maze_params",
                         [(1, [1, ]), (1, [1, 2, ])])
def test_find_paths_returns_all_existing_paths(expected, maze_params):
    labyrinth = wizard.conjure_maze(*maze_params)
    maze_paths = rogue.find_paths(labyrinth)
    assert len(maze_paths) is expected, "too many or few paths found"


@pytest.mark.parametrize("maze_params, expected", [(1, 1), ])
def test_detect_branches_returns_branching_halls(maze_params, expected):
    labyrinth = wizard.conjure_maze()
    beanches = rogue.detect_branches(labyrinth)


@pytest.mark.parametrize("maze_params, expected", [(1, 1), ])
def test_track_portals_returns_available_portal_areas(maze_params, expected):
    labyrinth = wizard.conjure_maze()
    portals = rogue.track_portals(labyrinth)


@pytest.mark.parametrize("hall_params, expected", [(1, 1), ])
def test_gather_coordinates_returns_coordinates_list(hall_params, expected):
    hall = wizard.summon_hall()
    coordinates = rogue.gather_coordinaes(hall)
    assert len(coordinates) is len(
        hall.areas), "too many or few coordinates found"
    # and loop thgough the hall areas and coordinates exist in the new list
