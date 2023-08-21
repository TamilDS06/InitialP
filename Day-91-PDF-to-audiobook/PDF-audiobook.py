import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QFileDialog, QLabel
from gtts import gTTS
import PyPDF2

class PDF2AudiobookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('PDF to Audiobook Converter')

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 50, 500, 200)

        self.load_button = QPushButton('Load PDF', self)
        self.load_button.setGeometry(50, 270, 100, 30)
        self.load_button.clicked.connect(self.load_pdf)

        self.convert_button = QPushButton('Convert to Audiobook', self)
        self.convert_button.setGeometry(200, 270, 150, 30)
        self.convert_button.clicked.connect(self.convert_to_audiobook)

        self.status_label = QLabel('', self)
        self.status_label.setGeometry(50, 320, 500, 30)

    def load_pdf(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if pdf_file:
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = '\n'.join([page.extract_text() for page in pdf_reader.pages])
                self.text_edit.setPlainText(text)

    def convert_to_audiobook(self):
        text = self.text_edit.toPlainText()
        if text:
            try:
                audio = gTTS(text)
                audio.save('audiobook.mp3')
                self.status_label.setText('Audiobook converted and saved as audiobook.mp3')
            except Exception as e:
                self.status_label.setText('Error converting to audiobook: ' + str(e))
        else:
            self.status_label.setText('No text to convert')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDF2AudiobookApp()
    window.show()
    sys.exit(app.exec_())
