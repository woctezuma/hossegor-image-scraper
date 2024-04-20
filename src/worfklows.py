from urllib.error import HTTPError

from tqdm import tqdm

from src.disk import load, save
from src.filters import filter_categories, filter_downloads, filter_images
from src.parsers import parse_homepage, parse_links
from src.standards import HTTP_SEPARATOR, standardize_url

DATA_FOLDER = "data/"
IMAGE_FNAME = f"{DATA_FOLDER}images.json"
DOWNLOAD_FNAME = f"{DATA_FOLDER}downloads.json"
CATEGORY_FNAME = f"{DATA_FOLDER}categories.json"
MAIN_CATEGORY_FNAME = f"{DATA_FOLDER}main_categories.json"

DISPLAY_THRESHOLD = 10


def run_workflow(homepage: str) -> set[str]:
    main_category_urls = load(MAIN_CATEGORY_FNAME)
    category_urls = load(CATEGORY_FNAME)
    download_urls = load(DOWNLOAD_FNAME)
    image_urls = load(IMAGE_FNAME)

    new_links = (
        parse_homepage(homepage).union(category_urls).difference(main_category_urls)
    )

    for url_suffix in tqdm(new_links):
        if len(new_links) < DISPLAY_THRESHOLD:
            print(url_suffix)

        url = f"{homepage}{HTTP_SEPARATOR}{url_suffix}"
        try:
            links = parse_links(url)
        except UnicodeEncodeError:
            print(url)
            links = parse_links(standardize_url(url))
        except HTTPError:
            print(url)
            continue

        category_urls.update(filter_categories(links))
        download_urls.update(filter_downloads(links))
        image_urls.update(filter_images(links))

    main_category_urls.update(new_links)

    save(main_category_urls, MAIN_CATEGORY_FNAME)
    save(category_urls, CATEGORY_FNAME)
    save(download_urls, DOWNLOAD_FNAME)
    save(image_urls, IMAGE_FNAME)

    return new_links
