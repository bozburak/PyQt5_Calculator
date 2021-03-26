__author__ = "Burak BOZ"
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QVBoxLayout, QHBoxLayout
import sys

class hesap_makinesi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setFixedWidth(270)
        self.setFixedHeight(220)
        self.hesap = ""
        self.islemyapilmismi = ""
        self.tiklanmismi = ""
        self.dugmeler = [x for x in range(10)]
        self.islemler = [z for z in range(4)]
        self.islemler_metin = ["+", "-", "*", "/"]

        """ LAYOUT AYARLARI """
        self.ana = QVBoxLayout(self)
        self.lineedit = QHBoxLayout(self)
        self.bir_iki_uc_geri = QHBoxLayout(self)
        self.dort_bes_alti_sil = QHBoxLayout(self)
        self.yedi_sekiz_dokuz_enter = QHBoxLayout(self)
        self.arti_eksi_carp_bol = QHBoxLayout(self)
        self.sifirr = QHBoxLayout(self)
        self.kesirr = QHBoxLayout(self)

        self.ana.addLayout(self.lineedit)
        self.ana.addLayout(self.bir_iki_uc_geri)
        self.ana.addLayout(self.dort_bes_alti_sil)
        self.ana.addLayout(self.yedi_sekiz_dokuz_enter)
        self.ana.addLayout(self.arti_eksi_carp_bol)
        self.ana.addLayout(self.sifirr)
        self.ana.addLayout(self.kesirr)



        """BUTON AYARLARI"""

        """ Sayı Butonlarının Ayarları """
        for i in range(10):
            self.dugmeler[i] = QPushButton(self)
            self.dugmeler[i].setText(str(i))
            self.dugmeler[i].setShortcut(str(i))
            self.islev_ata(i)

        """ Sayı Butonlarının Yerleşimi"""
        self.sifirr.addWidget(self.dugmeler[0])
        self.bir_iki_uc_geri.addWidget(self.dugmeler[1])
        self.bir_iki_uc_geri.addWidget(self.dugmeler[2])
        self.bir_iki_uc_geri.addWidget(self.dugmeler[3])
        self.dort_bes_alti_sil.addWidget(self.dugmeler[4])
        self.dort_bes_alti_sil.addWidget(self.dugmeler[5])
        self.dort_bes_alti_sil.addWidget(self.dugmeler[6])
        self.yedi_sekiz_dokuz_enter.addWidget(self.dugmeler[7])
        self.yedi_sekiz_dokuz_enter.addWidget(self.dugmeler[8])
        self.yedi_sekiz_dokuz_enter.addWidget(self.dugmeler[9])


        """ İşlem Butonlarının Ayarları """
        for j in range(4):
            self.islemler[j] = QPushButton(self)
            self.islemler[j].setText(str(self.islemler_metin[j]))
            self.islemler[j].setShortcut(str(self.islemler_metin[j]))

        self.islemler[0].clicked.connect(self.toplama)
        self.islemler[1].clicked.connect(self.cikarma)
        self.islemler[2].clicked.connect(self.carpma)
        self.islemler[3].clicked.connect(self.bolme)

        """ İşlem Butonlarının Yerleşimi"""
        for ı in range(4):
            self.arti_eksi_carp_bol.addWidget(self.islemler[ı])


        """ Diğer Butonların Ayarları """
        self.ekran = QLineEdit(self)
        self.ekran.setReadOnly(True)

        self.geribtn = QPushButton(self)
        self.geribtn.setText("←")
        self.geribtn.setShortcut("Backspace")

        self.silbtn = QPushButton(self)
        self.silbtn.setText("C")
        self.silbtn.setShortcut("Del")

        self.sonucbtn = QPushButton(self)
        self.sonucbtn.setText("⏎")
        self.sonucbtn.setShortcut("Return")

        self.kesirbtn = QPushButton(self)
        self.kesirbtn.setText(".")
        self.kesirbtn.setShortcut(".")

        self.silbtn.clicked.connect(self.silme)
        self.geribtn.clicked.connect(self.geri)
        self.kesirbtn.clicked.connect(self.kesir)
        self.sonucbtn.clicked.connect(self.sonuc)

        """ Diğer Butonların Yerleşimi """
        self.lineedit.addWidget(self.ekran)
        self.bir_iki_uc_geri.addWidget(self.geribtn)
        self.dort_bes_alti_sil.addWidget(self.silbtn)
        self.yedi_sekiz_dokuz_enter.addWidget(self.sonucbtn)
        self.kesirr.addWidget(self.kesirbtn)



    """FONKSİYONLAR"""

    """ Sayı Fonksiyonları """
    def islev(self, rakam):
        if self.islemyapilmismi == "evet":
            self.ekran.setText("")
            self.ekran.setText(self.ekran.text() + rakam)
            self.islemyapilmismi = ""
        else:
            self.ekran.setText(self.ekran.text() + str(rakam))

    def islev_ata(self, sayi):
        self.dugmeler[sayi].clicked.connect(lambda: self.islev(str(sayi)))

    """ İslem Fonksiyonları """
    def toplama(self):
        self.hesap = "+"
        if self.ekran.text() == "":
            self.ekran.setText(str(self.ilksayi))
        self.ilksayi = float(self.ekran.text())
        self.ekran.setText("")
        self.tiklanmismi = "ikinci"

    def cikarma(self):
        self.hesap = "-"
        if self.ekran.text() == "":
            self.ekran.setText(str(self.ilksayi))
        self.ilksayi = float(self.ekran.text())
        self.ekran.setText("")
        self.tiklanmismi = "ikinci"

    def carpma(self):
        self.hesap = "*"
        if self.ekran.text() == "":
            self.ekran.setText(str(self.ilksayi))
        self.ilksayi = float(self.ekran.text())
        self.ekran.setText("")
        self.tiklanmismi = "ikinci"

    def bolme(self):
        self.hesap = "/"
        if self.ekran.text() == "":
            self.ekran.setText(str(self.ilksayi))
        self.ilksayi = float(self.ekran.text())
        self.ekran.setText("")
        self.tiklanmismi = "ikinci"


    """ Diğer Fonksiyonlar """
    def silme(self):
        self.ekran.clear()
        self.tiklanmismi = "silme"

    def geri(self):
        self.ekran.backspace()
        self.tiklanmismi = "geri"

    def kesir(self):
        if self.ekran.text() == "":
            self.ekran.setText("")
        elif self.islemyapilmismi == "evet":
            self.ekran.setText("")
            self.islemyapilmismi = ""
        else:
            if self.tiklanmismi == "evet":
                self.ekran.setText(self.ekran.text())
            elif self.tiklanmismi == "ikinci":
                self.ekran.setText(self.ekran.text() + ".")
                self.tiklanmismi = "evet"
            elif self.tiklanmismi == "silme":
                self.ekran.setText(self.ekran.text() + ".")
                self.tiklanmismi = "evet"
            elif self.tiklanmismi == "geri":
                self.ekran.setText(self.ekran.text() + ".")
                self.tiklanmismi = "evet"
            else:
                self.ekran.setText(self.ekran.text() + ".")
                self.tiklanmismi = "evet"


    """ Sonuc Fonksiyonu """
    def sonuc(self):
        if self.hesap == "":
            self.ekran.setText("İşlem Yapmadınız!")
        else:
            self.ikincisayi = float(self.ekran.text())
            if self.hesap == "+":
                self.islem = self.ilksayi + self.ikincisayi
                if self.islem == int(self.islem):
                    self.ekran.setText(str(int(self.islem)))
                elif self.islem == float(self.islem):
                    self.ekran.setText(str(float(self.islem)))
            elif self.hesap == "-":
                self.islem = self.ilksayi - self.ikincisayi
                if self.islem == int(self.islem):
                    self.ekran.setText(str(int(self.islem)))
                elif self.islem == float(self.islem):
                    self.ekran.setText(str(float(self.islem)))
            elif self.hesap == "*":
                self.islem = self.ilksayi * self.ikincisayi
                if self.islem == int(self.islem):
                    self.ekran.setText(str(int(self.islem)))
                elif self.islem == float(self.islem):
                    self.ekran.setText(str(float(self.islem)))
            elif self.hesap == "/":
                if self.ikincisayi == 0:
                    self.ekran.setText("HATA")
                else:
                    self.islem = self.ilksayi / self.ikincisayi
                    if self.islem == int(self.islem):
                        self.ekran.setText(str(int(self.islem)))
                    elif self.islem == float(self.islem):
                        self.ekran.setText(str(float(self.islem)))
        self.islemyapilmismi = "evet"
        self.tiklanmismi = ""


uygulama = QApplication(sys.argv)
pencere = hesap_makinesi()
pencere.show()
uygulama.exec_()
