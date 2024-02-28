from typing import Tuple, Union

from fastapi.responses import JSONResponse
from ..response2client import to_json_error_response


class VulcanBaseError():
    code: Union[int, str]
    default_message: str
    http_status_code: int
    extra_message: str
    internal_log_message: str
    
    def __init__(self, code: Union[int, str], default_message: str, http_status_code: int):
        self.code = code
        self.default_message = default_message
        self.http_status_code = http_status_code
        
class VulcanBaseException(Exception, VulcanBaseError):    
    def __init__(self, extra_detail: str = "", internal_log_message: str = ""):
        self.extra_message = extra_detail
        self.internal_log_message = internal_log_message
        
def map_internal_server_error_to_exception(exception: VulcanBaseError) -> Tuple[Union[int, str], str, int]:
    """ First, function will look up at the defined error_map in InternalServerError class
    Then, it will return the code, default_message, and http_status_code of the exception

    Args:
        exception (VulcanBaseError): a VulcanBaseError object in InternalServerError class

    Returns:
        Tuple[int, str, int]: code, default_message, and http_status_code of the exception
    """
    return exception.code, exception.default_message, exception.http_status_code

def handle_vulcan_exception(exception: VulcanBaseException) -> JSONResponse:
    """ This middleware handler will handle the VulcanBaseException and return a JSONResponse

    Args:
        exception (VulcanBaseException): _description_

    Returns:
        JSONResponse: _description_
    """
    return to_json_error_response(exception)