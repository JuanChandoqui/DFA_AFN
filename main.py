from Models.select_automaton import SelectAutomaton
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic 

text_file = ''
selected_automaton = SelectAutomaton()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)
        self.label_alert.hide()
        self.label_file_sucessful.hide()
        self.button_selectFile.clicked.connect(self.openFileNameDialog)
        self.button_import.clicked.connect(self.isClickedImportButton)
        self.button_ok.setEnabled(False)
        self.button_ok.clicked.connect(self.isClickedButtonOK)
        self.button_exit.clicked.connect(self.close)

    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            global text_file
            text_file = fileName
            self.textField_selected_file.setText(fileName)
            self.label_alert.hide()
    

    def isClickedImportButton(self):
        global text_file
        global selected_automaton
        if(len(text_file) == 0):
            self.label_alert.show()
        else:
           selected_automaton.read_text_file(text_file)
           self.label_file_sucessful.show()
           self.button_ok.setEnabled(True)
        
    def isClickedButtonOK(self):
        global selected_automaton
        text = self.textField_text.text()

        text = text.lower()
        input_text = list(text)            
            
        if(selected_automaton.automaton_function(input_text)):
            self.label_status.setText('ACCEPT')
        else:
            self.label_status.setText('FAILED')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
