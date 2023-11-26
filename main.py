import time

from download_img import download_img
from excel_parser import get_data_in_excel
from path_check import path_check_and_create
from multiprocessing import Process
from loguru import logger
from tqdm import tqdm


@logger.catch(reraise=True)
def full_download_img(data) -> None:
    for i in data:
        url, name, sava_path = i
        path_check_and_create(sava_path)
        download_img(url, name, sava_path)


@logger.catch(reraise=True)
def main(data):

    pbar = tqdm(total=len(data), colour="green", desc="Прогресс: ", ncols=150)

    list_processing = []
    while data or list_processing:

        if len(list_processing) < 6:
            for x in range(6 - len(list_processing)):

                data_list = [data.pop() for _ in range(30) if len(data)] # наполняем дата лист 10 значениями из экселя
                pbar.update(len(data_list))

                if data_list:
                    p = Process(target=full_download_img, args=(data_list,), daemon=True)
                    list_processing.append(p)
                    p.start()

        for proc in list_processing:
            if not proc.is_alive():
                list_processing.remove(proc)
        time.sleep(0.1)
    pbar.close()


if __name__ == '__main__':
    # Регистрация логера
    logger.remove()
    logger.add('logs/logs.log', level='DEBUG', rotation="5 MB", compression="zip", format="{time} {level} {message}",
               enqueue=True, colorize=True)

    path = input(r"Путь к файлу excel: ")
    res = get_data_in_excel(path)
    main(res)

    print("Работа завершена")
    input()

