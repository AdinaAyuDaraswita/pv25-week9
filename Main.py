import sys
from PyQt5.QtWidgets import QApplication
from aplikasi_utama import AplikasiUtama


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AplikasiUtama()
    window.show()
    sys.exit(app.exec_())
