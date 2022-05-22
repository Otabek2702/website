from PyQt5 import QtCore, QtGui, QtWidgets
from models import Club, Player, Club_Managment, Contract, CoachingStuff, BaseModel


class Ui_MainWindow(object):
    def OpenClubManagmentPage(self):
        self.clubM_Window = QtWidgets.QWidget()
        ui = Ui_HomePage()
        ui.setupUi(self.clubM_Window)
        self.clubM_Window.show()

    def OpenPlayersPage(self):
        self.playerWindow = QtWidgets.QWidget()
        ui = Ui_PlayerWin()
        ui.setupUi(self.playerWindow)
        self.playerWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 581)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 9, 741, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.stackedWidget.addWidget(self.home_page)

        self.player_page = QtWidgets.QWidget()
        self.player_page.setObjectName("player_page")
        self.stackedWidget.addWidget(self.player_page)
        self.contracts_page = QtWidgets.QWidget()
        self.contracts_page.setObjectName("contracts_page")
        self.stackedWidget.addWidget(self.contracts_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(238, 167, 159, 150))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuServices = QtWidgets.QMenu(self.menubar)
        self.menuServices.setObjectName("menuServices")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClub_info = QtWidgets.QAction(MainWindow)
        self.actionClub_info.setObjectName("actionClub_info")
        self.actionClub_Mangment = QtWidgets.QAction(MainWindow)
        self.actionClub_Mangment.setObjectName("actionClub_Mangment")
        self.actionCoaching_Stuff = QtWidgets.QAction(MainWindow)
        self.actionCoaching_Stuff.setObjectName("actionCoaching_Stuff")
        self.actionContracts = QtWidgets.QAction(MainWindow)
        self.actionContracts.setObjectName("actionContracts")
        self.actionContract = QtWidgets.QAction(MainWindow)
        self.actionContract.setObjectName("actionContract")
        self.actionPlayers_2 = QtWidgets.QAction(MainWindow)
        self.actionPlayers_2.setObjectName("actionPlayers_2")
        self.actionContracts_2 = QtWidgets.QAction(MainWindow)
        self.actionContracts_2.setObjectName("actionContracts_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuServices.addAction(self.actionClub_info)
        self.menuServices.addAction(self.actionClub_Mangment)
        self.menuServices.addAction(self.actionCoaching_Stuff)
        self.menuServices.addAction(self.actionPlayers_2)
        self.menuServices.addAction(self.actionContracts_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuServices.menuAction())

        # triggered
        self.actionClub_Mangment.triggered.connect(self.OpenClubManagmentPage)
        self.actionClub_info.triggered.connect(self.OnOpenContractsPage)
        self.actionPlayers_2.triggered.connect(self.OpenPlayersPage)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuServices.setTitle(_translate("MainWindow", "&Services"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionClub_info.setText(_translate("MainWindow", "Club info"))
        self.actionClub_Mangment.setText(_translate("MainWindow", "Club Mangment"))
        self.actionCoaching_Stuff.setText(_translate("MainWindow", "Coaching Stuff"))
        self.actionContracts.setText(_translate("MainWindow", "Contracts"))
        self.actionContract.setText(_translate("MainWindow", "Contracts"))
        self.actionPlayers_2.setText(_translate("MainWindow", "Players"))
        self.actionContracts_2.setText(_translate("MainWindow", "Contracts"))

    def OnOpenCoachStuffPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def OnOpenContractsPage(self):
        self.stackedWidget.setCurrentIndex(4)


class Ui_HomePage(object):

    def loadata_Cm(self):
        self.ClubM_table.setRowCount(len(Club_Managment.objects()))
        row = 0
        for item in Club_Managment.objects():
            self.ClubM_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item.name)))
            self.ClubM_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item.surname)))
            self.ClubM_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item.nationality)))
            self.ClubM_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item.birthday)))
            self.ClubM_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(item.prestige)))
            row = row + 1

    def DeleteBtn(self):
        cm = Club_Managment.objects()[self.ClubM_table.currentRow()]
        cm.delete()
        self.loadata_Cm()

    def EnableCreateButton(self):
        if self.line_name.displayText() and self.line_surname.displayText():
            if self.line_prestige.displayText() and self.countriesBox.currentIndex() >= 0:
                self.createButton.setEnabled(True)
            else:
                self.createButton.setEnabled(False)
        else:
            self.createButton.setEnabled(False)

    def CreateBtn(self):
        club_manag = Club_Managment(self.line_name.displayText(),
                                    self.line_surname.displayText(),
                                    self.countriesBox.currentText(),
                                    self.dateEdit.text(),
                                    self.line_prestige.displayText())
        club_manag.save()
        self.line_name.clear()
        self.line_surname.clear(),
        self.countriesBox.setCurrentIndex(-1),
        self.line_prestige.clear()
        self.loadata_Cm()

    def UpdateBtn(self):
        cm = Club_Managment.objects()[self.ClubM_table.currentRow()]
        cm.name = self.line_name.displayText()
        cm.surname = self.line_surname.displayText()
        cm.prestige = self.line_prestige.displayText()
        cm.nationality = self.countriesBox.currentText()
        cm.birthday = self.dateEdit.text()

        cm.save()
        self.loadata_Cm()

    def EnableUpdateButton(self):
        self.line_name.setText(
            f"{self.ClubM_table.item(self.ClubM_table.currentRow(), 0).text()}"
        )
        self.line_surname.setText(
            f"{self.ClubM_table.item(self.ClubM_table.currentRow(), 1).text()}"
        )
        self.line_prestige.setText(
            f"{self.ClubM_table.item(self.ClubM_table.currentRow(), 4).text()}"
        )
        self.updateButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        self.updateButton.clicked.connect(self.UpdateBtn)
        self.deleteButton.clicked.connect(self.DeleteBtn)

    def setupUi(self, clubWindow: QtWidgets.QWidget):
        clubWindow.setObjectName("clubM_page")
        clubWindow.resize(760, 581)
        self.line_name = QtWidgets.QLineEdit(clubWindow)
        self.line_name.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.line_name.setObjectName("line_name")
        self.line_surname = QtWidgets.QLineEdit(clubWindow)
        self.line_surname.setGeometry(QtCore.QRect(190, 20, 151, 31))
        self.line_surname.setObjectName("line_surname")
        self.dateEdit = QtWidgets.QDateEdit(clubWindow)
        self.dateEdit.setGeometry(QtCore.QRect(500, 20, 111, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.countriesBox = QtWidgets.QComboBox(clubWindow)
        self.countriesBox.setGeometry(QtCore.QRect(350, 20, 141, 31))
        self.countriesBox.addItems(BaseModel.objects)
        self.countriesBox.setCurrentText("")
        self.countriesBox.setObjectName("countriesBox")
        self.line_prestige = QtWidgets.QLineEdit(clubWindow)
        self.line_prestige.setGeometry(QtCore.QRect(620, 20, 113, 31))
        self.line_prestige.setObjectName("line_prestige")
        self.createButton = QtWidgets.QPushButton(clubWindow)
        self.createButton.setEnabled(False)
        self.createButton.setGeometry(QtCore.QRect(420, 80, 89, 31))
        self.createButton.setObjectName("createButton")
        self.deleteButton = QtWidgets.QPushButton(clubWindow)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setGeometry(QtCore.QRect(640, 80, 89, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.updateButton = QtWidgets.QPushButton(clubWindow)
        self.updateButton.setEnabled(False)
        self.updateButton.setGeometry(QtCore.QRect(530, 80, 89, 31))
        self.updateButton.setObjectName("updateButton")
        self.ClubM_table = QtWidgets.QTableWidget(clubWindow)
        self.ClubM_table.setGeometry(QtCore.QRect(40, 180, 681, 321))
        self.ClubM_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ClubM_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ClubM_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ClubM_table.setShowGrid(True)
        self.ClubM_table.setObjectName("ClubM_table")
        self.ClubM_table.setColumnCount(5)
        self.ClubM_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table.setHorizontalHeaderItem(4, item)
        self.ClubM_table.horizontalHeader().setVisible(False)
        self.ClubM_table.horizontalHeader().setDefaultSectionSize(136)
        self.ClubM_table.horizontalHeader().setHighlightSections(True)
        self.ClubM_table.verticalHeader().setDefaultSectionSize(40)

        self.countriesBox.setCurrentIndex(-1)
        clubWindow.setTabOrder(self.line_name, self.line_surname)
        clubWindow.setTabOrder(self.line_surname, self.countriesBox)
        clubWindow.setTabOrder(self.countriesBox, self.dateEdit)
        clubWindow.setTabOrder(self.dateEdit, self.line_prestige)

        self.loadata_Cm()
        self.line_name.textChanged.connect(lambda: self.EnableCreateButton())
        self.line_surname.textChanged.connect(lambda: self.EnableCreateButton())
        self.line_prestige.textChanged.connect(lambda: self.EnableCreateButton())
        self.countriesBox.currentIndexChanged.connect(lambda: self.EnableCreateButton())
        self.createButton.clicked.connect(lambda: self.CreateBtn())
        self.ClubM_table.cellClicked.connect(lambda: self.EnableUpdateButton())

        # self.btn = QtWidgets.QPushButton(clubWindow)
        # self.btn.setGeometry(QtCore.QRect(40, 110, 89, 31))
        # self.btn.setObjectName("btn")
        # self.btn.clicked.connect(lambda: self.openit(mainwin))

        self.retranslateUi(clubWindow)
        QtCore.QMetaObject.connectSlotsByName(clubWindow)

    def retranslateUi(self, clubWindow):
        _translate = QtCore.QCoreApplication.translate
        clubWindow.setWindowTitle(_translate("clubM_page", "Club Managment"))
        self.line_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.line_surname.setPlaceholderText(_translate("MainWindow", "Surname"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.line_prestige.setPlaceholderText(_translate("MainWindow", "Prestige"))
        self.createButton.setText(_translate("MainWindow", "Create"))
        # self.btn.setText(_translate("MainWindow", "btn"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.ClubM_table.setSortingEnabled(True)
        item = self.ClubM_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.ClubM_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.ClubM_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nationality"))
        item = self.ClubM_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Birthday"))
        item = self.ClubM_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Prestige"))


class Ui_PlayerWin(object):
    def loadata_pl(self):
        self.ClubM_table_2.setRowCount(len(Player.objects))
        row = 0
        for item in Player.objects:
            self.ClubM_table_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item.name)))
            self.ClubM_table_2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item.surname)))
            self.ClubM_table_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item.player_number)))
            self.ClubM_table_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item.birthday_date)))
            self.ClubM_table_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(item.age)))
            self.ClubM_table_2.setItem(row, 5, QtWidgets.QTableWidgetItem(str(item.nationality)))
            self.ClubM_table_2.setItem(row, 6, QtWidgets.QTableWidgetItem(str(item.number_of_games)))
            self.ClubM_table_2.setItem(row, 7, QtWidgets.QTableWidgetItem(str(item.height)))
            self.ClubM_table_2.setItem(row, 8, QtWidgets.QTableWidgetItem(str(item.weight)))
            self.ClubM_table_2.setItem(row, 9, QtWidgets.QTableWidgetItem(str(item.contract_id)))
            row = row + 1

    def DeleteBtn(self):
        cm = Player.objects[self.ClubM_table_2.currentRow()]
        cm.delete()
        self.loadata_pl()

    def EnableCreateButton(self):
        if self.line_name_pl.displayText() and self.line_surname_pl.displayText() and self.ageBox.value() > 0:
            if self.line_contractId_pl.displayText() and self.countriesBox_pl.currentIndex() >= 0:
                if self.playerNumberBox.value() > 0 and self.heightSpinBox.value() > 0:
                    if self.weightSpinBox.value() > 0:
                        self.createButton_2.setEnabled(True)
                    else:
                        self.createButton_2.setEnabled(False)
                else:
                    self.createButton_2.setEnabled(False)
            else:
                self.createButton_2.setEnabled(False)
        else:
            self.createButton_2.setEnabled(False)

    def CreateBtn(self):
        pl = Player(self.line_name_pl.displayText(),
                    self.line_surname_pl.displayText(),
                    self.playerNumberBox.value(),
                    self.datePLayer.text(),
                    self.ageBox.value(),
                    self.countriesBox_pl.currentText(),
                    self.spinBox.value(),
                    self.heightSpinBox.value(),
                    self.weightSpinBox.value(),
                    self.line_contractId_pl.displayText())
        pl.save()
        self.line_name_pl.clear(),
        self.line_surname_pl.clear(),
        self.playerNumberBox.clear(),
        self.datePLayer.clear(),
        self.ageBox.clear(),
        self.countriesBox_pl.clear(),
        self.spinBox.clear(),
        self.heightSpinBox.clear(),
        self.weightSpinBox.clear(),
        self.line_contractId_pl.clear()
        self.loadata_pl()

    def setupUi(self, playerWindow):
        playerWindow.resize(760, 581)
        playerWindow.setObjectName("playerWindow")
        self.createButton_2 = QtWidgets.QPushButton(playerWindow)
        self.createButton_2.setEnabled(False)
        self.createButton_2.setGeometry(QtCore.QRect(410, 180, 89, 31))
        self.createButton_2.setObjectName("createButton_2")
        self.updateButton_2 = QtWidgets.QPushButton(playerWindow)
        self.updateButton_2.setEnabled(False)
        self.updateButton_2.setGeometry(QtCore.QRect(520, 180, 89, 31))
        self.updateButton_2.setObjectName("updateButton_2")
        self.deleteButton_2 = QtWidgets.QPushButton(playerWindow)
        self.deleteButton_2.setEnabled(False)
        self.deleteButton_2.setGeometry(QtCore.QRect(630, 180, 89, 31))
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.line_name_pl = QtWidgets.QLineEdit(playerWindow)
        self.line_name_pl.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.line_name_pl.setObjectName("line_name_pl")
        self.line_surname_pl = QtWidgets.QLineEdit(playerWindow)
        self.line_surname_pl.setGeometry(QtCore.QRect(180, 30, 161, 31))
        self.line_surname_pl.setObjectName("line_surname_pl")
        self.ClubM_table_2 = QtWidgets.QTableWidget(playerWindow)
        self.ClubM_table_2.setGeometry(QtCore.QRect(10, 310, 711, 221))
        self.ClubM_table_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ClubM_table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ClubM_table_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ClubM_table_2.setShowGrid(True)
        self.ClubM_table_2.setObjectName("ClubM_table_2")
        self.ClubM_table_2.setColumnCount(10)
        self.ClubM_table_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClubM_table_2.setHorizontalHeaderItem(9, item)
        self.ClubM_table_2.horizontalHeader().setVisible(True)
        self.ClubM_table_2.horizontalHeader().setDefaultSectionSize(136)
        self.ClubM_table_2.horizontalHeader().setHighlightSections(True)
        self.ClubM_table_2.verticalHeader().setDefaultSectionSize(40)
        self.line_contractId_pl = QtWidgets.QLineEdit(playerWindow)
        self.line_contractId_pl.setGeometry(QtCore.QRect(550, 110, 101, 31))
        self.line_contractId_pl.setObjectName("line_contractId_pl")
        self.datePLayer = QtWidgets.QDateEdit(playerWindow)
        self.datePLayer.setGeometry(QtCore.QRect(480, 30, 111, 31))
        self.datePLayer.setObjectName("datePLayer")
        self.ageBox = QtWidgets.QSpinBox(playerWindow)
        self.ageBox.setGeometry(QtCore.QRect(350, 30, 121, 31))
        self.ageBox.setObjectName("ageBox")
        self.playerNumberBox = QtWidgets.QSpinBox(playerWindow)
        self.playerNumberBox.setGeometry(QtCore.QRect(600, 30, 101, 31))
        self.playerNumberBox.setObjectName("playerNumberBox")
        self.countriesBox_pl = QtWidgets.QComboBox(playerWindow)
        self.countriesBox_pl.setGeometry(QtCore.QRect(10, 110, 161, 31))
        self.countriesBox_pl.setCurrentText("")
        self.countriesBox_pl.addItems(BaseModel.objects)
        self.countriesBox_pl.setObjectName("countriesBox_pl")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(playerWindow)
        self.heightSpinBox.setGeometry(QtCore.QRect(330, 110, 101, 31))
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.weightSpinBox = QtWidgets.QDoubleSpinBox(playerWindow)
        self.weightSpinBox.setGeometry(QtCore.QRect(440, 110, 101, 31))
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.spinBox = QtWidgets.QSpinBox(playerWindow)
        self.spinBox.setGeometry(QtCore.QRect(180, 110, 131, 31))
        self.spinBox.setObjectName("spinBox")

        # connects
        self.loadata_pl()
        self.line_name_pl.textChanged.connect(lambda: self.EnableCreateButton())
        self.line_surname_pl.textChanged.connect(lambda: self.EnableCreateButton())
        self.ageBox.valueChanged.connect(lambda: self.EnableCreateButton())
        self.line_contractId_pl.textChanged.connect(lambda: self.EnableCreateButton())
        self.countriesBox_pl.currentIndexChanged.connect(lambda: self.EnableCreateButton())
        self.playerNumberBox.valueChanged.connect(lambda: self.EnableCreateButton())
        self.weightSpinBox.valueChanged.connect(lambda: self.EnableCreateButton())
        self.heightSpinBox.valueChanged.connect(lambda: self.EnableCreateButton())
        self.createButton_2.clicked.connect(lambda: self.CreateBtn())

        # Labels
        self.name_label = QtWidgets.QLabel(playerWindow)
        self.name_label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.name_label.setObjectName("name_label")
        self.surname_label = QtWidgets.QLabel(playerWindow)
        self.surname_label.setGeometry(QtCore.QRect(180, 10, 67, 17))
        self.surname_label.setObjectName("surname_label")
        self.playernumber_label = QtWidgets.QLabel(playerWindow)
        self.playernumber_label.setGeometry(QtCore.QRect(350, 10, 111, 17))
        self.playernumber_label.setObjectName("playernumber_label")
        self.birthday_label = QtWidgets.QLabel(playerWindow)
        self.birthday_label.setGeometry(QtCore.QRect(480, 10, 67, 17))
        self.birthday_label.setObjectName("birthday_label")
        self.age_label = QtWidgets.QLabel(playerWindow)
        self.age_label.setGeometry(QtCore.QRect(600, 10, 67, 17))
        self.age_label.setObjectName("age_label")
        self.nationality_label = QtWidgets.QLabel(playerWindow)
        self.nationality_label.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.nationality_label.setObjectName("nationality_label")
        self.countgames_label = QtWidgets.QLabel(playerWindow)
        self.countgames_label.setGeometry(QtCore.QRect(180, 90, 131, 17))
        self.countgames_label.setObjectName("countgames_label")
        self.height_label = QtWidgets.QLabel(playerWindow)
        self.height_label.setGeometry(QtCore.QRect(330, 90, 67, 17))
        self.height_label.setObjectName("height_label")
        self.weight_label = QtWidgets.QLabel(playerWindow)
        self.weight_label.setGeometry(QtCore.QRect(440, 90, 67, 17))
        self.weight_label.setObjectName("weight_label")
        self.contract_label = QtWidgets.QLabel(playerWindow)
        self.contract_label.setGeometry(QtCore.QRect(550, 90, 81, 17))
        self.contract_label.setObjectName("contract_label")

        self.retranslateUi(playerWindow)
        QtCore.QMetaObject.connectSlotsByName(playerWindow)

    def retranslateUi(self, playerWindow):
        _translate = QtCore.QCoreApplication.translate
        playerWindow.setWindowTitle(_translate("playerWindow", "Player Window"))
        self.createButton_2.setText(_translate("playerWindow", "Create"))
        self.updateButton_2.setText(_translate("playerWindow", "Update"))
        self.deleteButton_2.setText(_translate("playerWindow", "Delete"))
        self.line_name_pl.setPlaceholderText(_translate("playerWindow", "Name"))
        self.line_surname_pl.setPlaceholderText(_translate("playerWindow", "Surname"))
        self.ClubM_table_2.setSortingEnabled(True)
        item = self.ClubM_table_2.horizontalHeaderItem(0)
        item.setText(_translate("playerWindow", "Name"))
        item = self.ClubM_table_2.horizontalHeaderItem(1)
        item.setText(_translate("playerWindow", "Surname"))
        item = self.ClubM_table_2.horizontalHeaderItem(2)
        item.setText(_translate("playerWindow", "Player Number"))
        item = self.ClubM_table_2.horizontalHeaderItem(3)
        item.setText(_translate("playerWindow", "Birthday"))
        item = self.ClubM_table_2.horizontalHeaderItem(4)
        item.setText(_translate("playerWindow", "Age"))
        item = self.ClubM_table_2.horizontalHeaderItem(5)
        item.setText(_translate("playerWindow", "Nationality"))
        item = self.ClubM_table_2.horizontalHeaderItem(6)
        item.setText(_translate("playerWindow", "Number of Games"))
        item = self.ClubM_table_2.horizontalHeaderItem(7)
        item.setText(_translate("playerWindow", "New Column"))
        item = self.ClubM_table_2.horizontalHeaderItem(8)
        item.setText(_translate("playerWindow", "Height"))
        item = self.ClubM_table_2.horizontalHeaderItem(9)
        item.setText(_translate("playerWindow", "Contract_id"))
        self.line_contractId_pl.setPlaceholderText(_translate("playerWindow", "Contract_id"))
        self.datePLayer.setDisplayFormat(_translate("playerWindow", "yyyy-MM-dd"))
        self.name_label.setText(_translate("playerWindow", "Name"))
        self.surname_label.setText(_translate("playerWindow", "Surname"))
        self.playernumber_label.setText(_translate("playerWindow", "Player number"))
        self.birthday_label.setText(_translate("playerWindow", "Birthday"))
        self.age_label.setText(_translate("playerWindow", "Age"))
        self.nationality_label.setText(_translate("playerWindow", "Nationality"))
        self.countgames_label.setText(_translate("playerWindow", "Number of games"))
        self.height_label.setText(_translate("playerWindow", "Height"))
        self.weight_label.setText(_translate("playerWindow", "Weight"))
        self.contract_label.setText(_translate("playerWindow", "Contract ID"))