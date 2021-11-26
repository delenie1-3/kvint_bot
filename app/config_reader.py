import configparser
from dataclasses import dataclass

@dataclass
class TgBot:#класс для токена телеграм бота
    token: str

@dataclass
class Config:#класс конфиги телеграм бота
    tg_bot: TgBot


def load_config(path: str):
    #функция загрузки конфигурации бота
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot["token"],
        )
    )