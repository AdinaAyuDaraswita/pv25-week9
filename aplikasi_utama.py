from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QDialog,
    QPushButton, QTabWidget, QTextEdit, QFileDialog, QFontDialog, QAction, QMessageBox
)
from PyQt5.QtGui import QFont
from dialog_input_nama import DialogInputNama


class AplikasiUtama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.resize(820, 420)
        self.setupUI()

    def setupUI(self):
        self.menuBarKu = self.menuBar()
        self.menuBarKu.setStyleSheet("font-size: 14px;")

        menuFile = self.menuBarKu.addMenu('File')
        menuFitur = self.menuBarKu.addMenu('Fitur')

        aksiKeluar = QAction('Keluar', self)
        aksiKeluar.triggered.connect(self.close)
        menuFile.addSeparator()
        menuFile.addAction(aksiKeluar)

        aksiTabNama = QAction('Input Nama', self)
        aksiTabNama.triggered.connect(self.pindahKeTabInputNama)

        aksiTabFont = QAction('Pilih Font', self)
        aksiTabFont.triggered.connect(self.pindahKeTabFont)

        aksiTabFile = QAction('Buka File', self)
        aksiTabFile.triggered.connect(self.pindahKeTabFile)

        menuFitur.addAction(aksiTabNama)
        menuFitur.addAction(aksiTabFont)
        menuFitur.addAction(aksiTabFile)

        self.tabWidget = QTabWidget()
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setStyleSheet("""
            QTabBar {
                qproperty-drawBase: 0;
                alignment: center;
            }
            QTabBar::tab {
                background: #f0f0f0;
                padding: 8px 24px;
                min-width: 120px;
                height: 32px;
                font-size: 13px;
                font-weight: bold;
                color: black;
                border: 1px solid lightgray;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                margin-left: 4px;
                margin-right: 4px;
            }
            QTabBar::tab:selected {
                background: #00aa00;
                color: white;
            }
            QTabWidget::pane {
                border: 1px solid lightgray;
                top: -1px;
            }
        """)

        self.tabWidget.addTab(self.buatTabInputNama(), "Input Nama")
        self.tabWidget.addTab(self.buatTabFont(), "Pilih Font")
        self.tabWidget.addTab(self.buatTabBukaFile(), "Buka File")


        self.setCentralWidget(self.tabWidget)


    def buatTombol(self, teks):
        tombol = QPushButton(teks)
        tombol.setFixedHeight(40)
        tombol.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 8px 20px;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                background-color: white;
            }
            QPushButton:hover {
                background-color: #f2fff2;
            }
        """)

        return tombol
    


    def buatTabInputNama(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.btnInputNama = self.buatTombol("Input Nama")
        self.btnInputNama.clicked.connect(self.bukaDialogNama)
        layout.addWidget(self.btnInputNama)

        self.lblHasilNama = QLabel("Nama:")
        self.lblHasilNama.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.lblHasilNama)

        layout.addStretch()
        tab.setLayout(layout)
        return tab

    def buatTabFont(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.btnPilihFont = self.buatTombol("Pilih Font")
        self.btnPilihFont.clicked.connect(self.dialogFont)
        layout.addWidget(self.btnPilihFont)

        self.lblFontNama = QLabel("Nama:")
        self.lblFontNama.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.lblFontNama)

        layout.addStretch()

        tab.setLayout(layout)

        return tab

    def buatTabBukaFile(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.btnBukaFile = self.buatTombol("Buka File .txt")
        self.btnBukaFile.clicked.connect(self.bukaFileTxt)
        layout.addWidget(self.btnBukaFile)

        self.teksIsiFile = QTextEdit()
        self.teksIsiFile.setFixedHeight(150)
        self.teksIsiFile.setStyleSheet("font-size: 13px;")
        layout.addWidget(self.teksIsiFile)

        layout.addStretch()
        tab.setLayout(layout)
        return tab

    def bukaDialogNama(self):
        dlg = DialogInputNama(self)
        if dlg.exec_() == QDialog.Accepted:
            nama = dlg.ambilNama()
            if nama.strip():
                self.lblHasilNama.setText(f"Nama: {nama}")
            else:
                QMessageBox.warning(self, "Peringatan", "Nama tidak boleh kosong!")
                

    def dialogFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lblFontNama.setFont(font)


    def bukaFileTxt(self):
        path, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt)")
        if path:
            with open(path, 'r') as file:
                isi = file.read()
                self.teksIsiFile.setText(isi)

    def pindahKeTabInputNama(self):
        self.tabWidget.setCurrentIndex(0)

    def pindahKeTabFont(self):
        self.tabWidget.setCurrentIndex(1)

    def pindahKeTabFile(self):
        self.tabWidget.setCurrentIndex(2)
