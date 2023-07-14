import argparse


def cli():
    cli_parser = argparse.ArgumentParser(
        prog="silf",
        description="This program download images from ligthshot's site. See more in README file"
    )
    cli_parser.add_argument(
        "count_of_images",
        help="Just print hello world",
        type=int
    )
    cli_parser.add_argument(
        "-D", "--delete_images",
        action="store_false",
        help="to don't delete images in folder",
        default=True
    )

    return cli_parser.parse_args()
