"""
Tests to define and verify the wizard spells behaviour
"""
import pytest
import wizard


def test_sumon_hall_defaul_casting_returns_single_portal_room(self):
    pass

def test_sumon_hall_lenght_is_too_small_returns_spell_error(self):
    pass

def test_sumon_hall_branching_area_is_fully_branched_returns_spell_error(self):
    pass

def test_sumon_hall_new_hall_has_no_space_returns_spell_error(self):
    pass

def test_sumon_hall_new_hall_has_required_number_of_portals(self):
    pass

def test_sumon_hall_

@pytest.mark.parametrize(
    "length, with_entrance, with_exit",
    [
        (2, True, False),
        (5, False, True),
        (8, True, True)
    ])
def test_summon_hall_of_size_and_any_endpoint_returns_path_of_set_size(
        length, with_entrance, with_exit):
    hall = wizard._summon_hall(
        length, has_start=with_entrance, has_end=with_exit)

    assert hall.is_path
    assert len(hall.areas) == length

    if with_entrance:
        assert hall.areas[0].is_portal

    if with_exit:
        assert hall.areas[-1].is_portal

    if with_entrance and with_exit:
        assert len(hall.portals) == 2
    else:
        assert len(hall.portals) == 1
        assert len(hall.portals) == 1


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
def test_summon_hall_branching_from_area_links_area_to_branch(
        as_portal, with_start, with_end):
    connected_area = wizard._summon_area(as_portal)
    branch = wizard._summon_hall(3, connected_area, with_start, with_end)
    assert connected_area in branch.passages[0]
    assert connected_area not in branch.areas
    assert connected_area.links[0] in branch.areas

    if with_start or with_end:
        assert branch.is_path
        assert branch.portals


def test_cast_maze_default_returns_one_room_maze():
    one_room = wizard.cast_maze()
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
def test_cast_maze_multiple_branches_returns_correct_maze(
        portal_cnt, hall_cnt, branching_limit, min_length, max_length):
    labyrinth = wizard.cast_maze(
        portal_cnt, hall_cnt, branching_limit, (min_length, max_length))

    assert (len(labyrinth.halls) == hall_cnt,
            "halls created where out of bound")

    hall_joints = [hall for hall in labyrinth.halls if hall.passages]
    if hall_joints:
        assert (len(hall_joints) == len(labyrinth.halls),
                "not all halls are connected")

    for hall in labyrinth.halls:
        assert (min_length <= len(hall.areas) <= max_length,
                "length of halls was outside of bound")
        for area in hall.areas:
            assert (len(area.links) <= branching_limit,
                    "an area had more links than allowed")

    assert labyrinth.paths, "resulting maze had no paths"

    portals_made = []
    for hall in labyrinth.paths:
        for area in hall.areas:
            if area.is_portal:
                portals_made.append(area)
    assert len(portals_made) <= portal_cnt, "made too many portals"
