import os
import sys
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from pytube import YouTube
from pytube.cli import on_progress
from GUI import Ui_MainWindow

class MainApp(QMainWindow , Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_UI()
        self.handel_PushButton()

    def handel_UI(self):
        self.setWindowTitle("Download Youtube")
        self.setFixedSize(500,251)

    def handel_PushButton(self):
        self.pushButton.clicked.connect(self.handle_Brows)
        self.pushButton_2.clicked.connect(self.get_video)
        self.pushButton_3.clicked.connect(self.download_video)

    def handle_Brows(self):
        save_place = QFileDialog.getExistingDirectory(self,"Select Download Derictory")
        self.lineEdit_2.setText(save_place)

    def get_video(self):
        video_url = self.lineEdit.text()
        video = YouTube(video_url)
        qalit = video.streams.all()
        i = 1
        for s in qalit:
            s = str(s).split(" ")
            f = list(s)
            f = str(i)+" "+f[2].replace("mime_type=","")+" "+(f[3].replace("res=","")).replace("abr=","")
            self.comboBox.addItem(f)
            i+=1

    def download_video(self):
        video_url = self.lineEdit.text()
        yt = YouTube(video_url,on_progress_callback=on_progress)
        video = yt.streams.all()
        index = self.comboBox.currentText()
        path = self.lineEdit_2.text()
        video = video[int(index.split(" ")[0]) - 1 ]
        video.download(path)
        QMessageBox.information(self, "Download", "The Download Complited")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
