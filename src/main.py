# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>
"""

from PyQt5 import QtWidgets
from presentation.GUIAssist import Ui_GUIAssist
import qdarkstyle

if __name__ == "__main__":
    """
    Creates an application object based on PyQt5 QApplication widget
    and shows the GUI stored in the presentation layer
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_GUIAssist()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
