import sys
import itertools
from PyQt5 import QtCore, QtWidgets


class Functions():

    def __init__(self):
        self.converted_notes_path = []
        self.notes_path = []

    def close_application(self):
        print('kileptel yoyo from func')
        sys.exit()

    @staticmethod
    def file_open(self, titleEdit):
        pass

        # del self.notes_path[:]
        # default_open_path = 'C://Users//Erik_Dubrovszkij//OneDrive - EPAM//EPHUBUDW0340//Desktop//Notes'
        # self.notes_path.append(QtWidgets.QFileDialog.getOpenFileName(
        #     titleEdit, 'Open File', default_open_path))
        # self.converted_notes_path = list(itertools.chain(*self.notes_path))
        # print(self.converted_notes_path[0])
        # file = open(name , 'r')
