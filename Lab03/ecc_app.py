from PyQt5 import QtWidgets
from ui.ecc import Ui_MainWindow
from cipher.ecc.ecc_cipher import ECCCipher
import sys

class ECCApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cipher = ECCCipher()
        self.private_key = None
        self.public_key = None

        self.ui.Generate_keys.clicked.connect(self.generate_keys)
        self.ui.Sign.clicked.connect(self.sign_message)
        self.ui.Verify.clicked.connect(self.verify_signature)

    def generate_keys(self):
        self.private_key, self.public_key = self.cipher.generate_keys()
        self.ui.txt_info.setPlainText("✅ ECC key pair generated!")

    def sign_message(self):
        if not self.private_key:
            self.ui.txt_info.setPlainText("⚠️ Please generate keys first!")
            return
        message = self.ui.txt_info.toPlainText()
        signature = self.cipher.sign(message, self.private_key)
        self.ui.txt_sign.setPlainText(signature.hex())

    def verify_signature(self):
        if not self.public_key:
            self.ui.txt_info.setPlainText("⚠️ Please generate keys first!")
            return
        try:
            message = self.ui.txt_info.toPlainText()
            signature = bytes.fromhex(self.ui.txt_sign.toPlainText())
            result = self.cipher.verify(message, signature, self.public_key)
            self.ui.txt_info.setPlainText("✅ Signature valid!" if result else "❌ Invalid signature.")
        except:
            self.ui.txt_info.setPlainText("❌ Error during verification.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())
