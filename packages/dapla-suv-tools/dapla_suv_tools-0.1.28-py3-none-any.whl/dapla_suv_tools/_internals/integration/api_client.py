import inspect
import os

import requests

from dapla_suv_tools._internals.integration import user_tools
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util import constants

END_USER_API_BASE_URL = os.getenv("SUV_END_USER_API_URL")


def _get(path: str, context: SuvOperationContext) -> str:
    headers = _get_headers(context)

    response = requests.get(f"{END_USER_API_BASE_URL}{path}", headers=headers)

    return _handle_response(response=response, context=context)


def _post(path: str, body_json: str, context: SuvOperationContext) -> str:
    headers = _get_headers(context)

    response = requests.post(url=f"{END_USER_API_BASE_URL}{path}", headers=headers, data=body_json)

    return _handle_response(response=response, context=context)


def _delete(path: str, context: SuvOperationContext) -> str:
    headers = _get_headers(context)

    response = requests.delete(url=f"{END_USER_API_BASE_URL}{path}", headers=headers)

    return _handle_response(response, context=context)


def _handle_response(response: requests.Response, context: SuvOperationContext) -> str:

    called = _get_caller(2)
    caller = _get_caller(3)

    msg = f"calling '{called}' from '{caller}'."

    if not _success(response.status_code):
        error = response.content.decode("UTF-8")
        ex = Exception(f"Failed call to api while {msg}.")
        context.set_error(f"Error (status: {response.status_code}) {msg}:  {error}", ex)
        raise ex

    context.log(level=constants.LOG_DIAGNOSTIC, operation=called, message=msg)

    return response.content.decode("UTF-8")


def _get_headers(context: SuvOperationContext) -> dict:
    token: str = user_tools.get_access_token(context)

    return {
        "authorization": f"Bearer {token}",
        "content-type": "application/json"
    }


def _get_caller(depth: int) -> str:
    frames = inspect.stack()
    caller = frames[depth]
    return caller.function


def _success(status_code: int) -> bool:
    return str(status_code).startswith("2")
