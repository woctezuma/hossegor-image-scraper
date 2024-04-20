from src.standards import HTTP_SEPARATOR

HTTP_PREFIX = "http"
INTERFACE_PREFIX = "/dsbinterface/"


def is_interface(url: str) -> bool:
    return url.startswith(INTERFACE_PREFIX)


def is_image(url: str) -> bool:
    return url.startswith(HTTP_PREFIX)


def is_dummy_url(url: str) -> bool:
    return url == HTTP_SEPARATOR
