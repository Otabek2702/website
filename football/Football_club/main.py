from PyQt5 import QtWidgets
from mainWindow import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.focusNextChild()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
