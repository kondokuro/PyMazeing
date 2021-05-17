from sections import Maze, Hall, Area
import pytest


def test_area_each_instance_has_increased_id():
    area_one = Area()
    area_two = Area()
    assert area_one.id < area_two.id


@pytest.mark.parametrize("has_portal", [True, False])
def test_area_is_portal_returns_area_portal_state(has_portal):
    assert Area(has_portal).is_portal == has_portal


def test_hall_each_instance_has_increased_id():
    hall_one = Hall()
    hall_two = Hall()
    assert hall_one.id < hall_two.id


@pytest.mark.parametrize("has_portal", [True, False])
def test_hall_is_path_returns_hall_path_state(has_portal):
    hall = Hall()
    hall.add_area(has_portal)
    assert hall.is_path == has_portal


def test_hall_add_area_with_portal_adds_a_portal():
    hall = Hall()
    hall.add_area(with_portal=True)
    assert hall.portals


def test_hall_add_area_new_linked_area_added_at_end():
    hall = Hall()
    hall.add_area()
    hall.add_area()
    assert hall.areas[1] in hall.areas[0].links
    assert hall.areas[0] in hall.areas[1].links
    assert hall.areas[0].id < hall.areas[1].id
    for room in hall.areas:
        assert hall == room.hall


def test_hall_passages_returns_external_areas():
    external = Area()
    branch = Hall()
    branch.add_area(entrance=external)
    joint_area = branch.areas[0]
    assert len(branch.passages) == 1
    assert (joint_area, external) in branch.passages
    assert external not in branch.areas


def test_maze_each_instance_has_increased_id():
    maze_one = Maze()
    maze_two = Maze()
    assert maze_one.id < maze_two.id


def test_maze_branches_returns_branch_list():
    branches = Maze([Hall(), Hall(), Hall()]).branches
    assert branches
    for branch in branches:
        assert branch.is_path is False


def test_maze_branches_without_branches_returns_emtpy_list():
    path = Hall()
    path.add_area(True)
    assert Maze([path]).branches == []


def test_maze_paths_with_paths_returns_path_list():
    a_path = Hall()
    a_path.add_area(True)
    paths = Maze([a_path]).paths
    assert paths
    for path in paths:
        assert path.is_path is True


def test_maze_paths_without_paths_returns_emtpy_list():
    assert Maze([Hall(), Hall(), Hall()]).paths == []
