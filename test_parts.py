from parts import Maze, Hall, Area
import pytest


def test_area_each_instance_has_increased_id():
    area_one = Area()
    area_two = Area()
    assert area_one.id < area_two.id


def test_hall_each_instance_has_increased_id():
    hall_one = Hall()
    hall_two = Hall()
    assert hall_one.id < hall_two.id


def test_maze_each_instance_has_increased_id():
    maze_one = Maze()
    maze_two = Maze()
    assert maze_one.id < maze_two.id


@pytest.mark.parametrize("has_portal", [True, False])
def test_area_is_portal_returns_area_portal_state(has_portal):
    assert Area(has_portal).is_portal == has_portal


@pytest.mark.parametrize("has_portal", [True, False])
def test_hall_is_path_returns_hall_path_state(has_portal):
    assert Hall([Area(has_portal)]).is_path == has_portal


def test_hall_joints_returns_external_areas():
    joint_area = Area()
    external = Area()
    joint_area.links.append(external)
    branch = Hall([joint_area, Area()])
    assert len(branch.joints) == 1
    assert (joint_area, external) in branch.joints
    assert external not in branch.areas


def test_maze_branches_returns_branch_list():
    branches = Maze([Hall([Area(False)])]).branches
    assert branches
    for branch in branches:
        assert branch.is_path is False


def test_maze_branches_without_branches_returns_emtpy_list():
    assert Maze([Hall([Area(True)])]).branches == []


def test_maze_paths_with_paths_returns_path_list():
    paths = Maze([Hall([Area(True)])]).paths
    assert paths
    for path in paths:
        assert path.is_path is True


def test_maze_paths_without_paths_returns_emtpy_list():
    assert Maze([Hall([Area(False)])]).paths == []
