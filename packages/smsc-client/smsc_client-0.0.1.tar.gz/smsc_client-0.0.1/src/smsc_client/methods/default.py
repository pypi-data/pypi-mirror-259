from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any
from uuid import UUID

from smsc_client.base.category import BaseCategory

if TYPE_CHECKING:
    from smsc_client.base import AbstractAPI


def str_to_dict(raw_str: str, key_to_split_paires: str, key_to_split: str):
    splited_strs = raw_str.split(key_to_split_paires)
    output_dict = {}
    for splited_str in splited_strs:
        key, value = splited_str.split(key_to_split)
        output_dict.update({key: value})
    return output_dict


@dataclass
class SendResponse:
    OK: str
    ID: str


class DefaultCategory(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def send(
            self,
            phones: str,
            mes: str,
            id: UUID,
            sender: str,
            time: int = 0
    ) -> SendResponse:
        data = self.handle_parameters(locals())

        response = self.api.request(
            method='send.php',
            http_method='POST',
            data=data
        )

        response = str_to_dict(response, ', ', ' - ')

        return SendResponse(**response)
