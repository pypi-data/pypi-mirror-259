"""ORM Implementation for the TORUS Reference Element
"""


class Reference:
    """ORM Implementation for the TORUS Reference Element
    """

    def __init__(self, ref_type: str, **kwargs):
        """Initialize the Reference Element

        Args:
            ref_type (str): The type of reference
        """
        self.ref_type = ref_type
        self.kwargs = kwargs
