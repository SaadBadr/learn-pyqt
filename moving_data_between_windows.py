import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


# window to edit messages
class EditWindow(qtw.QWidget):

    # signal to be transfered to the main window on submit
    submitted = qtc.pyqtSignal(str, str)

    def __init__(self, message1, message2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # layout
        self.message1 = qtw.QLineEdit()
        self.message2 = qtw.QLineEdit()
        self.message1.setText(message1)
        self.message2.setText(message2)
        self.cancel_btn = qtw.QPushButton(text='cancel')
        self.submit_btn = qtw.QPushButton(text='submit')

        layout = qtw.QFormLayout()
        layout.addRow('message 1', self.message1)
        layout.addRow('message 2', self.message2)

        button_widget = qtw.QHBoxLayout()
        button_widget.addWidget(self.submit_btn)
        button_widget.addWidget(self.cancel_btn)
        
        layout.addRow('', button_widget)

        self.setLayout(layout)

        # signals and slots

        self.cancel_btn.clicked.connect(self.close)
        self.submit_btn.clicked.connect(self.submit)

    @qtc.pyqtSlot()
    def submit(self):
        self.submitted.emit(self.message1.text(), self.message2.text())
        self.close()





# Main window
class MainWindow(qtw.QWidget):        
    def __init__(self, message1, message2,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # layout

        self.message1 = qtw.QLabel(text=message1)
        self.message2 = qtw.QLabel(text=message2)
        self.edit_btn = qtw.QPushButton(text='Edit')
        self.cancel_btn = qtw.QPushButton(text='Cancel')

        layout = qtw.QVBoxLayout()
        layout.addWidget(self.message1)
        layout.addWidget(self.message2)
        layout.addWidget(self.edit_btn)
        layout.addWidget(self.cancel_btn)
        
        self.setLayout(layout)
        
        # signals and slots

        self.edit_btn.clicked.connect(self.edit_messages)        
        self.cancel_btn.clicked.connect(self.close)

        self.show()

    @qtc.pyqtSlot()
    def edit_messages(self):
        self.editWindow = EditWindow(windowTitle="Edit!", message1=self.message1.text(), message2=self.message2.text())
        self.editWindow.submitted.connect(self.updateMessages)
        self.editWindow.show()

    @qtc.pyqtSlot(str, str)
    def updateMessages(self, message1, message2):
        self.message1.setText(message1)
        self.message2.setText(message2)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle="Edit!", message1='my Name is Nemo', message2="I'm 3 years old!")
    sys.exit(app.exec_())
