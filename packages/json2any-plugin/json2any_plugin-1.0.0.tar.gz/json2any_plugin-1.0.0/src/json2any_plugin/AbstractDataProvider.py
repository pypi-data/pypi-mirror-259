from abc import abstractmethod
from typing import Any, Dict

from json2any_plugin.AbstractArgParser import AbstractArgParser

DATA_KEY_RUN_DATA = "run_data"
DATA_KEY_QUERY = "query"
DATA_KEY_RUN = "run"
DATA_KEY_RUNS = "runs"
FORBIDDEN_KEYS = [DATA_KEY_QUERY, DATA_KEY_RUN, DATA_KEY_RUNS]


class AbstractDataProvider(AbstractArgParser):

    @abstractmethod
    def load_data(self) -> Dict[str, Any]:
        """
        loads the data for template.
        Do not use the "FORBIDDEN_KEYS"
        :return Dict[str, Any]: the data for template. This dictionary will be "mounted" at "root" in template,
         along with the "DATA_KEY_XXX" data. Do not use the "FORBIDDEN_KEYS" as keys in returned data.
        """
        raise NotImplementedError()
