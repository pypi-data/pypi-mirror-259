"""Tests for the reference module.
"""

from torus.schema.reference import Reference


class TestReference:
    """Tests for reference elements"""

    def test_create(self):
        """Test creating a reference element"""
        ref = Reference(ref_type="test")
        assert isinstance(ref, Reference)
