import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
#insert paths for importing the function and class
sys.path.insert(0, './/gui')
sys.path.insert(1, './/voice_out_funcs')
from voicer import Ui_MainWindow
from docx_to_mp3 import docx_to_mp3
from txt_to_mp3 import txt_to_mp3
from pdf_to_mp3 import pdf_to_mp3


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #FIRST PAGE
        ##############################################################################################################
        self.ui.docx_to_mp3_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.DOCX_TO_MP3))
        self.ui.txt_to_mp3_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.TXT_TO_MP3))
        self.ui.pdf_to_mp3_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.PDF_TO_MP3))


        #DOCX_TO_MP3
        ##############################################################################################################
        self.ui.DOCX_BACK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FIRST_PAGE))
        self.ui.BTN_SELECT_INPUT_PATH_DOCX.clicked.connect(self.input_path_docx)
        self.ui.BTN_SELECT_OUTPUT_PATH_DOCX.clicked.connect(self.output_path_docx)
        self.ui.DOCX_FILE_DUBBING.clicked.connect(self.docx_file_dubbing)

        #TXT_TO_MP3
        ##############################################################################################################
        self.ui.TXT_BACK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FIRST_PAGE))
        self.ui.BTN_SELECT_INPUT_PATH_TXT.clicked.connect(self.input_path_txt)
        self.ui.BTN_SELECT_OUTPUT_PATH_TXT.clicked.connect(self.output_path_txt)
        self.ui.TXT_FILE_DUBBING.clicked.connect(self.txt_file_dubbing)

        #PDF_TO_MP3
        ##############################################################################################################
        self.ui.PDF_BACK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FIRST_PAGE))
        self.ui.BTN_SELECT_INPUT_PATH_PDF.clicked.connect(self.input_path_pdf)
        self.ui.BTN_SELECT_OUTPUT_PATH_PDF.clicked.connect(self.output_path_pdf)
        self.ui.PDF_FILE_DUBBING.clicked.connect(self.pdf_file_dubbing)

        #FINAL PAGE
        ##############################################################################################################
        self.ui.BTN_USE_AGAIN.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FIRST_PAGE))
        self.ui.BTN_EXIT.clicked.connect(lambda: exit())


        self.ui.stackedWidget.setCurrentWidget(self.ui.FIRST_PAGE)
        self.show()

    ##############################################
    ###################DOCX#######################
    ##############################################

    #GET THE USER'S PATH TO THE FOLDER WHERE HE WANTS TO SAVE THE DOCX --> MP3 FILE
    def output_path_docx(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.ui.INPUT_PATH_OUTPUT_DOCX.setText(str(folder_path))

    #GET DOCX FILE PATH FROM USER
    def input_path_docx(self):
        file_name = QFileDialog.getOpenFileName(self, "Select File", "", "Word Files (*.docx), *.docx")
        if file_name:
            self.ui.INPUT_PATH_INPUT_DOCX_.setText(str(file_name[0]))

    #VOICE OUT FILE IF BOTH DOCX INPUTS ARE NOT EMPTY
    def docx_file_dubbing(self):
        if self.ui.INPUT_PATH_INPUT_DOCX_.text() != "" and self.ui.INPUT_PATH_OUTPUT_DOCX.text() != "" and (self.ui.RADIO_RU_LANG_DOCX.isChecked() or self.ui.RADIO_EN_LANG_DOCX.isChecked()):
            if self.ui.RADIO_RU_LANG_DOCX.isChecked():
                lang = 'ru'
            else: 
                lang = 'en'
            voiceover = docx_to_mp3(file_path=self.ui.INPUT_PATH_INPUT_DOCX_.text(), language=lang, save_path=self.ui.INPUT_PATH_OUTPUT_DOCX.text())
            if (voiceover):
                self.ui.INPUT_PATH_INPUT_DOCX_.setText("")
                self.ui.INPUT_PATH_OUTPUT_DOCX.setText("")
                self.ui.RADIO_RU_LANG_DOCX.setChecked(False)
                self.ui.RADIO_EN_LANG_DOCX.setChecked(False)
                self.ui.stackedWidget.setCurrentWidget(self.ui.FINAL_PAGE)
            else:
                self.ui.INPUT_PATH_INPUT_DOCX_.setText("")
                self.ui.INPUT_PATH_OUTPUT_DOCX.setText("")
                self.ui.RADIO_RU_LANG_DOCX.setChecked(False)
                self.ui.RADIO_EN_LANG_DOCX.setChecked(False)

    ##############################################
    ###################TXT########################
    ##############################################

    #GET THE USER'S PATH TO THE FOLDER WHERE HE WANTS TO SAVE THE DOCX --> MP3 FILE
    def output_path_txt(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.ui.INPUT_PATH_OUTPUT_TXT.setText(str(folder_path))

    #GET TXT FILE PATH FROM USER 
    def input_path_txt(self):
        file_name = QFileDialog.getOpenFileName(self, "Select File", "", "TXT FILES (*.txt), *.txt")
        if file_name:
            self.ui.INPUT_PATH_INPUT_TXT_.setText(str(file_name[0]))


    #VOICE OUT TXT FILE IF BOTH TXT INPUTS ARE NOT EMPTY
    def txt_file_dubbing(self):
        if self.ui.INPUT_PATH_INPUT_TXT_.text() != "" and self.ui.INPUT_PATH_OUTPUT_TXT.text() != "" and (self.ui.RADIO_RU_LANG_TXT.isChecked() or self.ui.RADIO_EN_LANG_TXT.isChecked()):
            if self.ui.RADIO_RU_LANG_TXT.isChecked():
                lang = 'ru'
            else: 
                lang = 'en'
            voiceover = txt_to_mp3(file_path=self.ui.INPUT_PATH_INPUT_TXT_.text(), language=lang, save_path=self.ui.INPUT_PATH_OUTPUT_TXT.text())
            if (voiceover):
                self.ui.INPUT_PATH_INPUT_TXT_.setText("")
                self.ui.INPUT_PATH_OUTPUT_TXT.setText("")
                self.ui.RADIO_RU_LANG_TXT.setChecked(False)
                self.ui.RADIO_EN_LANG_TXT.setChecked(False)
                self.ui.stackedWidget.setCurrentWidget(self.ui.FINAL_PAGE)
            else:
                self.ui.INPUT_PATH_INPUT_TXT_.setText("")
                self.ui.INPUT_PATH_OUTPUT_TXT.setText("")
                self.ui.RADIO_RU_LANG_TXT.setChecked(False)
                self.ui.RADIO_EN_LANG_TXT.setChecked(False)

    ##############################################
    ###################PDF########################
    ##############################################

    #GET THE USER'S PATH TO THE FOLDER WHERE HE WANTS TO SAVE THE DOCX --> MP3 FILE
    def output_path_pdf(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.ui.INPUT_PATH_OUTPUT_PDF.setText(str(folder_path))

    #GET PDF FILE PATH FROM USER
    def input_path_pdf(self):
        file_name = QFileDialog.getOpenFileName(self, "Select File", "", "PDF FILES (*.pdf), *.pdf")
        if file_name:
            self.ui.INPUT_PATH_INPUT_PDF_.setText(str(file_name[0]))

    #VOICE OUT FILE IF BOTH PDF INPUTS ARE NOT EMPTY
    def pdf_file_dubbing(self):
        if self.ui.INPUT_PATH_INPUT_PDF_.text() != "" and self.ui.INPUT_PATH_OUTPUT_PDF.text() != "" and (self.ui.RADIO_RU_LANG_PDF.isChecked() or self.ui.RADIO_EN_LANG_PDF.isChecked()):
            if self.ui.RADIO_RU_LANG_PDF.isChecked():
                lang = 'ru'
            else: 
                lang = 'en'
            voiceover = pdf_to_mp3(file_path=self.ui.INPUT_PATH_INPUT_PDF_.text(), language=lang, save_path=self.ui.INPUT_PATH_OUTPUT_PDF.text())
            if (voiceover):
                self.ui.INPUT_PATH_INPUT_PDF_.setText("")
                self.ui.INPUT_PATH_OUTPUT_PDF.setText("")
                self.ui.RADIO_RU_LANG_PDF.setChecked(False)
                self.ui.RADIO_EN_LANG_PDF.setChecked(False)
                self.ui.stackedWidget.setCurrentWidget(self.ui.FINAL_PAGE)
            else:
                self.ui.INPUT_PATH_INPUT_PDF_.setText("")
                self.ui.INPUT_PATH_OUTPUT_PDF.setText("")
                self.ui.RADIO_RU_LANG_PDF.setChecked(False)
                self.ui.RADIO_EN_LANG_PDF.setChecked(False)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    exit(app.exec_())
