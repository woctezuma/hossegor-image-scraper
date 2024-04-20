HTTP_SEPARATOR = "/"


def simplify_url(url: str) -> str:
    return url.removeprefix(HTTP_SEPARATOR)


def standardize_url(url: str) -> str:
    return url.replace("é", "e").replace("°", "%C2%B0")
