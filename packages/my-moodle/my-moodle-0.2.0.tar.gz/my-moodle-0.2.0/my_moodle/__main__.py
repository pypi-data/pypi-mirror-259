"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Entry point for the application.
"""

from . import ConfigUtility, MoodleDataDownloader
from .version import __version__


def main() -> None:
    """Entry point for the application."""
    print(f"my_moodle version {__version__}")

    server, token = ConfigUtility.check_and_read_config()

    moodle_data_downloader: MoodleDataDownloader = MoodleDataDownloader(server, token)

    moodle_data_downloader.download_my_data()


if __name__ == "__main__":
    main()
