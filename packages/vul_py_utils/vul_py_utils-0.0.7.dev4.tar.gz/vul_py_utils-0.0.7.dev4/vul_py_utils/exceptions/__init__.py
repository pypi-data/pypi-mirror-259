from typing import Tuple, Union

from ..exceptions.custom import VulcanBaseError

        
def map_internal_server_error_to_exception(exception: VulcanBaseError) -> Tuple[Union[int, str], str, int]:
    """ First, function will look up at the defined error_map in InternalServerError class
    Then, it will return the code, default_message, and http_status_code of the exception

    Args:
        exception (VulcanBaseError): a VulcanBaseError object in InternalServerError class

    Returns:
        Tuple[int, str, int]: code, default_message, and http_status_code of the exception
    """
    return exception.code, exception.default_message, exception.http_status_code