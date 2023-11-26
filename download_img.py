import requests
from loguru import logger


@logger.catch(reraise=True)
def download_img(url: str, name: str, save_path: str) -> None:
    try:
        logger.remove()
        logger.add('logs/logs.log', level='DEBUG', rotation="5 MB", compression="zip", format="{time} {level} {message}",
                  enqueue=True, colorize=True)
        p = requests.get(url)
        out = open(save_path + name, "wb")
        out.write(p.content)
        out.close()
        logger.debug(f'{name} - true')
    except:
        logger.debug(f'{name} - false')
