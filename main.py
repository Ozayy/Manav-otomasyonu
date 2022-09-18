import time
import datetime
import sys
from PyQt5 import QtCore, QtGui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QCalendarWidget
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime,QDate,QTime
from PyQt5.QtWidgets import QApplication,QWidget,QTimeEdit
import requests
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer,QRect,QPropertyAnimation,QPoint,QEasingCurve,QVariantAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
import smtplib
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

from manav import Ui_MainWindow




# KEY PRESS EVENTLERI ÖĞREN VE ENTERI KULLAN


class main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)



        self.connect = sqlite3.connect('C:\Manav_Veritabani\manav.db')
        self.im = self.connect.cursor()

        sebze = """CREATE TABLE IF NOT EXISTS Sebzeler(id INTEGER PRIMARY KEY AUTOINCREMENT,Sebze TEXT,Kilo TEXT)"""
        meyve = """CREATE TABLE IF NOT EXISTS Meyveler(id INTEGER PRIMARY KEY AUTOINCREMENT,Meyve VARHCAR(32),Kilo INTEGER)"""
        musteri_login="""CREATE TABLE IF NOT EXISTS Bilgiler(id INTEGER PRIMARY KEY AUTOINCREMENT,İsim TEXT,Soyisim TEXT, KullaniciAdi TEXT, Sifre TEXT,EPosta TEXT)"""
        muster_login2="""CREATE TABLE IF NOT EXISTS Bilgiler2(id INTEGER PRIMARY KEY AUTOINCREMENT,İsim TEXT,Soyisim TEXT,TcKimlik INTEGER,Cinsiyet TEXT, Telefon INTEGER,Adres TEXT)"""
        musteri_login3="""CREATE TABLE IF NOT EXISTS Bilgiler3(id INTEGER PRIMARY KEY AUTOINCREMENT,İsim TEXT,Soyisim TEXT,Dogum_Tarihi DATE,Gun INTEGER,Ay INTEGER,Yil INTEGER,Guncel_Tarih DATE)"""

        self.im.execute(musteri_login)
        self.im.execute(muster_login2)
        self.im.execute(musteri_login3)
        self.im.execute(sebze)
        self.im.execute(meyve)



        self.ana_ekran=0
        self.calisan_ekran=1
        self.listeleme_ekran=2
        self.musteri_login=3
        self.musteri_login2=4
        self.musteri_ekran=5
        self.meyve_ekran = 6

        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.start()
        self.timer.timeout.connect(self.digital)





        self.ui.calisan_button.clicked.connect(self.calisan_girisi)
        #ana sayfa
        self.ui.pushButton.clicked.connect(self.Ana_ekran)

        self.ui.pushButton_2.clicked.connect(self.Listeleme_ekrani)
        self.ui.sebze_kilo_buttonn.clicked.connect(self.sebze_kilo_buttonn)
        self.ui.meyve_kaydet.clicked.connect(self.meyve_kilo_butonn)
        self.ui.sebze_kilo_table_refreshh.clicked.connect(self.sebze_kilo_table_Refresh)
        self.ui.meyve_table_refresh.clicked.connect(self.meyve_table_refreshh)
        self.ui.tableWidgett.itemSelectionChanged.connect(self.doldur)
        self.ui.tableWidgett_2.itemSelectionChanged.connect(self.doldur_2)
        self.ui.sebze_guncellee.clicked.connect(self.sebze_guncelle)

        self.ui.musteri_button.clicked.connect(self.musteri_loginn)
        self.ui.pushButton_3.clicked.connect(self.giris_login)
        self.ui.pushButton_4.clicked.connect(self.musteri_loginn2)


        self.ui.kayit_ol_button.clicked.connect(self.kayit_button)
        self.ui.geri_git_button.clicked.connect(self.geri_git)


        self.ui.meyve_line.setPlaceholderText("Lütfen meyve giriniz")
        self.ui.meyve_kilo.setPlaceholderText("Lütfen kilo giriniz")
        self.ui.sebze_linee.setPlaceholderText("Lütfen sebze giriniz")
        self.ui.sebze_kilo_linee.setPlaceholderText("Lütfen kilo giriniz")

        self.ui.isim_line.setPlaceholderText("Zorunlu alandır")
        self.ui.soyisim_line.setPlaceholderText("Zorunlu alandır")
        self.ui.kullanici_line.setPlaceholderText("Zorunlu alandır")
        self.ui.sifre_line.setPlaceholderText("Zorunlu alandır")
        self.ui.tc_line.setPlaceholderText("Zorunlu alandır")
        self.ui.tel_line.setPlaceholderText("Tercihe bağlı")
        self.ui.eposta_line.setPlaceholderText("Zorunlu alandır")
        self.ui.adres_text.setPlaceholderText("Zorunlu alandır")

        self.timer=QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.musteri_ekrann)

        #self.ui.meyve_line.textEdited.connect(self.control)

        self.Ana_ekran()

    def digital(self):
        time=QTime.currentTime()
        last_time=time.addSecs(1)
        label_time=last_time.toString("hh:mm:ss")
        self.ui.label_4.setText(label_time)

    def musteri_ekrann(self):
        self.ui.stackedWidget.setCurrentIndex(self.musteri_ekran)
        self.ui.label_22.setText(self.kullanici)

        self.anim=QPropertyAnimation(self.ui.label_22,b"pos")
        self.anim.setEndValue(QPoint(150,60))
        self.anim.setDuration(2000)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.start()

        self.anim1 = QPropertyAnimation(self.ui.label_21, b"pos")
        self.anim1.setEndValue(QPoint(30, 60))
        self.anim1.setDuration(2000)
        self.anim1.setEasingCurve(QEasingCurve.OutBounce)
        self.anim1.start()

        self.anim2 = QPropertyAnimation(self.ui.label_31, b"pos")
        self.anim2.setEndValue(QPoint(50, 150))
        self.anim2.setDuration(2000)
        self.anim2.setEasingCurve(QEasingCurve.OutBounce)
        self.anim2.start()

        self.anim3 = QPropertyAnimation(self.ui.pushButton_5,b"pos")
        self.anim3.setEndValue(QPoint(50,200))
        self.anim3.setDuration(2000)
        self.anim3.setEasingCurve(QEasingCurve.OutBounce)
        self.anim3.start()

        self.anim4 = QPropertyAnimation(self.ui.pushButton_6,b"pos")
        self.anim4.setEndValue(QPoint(180,200))
        self.anim4.setDuration(2000)
        self.anim4.setEasingCurve(QEasingCurve.OutBounce)
        self.anim4.start()



        self.timer.start()
        self.animation=QVariantAnimation(startValue=QColor("red"),endValue=QColor("blue"),valueChanged=self.anim_1,duration=2000)
        self.timer.stop()
        self.animation.start()

        self.ui.pushButton_5.clicked.connect(self.sebze_bagla)

    def sebze_bagla(self):
        self.ui.stackedWidget.setCurrentIndex(self.meyve_ekran)

    def anim_1(self,v):

        self.ui.label_31.setStyleSheet("background-color: %s" % v.name())



    def giris_login(self):
        self.kullanici=self.ui.giris_kullanici_line.text()
        sifre=self.ui.giris_sifre_line.text()



        if self.kullanici=="" or sifre=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText("Kullanıcı adı veya şifre hatalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        else:
            self.im.execute("""SELECT * FROM Bilgiler WHERE KullaniciAdi=? and Sifre=?""", (self.kullanici,sifre))
            rows=self.im.fetchall()
            if len(rows)<1:
                messagebox = QMessageBox()
                messagebox.setIcon(QMessageBox.Warning)
                messagebox.setWindowTitle("Hatalı Giriş")
                messagebox.setText("Böyle bir hasta bulunamadı")
                messagebox.setStandardButtons(QMessageBox.Ok)
                buton_ok = messagebox.button(QMessageBox.Ok)
                buton_ok.setText("Tamam")
                messagebox.exec_()
            else:
                self.ui.statusbar.showMessage("Giriş Başarılı",3000)
                self.ui.statusbar.setStyleSheet("background-color : white")
                self.ui.giris_sifre_line.clear()
                self.ui.giris_kullanici_line.clear()
                self.musteri_ekrann()






    def isim_kontrol(self,isim):
        for kontrol in isim:
            x = kontrol.isdigit()
            if x == True:
                return x
    def soy_isim_kontrol(self,soyisim):
        for kontrol in soyisim:
            x = kontrol.isdigit()
            if x == True:
                return x

    def kullanici_isim(self,kullanici):
        for kontrol in kullanici:
            x = kontrol.isdigit()
            if x == True:
                return x
    def tc_kimlik_kontrol(self,tc_kimlik):
        for kontrol in tc_kimlik:
            x = kontrol.isalpha()
            if x == True:
                return x
    def telefon_kontrol(self,tel):
        for kontrol in tel:
            x = kontrol.isalpha()
            if x == True:
                return x

    def geri_git(self):
        self.ui.isim_line.clear()
        self.ui.soyisim_line.clear()
        self.ui.kullanici_line.clear()
        self.ui.sifre_line.clear()
        self.ui.eposta_line.clear()
        self.ui.comboBox.clear()
        self.ui.adres_text.clear()
        self.ui.tel_line.clear()
        self.ui.tc_line.clear()
        self.ui.giris_kullanici_line.clear()
        self.ui.giris_sifre_line.clear()
        self.ui.stackedWidget.setCurrentIndex(self.musteri_login)
    def kayit_button(self,d):



        isim=self.ui.isim_line.text().capitalize()

        soyisim=self.ui.soyisim_line.text().capitalize()
        kullanici=self.ui.kullanici_line.text()
        sifre=self.ui.sifre_line.text()
        tc_kimlik=self.ui.tc_line.text()
        cinsiyet=self.ui.comboBox.currentText()
        tel=self.ui.tel_line.text()
        eposta=self.ui.eposta_line.text()

        adres=self.ui.adres_text.toPlainText().capitalize()
        dogum_tarihi=self.ui.dogum_dateedit.text()
        gun=self.ui.dogum_dateedit.date().day()
        ay=self.ui.dogum_dateedit.date().month()
        yil=self.ui.dogum_dateedit.date().year()
        guncel_tarih=QDate.currentDate().year()

        veriyi_getir = self.im.execute("SELECT * FROM Bilgiler2 WHERE TcKimlik='"+tc_kimlik+"' ")
        karsilastir=veriyi_getir.fetchall()


        if isim=="" or soyisim=="" or kullanici=="" or sifre=="" or tc_kimlik=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Boş olmamalı")
            messagebox.setText(
                "İsim,soyisim,kullanıcı adı,şifre ve tc kimlik alanı boş bırakılmamalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        elif karsilastir:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Kayıt zaten var")
            messagebox.setText(
                "Bu kayıt sistemde mevcut")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        elif cinsiyet=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Boş olmamalı")
            messagebox.setText(
                "Cinsiyet alanı boş bırakılamaz")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()



        elif tel=="" or eposta=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Boş olmamalı")
            messagebox.setText(
                "Telefon ve eposta alanları boş bırakılmamalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()

        elif adres=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Boş Bırakılmamalı")
            messagebox.setText(
                "Lütfen adres bilginizi giriniz")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()





        elif self.isim_kontrol(isim):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "İsim alanına rakam giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.isim_line.clear()
        elif self.soy_isim_kontrol(soyisim):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "Soyisim alanına rakam giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.soyisim_line.clear()
        elif self.kullanici_isim(kullanici):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "Kullanıcı alanına rakam giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.kullanici_line.clear()
        elif len(sifre)!=6:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "Lütfen 6 haneli bir şifre giriniz")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.sifre_line.clear()

        elif self.tc_kimlik_kontrol(tc_kimlik):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Harf giremezsin")
            messagebox.setText(
                "Tc Kimlik alanına harf giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.tc_line.clear()
        elif len(tc_kimlik)!=11:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("11 Haneli olmak zorunda")
            messagebox.setText(
                "Lütfen 11 Haneli Tc Kimliğinizi Giriniz")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.tc_line.clear()

        elif self.telefon_kontrol(tel):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Harf giremezsin")
            messagebox.setText(
                "Telefwon alanına harf giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.tc_line.clear()


        else:
            #_sifre=hashlib.md5(sifre.encode())
            self.im.execute("""INSERT INTO Bilgiler(İsim,Soyisim,KullaniciAdi,Sifre,EPosta) VALUES (?,?,?,?,?)""", [isim,soyisim,kullanici,sifre,eposta])
            self.im.execute("""INSERT INTO Bilgiler2(İsim,Soyisim,TcKimlik,Cinsiyet,Telefon,Adres) VALUES (?,?,?,?,?,?)""",[isim,soyisim,tc_kimlik,cinsiyet,tel,adres])
            self.im.execute("""INSERT INTO Bilgiler3(İsim,Soyisim,Dogum_Tarihi,Gun,Ay,Yil,Guncel_Tarih) VALUES (?,?,?,?,?,?,?)""",[isim,soyisim,dogum_tarihi,gun,ay,yil,guncel_tarih])
            self.connect.commit()
            self.ui.statusbar.showMessage("Kayıt oluşturuldu", 1500)
            self.ui.statusbar.setStyleSheet("background-color : white")
            self.ui.isim_line.clear()
            self.ui.soyisim_line.clear()
            self.ui.kullanici_line.clear()
            self.ui.sifre_line.clear()
            self.ui.eposta_line.clear()
            self.ui.adres_text.clear()
            self.ui.tel_line.clear()
            self.ui.tc_line.clear()



            try:
                gonderen = "ozaytepe111@gmail.com"
                sifre = "ftdzhurfrrgyyqnz"
                mail=smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login(gonderen,sifre)

                mesaj=MIMEMultipart()
                asd= f"Merhaba {isim} {soyisim}"
                mesaj["From"]="ozaytepe111@gmail.com"
                mesaj["Subject"]="BU BİR BİLDİRİM MESAJIDIR"
                mesaj["To"]=eposta

                body = asd + " Bizi seçtiğiniz için teşekkürler"

                body_text=MIMEText(body,'plain')
                mesaj.attach(body_text)

                mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
                print("mail gonderıldı bak")
                mail.close()
            except:
                print("Hata:",sys.exc_info()[0])





    def musteri_loginn2(self):
        self.ui.stackedWidget.setCurrentIndex(self.musteri_login2)

    def musteri_loginn(self):
        self.ui.stackedWidget.setCurrentIndex(self.musteri_login)


    def calisan_girisi(self):
        self.ui.stackedWidget.setCurrentIndex(self.calisan_ekran)
    def Ana_ekran(self):
        self.ui.tableWidgett.clear()
        self.ui.stackedWidget.setCurrentIndex(self.ana_ekran)
    '''
    def control(self):
        if self.ui.meyve_line=="":
            self.ui.meyve_line.setStyleSheet("border: 2px solid lightskyblue;")
        else:
            self.ui.meyve_line.setStyleSheet("border: 2px solid red")
            self.ui.meyve_line.setStyleSheet("background-color: rgb(255, 255, 255);")
    '''

    def Listeleme_ekrani(self):


        sifre1=self.ui.lineEdit_3.text()

        sifre="12345"

        if sifre1==sifre:
            self.ui.stackedWidget.setCurrentIndex(self.listeleme_ekran)
            self.ui.statusbar.showMessage("Giriş Başarılı", 1500)
            self.ui.statusbar.setStyleSheet("background-color : white")
            self.ui.lineEdit_3.clear()
        else:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText(
                "Şifre boş veya hatalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()

    def meyve_int_kontrol(self,meyve):
        for kontrol in meyve:
            x = kontrol.isdigit()
            if x == True:
                return x
    def meyve_kilo_str_kontrol(self,meyve_kilo):
        for kontrol in meyve_kilo:
            x = kontrol.isalpha()
            if x == True:
                return x

    def int_kontroll(self,sebze):
        for kontrol in sebze:
            x=kontrol.isdigit()
            if x == True:
                return x
    def str_kontrol(self,sebze_kilo):
        for kontrol in sebze_kilo:
            x = kontrol.isalpha()
            if x == True:
                return x

    def closeEvent(self,event):
        message=QMessageBox(QMessageBox.Warning,"Çıkış Ekranı","Veriler Kaybolacak Emin misin?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        message.exec()




    def sebze_kilo_buttonn(self):


        sebze=self.ui.sebze_linee.text()
        sebze_kilo=self.ui.sebze_kilo_linee.text()
        veriyi_getir=self.im.execute("SELECT * FROM Sebzeler WHERE Sebze='"+sebze+"'")
        karsilastir=veriyi_getir.fetchall()





        if sebze=="" or sebze_kilo=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText("Sebze ve kilo alanları boş bırakılmamalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()

        elif self.int_kontroll(sebze):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "Sebze Bölümüne rakam giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.sebze_linee.clear()
            self.ui.sebze_kilo_linee.clear()



        elif self.str_kontrol(sebze_kilo):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Harf Giremezsin")
            messagebox.setText(
                "Kilo Bölümüne harf giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.sebze_linee.clear()
            self.ui.sebze_kilo_linee.clear()

        elif karsilastir:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Kayıt Var")
            messagebox.setText("Sistemde böyle bir ürün bulunmaktadır")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.sebze_linee.clear()
            self.ui.sebze_kilo_linee.clear()
        elif sebze == "":
            self.im.execute("""DELETE FROM Sebzeler  WHERE Sebze=? """, [sebze])
            self.connect.commit()

        else:


            self.im.execute("""INSERT INTO Sebzeler(Sebze,Kilo) VALUES (?,?)""",[sebze,sebze_kilo])
            self.connect.commit()
            self.ui.statusbar.showMessage("Ürün Kaydedildi", 1500)
            self.ui.statusbar.setStyleSheet("background-color : white")
            self.ui.sebze_linee.clear()
            self.ui.sebze_kilo_linee.clear()





    def meyve_kilo_butonn(self):


        meyve=self.ui.meyve_line.text()
        meyve_kilo=self.ui.meyve_kilo.text()
        veriyi_getir=self.im.execute("SELECT * FROM Meyveler WHERE Meyve='"+meyve+"'")
        karsilastir=veriyi_getir.fetchall()


        if meyve=="" or meyve_kilo=="":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText("Meyve ve kilo alanları boş bırakılmamalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()


        elif self.meyve_int_kontrol(meyve):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Rakam giremezsin")
            messagebox.setText(
                "Meyve Bölümüne rakam giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.meyve_line.clear()
            self.ui.meyve_kilo.clear()


        elif self.meyve_kilo_str_kontrol(meyve_kilo):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Harf Giremezsin")
            messagebox.setText(
                "Kilo Bölümüne harf giremezsin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.meyve_line.clear()
            self.ui.meyve_kilo.clear()



        elif karsilastir:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Kayıt Var")
            messagebox.setText("Sistemde böyle bir ürün bulunmaktadır")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.meyve_line.clear()
            self.ui.meyve_kilo.clear()
        elif meyve == "":
            self.im.execute("""DELETE FROM Meyveler  WHERE Meyve =? """, [meyve])
            self.connect.commit()

        else:

            self.im.execute("""INSERT INTO Meyveler(Meyve,Kilo) VALUES (?,?)""",[meyve,meyve_kilo])
            self.connect.commit()
            self.ui.statusbar.showMessage("Ürün Kaydedildi", 1500)
            self.ui.statusbar.setStyleSheet("background-color : white")

            self.ui.meyve_line.clear()
            self.ui.meyve_kilo.clear()




    def sebze_kilo_table_Refresh(self):
        self.ui.tableWidgett_2.clear()
        self.ui.tableWidgett.setHorizontalHeaderLabels(('Sebze','Kilo'))
        self.ui.tableWidgett.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidgett.setSelectionMode(QAbstractItemView.SingleSelection) #tek seçeneği seçmek
        self.ui.tableWidgett.setAlternatingRowColors(True)
        pallete=self.ui.tableWidgett.palette()
        pallete.setColor(QPalette.Background,QColor(60,60,60))
        pallete.setColor(QPalette.AlternateBase,QColor("darkkhaki"))
        pallete.setColor(QPalette.Base,QColor('#bbb'))

        self.ui.tableWidgett.setPalette(pallete)



        connect = sqlite3.connect('C:\Manav_Veritabani\manav.db')
        im = connect.cursor()

        im.execute("""SELECT Sebze,Kilo FROM Sebzeler""")
        okuma=im.fetchall()



        self.ui.tableWidgett.setRowCount(0)
        for row_number, row_data in enumerate(okuma):
            self.ui.tableWidgett.insertRow(row_number)
            for columb_number, data in enumerate(row_data):
                self.ui.tableWidgett.setItem(row_number, columb_number, QTableWidgetItem(str(data)))

    def meyve_table_refreshh(self):
        self.ui.tableWidgett.clear()
        self.ui.tableWidgett_2.setHorizontalHeaderLabels(('Meyve','Kilo'))
        self.ui.tableWidgett_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidgett_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidgett_2.setAlternatingRowColors(True)

        pallete = self.ui.tableWidgett_2.palette()
        pallete.setColor(QPalette.Background, QColor(60, 60, 60))
        pallete.setColor(QPalette.AlternateBase, QColor("darkkhaki"))
        pallete.setColor(QPalette.Base, QColor('#bbb'))

        self.ui.tableWidgett_2.setPalette(pallete)


        connect = sqlite3.connect('C:\Manav_Veritabani\manav.db')
        im = connect.cursor()

        im.execute("""SELECT Meyve,Kilo FROM Meyveler""")
        okuma = im.fetchall()



        self.ui.tableWidgett_2.setRowCount(0)
        for row_number, row_data in enumerate(okuma):
            self.ui.tableWidgett_2.insertRow(row_number)
            for columb_number, data in enumerate(row_data):
                self.ui.tableWidgett_2.setItem(row_number, columb_number, QTableWidgetItem(str(data)))


    def doldur(self):
        try:
            secili=self.ui.tableWidgett.selectedItems()

            self.ui.sebze_table_linee.setText(secili[0].text())
            self.ui.kilo_table_linee.setText(secili[1].text())

            if secili==[]:
                return

        except Exception as Hata:
            self.ui.statusbar.showMessage("Hata var",2000)
    def doldur_2(self):
        try:
            secili=self.ui.tableWidgett_2.selectedItems()

            self.ui.meyve_table_line.setText(secili[0].text())
            self.ui.meyve_kilo_line.setText(secili[1].text())
        except Exception as Hata:
            self.ui.statusbar.showMessage("Hata var",2000)


    def sebze_guncelle(self):


        try:
            secili = self.ui.tableWidgett.selectedItems()
            _Id = int(secili[0].text())
            sebze= (self.ui.sebze_table_linee.text())
            kilo= (self.ui.sebze_kilo_linee.text())

            im.execute("UPDATE Sebzeler SET Sebze=?,Kilo=? WHERE id=?", [sebze, kilo, _Id])

            baglanti.commit()
            self.ui.statusbar.showMessage("GÜNCELLEME BAŞARILI", 3000)

        except Exception as Hata:
            self.ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))










































































