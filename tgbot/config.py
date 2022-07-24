from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    # Этот dataclass создан для базы данных
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    # class TgBot будет принимать в себя три параметра
    # Эти данные были получены с файла .env
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    # Этот dataclass создан для всего остального что не подходит в другие dataclass
    other_params: str = None # Стоит заглушка


@dataclass
class Config:
    # Этот dataclass создан для группировки остальных dataclass
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous

# Специальная функция которая выгружает данные с class Config
def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )
