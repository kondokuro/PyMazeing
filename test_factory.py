import factory
from parts import Area, Hall
import pytest


def __make_test_area(area: Area, connections: int):
    for i in range(connections):
        area.links.append(Area())
    return area


def test_connect_areas_both_areas_are_each_others_link():
    area = Area()
    room = Area()
    factory._connect_areas(area, room)
    assert room in area.links
    assert area in room.links


def test_areas_to_link_returns_all_areas_within_limit():
    test_branches = [
        Hall([__make_test_area(Area(), 4), __make_test_area(Area(True), 2)]),
        Hall([__make_test_area(Area(), 4), __make_test_area(Area(), 2)])
    ]
    assert len(factory._get_open_joints(test_branches, 4)) == 2


def test_make_hall_returned_branch_areas_are_connected():
    branch = factory._make_hall(4)
    for area in branch.areas:
        assert area.links
        for link in area.links:
            assert link in branch.areas


@pytest.mark.parametrize(
    "length, with_entrance, with_exit", [(2, True, False), (5, False, True), (7, True, True)])
def test_make_hall_of_size_and_any_endpoint_returns_path_of_set_size(length, with_entrance, with_exit):
    path = factory._make_hall(length, has_start=with_entrance, has_end=with_exit)
    assert path.is_path
    if with_entrance and with_exit:
        assert len(path.portals) == 2
    else:
        assert len(path.portals) == 1
    if with_entrance:
        assert path.areas[0].is_portal
    if with_exit:
        assert path.areas[-1].is_portal
    assert len(path.areas) == length


@pytest.mark.parametrize(
    "as_portal, with_start, with_end",
    [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True), 
    ])
def test_make_hall_branching_from_area_links_area_to_branch(as_portal, with_start, with_end):
    connected_area = Area(as_portal)
    branch = factory._make_hall(3, connected_area, with_start, with_end)
    assert connected_area in branch.joints
    assert connected_area not in branch.areas
    assert connected_area.links[0] in branch.areas
    if with_start or with_end:
        assert branch.is_path
        assert branch.portals


def test_create_maze_default_returns_one_room_maze():
    one_room = factory.create_maze()
    assert len(one_room.halls) == 1, "maze has too many halls"
    assert len(one_room.paths) == 1, "maze has too many paths"
    assert len(one_room.branches) == 0, "maze has a branch"


@pytest.mark.parametrize(
    "portal_cnt, hall_cnt, branching_limit, min_length, max_length",
    [
        (1, 1, 2, 4, 5),
        (2, 1, 2, 4, 5),
        (1, 2, 3, 4, 5),
        (2, 8, 4, 5, 9),
        (3, 6, 9, 2, 6),
        (6, 2, 9, 2, 2),
    ])
def test_create_maze_multiple_branches_returns_correct_maze(
        portal_cnt, hall_cnt, branching_limit, min_length, max_length):
    labyrinth = factory.create_maze(portal_cnt, hall_cnt, branching_limit, (min_length, max_length))

    assert len(labyrinth.halls) == hall_cnt, "halls created where out of bound"

    hall_joints = [hall for hall in labyrinth.halls if hall.joints]
    if hall_joints:
        assert len(hall_joints) == len(labyrinth.halls), "not all halls are connected"

    for hall in labyrinth.halls:
        assert min_length <= len(hall.areas) <= max_length, "length of halls was outside of bound"
        for area in hall.areas:
            assert len(area.links) <= branching_limit, "an area had more links than allowed"

    assert labyrinth.paths, "resulting maze had no paths"

    portals_made = []
    for hall in labyrinth.paths:
        for area in hall.areas:
            if area.is_portal:
                portals_made.append(area)
    assert len(portals_made) <= portal_cnt, "made too many portals"
