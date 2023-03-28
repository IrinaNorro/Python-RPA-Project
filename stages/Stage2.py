"""Example Consumer stage of an RPA process.

This is a template to be used as the starting point for RPA development.
Replace all docstrings in this module with your own when implementing the stage
(including this one).
"""

from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Consumer import Consumer

from libraries.utils import debug, run_kw, get_variable, get_library


class Stage2(Consumer):
    """Stage class inherits either RPALibrary.stages.Producer or RPALibrary.stages.Consumer
    and is named according to its place in the overall process sequence
    (starting from ``Stage0.py``, followed by ``Stage1.py`` etc.).

    Typically, stages following the first one (numbered 1 and upwards) are Consumers.
    Implement ``main_action`` and, optionally, ``pre_action`` and ``post_action`` for handling task objects.
    Call ``main loop`` from Robot script:

    .. code:: robotframework

        Library  ../stages/Stage0.py

        *** Tasks ***
        My Consumer stage
            [Tags]    stage_1
            [Setup]    Stage1.Setup
            Stage1.Main Loop
            [Teardown]    Stage1.Teardown
    """

    def main_action(self, to):
        """Define the main workflow for consuming task objects.

        Implementation is mandatory. See ``RPALibrary.stages.Consumer`` for details.
        """
        raise NotImplementedError

   