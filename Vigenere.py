from jiemian import Ui_Vigenere
import sys
from PyQt5 import QtWidgets, QtGui
from weijiniya import Weiji


class mywindow(QtWidgets.QWidget, Ui_Vigenere):

    def __init__(self):
        self.WJNY = Weiji()
        super(mywindow, self).__init__()
        self.count = 0
        self.setupUi(self)

    def jiami(self):
        Secret = self.WJNY.jiami(self.MingWord.text(), self.Key.text())
        self.SecretWord.setText(Secret)
        self.Record.append('本次加密，明文为' + self.MingWord.text() + '，秘钥为' + self.Key.text() + '，密文为' + Secret)

    # 定义槽函数
    def jiemi(self):
        Ming = self.WJNY.jiemi(self.SecretWord.text(), self.Key.text())
        self.MingWord.setText(Ming)
        self.Record.append('本次解密，密文为' + self.MingWord.text() + '，秘钥为' + self.Key.text() + '，明文为' + Ming)


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
