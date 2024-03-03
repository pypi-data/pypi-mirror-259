from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace


class AbstractArgParser(ABC):

    @abstractmethod
    def init(self) -> None:
        """
        Initialisation function. it is called before update_arg_parser
        """
        raise NotImplementedError()

    @abstractmethod
    def update_arg_parser(self, parser: ArgumentParser) -> None:
        """
        This is opportunity for plugin to add command-line arguments definitions
        :param parser:
        """
        raise NotImplementedError()

    @abstractmethod
    def process_args(self, args: Namespace) -> bool:
        """
        This method provide ability for plugin to process and store data from command-line
        :param args: parsed command-line arguments
        :return: True if args are valid and indicate this class is active, False otherwise
        """
        raise NotImplementedError()
