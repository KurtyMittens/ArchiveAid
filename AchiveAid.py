import os
import shutil
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from config import setting


class Ui_ArchiveAid(QtWidgets.QMainWindow):
    def __init__(self):
        """It's the constructor, loading the recent file, if its empty then it will prompt one to add your default"""
        super().__init__()
        self.setupUi(self)
        self.show()
        self.load_start()

    def load_start(self):
        """Loads all the recent saved configurations, follows recent.conf in the config file"""
        run_recent = setting.Recent()
        for i in run_recent.get_filepath():
            self.addButtonFrame(i[0], i[1])
        self.file_sourceselection.setText(f"CURRENT FILE SOURCE: \n {run_recent.get_sourcepath()[0]}")

    def font_(self, point_size=None, weight=75, bold=True, family="JetBrainsMono NF SemiBold"):
        """Returns the font, you can change it your own desire"""
        font = QtGui.QFont()
        font.setFamily(family)
        if point_size is not None:
            font.setPointSize(point_size)
        font.setBold(bold)
        font.setWeight(weight)
        return font

    def get_file(self):
        """gets the directory to put the organized files"""
        self.filename = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.filename) != 0:
            self.addButtonFrame(self.filename)

    def get_source(self):
        """get the source directory you want to organize"""
        self.source_file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.source_file) != 0:
            self.file_sourceselection.setText(f"CURRENT FILE SOURCE: \n {self.source_file}")

    def get_trash(self):
        """get the trash directory you want to organize"""
        self.trash_file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.trash_file) != 0:
            self.file_trashselection.setText(f"CURRENT TRASH FILE: \n {self.trash_file}")

    def if_repeat_ext(self, extensions):
        for i in range(len(extensions)):
            for j in range(len(extensions)):
                if j == i:
                    continue
                if extensions[i] == extensions[j]:
                    return True
        return False

    def what_repeat_ext(self, extensions):
        return list(set([i for i in extensions if extensions.count(i) > 1]))

    def addButtonFrame(self, filename, recent_class=None):
        """Add Files in the form of a button in the scroll area"""
        self.File_frames = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        items = setting.Files_extensions()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.File_frames.sizePolicy().hasHeightForWidth())
        self.File_frames.setSizePolicy(sizePolicy)
        self.File_frames.setMinimumSize(QtCore.QSize(380, 90))
        self.File_frames.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                                       "border:2px;\n"
                                       "border-radius:25px;")
        self.File_frames.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.File_frames.setFrameShadow(QtWidgets.QFrame.Raised)
        self.File_frames.setObjectName("File_frames")

        self.Filename_label = QtWidgets.QLabel(self.File_frames)
        self.Filename_label.setGeometry(QtCore.QRect(100, 15, 151, 41))
        self.Filename_label.setFont(self.font_(point_size=12))
        self.Filename_label.setText(filename.split("/")[-1:][0])
        self.Filename_label.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "")
        self.Filename_label.setObjectName("Filename_label")

        self.Filepath_label = QtWidgets.QLabel(self.File_frames)
        self.Filepath_label.setGeometry(QtCore.QRect(100, 45, 160, 30))
        self.Filepath_label.setFont(self.font_(point_size=8))
        self.Filepath_label.setText(filename)
        self.Filepath_label.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "")
        self.Filepath_label.setObjectName("Filepath_label")

        self.extension_select = QtWidgets.QComboBox(self.File_frames)
        self.extension_select.setGeometry(QtCore.QRect(280, 40, 90, 21))
        self.extension_select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color:rgb(0, 0, 0);\n"
                                            "")
        self.extension_select.setEditable(True)
        self.extension_select.setObjectName("extension_select")
        self.extension_select.addItems(items.get_class_ext())
        self.extension_label = QtWidgets.QLabel(self.File_frames)
        self.extension_label.setGeometry(QtCore.QRect(280, 20, 71, 21))
        self.extension_label.setFont(self.font_(point_size=10))
        self.extension_label.setText('Extensions')
        self.extension_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.extension_label.setObjectName("extension_label")

        self.file_select_button = QtWidgets.QPushButton(self.File_frames)
        self.file_select_button.setGeometry(QtCore.QRect(10, 10, 81, 71))
        self.file_select_button.setFont(self.font_(point_size=14))
        self.file_select_button.setStyleSheet("QPushButton{\n"
                                              "    background-color:rgb(102, 111, 128);\n"
                                              "    border:2px;\n"
                                              "    border-radius:25px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(251, 109, 108);\n"
                                              "    color:rgb(102, 111, 128)\n"
                                              "}")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("dev/../assets/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_select_button.setIcon(icon2)
        self.file_select_button.setIconSize(QtCore.QSize(70, 70))
        self.file_select_button.setObjectName("file_select_button")
        self.verticalLayout.addWidget(self.File_frames)
        if recent_class is not None:
            self.extension_select.setCurrentText(recent_class)

    def del_buttons(self):
        """Deletes all the buttons you have done"""
        while self.verticalLayout.count() > 0:
            self.verticalLayout.itemAt(0).widget().setParent(None)

    def del_current_buttons(self):
        """deletes the current button"""
        pass

    def restore_past(self):
        run_recent = setting.Recent()
        self.del_buttons()
        for i in run_recent.get_filepath():
            self.addButtonFrame(i[0], i[1])

    def organize_(self):
        source = self.OptionSelection.children()[3].text().split('\n')[1]
        filepath = []
        file_cat = []
        file_path = []
        file_ext = []
        for i in range(self.verticalLayout.count()):
            file = self.verticalLayout.itemAt(i).widget().children()[1].text()
            extension = self.verticalLayout.itemAt(i).widget().children()[2].currentText()
            if '.' in extension:
                file_path.append(file)
                file_ext.append(extension)
            else:
                filepath.append(file)
                file_cat.append(extension)
        if self.if_repeat_ext(file_cat):
            self.display_criticalMsg(mode='rep', detail=self.what_repeat_ext(file_cat))
        else:
            self.organize_files(src=source, dic_cat=dict(zip(file_cat, filepath)),
                                dic_ext=dict(zip(file_ext, file_path)))

    def organize_files(self, src, dic_cat, dic_ext):
        organize_guide = setting.Files_extensions()
        files = os.listdir(src.strip())
        done = 0
        for i in files:
            try:
                cat = organize_guide.find_support(os.path.splitext(i)[1])
                shutil.move(f"{src.strip()}/{i}", dic_cat[cat])
                done += 1
            except KeyError:
                try:
                    cat = os.path.splitext(i)[1]
                    shutil.move(f"{src.strip()}/{i}", dic_ext[cat])
                    done += 1
                except KeyError:
                    shutil.move(f"{src.strip()}/{i}", f"{src.strip()}/{i}")
            except FileNotFoundError:
                 self.display_criticalMsg(detail="LOLOLO")
        print(done)



    def display_criticalMsg(self, mode='def', detail=""):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Something is Wrong!")
        msg.setText("err0rep: REPEATED CATEGORIZED EXTENSIONS")
        msg.setInformativeText(
            "Repetition of Categorized File-Extensions are not allowed! it may break or lose your files")
        msg.setDetailedText(f"{detail} categories are repeated multiple times...")
        retval = msg.exec_()

    def optionFrameAnimation(self):
        """Force the animation of the Option Frame"""
        hidden = -250
        self.animate = QtCore.QPropertyAnimation(self.OptionFrame, b'geometry')
        if self.OptionFrame.x() == hidden:
            self.animate.setStartValue(
                QtCore.QRect(self.OptionFrame.x(), self.OptionFrame.y(), self.OptionFrame.width(),
                             self.OptionFrame.height()))
            self.animate.setEndValue(
                QtCore.QRect(0, self.OptionFrame.y(), self.OptionFrame.width(), self.OptionFrame.height()))
            self.animate.start()

        else:
            self.animate.setStartValue(
                QtCore.QRect(self.OptionFrame.x(), self.OptionFrame.y(), self.OptionFrame.width(),
                             self.OptionFrame.height()))
            self.animate.setEndValue(
                QtCore.QRect(hidden, self.OptionFrame.y(), self.OptionFrame.width(), self.OptionFrame.height()))
            self.animate.start()

    def setupUi(self, ArchiveAid):
        """The main Config for the Software"""
        ArchiveAid.setObjectName("ArchiveAid")
        ArchiveAid.setWindowModality(QtCore.Qt.WindowModal)
        ArchiveAid.resize(450, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ArchiveAid.sizePolicy().hasHeightForWidth())
        ArchiveAid.setSizePolicy(sizePolicy)
        ArchiveAid.setMinimumSize(QtCore.QSize(450, 600))
        ArchiveAid.setMaximumSize(QtCore.QSize(450, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dev/../assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ArchiveAid.setWindowIcon(icon)
        ArchiveAid.setStyleSheet("background-color: rgb(251, 109, 108);")
        ArchiveAid.setUnifiedTitleAndToolBarOnMac(True)

        self.centralwidget = QtWidgets.QWidget(ArchiveAid)
        self.centralwidget.setObjectName("centralwidget")

        self.MenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(10, 10, 51, 50))
        self.MenuButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(102, 111, 128);\n"
                                      "    border: 2px ;\n"
                                      "    border-radius: 15px;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "    background-color: rgb(102, 111, 128);\n"
                                      "    border: 2px solid #C3C8D3;\n"
                                      "    border-radius: 15px;\n"
                                      "}")
        icon1 = QtGui.QIcon()

        icon1.addPixmap(QtGui.QPixmap("dev/../assets/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuButton.setIcon(icon1)
        self.MenuButton.setIconSize(QtCore.QSize(50, 50))
        self.MenuButton.setCheckable(False)
        self.MenuButton.setObjectName("MenuButton")
        self.MenuButton.clicked.connect(self.optionFrameAnimation)

        self.TitleFrame = QtWidgets.QFrame(self.centralwidget)
        self.TitleFrame.setGeometry(QtCore.QRect(70, 10, 371, 55))
        self.TitleFrame.setStyleSheet("#TitleFrame{\n"
                                      "    background-color: rgb(102, 111, 128);\n"
                                      "    border:2px;\n"
                                      "border-radius: 25px;\n"
                                      "\n"
                                      "}")
        self.TitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleFrame.setObjectName("TitleFrame")

        self.title_label = QtWidgets.QLabel(self.TitleFrame)
        self.title_label.setGeometry(QtCore.QRect(90, 7, 251, 41))
        self.title_label.setFont(self.font_(point_size=28))
        self.title_label.setStyleSheet("#title_label{\n"
                                       "    background-color: rgb(102, 111, 128);\n"
                                       "    \n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.title_label.setObjectName("title_label")

        self.Logo_pixmap = QtWidgets.QLabel(self.TitleFrame)
        self.logo = QtGui.QPixmap("assets/logo.png")
        self.Logo_pixmap.setGeometry(QtCore.QRect(20, 7, 51, 41))
        self.Logo_pixmap.setStyleSheet("background-color: rgb(102, 111, 128);")
        self.Logo_pixmap.setPixmap(self.logo)
        self.Logo_pixmap.setScaledContents(True)
        self.Logo_pixmap.setObjectName("Logo_pixmap")

        self.FileFrame = QtWidgets.QFrame(self.centralwidget)
        self.FileFrame.setGeometry(QtCore.QRect(10, 70, 431, 521))
        self.FileFrame.setStyleSheet("#FileFrame{\n"
                                     "    background-color: rgb(102, 111, 128);\n"
                                     "    border:2px;\n"
                                     "    border-radius: 20px;\n"
                                     "\n"
                                     "}")
        self.FileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FileFrame.setObjectName("FileFrame")

        self.scrollArea = QtWidgets.QScrollArea(self.FileFrame)
        self.scrollArea.setGeometry(QtCore.QRect(5, 20, 411, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(" QWidget {\n"
                                      "        border: none;\n"
                                      "        background-color: rgb(102, 111, 128);\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar {\n"
                                      "        background: rgb(195, 200, 211);\n"
                                      "        border-radius: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar:horizontal {\n"
                                      "        height: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar:vertical {\n"
                                      "        width: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar::handle {\n"
                                      "        background: #FB6D6C;\n"
                                      "        border-radius: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar::handle:horizontal {\n"
                                      "        height: 5px;\n"
                                      "        min-width: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "    QScrollBar::handle:vertical {\n"
                                      "        width: 5px;\n"
                                      "        min-height: 5px;\n"
                                      "    }\n"
                                      "\n"
                                      "")

        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 401, 431))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.OrganizeBtn = QtWidgets.QPushButton(self.FileFrame)
        self.OrganizeBtn.setGeometry(QtCore.QRect(150, 460, 131, 51))
        self.OrganizeBtn.setFont(self.font_(point_size=14))
        self.OrganizeBtn.setStyleSheet("QPushButton{\n"
                                       "    background-color: rgb(251, 109, 108);\n"
                                       "    border:2px;\n"
                                       "    border-radius:25px;\n"
                                       "    color:rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    color: rgb(251, 109, 108);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(195, 200, 211);\n"
                                       "    color:rgb(102, 111, 128)\n"
                                       "}")
        self.OrganizeBtn.setObjectName("OrganizeBtn")
        self.OrganizeBtn.clicked.connect(self.organize_)

        self.add_btn = QtWidgets.QPushButton(self.FileFrame)
        self.add_btn.setGeometry(QtCore.QRect(90, 460, 51, 51))
        self.add_btn.setFont(self.font_(point_size=14))
        self.add_btn.setStyleSheet("QPushButton{\n"
                                   "    background-color: rgb(251, 109, 108);\n"
                                   "    border:2px;\n"
                                   "    border-radius:25px;\n"
                                   "    color:rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "    color: rgb(251, 109, 108);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: rgb(195, 200, 211);\n"
                                   "    color:rgb(102, 111, 128)\n"
                                   "}")
        self.add_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("dev/../assets/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon3)
        self.add_btn.setIconSize(QtCore.QSize(35, 35))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.get_file)

        self.Refresh_btn = QtWidgets.QPushButton(self.FileFrame)
        self.Refresh_btn.setGeometry(QtCore.QRect(290, 460, 51, 51))
        self.Refresh_btn.setFont(self.font_(point_size=14))
        self.Refresh_btn.setStyleSheet("QPushButton{\n"
                                       "    background-color: rgb(251, 109, 108);\n"
                                       "    border:2px;\n"
                                       "    border-radius:25px;\n"
                                       "    color:rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    color: rgb(251, 109, 108);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(195, 200, 211);\n"
                                       "    color:rgb(102, 111, 128)\n"
                                       "}")
        self.Refresh_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("dev/../assets/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_btn.setIcon(icon4)
        self.Refresh_btn.setIconSize(QtCore.QSize(40, 40))
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.Refresh_btn.clicked.connect(self.restore_past)

        self.OptionFrame = QtWidgets.QFrame(self.centralwidget)
        self.OptionFrame.setGeometry(QtCore.QRect(-250, 0, 251, 601))
        self.OptionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OptionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionFrame.setObjectName("OptionFrame")

        self.back_button = QtWidgets.QPushButton(self.OptionFrame)
        self.back_button.setGeometry(QtCore.QRect(190, 10, 51, 50))
        self.back_button.setStyleSheet("QPushButton{\n"
                                       "    background-color: rgb(102, 111, 128);\n"
                                       "    border: 2px ;\n"
                                       "    border-radius: 15px;\n"
                                       "}\n"
                                       "QPushButton::hover{\n"
                                       "    background-color: rgb(102, 111, 128);\n"
                                       "    border: 2px solid #C3C8D3;\n"
                                       "    border-radius: 15px;\n"
                                       "}")
        self.back_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("dev/../assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon5)
        self.back_button.setIconSize(QtCore.QSize(50, 50))
        self.back_button.setCheckable(False)
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.optionFrameAnimation)

        self.option_label = QtWidgets.QLabel(self.OptionFrame)
        self.option_label.setGeometry(QtCore.QRect(20, 15, 161, 41))
        self.option_label.setFont(self.font_(point_size=28))
        self.option_label.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.option_label.setObjectName("option_label")

        self.OptionSelection = QtWidgets.QFrame(self.OptionFrame)
        self.OptionSelection.setGeometry(QtCore.QRect(10, 70, 231, 521))
        self.OptionSelection.setStyleSheet("#OptionSelection{\n"
                                           "    background-color: rgb(102, 111, 128);\n"
                                           "    border:2px;\n"
                                           "    border-radius: 20px;\n"
                                           "\n"
                                           "}")
        self.OptionSelection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OptionSelection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionSelection.setObjectName("OptionSelection")

        self.historychange = QtWidgets.QPushButton(self.OptionSelection)
        self.historychange.setGeometry(QtCore.QRect(10, 250, 210, 70))

        self.pickundoselaercion = QtWidgets.QPushButton(self.OptionSelection)
        self.pickundoselaercion.setGeometry(QtCore.QRect(10, 170, 210, 70))

        self.file_trashselection = QtWidgets.QPushButton(self.OptionSelection)
        self.file_trashselection.setGeometry(QtCore.QRect(10, 90, 210, 70))
        self.file_trashselection.clicked.connect(self.get_trash)

        self.file_sourceselection = QtWidgets.QPushButton(self.OptionSelection)
        self.file_sourceselection.setGeometry(QtCore.QRect(10, 10, 210, 70))
        self.file_sourceselection.clicked.connect(self.get_source)

        for button in [self.historychange, self.pickundoselaercion, self.file_trashselection,
                       self.file_sourceselection]:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            button.setMinimumSize(QtCore.QSize(210, 70))
            button.setFont(self.font_())
            button.setStyleSheet("QPushButton{\n"
                                 "    background-color: rgb(195, 200, 211);\n"
                                 "    border:2 px;\n"
                                 "    border-radius:25px;\n"
                                 "    color:rgb(0, 0, 0);\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "    background-color: rgb(251, 109, 108);\n"
                                 "    border:2 px;\n"
                                 "    border-radius:25px;\n"
                                 "    color:rgb(0, 0, 0);\n"
                                 "}")

        self.file_sourceselection.setObjectName("file_sourceselection")
        ArchiveAid.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArchiveAid)
        QtCore.QMetaObject.connectSlotsByName(ArchiveAid)

    def retranslateUi(self, ArchiveAid):
        _translate = QtCore.QCoreApplication.translate
        ArchiveAid.setWindowTitle(_translate("ArchiveAid", "ArchiveAid"))
        self.title_label.setText(_translate("ArchiveAid", "ARCHIVE/AID"))

        self.OrganizeBtn.setText(_translate("ArchiveAid", "ORGANIZE"))
        self.option_label.setText(_translate("ArchiveAid", "OPTIONS"))
        self.pickundoselaercion.setText(_translate("ArchiveAid", "UNDO SELECTED \n ORGANIZATION"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    run = Ui_ArchiveAid()
    sys.exit(app.exec_())
