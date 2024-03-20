import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QComboBox, QListWidget, QFileDialog, QScrollArea, QMessageBox,
    QCheckBox
)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt


class StokYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stok Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' STOK YÖNETİMİ')
        baslik_etiketi.setStyleSheet("font-size: 48px; font-weight: bold; color: #008C9E;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        motor_tanimlari_btn = QPushButton('MOTOR TANIMLARI')
        motor_tanimlari_btn.setStyleSheet("background-color: #008C9E; color: white;font-size: 24px; padding: 20px;")
        motor_tanimlari_btn.clicked.connect(self.MotorTanimlariSayfasiniAc)#buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(motor_tanimlari_btn)
     
        motor_tanimlar_listesi_btn = QPushButton('MOTOR TANIMLAR LİSTESİ')
        motor_tanimlar_listesi_btn.setStyleSheet("background-color: #BB3A6A; color: white;font-size: 24px; padding: 20px;")
        motor_tanimlar_listesi_btn.clicked.connect(self.MotorTanimlarListesiAc)#buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        
        layout.addWidget(motor_tanimlar_listesi_btn)

        motor_giris_hareketleri_btn = QPushButton('MOTOR GİRİŞ HAREKETLERİ')
        motor_giris_hareketleri_btn.setStyleSheet("background-color: #008C9E; color: white;font-size: 24px; padding: 20px;")
        
        layout.addWidget(motor_giris_hareketleri_btn)

        motor_cikis_hareketleri_btn = QPushButton('MOTOR ÇIKIŞ HAREKETLERİ')
        motor_cikis_hareketleri_btn.setStyleSheet("background-color: #BB3A6A; color: white;font-size: 24px; padding: 20px;")
        layout.addWidget(motor_cikis_hareketleri_btn)
    
        bosluk = QLabel()
        bosluk.setAlignment(Qt.AlignCenter)
        layout.addWidget(bosluk)
           
        
        self.setLayout(layout)  
    def MotorTanimlariSayfasiniAc(self):
        self.motor_tanimlari = MotorTanimlariSayfasi()
        self.motor_tanimlari.show()
    def MotorTanimlarListesiAc(self):
        self.motor_tanimlar_listesi = MotorTanimlarListesiSayfasi()
        self.motor_tanimlar_listesi.show()
class MotorTanimlariSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Motor Tanımları')
        self.setGeometry(200, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))
        self.kayit_sayaci = 1  
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        widget = QWidget()
        scroll_area.setWidget(widget)
        scroll_layout = QVBoxLayout()
        widget.setLayout(scroll_layout)

        marka_model_layout = QHBoxLayout()
        self.marka_combo = QComboBox()
        self.marka_combo.addItems(['Marka 1', 'Marka 2', 'Marka 3'])
        self.marka_combo.setCurrentIndex(-1)  
        self.marka_combo.currentIndexChanged.connect(self.on_marka_changed)
        self.model_combo = QComboBox()
        marka_model_layout.addWidget(QLabel("Marka:"))
        marka_model_layout.addWidget(self.marka_combo)
        marka_model_layout.addWidget(QLabel("Model:"))
        marka_model_layout.addWidget(self.model_combo)
        scroll_layout.addLayout(marka_model_layout)

        self.text_inputs = {}  
        self.addDualTextInputs(scroll_layout, [
            ("ID", "Tipi", "Yıl"),
            ("Araç Durumu", "Km"),
            ("Motor Hacmi", "Motor Gücü"),
            ("Silindir Sayısı", "Vites"),
            ("Soğutma", "Renk")
        ])

        grup_layout = QHBoxLayout()
        self.grup_combo = QComboBox()
        self.grup_combo.addItems(['SIFIR', 'İKİNCİ EL', 'KONSİNYE'])
        grup_layout.addWidget(QLabel("Grup:"))
        grup_layout.addWidget(self.grup_combo)
        scroll_layout.addLayout(grup_layout)

        guvenlik_layout = QHBoxLayout()
        self.abs_checkbox = QCheckBox('ABS')
        self.cekis_checkbox = QCheckBox('Çekiş Kontrolü')
        self.navigat_checkbox = QCheckBox('Navigasyon')
        guvenlik_layout.addWidget(QLabel("Güvenlik:"))
        guvenlik_layout.addWidget(self.abs_checkbox)
        guvenlik_layout.addWidget(self.cekis_checkbox)
        guvenlik_layout.addWidget(self.navigat_checkbox)
        scroll_layout.addLayout(guvenlik_layout)

        aksesuar_layout = QHBoxLayout()
        self.cam_checkbox = QCheckBox('Ön Cam')
        self.led_checkbox = QCheckBox('LED Stop')
        self.navi_checkbox = QCheckBox('Navigasyon')
        aksesuar_layout.addWidget(QLabel("Aksesuarlar:"))
        aksesuar_layout.addWidget(self.cam_checkbox)
        aksesuar_layout.addWidget(self.led_checkbox)
        aksesuar_layout.addWidget(self.navi_checkbox)
        scroll_layout.addLayout(aksesuar_layout)

        self.addMediaSection(scroll_layout, "Resimler", "Resim Ekle")
        self.addMediaSection(scroll_layout, "Videolar", "Video Ekle")
        self.addMediaSection(scroll_layout, "Hasarlı Resimler", "Hasarlı Resim Ekle")
        self.addMediaSection(scroll_layout, "Hasarlı Videolar", "Hasarlı Video Ekle")
      
        kaydet_btn = QPushButton('Kaydet')
        kaydet_btn.clicked.connect(self.kaydet)
        kaydet_btn.setStyleSheet("""
            QPushButton {
                background-color: #008C9E;
                border: none;
                color: white;
                padding: 12px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 18px;
                margin: 12px 0px;
                transition-duration: 0.4s;
                cursor: pointer;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E37222;
                color: white;
            }
        """)
        scroll_layout.addWidget(kaydet_btn, alignment=Qt.AlignCenter)

        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
            }
            QLabel {
                font-size: 16px;
                color: #37474F;
            }
            QLineEdit, QComboBox, QCheckBox {
                font-size: 16px;
                padding: 8px;
                border: 1px solid #B0BEC5;
                border-radius: 3px;
            }
            QScrollArea {
                background-color: #E0E0E0;
                border: 2px solid #BDBDBD;
            }
            QPushButton {
                font-size: 16px;
                background-color: #008C9E;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #BB3A6A;
            }
        """)
        
        # Set font for all widgets
        font = QFont("Arial", 12)
        self.setFont(font)

    def addDualTextInputs(self, layout, labels):
        for label_group in labels:
            text_layout = QHBoxLayout()
            for label_text in label_group:
                label = QLabel(label_text + ":")
                line_edit = QLineEdit()
                text_layout.addWidget(label)
                text_layout.addWidget(line_edit)
                if label_text == "ID":
                    line_edit.setText(str(self.kayit_sayaci))
                self.text_inputs[label_text] = line_edit
            layout.addLayout(text_layout)

    def addMediaSection(self, layout, title, button_text):
        media_layout = QVBoxLayout()
        media_layout.addWidget(QLabel(title))
        list_widget = QListWidget()
        list_widget.setFixedHeight(120)
        list_widget.setObjectName(title)  # ListWidget'ın adını ayarla
        media_layout.addWidget(list_widget)
        dosya_ekle_btn = QPushButton(button_text)
        dosya_ekle_btn.clicked.connect(lambda: self.dosya_ekle(list_widget))
        media_layout.addWidget(dosya_ekle_btn)
        layout.addLayout(media_layout)

    def dosya_ekle(self, list_widget):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "Dosya Seç")
        if dosya_yolu:
            list_widget.addItem(dosya_yolu)

    def kaydet(self):
        grup = self.grup_combo.currentText()
        marka = self.marka_combo.currentText()
        model = self.model_combo.currentText()
        text_inputs_values = {key: widget.text() for key, widget in self.text_inputs.items()}
        guvenlik_secenekleri = [self.abs_checkbox.text(), self.cekis_checkbox.text(), self.navigat_checkbox.text()]
        aksesuar_secenekleri = [self.cam_checkbox.text(), self.led_checkbox.text(), self.navi_checkbox.text()]
        resimler = [self.findChild(QListWidget, "Resimler").item(i).text() for i in range(self.findChild(QListWidget, "Resimler").count())]
        videolar = [self.findChild(QListWidget, "Videolar").item(i).text() for i in range(self.findChild(QListWidget, "Videolar").count())]
        hasarli_resimler = [self.findChild(QListWidget, "Hasarlı Resimler").item(i).text() for i in range(self.findChild(QListWidget, "Hasarlı Resimler").count())]
        hasarli_videolar = [self.findChild(QListWidget, "Hasarlı Videolar").item(i).text() for i in range(self.findChild(QListWidget, "Hasarlı Videolar").count())]

        if grup == 'SIFIR':
            print("Sıfır Motorsikletler grubuna kaydedildi:")
            print("Marka:", marka)
            print("Model:", model)
            print("Diğer değerler:", text_inputs_values)
            print("Güvenlik seçenekleri:", guvenlik_secenekleri)
            print("Aksesuar seçenekleri:", aksesuar_secenekleri)
            print("Resimler:", resimler)
            print("Videolar:", videolar)
            print("Hasarlı Resimler:", hasarli_resimler)
            print("Hasarlı Videolar:", hasarli_videolar)
        elif grup == 'İKİNCİ EL':
            print("İkinci El Motorsikletler grubuna kaydedildi:")
            # İkinci El Motorsikletler grubuna göre kayıt işlemleri
        elif grup == 'KONSİNYE':
            print("Konsinye Motorsikletler grubuna kaydedildi:")
            # Konsinye Motorsikletler grubuna göre kayıt işlemleri

        QMessageBox.information(self, "Bilgi", "Veri başarıyla kaydedildi!")

    def on_marka_changed(self, index):
        marka = self.marka_combo.currentText()
        if marka == 'Marka 1':
            self.model_combo.clear()
            self.model_combo.addItems(['Model 1', 'Model 2', 'Model 3'])
        elif marka == 'Marka 2':
            self.model_combo.clear()
            self.model_combo.addItems(['Model A', 'Model B', 'Model C'])
        elif marka == 'Marka 3':
            self.model_combo.clear()
            self.model_combo.addItems(['Model X', 'Model Y', 'Model Z'])
class MotorTanimlarListesiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Motor Tanımları listesi')
        self.setGeometry(200, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))
        self.kayit_sayaci = 1  
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' MOTOR TANIMLAR LİSTESİ ')
        baslik_etiketi.setStyleSheet("font-size: 48px; font-weight: bold; color: #BB3A6A;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        motor_tanimlar_listesi_giris = QPushButton('SIFIR MOTORSİKLETLERİ LİSTELEYİN')
        motor_tanimlar_listesi_giris.setStyleSheet("background-color: #E37222; color: white;font-size: 24px; padding: 20px;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(motor_tanimlar_listesi_giris)
     
        motor_tanimlar_listesi_giris = QPushButton('İKİNCİ EL MOTORSİKLETLERİ LİSTELEYİN')
        motor_tanimlar_listesi_giris.setStyleSheet("background-color: #BB3A6A; color: white;font-size: 24px; padding: 20px;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(motor_tanimlar_listesi_giris)
        
        motor_tanimlar_listesi_giris = QPushButton('KONSİNYE MOTORSİKLETLERİ LİSTELEYİN')
        motor_tanimlar_listesi_giris.setStyleSheet("background-color: #008C9E; color: white;font-size: 24px; padding: 20px;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(motor_tanimlar_listesi_giris)
     

        self.setLayout(layout)      
class SatinAlmaYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Satınalma Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()
       
        bosluk = QLabel()
        bosluk.setStyleSheet("font-size: 10px; color: #008C9E;")
        bosluk.setAlignment(Qt.AlignCenter)
        layout.addWidget(bosluk)
        
        
        #BAŞLIK
        baslik_etiketi = QLabel(' SATIN ALMA YÖNETİMİ SAYFASI ')
        baslik_etiketi.setStyleSheet("font-size: 48px; font-weight: bold; color: #008C9E;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white; font-size: 24px; padding: 20px;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white; font-size: 24px; padding: 20px;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white; font-size: 24px; padding: 20px;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white; font-size: 24px; padding: 20px;")
        layout.addWidget(satin_alma_masraflar_btn)

        bosluk = QLabel()
        bosluk.setStyleSheet("font-size: 10px; color: #008C9E;")
        bosluk.setAlignment(Qt.AlignCenter)
        layout.addWidget(bosluk)
        
        self.setLayout(layout)
class KonsinyeMotorsikletYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Konsinye Motorsiklet Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' KONSİNYE MOTORSİKLET YÖNETİMİ SAYFASI ')
        baslik_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class SatisYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Satış Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' SATIŞ YÖNETİMİ SAYFASI ')
        baslik_etiketi.setStyleSheet("font-size: 48px; font-weight: bold; color: #E37222;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class MotorsikletServisYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Motosiklet Servis Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' MOTOSİKLET SERVİS YÖNETİMİ SAYFASI')
        baslik_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class FinansYonetimiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Finans Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' FİNANS YÖNETİM SAYFASI')
        baslik_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class RaporlarSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Raporlar Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' RAPORLAR SAYFASI')
        baslik_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class YetkiliSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yetkili Yönetimi Sayfası')
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
       #BAŞLIK
        baslik_etiketi = QLabel(' YETKİLİ YÖNETİMİ SAYFASI')
        baslik_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)
        
        
        # Dört yeni buton ekleniyor
        sifir_motor_alma_btn = QPushButton('SIFIR MOTORSİKLET ALMA İŞLEMLERİ')
        sifir_motor_alma_btn.setStyleSheet("background-color: #008C9E; color: white;")
        #buraya ilgili sayfaya gitmesi için tıklama koyma yeri
        layout.addWidget(sifir_motor_alma_btn)
     
        ikinciel_motor_alma_btn = QPushButton('2. EL MOTORRSİKLET ALMA İŞLEMLERİ')
        ikinciel_motor_alma_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        
        layout.addWidget(ikinciel_motor_alma_btn)

        satin_alma_teklifi_gelen_btn = QPushButton('SATINALMA TEKLİFİ GELEN MOTORSİKLETLER')
        satin_alma_teklifi_gelen_btn.setStyleSheet("background-color: #008C9E; color: white;")
        
        layout.addWidget(satin_alma_teklifi_gelen_btn)

        satin_alma_masraflar_btn = QPushButton(' MASRAF RAPORLAR  ')
        satin_alma_masraflar_btn.setStyleSheet("background-color: #BB3A6A; color: white;")
        layout.addWidget(satin_alma_masraflar_btn)

        self.setLayout(layout)
class MotorcycleShopUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MOTORSİKLET MAĞZASI')
        self.setGeometry(200, 200, 600, 400)
        self.setStyleSheet("background-color: #F2F2F2; color: #333333;")
        self.initArayuz()

    def initArayuz(self):
        layout = QVBoxLayout()

        # Logo
        logo_etiketi = QLabel()
        logo_pixmap = QPixmap('italian_flag.png').scaledToHeight(300)
        logo_etiketi.setPixmap(logo_pixmap)
        layout.addWidget(logo_etiketi, alignment=Qt.AlignCenter)

        # Başlık
        baslik_etiketi = QLabel('MOTOSİKLET MAĞAZA YÖNETİCİSİ ')
        baslik_etiketi.setStyleSheet("font-size: 48px; font-weight: bold; color: #008C9E;")
        layout.addWidget(baslik_etiketi, alignment=Qt.AlignCenter)

        karsilama = QLabel('UYGULAMAMIZA HOŞGELSİNİZ!', self)
        karsilama.setStyleSheet("font-size: 34px; color: #666666;")
        karsilama.setAlignment(Qt.AlignCenter)
        layout.addWidget(karsilama)

        # Stok Yönetimi ve Satın Alma Yönetimi düğmeleri
        row1_layout = QHBoxLayout()
        stok_yonetimi_dugme = QPushButton('STOK YÖNETİMİ')
        stok_yonetimi_dugme.setStyleSheet("background-color: #008C9E; color: white; font-size: 24px; padding: 20px;")
        stok_yonetimi_dugme.clicked.connect(self.stokYonetimiSayfasiniAc)
        satin_alma_yonetimi_dugme = QPushButton('SATIN ALMA YÖNETİMİ')
        satin_alma_yonetimi_dugme.setStyleSheet("background-color: #008C9E; color: white; font-size: 24px; padding: 20px;")
        satin_alma_yonetimi_dugme.clicked.connect(self.satinAlmaYonetimiSayfasiniAc)
        row1_layout.addWidget(stok_yonetimi_dugme)
        row1_layout.addWidget(satin_alma_yonetimi_dugme)
        layout.addLayout(row1_layout)

        # Satış Yönetimi ve Konsinye Motorsiklet Yönetimi düğmeleri
        row2_layout = QHBoxLayout()
        satis_yonetimi_dugme = QPushButton('SATIŞ YÖNETİMİ')
        satis_yonetimi_dugme.setStyleSheet("background-color: #E37222; color: white; font-size: 24px; padding: 20px;")
        satis_yonetimi_dugme.clicked.connect(self.satisYonetimiSayfasiniAc)
        konsinye_yonetimi_dugme = QPushButton('KONSİNYE MOTORSİKLET YÖNETİMİ')
        konsinye_yonetimi_dugme.setStyleSheet("background-color: #E37222; color: white; font-size: 24px; padding: 20px;")
        konsinye_yonetimi_dugme.clicked.connect(self.konsinyeMotorsikletYonetimiSayfasiniAc)
        row2_layout.addWidget(satis_yonetimi_dugme)
        row2_layout.addWidget(konsinye_yonetimi_dugme)
        layout.addLayout(row2_layout)

        # Motorsiklet Servis Yönetimi ve Finans Yönetimi düğmeleri
        row3_layout = QHBoxLayout()
        servis_yonetimi_dugme = QPushButton('MOTORSİKLET SERVİS YÖNETİMİ')
        servis_yonetimi_dugme.setStyleSheet("background-color: #BB3A6A; color: white; font-size: 24px; padding: 20px;")
        servis_yonetimi_dugme.clicked.connect(self.motorsikletServisYonetimiSayfasiniAc)
        finans_yonetimi_dugme = QPushButton('FİNANS YÖNETİMİ')
        finans_yonetimi_dugme.setStyleSheet("background-color: #BB3A6A; color: white; font-size: 24px; padding: 20px;")
        finans_yonetimi_dugme.clicked.connect(self.finansYonetimiSayfasiniAc)
        row3_layout.addWidget(servis_yonetimi_dugme)
        row3_layout.addWidget(finans_yonetimi_dugme)
        layout.addLayout(row3_layout)

        # Raporlar düğmesi
        raporlar_dugme = QPushButton('RAPORLAR')
        raporlar_dugme.setStyleSheet("background-color: #4B4E6D; color: white;font-size: 24px; padding: 20px;")
        raporlar_dugme.clicked.connect(self.raporlarSayfasiniAc)
        layout.addWidget(raporlar_dugme)

        # Programı kullanacak kişilere yetki verme düğmesi
        yetkili_dugme = QPushButton('YETKİLİ')
        yetkili_dugme.setStyleSheet("background-color: #E37222; color: white;font-size: 24px; padding: 20px;")
        yetkili_dugme.clicked.connect(self.yetkiliSayfasiniAc)
        layout.addWidget(yetkili_dugme)

        iletisim_bilgileri = QLabel('İLETİŞİM BİLGİLERİ: \nTelefon: 0090-542-501-58-91 \nEmail: receptekin38@gmail.com')
        iletisim_bilgileri.setStyleSheet("font-size: 18px; color: #666666;")
        iletisim_bilgileri.setAlignment(Qt.AlignCenter)
        layout.addWidget(iletisim_bilgileri)

        self.setLayout(layout)

    def stokYonetimiSayfasiniAc(self):
        self.stok_sayfasi = StokYonetimiSayfasi()
        self.stok_sayfasi.show()
    def MotorTanimlariSayfasiniAc(self):
        self.motor_tanimlari = MotorTanimlariSayfasi()
        self.motor_tanimlari.show()        
 
   
    def closeEvent(self, event):
        if hasattr(self, 'stok_sayfasi'):
            self.stok_sayfasi.close()
            event.accept()
    


    def satinAlmaYonetimiSayfasiniAc(self):
        self.satin_alma_sayfasi = SatinAlmaYonetimiSayfasi()
        self.satin_alma_sayfasi.show()

    def konsinyeMotorsikletYonetimiSayfasiniAc(self):
        self.konsinye_sayfasi = KonsinyeMotorsikletYonetimiSayfasi()
        self.konsinye_sayfasi.show()

    def satisYonetimiSayfasiniAc(self):
        self.satis_sayfasi = SatisYonetimiSayfasi()
        self.satis_sayfasi.show()

    def motorsikletServisYonetimiSayfasiniAc(self):
        self.servis_sayfasi = MotorsikletServisYonetimiSayfasi()
        self.servis_sayfasi.show()

    def finansYonetimiSayfasiniAc(self):
        self.finans_sayfasi = FinansYonetimiSayfasi()
        self.finans_sayfasi.show()

    def raporlarSayfasiniAc(self):
        self.raporlar_sayfasi = RaporlarSayfasi()
        self.raporlar_sayfasi.show()

    def yetkiliSayfasiniAc(self):
        self.yetkili_sayfasi = YetkiliSayfasi()
        self.yetkili_sayfasi.show()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = MotorcycleShopUygulamasi()
    uygulama.show()
    sys.exit(app.exec_())

