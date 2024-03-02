"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the project.
"""

import unittest
from my_moodle import ConfigUtility, MoodleDataDownloader


class MoodleDataDownloaderTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataDownloader class."""

    def test_check_and_read_config(self) -> None:
        """Test the check_and_read_config function."""

        test_config_file: str = "test-data/config-a-s.ini"

        server, token = ConfigUtility.check_and_read_config(test_config_file)

        moodle_data_downloader: MoodleDataDownloader = MoodleDataDownloader(
            server, token
        )

        moodle_data_downloader.download_my_data()


if __name__ == "__main__":
    unittest.main()
