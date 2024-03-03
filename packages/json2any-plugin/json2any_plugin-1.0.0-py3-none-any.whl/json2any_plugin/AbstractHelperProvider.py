from abc import abstractmethod, ABC
from typing import Callable, Dict


class AbstractHelperProvider(ABC):

    @abstractmethod
    def get_helpers(self) -> Dict[str, Callable]:
        raise NotImplementedError()


