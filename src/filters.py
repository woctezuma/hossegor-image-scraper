from src.checkers import is_dummy_url, is_image, is_interface
from src.standards import simplify_url


def filter_categories(links: set[str]) -> set[str]:
    return {
        simplify_url(url)
        for url in links
        if not is_interface(url) and not is_image(url) and not is_dummy_url(url)
    }


def filter_downloads(links: set[str]) -> set[str]:
    return {url for url in links if is_interface(url)}


def filter_images(links: set[str]) -> set[str]:
    return {url.split("?itok=")[0] for url in links if is_image(url)}
