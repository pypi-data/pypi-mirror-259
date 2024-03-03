from abc import abstractmethod

from jinja2 import BaseLoader

from json2any_plugin.AbstractArgParser import AbstractArgParser


class AbstractTemplateProvider(AbstractArgParser):

    @abstractmethod
    def get_loader(self) -> BaseLoader:
        raise NotImplementedError()

