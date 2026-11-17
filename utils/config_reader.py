import configparser
import os
from pathlib import Path


class ConfigReader:

    def __init__(self):

        self.config = configparser.ConfigParser()

        project_root = Path(__file__).resolve().parent.parent

        self.config_path = (
            project_root / "config" / "config.ini"
        )

        if not self.config_path.exists():

            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        self.config.read(
            self.config_path,
            encoding="utf-8"
        )

    def get(self, section, key):

        env_key = f"SAUCEDEMO_{key.upper()}"

        env_value = os.getenv(env_key)

        if env_value is not None:
            return env_value

        return self.config.get(section, key)

    def get_int(self, section, key):

        return int(
            self.get(section, key)
        )

    def get_bool(self, section, key):

        return self.config.getboolean(
            section,
            key
        ) if os.getenv(
            f"SAUCEDEMO_{key.upper()}"
        ) is None else self.get(
            section,
            key
        ).lower() in ("true", "1", "yes")


config = ConfigReader()