from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox


class DialogInputNama(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Masukkan Nama")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        self.inputNama = QLineEdit()
        self.inputNama.setPlaceholderText("Tulis nama kamu di sini...")
        layout.addWidget(self.inputNama)

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btnBox.accepted.connect(self.accept)
        btnBox.rejected.connect(self.reject)
        layout.addWidget(btnBox)

        self.setLayout(layout)

    def ambilNama(self):
        return self.inputNama.text()
