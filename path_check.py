from os import path, makedirs
from loguru import logger


@logger.catch(reraise=True)
def path_check_and_create(data_path: str):
    if not path.exists(data_path):
        makedirs(data_path)
