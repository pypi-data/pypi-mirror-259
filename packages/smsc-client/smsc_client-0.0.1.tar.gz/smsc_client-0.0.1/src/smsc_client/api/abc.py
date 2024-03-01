from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, NoReturn

if TYPE_CHECKING:
    from requests import Response

from smsc_client.categories import APICategories


class AbstractAPI(ABC, APICategories):
    @abstractmethod
    def request(
            self,
            method: str,
            http_method: str = 'GET',
            data: None | dict = None,
    ) -> None | dict:
        pass

    @abstractmethod
    def json_request(
        self,
        method,
        http_method: str = 'GET',
        data: None | dict = None,
    ) -> None | dict:
        pass

    @abstractmethod
    def _validate_response(
            self,
            response: "Response"
    ) -> (None | dict) | NoReturn:
        pass


__all__ = ['AbstractAPI']
