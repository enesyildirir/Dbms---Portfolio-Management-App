from PyQt5 import QtWidgets, uic
import sys

class Uygulamam(QtWidgets.QMainWindow):
    def __init__(self):
        super(Uygulamam, self).__init__()
        # .ui dosyasını burada yüklüyoruz
        uic.loadUi('arayüzPart3.ui', self) 
        
        # Örnek: Butona tıklama özelliği eklemek isterseniz:
        # self.pushButton.clicked.connect(self.fonksiyonum)


# Uygulamayı çalıştıran standart kodlar
app = QtWidgets.QApplication(sys.argv)
pencere = Uygulamam()
pencere.show()
app.exec_()