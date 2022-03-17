import subprocess
import shlex
import os
import signal
import subprocess


def RunCmd(command, file=None):
    subprocess.run(command, stdout=file, stderr=subprocess.STDOUT,
                   executable="/bin/bash", shell=True)


def RunCmdNohup(command, file=None):
    return subprocess.Popen(command, stdout=file, stderr=subprocess.STDOUT, executable="/bin/bash", shell=True)


def KillProc(proc_id):
    # import psutil
    # process = psutil.Process(proc_id)
    # for proc in process.children(recursive=True):
    #     proc.kill()
    # process.kill()
    os.killpg(os.getpgid(proc_id), signal.SIGTERM)


def GetFreePort():
    import socket
    sock = socket.socket()
    sock.bind(('', 0))
    return sock.getsockname()[1]
