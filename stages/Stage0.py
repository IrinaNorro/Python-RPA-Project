"""Example Producer stage of an RPA process.

This is a template to be used as the starting point for RPA development.
Replace all docstrings in this module with your own when implementing the stage
(including this one).
"""

from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Producer import Producer

from libraries.utils import debug, run_kw, get_variable, get_library
import json
import pandas as pd
from robot.api import logger
from robot.api.deco import keyword
from RPALibrary.stages.Producer import Producer


class Stage0(Producer):
    """Stage class inherits either RPALibrary.stages.Producer or RPALibrary.stages.Consumer
    and is named according to its place in the overall process sequence
    (starting from ``Stage0.py``, followed by ``Stage1.py`` etc.).

    Typically, the first stage (numbered 0) is a Producer.
    Implement ``process_data`` and, optionally, ``preloop_action``, ``postprocess_data`` for creating task objects.
    Call ``main loop`` from Robot script:

    .. code:: robotframework

        Library  ../stages/Stage0.py

        *** Tasks ***
        My Producer Stage
            [Tags]    stage_0
            [Setup]    Stage0.Setup
            Stage0.Main Loop
            [Teardown]    Stage0.Teardown
    """

    def __init__(self):
        super().__init__()
        # LADATAAN TIEDOSTO - download_url sijaitsee Resources/Settings.py
        self.download_url = get_variable("$download_url")

    def preloop_action(self):
        """Prefetch data to iterate in ``process_data``.
        This method should return a sequence (list, tuple) or a generator.

        Implementation is optional, but needed in most processes. See ``RPALibrary.stages.Producer`` for details.
        """
        #
        # READ EXCEL FILE
        df = pd.read_excel('./csv/challenge0.xlsx')

      # poistaa turhat välilyonnit (sukunimestä)
        df.columns = df.columns.str.replace(' ', '')
        # muuttaa excelin jsoniksi, dataframesta listan objekteja (pidä orient)
        result = df.to_json(orient="records")
        # lista json 10 objekteista jotta task storage pystyy käsittelee
        data = json.loads(result)
        return data

    def process_data(self, item):
        """Define how the data is turned into a task object.
        Task object(s) are created from the return value of this method.

        Implementation is mandatory. See ``RPALibrary.stages.Producer`` for details.
        """
        # palauttaa datalistan yhden alkion json objekteista
        # luo rivin csv:stä mongo db kantaan
       
        return item
