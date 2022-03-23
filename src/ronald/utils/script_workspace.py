from ronald.utils.common_include import *
from ronald.utils.files_manager import *
from ronald.utils.shell_utils import *
from ronald.utils.logger import logger, set_level


import multiprocessing as mp


class ScriptProcessBase:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        FilesManager.CreateFolder(self.log_dir, remove_old=True)
        self.file_manager = FilesManager(self.log_dir)
        self.proc_dict: dict[str, mp.Process] = {}

    def RunBackground(self, cmd, proc_name: str, log=True):
        if log == False:
            new_proc = RunCmdNohup(cmd)
        else:
            log_file_name = proc_name + ".log"
            f = self.file_manager.CreatFile(log_file_name, mode='a')
            new_proc = RunCmdNohup(cmd, f)
        self.proc_dict[proc_name] = new_proc

    def KillAll(self):
        for process in self.proc_dict.values():
            self.file_manager.CloseAll()
            process.terminate()
