# -*- coding: utf-8 -*-

"""
Author: Juan Camilo Florez R. <florez87@gmail.com>

Form implementation generated from reading ui file 'Graphic Interface.ui'

Created by: PyQt5 UI code generator 5.5.1

"""

from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from presentation.Controllers import AppController

class Ui_GUIAssist(object):
    """
    Auto-generated code to build the graphic user interface.
    It has an AppController for managing business logic.
    """
    def setupUi(self, GUIAssist):
        GUIAssist.setObjectName("GUIAssist")
        GUIAssist.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GUIAssist.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GUIAssist)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.assist = QtWidgets.QWidget()
        self.assist.setObjectName("assist")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.assist)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxInformation = QtWidgets.QGroupBox(self.assist)
        self.groupBoxInformation.setMinimumSize(QtCore.QSize(379, 523))
        self.groupBoxInformation.setObjectName("groupBoxInformation")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxInformation)
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayoutInformation = QtWidgets.QFormLayout()
        self.formLayoutInformation.setVerticalSpacing(20)
        self.formLayoutInformation.setObjectName("formLayoutInformation")
        self.labelDatabase = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelDatabase.setObjectName("labelDatabase")
        self.formLayoutInformation.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDatabase)
        self.comboBoxDatabase = QtWidgets.QComboBox(self.groupBoxInformation)
        self.comboBoxDatabase.setObjectName("comboBoxDatabase")
        self.comboBoxDatabase.addItem("")
        self.comboBoxDatabase.addItem("")
        self.formLayoutInformation.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxDatabase)
        self.labelCDR = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelCDR.setObjectName("labelCDR")
        self.formLayoutInformation.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCDR)
        self.comboBoxCDR = QtWidgets.QComboBox(self.groupBoxInformation)
        self.comboBoxCDR.setObjectName("comboBoxCDR")
        self.comboBoxCDR.addItem("")
        self.comboBoxCDR.addItem("")
        self.comboBoxCDR.addItem("")
        self.comboBoxCDR.addItem("")
        self.comboBoxCDR.addItem("")
        self.formLayoutInformation.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxCDR)
        self.labelMMSE = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelMMSE.setObjectName("labelMMSE")
        self.formLayoutInformation.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelMMSE)
        self.spinBoxMMSE = QtWidgets.QSpinBox(self.groupBoxInformation)
        self.spinBoxMMSE.setMaximum(30)
        self.spinBoxMMSE.setObjectName("spinBoxMMSE")
        self.formLayoutInformation.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxMMSE)
        self.labelAge = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelAge.setObjectName("labelAge")
        self.formLayoutInformation.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelAge)
        self.spinBoxAge = QtWidgets.QSpinBox(self.groupBoxInformation)
        self.spinBoxAge.setEnabled(False)
        self.spinBoxAge.setMinimum(50)
        self.spinBoxAge.setMaximum(150)
        self.spinBoxAge.setObjectName("spinBoxAge")
        self.formLayoutInformation.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBoxAge)
        self.labelEducation = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelEducation.setObjectName("labelEducation")
        self.formLayoutInformation.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelEducation)
        self.spinBoxEducation = QtWidgets.QSpinBox(self.groupBoxInformation)
        self.spinBoxEducation.setEnabled(False)
        self.spinBoxEducation.setObjectName("spinBoxEducation")
        self.formLayoutInformation.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBoxEducation)
        self.pushButtonDiagnosis = QtWidgets.QPushButton(self.groupBoxInformation)
        self.pushButtonDiagnosis.setObjectName("pushButtonDiagnosis")
        self.formLayoutInformation.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButtonDiagnosis)
        self.labelMoCA = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelMoCA.setObjectName("labelMoCA")
        self.formLayoutInformation.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelMoCA)
        self.spinBoxMoCA = QtWidgets.QSpinBox(self.groupBoxInformation)
        self.spinBoxMoCA.setMaximum(30)
        self.spinBoxMoCA.setObjectName("spinBoxMoCA")
        self.formLayoutInformation.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxMoCA)
        self.labelGDS = QtWidgets.QLabel(self.groupBoxInformation)
        self.labelGDS.setObjectName("labelGDS")
        self.formLayoutInformation.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelGDS)
        self.spinBoxGDS = QtWidgets.QSpinBox(self.groupBoxInformation)
        self.spinBoxGDS.setMinimum(1)
        self.spinBoxGDS.setMaximum(7)
        self.spinBoxGDS.setObjectName("spinBoxGDS")
        self.formLayoutInformation.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxGDS)
        self.horizontalLayout_2.addLayout(self.formLayoutInformation)
        self.horizontalLayout.addWidget(self.groupBoxInformation)
        self.groupBoxResult = QtWidgets.QGroupBox(self.assist)
        self.groupBoxResult.setMinimumSize(QtCore.QSize(379, 523))
        self.groupBoxResult.setObjectName("groupBoxResult")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxResult)
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.labelResult = QtWidgets.QLabel(self.groupBoxResult)
        self.labelResult.setObjectName("labelResult")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelResult)
        self.lineEditResult = QtWidgets.QLineEdit(self.groupBoxResult)
        self.lineEditResult.setReadOnly(True)
        self.lineEditResult.setObjectName("lineEditResult")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditResult)
        self.labelSane = QtWidgets.QLabel(self.groupBoxResult)
        self.labelSane.setObjectName("labelSane")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSane)
        self.lineEditSane = QtWidgets.QLineEdit(self.groupBoxResult)
        self.lineEditSane.setReadOnly(True)
        self.lineEditSane.setObjectName("lineEditSane")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditSane)
        self.labelMild = QtWidgets.QLabel(self.groupBoxResult)
        self.labelMild.setObjectName("labelMild")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelMild)
        self.lineEditMild = QtWidgets.QLineEdit(self.groupBoxResult)
        self.lineEditMild.setReadOnly(True)
        self.lineEditMild.setObjectName("lineEditMild")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditMild)
        self.labelSerious = QtWidgets.QLabel(self.groupBoxResult)
        self.labelSerious.setObjectName("labelSerious")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelSerious)
        self.lineEditSerious = QtWidgets.QLineEdit(self.groupBoxResult)
        self.lineEditSerious.setReadOnly(True)
        self.lineEditSerious.setObjectName("lineEditSerious")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditSerious)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.groupBoxResult)
        self.stackedWidget.addWidget(self.assist)
        self.train = QtWidgets.QWidget()
        self.train.setObjectName("train")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.train)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBoxTrain = QtWidgets.QGroupBox(self.train)
        self.groupBoxTrain.setObjectName("groupBoxTrain")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBoxTrain)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayoutTraining = QtWidgets.QFormLayout()
        self.formLayoutTraining.setVerticalSpacing(20)
        self.formLayoutTraining.setObjectName("formLayoutTraining")
        self.labelFileTrain = QtWidgets.QLabel(self.groupBoxTrain)
        self.labelFileTrain.setObjectName("labelFileTrain")
        self.formLayoutTraining.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFileTrain)
        self.labelDatabaseTrain = QtWidgets.QLabel(self.groupBoxTrain)
        self.labelDatabaseTrain.setObjectName("labelDatabaseTrain")
        self.formLayoutTraining.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDatabaseTrain)
        self.comboBoxDatabaseTrain = QtWidgets.QComboBox(self.groupBoxTrain)
        self.comboBoxDatabaseTrain.setObjectName("comboBoxDatabaseTrain")
        self.comboBoxDatabaseTrain.addItem("")
        self.comboBoxDatabaseTrain.addItem("")
        self.formLayoutTraining.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxDatabaseTrain)
        self.pushButtonFileTrain = QtWidgets.QPushButton(self.groupBoxTrain)
        self.pushButtonFileTrain.setObjectName("pushButtonFileTrain")
        self.formLayoutTraining.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButtonFileTrain)
        self.pushButtonTrain = QtWidgets.QPushButton(self.groupBoxTrain)
        self.pushButtonTrain.setObjectName("pushButtonTrain")
        self.formLayoutTraining.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButtonTrain)
        self.horizontalLayout_6.addLayout(self.formLayoutTraining)
        self.horizontalLayout_5.addWidget(self.groupBoxTrain)
        self.stackedWidget.addWidget(self.train)
        self.validate = QtWidgets.QWidget()
        self.validate.setObjectName("validate")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.validate)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBoxValidateInformation = QtWidgets.QGroupBox(self.validate)
        self.groupBoxValidateInformation.setMinimumSize(QtCore.QSize(379, 523))
        self.groupBoxValidateInformation.setObjectName("groupBoxValidateInformation")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBoxValidateInformation)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.formLayoutValidateInformation = QtWidgets.QFormLayout()
        self.formLayoutValidateInformation.setVerticalSpacing(20)
        self.formLayoutValidateInformation.setObjectName("formLayoutValidateInformation")
        self.labelDatabaseValidate = QtWidgets.QLabel(self.groupBoxValidateInformation)
        self.labelDatabaseValidate.setObjectName("labelDatabaseValidate")
        self.formLayoutValidateInformation.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDatabaseValidate)
        self.comboBoxDatabaseValidate = QtWidgets.QComboBox(self.groupBoxValidateInformation)
        self.comboBoxDatabaseValidate.setObjectName("comboBoxDatabaseValidate")
        self.comboBoxDatabaseValidate.addItem("")
        self.comboBoxDatabaseValidate.addItem("")
        self.formLayoutValidateInformation.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxDatabaseValidate)
        self.labelFoldsValidate = QtWidgets.QLabel(self.groupBoxValidateInformation)
        self.labelFoldsValidate.setObjectName("labelFoldsValidate")
        self.formLayoutValidateInformation.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFoldsValidate)
        self.spinBoxFolds = QtWidgets.QSpinBox(self.groupBoxValidateInformation)
        self.spinBoxFolds.setMaximum(10)
        self.spinBoxFolds.setSingleStep(5)
        self.spinBoxFolds.setObjectName("spinBoxFolds")
        self.formLayoutValidateInformation.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxFolds)
        self.labelFileValidate = QtWidgets.QLabel(self.groupBoxValidateInformation)
        self.labelFileValidate.setObjectName("labelFileValidate")
        self.formLayoutValidateInformation.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelFileValidate)
        self.pushButtonFileValidate = QtWidgets.QPushButton(self.groupBoxValidateInformation)
        self.pushButtonFileValidate.setObjectName("pushButtonFileValidate")
        self.formLayoutValidateInformation.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButtonFileValidate)
        self.pushButtonValidate = QtWidgets.QPushButton(self.groupBoxValidateInformation)
        self.pushButtonValidate.setObjectName("pushButtonValidate")
        self.formLayoutValidateInformation.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonValidate)
        self.horizontalLayout_7.addLayout(self.formLayoutValidateInformation)
        self.horizontalLayout_4.addWidget(self.groupBoxValidateInformation)
        self.groupBoxValidateResult = QtWidgets.QGroupBox(self.validate)
        self.groupBoxValidateResult.setMinimumSize(QtCore.QSize(379, 523))
        self.groupBoxValidateResult.setObjectName("groupBoxValidateResult")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBoxValidateResult)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayoutValidateResult = QtWidgets.QFormLayout()
        self.formLayoutValidateResult.setVerticalSpacing(20)
        self.formLayoutValidateResult.setObjectName("formLayoutValidateResult")
        self.labelPrecision = QtWidgets.QLabel(self.groupBoxValidateResult)
        self.labelPrecision.setObjectName("labelPrecision")
        self.formLayoutValidateResult.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPrecision)
        self.lineEditPrecision = QtWidgets.QLineEdit(self.groupBoxValidateResult)
        self.lineEditPrecision.setEnabled(True)
        self.lineEditPrecision.setReadOnly(True)
        self.lineEditPrecision.setObjectName("lineEditPrecision")
        self.formLayoutValidateResult.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPrecision)
        self.labelAccuracy = QtWidgets.QLabel(self.groupBoxValidateResult)
        self.labelAccuracy.setObjectName("labelAccuracy")
        self.formLayoutValidateResult.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAccuracy)
        self.lineEditAccuracy = QtWidgets.QLineEdit(self.groupBoxValidateResult)
        self.lineEditAccuracy.setReadOnly(True)
        self.lineEditAccuracy.setObjectName("lineEditAccuracy")
        self.formLayoutValidateResult.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditAccuracy)
        self.labelSensitivity = QtWidgets.QLabel(self.groupBoxValidateResult)
        self.labelSensitivity.setObjectName("labelSensitivity")
        self.formLayoutValidateResult.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSensitivity)
        self.lineEditSensitivity = QtWidgets.QLineEdit(self.groupBoxValidateResult)
        self.lineEditSensitivity.setReadOnly(True)
        self.lineEditSensitivity.setObjectName("lineEditSensitivity")
        self.formLayoutValidateResult.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditSensitivity)
        self.labelSpecificity = QtWidgets.QLabel(self.groupBoxValidateResult)
        self.labelSpecificity.setObjectName("labelSpecificity")
        self.formLayoutValidateResult.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelSpecificity)
        self.lineEditSpecificity = QtWidgets.QLineEdit(self.groupBoxValidateResult)
        self.lineEditSpecificity.setReadOnly(True)
        self.lineEditSpecificity.setObjectName("lineEditSpecificity")
        self.formLayoutValidateResult.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditSpecificity)
        self.labelKappa = QtWidgets.QLabel(self.groupBoxValidateResult)
        self.labelKappa.setObjectName("labelKappa")
        self.formLayoutValidateResult.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelKappa)
        self.lineEditKappa = QtWidgets.QLineEdit(self.groupBoxValidateResult)
        self.lineEditKappa.setReadOnly(True)
        self.lineEditKappa.setObjectName("lineEditKappa")
        self.formLayoutValidateResult.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditKappa)
        self.horizontalLayout_8.addLayout(self.formLayoutValidateResult)
        self.horizontalLayout_4.addWidget(self.groupBoxValidateResult)
        self.stackedWidget.addWidget(self.validate)
        self.verticalLayout.addWidget(self.stackedWidget)
        GUIAssist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUIAssist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        GUIAssist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUIAssist)
        self.statusbar.setObjectName("statusbar")
        GUIAssist.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(GUIAssist)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/row 8/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionAssist = QtWidgets.QAction(GUIAssist)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/row 1/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAssist.setIcon(icon2)
        self.actionAssist.setObjectName("actionAssist")
        self.actionTrain = QtWidgets.QAction(GUIAssist)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/row 1/14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTrain.setIcon(icon3)
        self.actionTrain.setObjectName("actionTrain")
        self.actionValidate = QtWidgets.QAction(GUIAssist)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/icons/row 1/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValidate.setIcon(icon4)
        self.actionValidate.setObjectName("actionValidate")
        self.actionSave = QtWidgets.QAction(GUIAssist)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/icons/row 10/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuMode.addAction(self.actionAssist)
        self.menuMode.addAction(self.actionTrain)
        self.menuMode.addAction(self.actionValidate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        
        """
        Signals and slots from the graphic user interface.
        """
        self.actionExit.triggered.connect(self.close)
        self.actionSave.triggered.connect(self.save)
        self.actionAssist.triggered.connect(self.stackAssist)
        self.actionTrain.triggered.connect(self.stackTrain)
        self.actionValidate.triggered.connect(self.stackValidate)
        self.comboBoxDatabase.currentIndexChanged.connect(self.changeDatabase)
        self.pushButtonFileTrain.clicked.connect(self.openFileTrain)
        self.pushButtonFileValidate.clicked.connect(self.openFileValidate)
        self.pushButtonTrain.clicked.connect(self.trainSystem)
        self.pushButtonDiagnosis.clicked.connect(self.predictDiagnosis)
        self.pushButtonValidate.clicked.connect(self.validateSystem)
        self.path_train = None
        self.path_validate = None
        self.controller = AppController()

        self.retranslateUi(GUIAssist)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GUIAssist)
        
    def retranslateUi(self, GUIAssist):
        """
        Auto-generated code for text translation.
        """
        _translate = QtCore.QCoreApplication.translate
        GUIAssist.setWindowTitle(_translate("GUIAssist", "MCI Assisted Diagnosis"))
        self.groupBoxInformation.setTitle(_translate("GUIAssist", "Basic Information"))
        self.labelDatabase.setText(_translate("GUIAssist", "Database"))
        self.comboBoxDatabase.setItemText(0, _translate("GUIAssist", "Caldas"))
        self.comboBoxDatabase.setItemText(1, _translate("GUIAssist", "ADNI"))
        self.labelCDR.setText(_translate("GUIAssist", "CDR"))
        self.comboBoxCDR.setItemText(0, _translate("GUIAssist", "0"))
        self.comboBoxCDR.setItemText(1, _translate("GUIAssist", "0.5"))
        self.comboBoxCDR.setItemText(2, _translate("GUIAssist", "1"))
        self.comboBoxCDR.setItemText(3, _translate("GUIAssist", "2"))
        self.comboBoxCDR.setItemText(4, _translate("GUIAssist", "3"))
        self.labelMMSE.setText(_translate("GUIAssist", "MMSE"))
        self.labelAge.setText(_translate("GUIAssist", "Age"))
        self.labelEducation.setText(_translate("GUIAssist", "Education"))
        self.pushButtonDiagnosis.setText(_translate("GUIAssist", "Assisted Diagnosis"))
        self.labelMoCA.setText(_translate("GUIAssist", "MoCA"))
        self.labelGDS.setText(_translate("GUIAssist", "GDS"))
        self.groupBoxResult.setTitle(_translate("GUIAssist", "System Results"))
        self.labelResult.setText(_translate("GUIAssist", "Result"))
        self.labelSane.setText(_translate("GUIAssist", "Sane"))
        self.labelMild.setText(_translate("GUIAssist", "Mild"))
        self.labelSerious.setText(_translate("GUIAssist", "Serious"))
        self.groupBoxTrain.setTitle(_translate("GUIAssist", "System Training"))
        self.labelFileTrain.setText(_translate("GUIAssist", "File"))
        self.labelDatabaseTrain.setText(_translate("GUIAssist", "Database"))
        self.comboBoxDatabaseTrain.setItemText(0, _translate("GUIAssist", "Caldas"))
        self.comboBoxDatabaseTrain.setItemText(1, _translate("GUIAssist", "ADNI"))
        self.pushButtonFileTrain.setText(_translate("GUIAssist", "Pick Database File..."))
        self.pushButtonTrain.setText(_translate("GUIAssist", "Train System"))
        self.groupBoxValidateInformation.setTitle(_translate("GUIAssist", "Basic Information"))
        self.labelDatabaseValidate.setText(_translate("GUIAssist", "Database"))
        self.comboBoxDatabaseValidate.setItemText(0, _translate("GUIAssist", "Caldas"))
        self.comboBoxDatabaseValidate.setItemText(1, _translate("GUIAssist", "ADNI"))
        self.labelFoldsValidate.setText(_translate("GUIAssist", "Folds"))
        self.labelFileValidate.setText(_translate("GUIAssist", "File"))
        self.pushButtonFileValidate.setText(_translate("GUIAssist", "Pick Database File..."))
        self.pushButtonValidate.setText(_translate("GUIAssist", "Validate System"))
        self.groupBoxValidateResult.setTitle(_translate("GUIAssist", "Validation Result"))
        self.labelPrecision.setText(_translate("GUIAssist", "Precision"))
        self.labelAccuracy.setText(_translate("GUIAssist", "Accuracy"))
        self.labelSensitivity.setText(_translate("GUIAssist", "Sensitivity"))
        self.labelSpecificity.setText(_translate("GUIAssist", "Specificity"))
        self.labelKappa.setText(_translate("GUIAssist", "Kappa"))
        self.menuFile.setTitle(_translate("GUIAssist", "File"))
        self.menuMode.setTitle(_translate("GUIAssist", "Mode"))
        self.actionExit.setText(_translate("GUIAssist", "Exit"))
        self.actionAssist.setText(_translate("GUIAssist", "Assist"))
        self.actionTrain.setText(_translate("GUIAssist", "Train"))
        self.actionValidate.setText(_translate("GUIAssist", "Validate"))
        self.actionSave.setText(_translate("GUIAssist", "Save"))


    def close(self):
        """
        Closes the application instance.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        import sys
        sys.exit(0)
         
    def save(self):
        """
        Orders the AppController to save the current trained models.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        if self.controller.isTrained():
            self.controller.save()
            QMessageBox.information(self.train, "Message", "Save succesful.")
        else:
            QMessageBox.warning(self.train, "Message", "Must have at least 1 trained classifier.")
         
    def stackAssist(self):
        """
        Changes the system to assist mode.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.stackedWidget.setCurrentIndex(0)
         
    def stackTrain(self):
        """
        Changes the system to training mode.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.stackedWidget.setCurrentIndex(1)
         
    def stackValidate(self):
        """
        Changes the system to validation mode.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.stackedWidget.setCurrentIndex(2)
        
    def changeDatabase(self):
        """
        Changes the assist form based on the selected database.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        if self.comboBoxDatabase.currentText() == "Caldas":
            self.spinBoxMoCA.setEnabled(True)
            self.spinBoxGDS.setEnabled(True)
            self.spinBoxAge.setEnabled(False)
            self.spinBoxEducation.setEnabled(False)
        else:
            self.spinBoxMoCA.setEnabled(False)
            self.spinBoxGDS.setEnabled(False)
            self.spinBoxAge.setEnabled(True)
            self.spinBoxEducation.setEnabled(True)
    
    def openFileTrain(self):
        """
        Opens a file dialog to select the file for training.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.path_train, _ = QFileDialog.getOpenFileName(self.train, "Select Database File", "", "All files (*.*)")
            
    def openFileValidate(self):
        """
        Opens a file dialog to select the file for validation.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.path_validate, _ = QFileDialog.getOpenFileName(self.validate, "Select Database File", "", "All files (*.*)")
        
    def trainSystem(self):
        """
        Orders the AppController to train a model based on the selected database.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        if self.path_train:
            trained = self.controller.train(self.path_train, self.comboBoxDatabaseTrain.currentText())
            self.path_train = None
            if not trained:
                QMessageBox.critical(self.train, "Message", "File columns or labels mismatch.")
            else:
                QMessageBox.information(self.train, "Message", "Training succesful.")
        else:
            QMessageBox.warning(self.train, "Message", "Must pick a database file.")
    
    def validateSystem(self):
        """
        Orders the AppController to validate a model based on the selected database.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        if self.path_validate:
            checked, validated, accuracy, precision, sensitivity, specificity, kappa = self.controller.validate(self.path_validate, self.spinBoxFolds.value(), self.comboBoxDatabaseValidate.currentText())
            self.path_validate = None
            if not validated:
                QMessageBox.warning(self.validate, "Message", "Classifier for "+ self.comboBoxDatabaseValidate.currentText() + " database is not trained.")
                self.clearValidateLineEdits()
            else:
                self.lineEditAccuracy.setText(str(accuracy))
                self.lineEditPrecision.setText(str(precision))
                self.lineEditSensitivity.setText(str(sensitivity))
                self.lineEditSpecificity.setText(str(specificity))
                self.lineEditKappa.setText(str(kappa))
                QMessageBox.information(self.train, "Message", "Validation finished.")
            if not checked:
                QMessageBox.critical(self.validate, "Message", "File columns or labels mismatch.")
                self.clearValidateLineEdits()
        else:
            QMessageBox.warning(self.validate, "Message", "Must pick a database file.")
            self.clearValidateLineEdits()
            
    def predictDiagnosis(self):
        """
        Orders the AppController to predict the class and probabilities of the selected features.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """        
        predicted, diagnosis, prediction, classes = self.controller.predict(self.comboBoxCDR.currentText(), 
                                self.spinBoxMMSE.value(), 
                                self.spinBoxMoCA.value(), 
                                self.spinBoxGDS.value(),
                                self.spinBoxAge.value(),
                                self.spinBoxEducation.value(),
                                self.comboBoxDatabase.currentText())
        if not predicted:
            QMessageBox.warning(self.train, "Message", "Classifier for "+ self.comboBoxDatabase.currentText() + " database is not trained.")
            self.clearResultLineEdits()
        else:
            self.lineEditResult.setText(str(diagnosis[0]))
            self.lineEditSane.setText(str(prediction[0][list(classes).index('Sane')]) + '%')
            self.lineEditMild.setText(str(prediction[0][list(classes).index('Mild')]) + '%')
            self.lineEditSerious.setText(str(prediction[0][list(classes).index('Serious')]) + '%')
            
    
    def clearValidateLineEdits(self):
        """
        Erases all validation results.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.lineEditAccuracy.clear()
        self.lineEditPrecision.clear()
        self.lineEditSensitivity.clear()
        self.lineEditSpecificity.clear()
        self.lineEditKappa.clear()
        
    def clearResultLineEdits(self):
        """
        Erases all training results.
        
        Parameters
        ----------
        None
        
        Return
        ----------
        None
        """
        self.lineEditResult.clear()
        self.lineEditSane.clear()
        self.lineEditMild.clear()
        self.lineEditSerious.clear()