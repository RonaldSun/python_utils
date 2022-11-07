'''
Author: Jiaming Sun a297131009@qq.com
Date: 2022-03-18 00:46:04
LastEditors: Jiaming Sun a297131009@qq.com
LastEditTime: 2022-11-07 00:57:33
'''
import matplotlib.pyplot as plt
from ronald.utils.common_include import *
import matplotlib.dates as mdates


class Canvas():
    def __init__(self, subplot_N, plot_num=10, bottom_label="time(s)", sharex=True, sharey=False):
        self.subplot_N = subplot_N
        self.fig: plt.Figure = None
        self.axes: List[plt.Axes] = []
        self.sharex = sharex
        self.sharey = sharey
        self.fig, self.axes = plt.subplots(
            self.subplot_N, 1, figsize=(10, 13), sharex=sharex, sharey=sharey)
        if subplot_N == 1:
            self.axes = [self.axes]
        self.cmap = plt.get_cmap('viridis')
        self.colors = self.cmap(np.linspace(0, 1, plot_num))
        self.bottom_label = bottom_label

    def SetDateTimeAxes(self):
        self.fig.autofmt_xdate()
        myFmt = mdates.DateFormatter('%H:%M')
        self.axes[-1].xaxis.set_major_formatter(myFmt)

    def UpdateAxes(self):
        if (self.sharex):
            self.axes[-1].set_xlabel(self.bottom_label)
        for i in range(len(self.axes)):
            # labels along the bottom edge are on
            self.axes[i].tick_params(labelbottom=True)

        for i in range(self.subplot_N):
            self.axes[i].legend()
            self.axes[i].grid()

    def show(self, update_axes_only=False):
        self.UpdateAxes()
        if not update_axes_only:
            plt.ion()
            plt.ioff()
            plt.show()
            try:
                self.fig.clf()
                plt.close("all")
            except:
                pass
