'''
Author: LinSu(lin.su@nio.com)
Date: 2022-09-14 19:37:22
LastEditors: LinSu(lin.su@nio.com)
LastEditTime: 2022-09-15 11:49:45
'''
from ronald.utils.logger import *
from datetime import datetime
from pathlib import Path
import pandas as pd
from tabulate import tabulate


class CSVDataManager:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.data = None
        self.func_list = None
        self.file_extension = ".csv"

    def load_latest_data(self):
        files = [str(x) for x in Path(self.data_folder).glob(
            "*" + self.file_extension) if x.is_file()]
        if len(files) > 0:
            files.sort()
            self.latest_file = files[-1]
            self.data = pd.read_csv(self.latest_file, index_col=0)
            logger.info("loaded file: " + self.latest_file)
        else:
            logger.warning("target folder is empty!")

    def load_target_data(self, file_name):
        if Path(file_name).is_file():
            self.data = pd.read_csv(file_name, index_col=0)
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
        choose_sentence = choose_sentence + "\n4. exist\n"
        while(True):
            c = input(choose_sentence)
            if int(c) == len(func_list) + 1:
                break
            if int(c) > 0 and int(c) <= len(func_list):
                getattr(self, func_list[int(c)-1])()
            else:
                logger.error("error input!")
                break


if __name__ == "__main__":
    data_folder = "/home/linsu/Nutstore Files/database/invest_data"
    data_manager = CSVDataManager(data_folder)
    data_manager.user_interface()
