import allure
import dataclasses
import requests
from requests.models import Response
from typing import Type, Union

from integration.tests.basic.model.model import JsonRpcErrorResponse, JsonRpcRequest, JsonRpcResponse


class JsonRpcRequester:
    def __init__(self, proxy_url: str):
        self._url = proxy_url
        self._session = requests.Session()

    @allure.step("requesting Json-RPC")
    def request_json_rpc(self, data: JsonRpcRequest) -> Response:
        return self._session.post(self._url, json=dataclasses.asdict(data))

    # TODO: deserialize subobject
    # @allure.step("deserializing response from JSON as model ot type {2}")
    def deserialize_response(
            self,
            response: Response,
            type: Type = None) -> Union[JsonRpcResponse, JsonRpcErrorResponse]:
        str_data = self.stringify(response.json())
        if 'result' in str_data:
            return self.deserialize_successful_response(response=response,
                                                        type=type)
        elif 'error' in str_data:
            return JsonRpcErrorResponse(**response.json())
        else:
            return JsonRpcErrorResponse(**response.json())

    @allure.step('deserializing response from JSON as model ot type {0}')
    def deserialize_successful_response(self, response: Response,
                                        type: Type) -> JsonRpcResponse:
        json_rpc_response = JsonRpcResponse(**response.json())
        if type == None:
            return json_rpc_response

        result_dict = dict(json_rpc_response.result)
        result_subobject = type.from_dict(result_dict)
        json_rpc_response.result = result_subobject
        return json_rpc_response

    @allure.step("showing as JSON")
    def stringify(self, data) -> str:
        return str(data)