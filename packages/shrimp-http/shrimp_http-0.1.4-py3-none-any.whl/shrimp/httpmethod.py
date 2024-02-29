from enum import Enum
from .errors import InvalidMethodError

__all__ = ("HttpMethod", "http_method_from_str")


class HttpMethod(Enum):
    GET = 1
    HEAD = 2
    POST = 3
    PUT = 4
    PATCH = 5
    DELETE = 6
    OPTIONS = 7


def http_method_from_str(method: str) -> HttpMethod:
    """Function that converts a method string to a HttpMethod

    ## Arguments:
        `method` (`str`): The HTTP method as a string

    ## Returns:
        `HttpMethod`: The HTTP method as an HttpMethod enum

    ## Raises:
        `InvalidMethodError`: When the method string is invalid
    """

    match method:
        case "GET":
            return HttpMethod.GET
        case "HEAD":
            return HttpMethod.HEAD
        case "POST":
            return HttpMethod.POST
        case "PUT":
            return HttpMethod.PUT
        case "PATCH":
            return HttpMethod.PATCH
        case "DELETE":
            return HttpMethod.DELETE
        case "OPTIONS":
            return HttpMethod.OPTIONS
        case method:
            raise InvalidMethodError(f"Invalid request method {method}")
