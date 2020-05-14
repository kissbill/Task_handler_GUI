import sys
import re
import itertools
from PyQt5 import QtCore, QtWidgets
from main_gui import Ui_MainWindow


class Functions():

    def __init__(self):
        self.converted_notes_path = []
        self.notes_path = []
        self.string = []
        self.regex_words = ''
        self.finding = []
        self.urit = []
        self.notes_path = []

    def close_application(self):
        print('kileptel yoyo from func')
        sys.exit()

    def file_open(self):
        del self.notes_path[:]
        default_open_path = 'C://Users//Erik_Dubrovszkij//OneDrive - EPAM//EPHUBUDW0340//Desktop//Notes'
        self.notes_path.append(QtWidgets.QFileDialog.getOpenFileName())
        self.converted_notes_path = list(itertools.chain(*self.notes_path))
        print(self.converted_notes_path[0])
        return self.converted_notes_path[0]
        # file = open(name , 'r')

    @staticmethod
    def searching():
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        regex_words = "ToDo" + "".join(str(x) for x in string)
        kulcsSzo = r"(?=.*)" + regex_words
        file_path = converted_notes_path[0]

        # print(kulcsSzo)
        # self.init()
        # self.empty_array()
        ending = '\\-->'
        pattern_keyword = re.compile(kulcsSzo)
        pattern_end = re.compile(ending)

        # Loop through text
        for i, line in enumerate(open(file_path)):
            text.append(line)
            # Kulcs szo
            for match in re.finditer(pattern_keyword, line):
                kulcs_szo_sora.append(i + 1)  # talalt sor lementese
                break
            # Kereszt lezarasok keresese
            for match in re.finditer(pattern_end, line):
                sorban_end.append(i + 1)  # talalt kereszt sor lementese

        # Lezaro kereszt elemek tombjenek hossza
        # hossz = len(sorban_end)
        for hits in kulcs_szo_sora:
            print('Eredeti doksiban ezen sor : %s ' % hits)
            print()
            finding.append(
                '''------------------------------------------------------------------------------------------------------------------------''' + '\n')

            for lezaro in sorban_end[0:len(sorban_end)]:
                if hits < lezaro:
                    # print(hits)
                    # print(lezaro)
                    break

            for megVagy in text[hits - 1:lezaro - 1]:
                finding.append(megVagy)

        print(
            '----------------------------------oo------------------------------------')
        self.print_out()

    def print_out(self):

        gui.empty_editor()
        self.titleEdit.append(" ")
        finding_ = "".join(str(x) for x in self.finding)

        self.titleEdit.append(finding_)
        self.init()

    def init(self):
        del self.finding[:]
