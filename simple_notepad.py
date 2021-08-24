import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class SearchWidget(qtw.QWidget):
    submitted = qtc.pyqtSignal(str, bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(qtw.QFormLayout())
        self.term_input = qtw.QLineEdit()
        self.case_checkbox = qtw.QCheckBox('Case Sensitive?')
        self.submit_btn = qtw.QPushButton('Search', clicked=self.on_submit)

        self.layout().addRow('Search Term', self.term_input)
        self.layout().addRow('Search Term', self.case_checkbox)
        self.layout().addRow('Search Term', self.submit_btn)
    
    def on_submit(self):
        term = self.term_input.text()
        case_sensitive = self.case_checkbox.checkState == qtc.Qt.Checked
        self.submitted.emit(term, case_sensitive)

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        # Menubar

        menubar = self.menuBar() #QMenuBar
        file_menu = menubar.addMenu('File') #QMenu
        save_action = file_menu.addAction('Save') #QAction
        open_action = file_menu.addAction('Open')
        file_menu.addSeparator()
        file_menu.addAction('Quit', self.close)

        save_action.triggered.connect(self.save_file)
        open_action.triggered.connect(self.open_file)

        # Toolbar

        edit_toolbar = self.addToolBar('Edit')
        edit_toolbar.addAction('Copy', self.textedit.copy)
        edit_toolbar.addAction('Cut', self.textedit.cut)
        edit_toolbar.addAction('Paste', self.textedit.paste)
        edit_toolbar.addAction('Undo', self.textedit.undo)
        edit_toolbar.addAction('Redo', self.textedit.redo)

        # Dockwidget --> used to dock a qwidget inside our main widget
        search_dock = qtw.QDockWidget('Search')
        search_widget = SearchWidget()
        search_dock.setWidget(search_widget)

        self.addDockWidget(qtc.Qt.RightDockWidgetArea, search_dock)

        search_widget.submitted.connect(self.search)


        self.show()

    def search(self, term, case_sensitive=False):
        if case_sensitive:
            cur = self.textedit.find(term, qtg.QTextDocument.FindCaseSensitively)
        else:
            cur = self.textedit.find(term)
        if not cur:
            self.statusBar().showMessage('No matches found', 2000)

    def save_file(self):
        text = self.textedit.toPlainText()
        filename, _ = qtw.QFileDialog.getSaveFileName()
        if filename:
            with open(filename, 'w') as handle:
                handle.write(text)
                self.statusBar().showMessage(f'Saved to {filename}', 2000)

    def open_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}', 2000)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle="Notepad")
    sys.exit(app.exec_())
