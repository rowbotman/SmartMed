import pickle

from .apps import *


# logging decorator
import sys
sys.path.append("..")
from logs.logger import debug

from PyQt5 import QtWidgets


class GUI:
    '''Qt apps manipulator'''
    def __init__(self):
        self.__make_QAapp()

    @debug
    def __make_QAapp(self):
        self.mainQt = QtWidgets.QApplication(sys.argv)

    @debug
    def start_gui(self):
        '''display QT app'''
        app = StartingApp()
        app.start()
        self.mainQt.exec_()

        with open('settings.py', 'rb') as f:
            app.settings = pickle.load(f)
        print(app.settings)

        return app.settings