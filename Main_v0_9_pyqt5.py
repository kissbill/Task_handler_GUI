import sys
import re
from PyQt5 import QtCore, QtWidgets
import itertools

string = []
regex_words = ''
finding = []
urit = []
notes_path = []

pN = {}
tN = {}
wN = {}
mN = {}
tskN = {}
toN = {}
fN = {}
nN = {}

grid_layout = QtWidgets.QGridLayout()

project_names = ['Project', 'Enviroment', 'Parking',
                 'Demarcated', 'UndemarcatedSpace', 'Inferred']
topics_names = ['Automate', 'Manual', 'BackEnd',
                'FrontEnd', 'FrameWork', 'Code', 'DataBase', 'Java']
work_names = ['Requirement', 'Defect', 'Meeting',
              'Regression', 'Review', 'Ready4Qa']
misc_names = ['AddWorkFlow', 'KnowHow', 'HowTo', 'Directive', 'PlanForTheDay']
task_names = ['Starting', 'DataConsistency', 'e2e', 'Turnover', 'DwellTime']
tool_names = ['Looker', 'IntelliJ', 'Github', 'Jira',
              'Postman', 'DcOs', 'Kafka', 'Allure', 'Jenkins']
file_names = ['File', 'Xlsx', 'Link', 'LogIn', 'Letter']
needDo_names = ['ToDo', 'NeedToCheck', 'Done', 'Learning']


def tick_box_creation(arrays, short_Name):
    for x in range(0, len(arrays)):
        short_Name["checkBox_{0}".format(x)] = QtWidgets.QCheckBox(arrays[x])


def placing_tick_box(arrays, short_Name, lines):
    for x in range(0, len(arrays)):
        grid_layout.addWidget(short_Name['checkBox_' + str(x)], lines, x)


class Window(QtWidgets.QWidget):

    def __init__(self):
        # super(Window, self).__init__()
        # self.initUI()
        QtWidgets.QWidget.__init__(self)
        self.titleEdit = QtWidgets.QTextEdit()
        self.titleEdit.setFontPointSize(12)

        self.setStyleSheet('font-size: 14pt; font-family: Europa;')

        opening = QtWidgets.QPushButton('Open')
        searching = QtWidgets.QPushButton('Search')
        setAllButtonsChecked = QtWidgets.QPushButton('Set All')
        exit = QtWidgets.QPushButton('EXIT')

        tick_box_creation(project_names, pN)
        tick_box_creation(topics_names, tN)
        tick_box_creation(work_names, wN)
        tick_box_creation(misc_names, mN)
        tick_box_creation(task_names, tskN)
        tick_box_creation(tool_names, toN)
        tick_box_creation(file_names, fN)
        tick_box_creation(needDo_names, nN)

        placing_tick_box(project_names, pN, 0)
        placing_tick_box(topics_names, tN, 1)
        placing_tick_box(work_names, wN, 2)
        placing_tick_box(misc_names, mN, 3)
        placing_tick_box(task_names, tskN, 4)
        placing_tick_box(tool_names, toN, 5)
        placing_tick_box(file_names, fN, 6)
        placing_tick_box(needDo_names, nN, 7)

        # Gombok #####################################################
        gombok_line = 8
        grid_layout.addWidget(searching, gombok_line, 0)
        grid_layout.addWidget(setAllButtonsChecked, gombok_line, 2)
        grid_layout.addWidget(opening, gombok_line, 8)
        grid_layout.addWidget(exit, gombok_line, 9)

        # Gombok
        exit.clicked.connect(self.close_application)
        opening.clicked.connect(self.file_open)
        searching.clicked.connect(self.searching)
        setAllButtonsChecked.clicked.connect(self.setAllButtonsChecked)

        # miez =tN['checkBox_0'].isChecked()
        # print(miez)

        # for x in range( 0 , len(project_names) ):
        #    pN['checkBox_' + str(x)].stateChanged.connect(lambda state: self.tick(state, word1 = project_names[x]) )
        pN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[0]))
        pN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[1]))
        pN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[2]))
        pN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[3]))
        pN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[4]))
        pN['checkBox_5'].stateChanged.connect(
            lambda state: self.tick(state, word1=project_names[5]))
        # Topics
        tN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[0]))
        tN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[1]))
        tN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[2]))
        tN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[3]))
        tN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[4]))
        tN['checkBox_5'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[5]))
        tN['checkBox_6'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[6]))
        tN['checkBox_7'].stateChanged.connect(
            lambda state: self.tick(state, word1=topics_names[7]))
        # Works
        wN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[0]))
        wN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[1]))
        wN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[2]))
        wN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[3]))
        wN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[4]))
        wN['checkBox_5'].stateChanged.connect(
            lambda state: self.tick(state, word1=work_names[5]))
        #    Miscs
        mN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=misc_names[0]))
        mN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=misc_names[1]))
        mN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=misc_names[2]))
        mN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=misc_names[3]))
        mN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=misc_names[4]))
        # Infrastructs
        tskN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=task_names[0]))
        tskN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=task_names[1]))
        tskN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=task_names[2]))
        tskN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=task_names[3]))
        tskN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=task_names[4]))
        # Tools
        toN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[0]))
        toN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[1]))
        toN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[2]))
        toN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[3]))
        toN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[4]))
        toN['checkBox_5'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[5]))
        toN['checkBox_6'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[6]))
        toN['checkBox_7'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[7]))
        toN['checkBox_8'].stateChanged.connect(
            lambda state: self.tick(state, word1=tool_names[8]))
        # File_releated
        fN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=file_names[0]))
        fN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=file_names[1]))
        fN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=file_names[2]))
        fN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=file_names[3]))
        fN['checkBox_4'].stateChanged.connect(
            lambda state: self.tick(state, word1=file_names[4]))
        # Need Do
        nN['checkBox_0'].stateChanged.connect(
            lambda state: self.tick(state, word1=needDo_names[0]))
        nN['checkBox_1'].stateChanged.connect(
            lambda state: self.tick(state, word1=needDo_names[1]))
        nN['checkBox_2'].stateChanged.connect(
            lambda state: self.tick(state, word1=needDo_names[2]))
        nN['checkBox_3'].stateChanged.connect(
            lambda state: self.tick(state, word1=needDo_names[3]))

        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.addLayout(grid_layout)
        verticalLayout.addWidget(self.titleEdit)
        self.setLayout(verticalLayout)
        self.setGeometry(300, 300, 900, 900)
        self.setWindowTitle('DataBase for HashTagging')
        self.titleEdit.setReadOnly(True)

    def setAllButtonsChecked(self, state=2):
        for button in self.group.buttons():
            button.set_Checked(checked)

    def tick(self, state, word1):
        if state == QtCore.Qt.Checked:
            string.append('(?=.*#' + word1 + ')')
            print(word1)
        else:
            string.remove('(?=.*#' + word1 + ')')
            print(state)

    def print_out(self):

        self.empty_array()
        self.titleEdit.append(" ")
        finding_ = "".join(str(x) for x in finding)

        self.titleEdit.append(finding_)
        self.init()

        # finding_ = "".join(str(x) for x in urit)

    def empty_array(self):
        self.titleEdit.clear()

    def close_application(self):
        print('kileptel yoyo')
        sys.exit()

    converted_notes_path = []

    def file_open(self):
        del notes_path[:]
        default_open_path = 'C://Users//Erik_Dubrovszkij//OneDrive - EPAM//EPHUBUDW0340//Desktop//Notes'
        notes_path.append(QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', default_open_path))
        self.converted_notes_path = list(itertools.chain(*notes_path))
        print(self.converted_notes_path[0])
       # file = open(name , 'r')

    def init(self):
        del finding[:]

    def searching(self):
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        regex_words = "".join(str(x) for x in string)
        kulcsSzo = r"(?=.*)" + regex_words
        file_path = self.converted_notes_path[0]

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

        print('----------------------------------oo------------------------------------')
        self.print_out()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    k = input("press close to exit")
