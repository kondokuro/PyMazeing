"""
The magic messages that the mage gest when the spells fail
"""

class SpellError(Exception):
    """Receive a message why the spell failed."""
    pass

class SkillError(Exception):
    """Notice the mistake on the skill check."""
    pass
