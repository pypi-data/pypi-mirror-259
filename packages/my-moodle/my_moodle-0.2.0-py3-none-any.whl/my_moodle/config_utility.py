"""
Config utility Class
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""
import os
from configparser import ConfigParser


class ConfigUtility:
    """Config utility functions"""

    DEFAULT_CONFIG_FILE_PATH: str = "config.ini"

    @staticmethod
    def check_and_read_config(config_filepath: str = DEFAULT_CONFIG_FILE_PATH) -> tuple:
        """Check if the config file exists. If not, create it and
        then read and return the server and token config.

        Args:
            config_filepath (str): The config file path

        Returns:
            tuple: A tuple containing the server and token
        """
        if not os.path.exists(config_filepath):
            print(
                "Config file not found. Please provide Moodle server URL and access token."
            )
            ConfigUtility.create_config_file(config_filepath)

        return ConfigUtility.read_config(
            ConfigUtility.read_config_file(config_filepath)
        )

    @staticmethod
    def create_config_file(file_path: str) -> None:
        """Create a config file

        Args:
            file_path (str): The file path to create the config file
        """
        server = input("Enter Moodle server URL: ")
        print("To get your Moodle access token, visit")
        print(f"{server}/user/managetoken.php")
        token = input("Enter Moodle access token: ")

        config = ConfigParser()
        config["User"] = {"server": server, "token": token}

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as config_file:
            config.write(config_file)

    @staticmethod
    def read_config_file(file_path: str) -> ConfigParser:
        """Read the config file

        Args:
            file_path (str): The file path to read the config file

        Returns:
            ConfigParser: The config parser
        """
        config_parser: ConfigParser = ConfigParser()
        config_parser.read(file_path)
        return config_parser

    @staticmethod
    def read_config(config_parser: ConfigParser) -> tuple:
        """Read the config

        Args:
            config_parser (ConfigParser): The config parser

        Returns:
            tuple: A tuple containing the server and token
        """
        server: str = config_parser["User"]["server"]
        token: str = config_parser["User"]["token"]
        return server, token
