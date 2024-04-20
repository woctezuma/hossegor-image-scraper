from src.worfklows import run_workflow


def main() -> None:
    homepage = "http://dicks-sand-bar.com"
    new_links = None

    while new_links is None or new_links:
        new_links = run_workflow(homepage)


if __name__ == "__main__":
    main()
