from typing import TYPE_CHECKING, NoReturn

from requests import Response, Session

from .abc import AbstractAPI

import json
from urllib.parse import urlencode, quote_plus


class SMSCAPIError(Exception):
    _response_not_ok = '''Запрос к {url} не выполнен.
    Статус код {status_code}.
    {error_message}'''
    _other_errors = '''{error_message}'''

    def __init__(
            self,
            error_message: str,
            status_code: None | int = None,
            url: None | str = None
    ):
        self._status_code = status_code
        self._error_message = error_message
        self._url = url

    def __str__(self) -> str:
        if self._status_code is None:
            return self._other_errors.format(
                error_message=self._error_message
            )
        else:
            return self._response_not_ok.format(
                url=self._url,
                status_code=self._status_code,
                error_message=self._error_message
            )


class SMSCAPI(AbstractAPI):
    __api_prefix__ = 'sys/'

    def __init__(
            self,
            login: str | None = None,
            password: str | None = None
    ):
        if login is None:
            raise SMSCAPIError(
                error_message='Не указан логин для доступа к API'
            )
        if password is None:
            raise SMSCAPIError(
                error_message='Не указан пароль для доступа к API'
            )
        self._domain = 'https://smsc.ru/'
        self._login = login
        self._password = password

        super().__init__(self)

    def request(
            self,
            method: str,
            http_method: str = 'GET',
            data: None | dict = None
    ) -> dict:

        url = self._domain + self.__api_prefix__ + method

        if data:
            data.update({'login': self._login, 'psw': self._password})
        else:
            raise SMSCAPIError(
                error_message='Не указаны параметры запроса'
            )

        with Session() as session:
            response = session.request(
                method=http_method,
                url=url,
                data=data,
            )

        response = self._validate_response(response)

        return response

    def json_request(
            self,
            method,
            http_method: str = 'GET',
            data: dict | list[dict] | None = None,
            headers: dict | None = None,
    ) -> dict | None:
        pass

    def _validate_response(
            self,
            response: Response,
    ) -> dict | NoReturn:
        if response.status_code == 200:
            return response.text
        else:
            raise SMSCAPIError(
                response.url,
                response.status_code,
                'Ошибка выполнения запроса'
            )


__all__ = ['SMSCAPI', 'SMSCAPIError']
