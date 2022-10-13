'''
Author: RonaldSun a297131009@qq.com
Date: 2022-09-26 15:58:52
LastEditors: RonaldSun a297131009@qq.com
LastEditTime: 2022-10-13 20:22:11
'''
from ronald.utils.logger import *
from datetime import datetime
from pathlib import Path
import pandas as pd
from tabulate import tabulate


class CSVDataManager:
    def __init__(self, data_folder, usecols=None):
        self.data_folder = data_folder
        self.data = None
        self.file_path = None
        self.func_list = None
        self.file_extension = ".csv"
        self.usecols = usecols
        self.load_latest_data()

    def load_latest_data(self):
        files = [str(x) for x in Path(self.data_folder).glob(
            "*" + self.file_extension) if x.is_file()]
        if len(files) > 0:
            files.sort()
            self.latest_file = files[-1]
            self.load_target_data(self.latest_file)
        else:
            logger.warning("target folder is empty!")

    def get_file_date(self):
        file_name = Path(self.file_path).name
        file_date = file_name.split(".")[0]
        return file_date

    def load_target_data(self, file_name):
        self.file_path = file_name
        if Path(file_name).is_file():
            self.data = pd.read_csv(file_name, usecols=self.usecols)
            logger.info("loaded file: " + file_name)

    def make_copy_of_latest(self):
        self.load_latest_data()
        time_now = datetime.now()
        file_name = time_now.strftime("%Y%m%d") + self.file_extension
        file_path = Path(self.data_folder) / file_name
        if file_path.is_file():
            file_path.unlink()
        self.data.to_csv(file_path)
        logger.info("make a copy file: " + str(file_path))

    def show_data(self):
        print(tabulate(self.data, headers='keys', floatfmt=".2f"))

    def get_func_list(self):
        if self.func_list is None:
            self.func_list = ["load_latest_data",
                              "show_data", "make_copy_of_latest"]
        return self.func_list

    def user_interface(self):
        func_list = self.get_func_list()
        choose_sentence = "choose: "
        for i, func_name in enumerate(func_list):
            choose_sentence = choose_sentence + "\n"
            choose_sentence = choose_sentence + (str(i+1) + ". ")
            choose_sentence = choose_sentence + func_name
        choose_sentence = choose_sentence + \
            "\n{}. exist\n".format(len(func_list)+1)
        while(True):
            c = input(choose_sentence)
            if int(c) == len(func_list) + 1:
                break
            if int(c) > 0 and int(c) <= len(func_list):
                getattr(self, func_list[int(c)-1])()
            else:
                logger.error("error input!")
                break

    def __del__(self):
        if Path(self.file_path).exists():
            Path(self.file_path).unlink()
        self.data.to_csv(self.file_path)


if __name__ == "__main__":
    data_folder = "/home/linsu/Nutstore Files/database/invest_data"
    data_manager = CSVDataManager(data_folder)
    data_manager.user_interface()
