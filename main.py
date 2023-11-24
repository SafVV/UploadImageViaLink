from download_img import download_img
from excel_parser import get_data_in_excel
from path_check import path_check_and_create
from multiprocessing import Process


def full_download_img(data) -> None:
    for i in data:
        url, name, sava_path = i

        path_check_and_create(sava_path)
        download_img(url, name, sava_path)


def main(data):
    list_processing = []
    while data:
        for x in range(6):
            data_list = [data.pop() for _ in range(12) if len(data)]
            if data_list:
                p = Process(target=full_download_img, args=(data_list,), daemon=True, name=f"PhotoKax{x}")
                list_processing.append(p)
                p.start()

        for proc in list_processing:
            proc.join()
            list_processing.remove(proc)










if __name__ == '__main__':
    path = input(r"Путь к файлу excel: ")
    res = get_data_in_excel(r"D:\pythonProject\Oleg - UploadImageViaLink\данные\ф100.xlsx")
    main(res)
