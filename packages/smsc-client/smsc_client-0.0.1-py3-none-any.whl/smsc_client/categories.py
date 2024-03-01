from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from smsc_client.base import BaseCategory
from smsc_client.methods import DefaultCategory

if TYPE_CHECKING:
    from smsc_client.api import AbstractAPI


class APICategories:
    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    @property
    def default(self) -> DefaultCategory:
        return DefaultCategory(self.api)


__all__ = ['APICategories']
