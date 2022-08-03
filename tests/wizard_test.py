"""
Tests to define and verify the wizard spells behaviour
"""
import pytest
from src.characters import wizard
from src.maze import sections


class SumonHallTests:

    def test_defaul_casting_returns_single_portal_room(self):
        hall = wizard.summon_hall()
        assert len(hall.areas) is 1, "Hall has more than one area"
        assert isinstance(
            hall.areas[0].portal, sections.Portal), "The portal is not a portal"
        assert hall.areas[0].coordinates is (
            0, 0), "Hall starting point is not the origin"

    @pytest.mark.parametrize("length", [(0), (-1), (-8)])
    def test_requested_lenght_is_less_than_one_raises_spell_error(self, length):
        with pytest.raises(wizard.SpellError):
            hall = wizard.summon_hall(length)

    def test_new_hall_has_no_space_raisess_spell_error(self):
        # make a hall where all the areas will occupy the new hall available space
        surrounding_hall = sections.Hall()
        surrounding_hall.areas = sections.Area(0, 0), sections.Area()
        with pytest.raises(wizard.SpellError):
            hall = wizard.summon_hall()

    def test_starting_poin_is_occupied_raisess_spell_error(self):
        with pytest.raises(wizard.SpellError):
            hall = wizard.summon_hall()

    @pytest.mark.parametrize("", [()])
    def test_new_hall_has_required_number_of_portals(self):
        pass

    @pytest.mark.parametrize("", [()])
    def test_too_many_portals_raises_spell_error(self):
        with pytest.raises(wizard.SpellError):
            hall = wizard.summon_hall()

    @pytest.mark.parametrize("", [()])
    def test_new_hall_has_required_length(self):
        pass

    @pytest.mark.parametrize("length, portals, branching, occupied",
                             [(2,      True,    False, ),
                              (5,      False,   True, ),
                              (8,      True,    True, )])
    def test_of_size_and_any_endpoint_returns_path_of_set_size(
            length, portals, branching, occupied):
        hall = wizard.summon_hall(length, portals, branching, occupied)
        assert len(hall.areas) == length


class ConjureMazeTests:
    def test_default_casting_returns_one_room_maze():
        one_room = wizard.conjure_maze()
        assert len(one_room.halls) == 1, "maze has too many halls"
        #assert len(one_room.paths) == 1, "maze has too many paths"
        #assert len(one_room.branches) == 0, "maze has a branch"

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
    def test_multiple_branches_returns_correct_maze(
            portal_cnt, hall_cnt, branching_limit, min_length, max_length):
        labyrinth = wizard.conjure_maze(
            portal_cnt, hall_cnt, branching_limit, (min_length, max_length))
        # "halls created where out of bound")
        # "not all halls are connected")
        # "length of halls was outside of bound")
        # "an area had more links than allowed")
        # "resulting maze had no paths"
        # "made too many portals"
