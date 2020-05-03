import os
import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.showMaximized()
        self.setWindowTitle("Editory")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))

        self.current_editor = self.create_editor()
        self.editors = []

        self.tab_widget = QtGui.QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.currentChanged.connect(self.change_text_editor)
        self.tab_widget.tabCloseRequested.connect(self.remove_editor)
        self.new_document()
        self.setCentralWidget(self.tab_widget)

        self.configure_menuBar()
        self.configure_toolbar()

    def configure_menuBar(self):
        menubar = self.menuBar()

        menubar_items = {
            '&File': [
                ("&New", "Ctrl+N", self.new_document),
                ("&Open", "Ctrl+O", self.open_document),
                ("&Save", "Ctrl+S", self.save_document),
                ("&Print", "Ctrl+P", self.print_document),
                None,
                ("&Quit", "Ctrl+Q", self.quit),
            ],
            '&Edit': [
                ("&Cut", "Ctrl+X", self.cut_document),
                ("&Copy", "Ctrl+C", self.copy_document),
                ("&Paste", "Ctrl+V", self.paste_document),
                None,
                ("&Undo", "Ctrl+Z", self.undo_document),
                ("&Redo", "Ctrl+Y", self.redo_document)
            ],
            '&View': [
                ("&Fullscreen", "F11", self.fullscreen),
                None,
                ("&Align Left", "", self.align_left),
                ("&Align Right", "", self.align_right),
                ("&Align Center", "", self.align_center),
                ("&Align Justify", "", self.align_justify)
            ]
        }

        for menuitem, actions in menubar_items.items():
            menu = menubar.addMenu(menuitem)
            for act in actions:
                if act:
                    text, shorcut, callback = act
                    action = QtGui.QAction(text, self)
                    action.setShortcut(shorcut)
                    action.triggered.connect(callback)
                    menu.addAction(action)
                else :
                    menu.addSeparator()

        # Font Family Input
        fontBox = QtGui.QFontComboBox(self)
        fontBox.currentFontChanged.connect(self.FontFamily)

        fontSize = QtGui.QComboBox(self)
        fontSize.setEditable(True)
        fontSize.setMinimumContentsLength(3)

        fontSize.activated.connect(self.FontSize)

        # Font Sizes
        fontSizes = ['6', '7', '8', '9', '10', '11', '12', '13', '14',
            '15', '16', '18', '20', '22', '24', '26', '28',
            '32', '36', '40', '44', '48', '54', '60', '66',
            '72', '80', '88', '96'
        ]

        fontSize.addItems(fontSizes)
        font_family = QtGui.QWidgetAction(self)
        font_family.setDefaultWidget(fontBox)
        # Settings Menubar
        settings = menubar.addMenu('&Settings')
        menu_font = settings.addMenu("&Font")
        menu_font.addAction(font_family)

        font_size = QtGui.QWidgetAction(self)
        font_size.setDefaultWidget(fontSize)
        menu_size = settings.addMenu("&Font Size")
        menu_size.addAction(font_size)

    def configure_toolbar(self):
        items = (('icons/new.png', 'New', self.new_document),
            ('icons/open.png', 'Open', self.open_document),
            ('icons/save.png', 'Save', self.save_document),
            None,
            ('icons/cut.png', 'Cut', self.cut_document),
            ('icons/copy.png', 'Copy', self.copy_document),
            ('icons/paste.png', 'Paste', self.paste_document),
            None,
            ('icons/undo.png', 'Undo', self.undo_document),
            ('icons/redo.png', 'Redo', self.redo_document),
            None,
            ('icons/print.png', 'Print', self.print_document),
            None,
            ('icons/quit.png', 'Quit', self.quit),
        )

        self.toolbar = self.addToolBar("Toolbar")

        for item in items:
            if item:
                icon, text, callback = item
                action = QtGui.QAction(QtGui.QIcon(icon), text, self)
                action.triggered.connect(callback)
                self.toolbar.addAction(action)
            else :
                self.toolbar.addSeparator()

    def remove_editor(self, index):
        self.tab_widget.removeTab(index)
        if index < len(self.editors):
            del self.editors[index]

    def create_editor(self):
        text_editor = QtGui.QTextEdit()
        text_editor.setTabStopWidth(12)
        return text_editor

    def change_text_editor(self, index):
        if index < len(self.editors):
            self.current_editor = self.editors[index]

    # Input Functions
    def new_document(self, checked = False, title = "Untitled"):
        self.current_editor = self.create_editor()
        self.editors.append(self.current_editor)
        self.tab_widget.addTab(self.current_editor, title + str(len(self.editors)))
        self.tab_widget.setCurrentWidget(self.current_editor)

    def open_document(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if filename:
            f = open(filename, 'r')
        filedata = f.read()
        self.new_document(title = filename)
        self.current_editor.setText(filedata)
        f.close()

    def save_document(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        if file:
            text = self.current_editor.toPlainText()
            file.write(text)
            file.close()

    def print_document(self):
        print_dialog = QtGui.QPrintDialog()
        if print_dialog.exec_() == QtGui.QDialog.Accepted:
            self.current_editor.document().print_(print_dialog.printer())

    def quit(self): self.close()

    def undo_document(self): self.current_editor.undo()

    def redo_document(self): self.current_editor.redo()

    def cut_document(self): self.current_editor.cut()

    def copy_document(self): self.current_editor.copy()

    def paste_document(self): self.current_editor.paste()

    def align_left(self): self.current_editor.setAlignment(Qt.AlignLeft)

    def align_right(self): self.current_editor.setAlignment(Qt.AlignRight)

    def align_center(self): self.current_editor.setAlignment(Qt.AlignCenter)

    def align_justify(self):
        self.current_editor.setAlignment(Qt.AlignJustify)

    def fullscreen(self):
        if not self.isFullScreen():
            self.showFullScreen()
        else :
            self.showMaximized()

    def FontFamily(self, font):
        self.current_editor.setCurrentFont(font)

    def FontSize(self, fontsize):
        self.current_editor.setFontPointSize(int(fontsize))

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()