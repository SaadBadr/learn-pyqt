import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # my code start here
        username_label = qtw.QLabel('Username')
        password_label = qtw.QLabel('Password')
        
        username_input = qtw.QLineEdit()
        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password)

        cancel_button = qtw.QPushButton('Cancel')
        submit_button = qtw.QPushButton('Login')

        # we should add layout to show our inner widgets

        # Below there are three 3 ways to make the form layout we want

        ############## METHOD 1: NESTED LAYOUTS ##############
      
        # note that we can nest layouts
        layout = qtw.QVBoxLayout()

        username_layout = qtw.QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(username_input)
        
        password_layout = qtw.QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(password_input)

        layout.addLayout(username_layout)
        layout.addLayout(password_layout)

        ############## METHOD 2: GRID LAYOUT ##############
        
        # another way is to use grid layout instead of V/H layouts

        layout = qtw.QGridLayout()
        layout.addWidget(username_label, 0, 0)
        layout.addWidget(username_input, 0, 1)
        layout.addWidget(password_label, 1, 0)
        layout.addWidget(password_input, 1, 1)



        ############## METHOD 3: FORM LAYOUT ##############

        # finally, we can use form layout which is easier in this case as we don't need to make a label explicitly
        layout = qtw.QFormLayout()
        layout.addRow('Username', username_input)
        layout.addRow('Password', password_input)


        # now we can add form buttons in an inner widget with a horizontal layout
        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        # note that we still can modify the layout after assigning it to the widget
        button_widget.layout().addWidget(cancel_button)
        button_widget.layout().addWidget(submit_button)

        # add buttons widget to our main layout
        layout.addRow('', button_widget)

        # set the layout
        self.setLayout(layout)
       
        # my code end here
       
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='hello world!')
    sys.exit(app.exec_())


