from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.checkers import is_dummy_url
from src.standards import simplify_url


def parse_links(url: str) -> set[str]:
    links = set()
    with urlopen(url) as response:
        soup = BeautifulSoup(response, "html.parser")
        for anchor in soup.find_all("a"):
            link = anchor.get("href")
            if link and not link.startswith("#"):
                links.add(link)
    return links


def parse_homepage(homepage: str) -> set[str]:
    return {simplify_url(url) for url in parse_links(homepage) if not is_dummy_url(url)}
