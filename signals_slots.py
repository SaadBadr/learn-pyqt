import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    
    # custom signal
    authenticated = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # my code start here
        self.username_label = qtw.QLabel('Username')
        self.password_label = qtw.QLabel('Password')
        
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Login')

        # we should add layout to show our inner widgets

        layout = qtw.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)


        # now we can add form buttons in an inner widget with a horizontal layout
        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        # note that we still can modify the layout after assigning it to the widget
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)

        # add buttons widget to our main layout
        layout.addRow('', button_widget)

        # set the layout
        self.setLayout(layout)
       

        # connect buttons signals to slots

        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)

        self.username_input.textChanged.connect(self.set_button_text)

        self.authenticated.connect(self.user_logged_in)
        # my code end here
       
        self.show()
    
    # custom slot
    @qtc.pyqtSlot(str) #optional for slot type safety and little speed enhancement
    def set_button_text(self, text):
        if text:
            self.submit_button.setText(f'Log In {text}')
        else:
            self.submit_button.setText('Log In')

    # custom slot
    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()
       
        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'You are Logged in.')
            # emit the custom signal
            self.authenticated.emit(username)
        
        else:
           qtw.QMessageBox.information(self, 'Failed', 'You are not Logged in.')

    # custom slot for our custom signal authenticated
    def user_logged_in(self,username):
        qtw.QMessageBox.information(self, 'logged in', f'{username} is logged in')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='hello world!')
    sys.exit(app.exec_())


