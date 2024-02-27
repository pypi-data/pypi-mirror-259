class VulcanBaseError(Exception):
    code: int
    default_message: str
    http_status_code: int
    extra_message: str
    
    def __init__(self, code: int, default_message: str, http_status_code: int):
        self.code = code
        self.default_message = default_message
        self.http_status_code = http_status_code
        
def map_internal_server_error_to_exception(exception: VulcanBaseError) -> tuple:
    """ First, function will look up at the defined error_map in InternalServerError class
    Then, it will return the code, default_message, and http_status_code of the exception

    Args:
        exception (VulcanBaseError): a VulcanBaseError object in InternalServerError class

    Returns:
        Tuple[int, str, int]: code, default_message, and http_status_code of the exception
    """
    return exception.code, exception.default_message, exception.http_status_code