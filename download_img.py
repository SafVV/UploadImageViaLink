import requests
from loguru import logger


def download_img(url: str, name: str, save_path: str) -> None:
    try:
        p = requests.get(url)
        out = open(save_path + name, "wb")
        out.write(p.content)
        out.close()
        logger.debug(f'{name} - true')
    except:
        logger.debug(f'{name} - false')
