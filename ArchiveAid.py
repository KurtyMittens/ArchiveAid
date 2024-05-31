import os
import shutil
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from config import setting
import webbrowser


def font_(point_size=None, weight=75, bold=True, family="JetBrainsMono NF SemiBold"):
    """Returns the font, you can change it your own desire"""
    font = QtGui.QFont()
    font.setFamily(family)
    if point_size is not None:
        font.setPointSize(point_size)
    font.setBold(bold)
    font.setWeight(weight)
    return font


class FileButton(QtWidgets.QFrame):
    """Individual buttons that corresponds to the File Directory"""
    def __init__(self, filename, frame, recent_class):
        """Create a button for Files and File Editing/Config"""
        super().__init__(frame)
        items = setting.Files_extensions()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(380, 90))
        self.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                           "border:2px;\n"
                           "border-radius:25px;")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("File_frames")

        self.Filename_label = QtWidgets.QLabel(self)
        self.Filename_label.setGeometry(QtCore.QRect(100, 15, 151, 41))
        self.Filename_label.setFont(font_(point_size=12))
        self.Filename_label.setText(filename.split("/")[-1:][0])
        self.Filename_label.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "")
        self.Filename_label.setObjectName("Filename_label")

        self.Filepath_label = QtWidgets.QLabel(self)
        self.Filepath_label.setGeometry(QtCore.QRect(100, 45, 160, 30))
        self.Filepath_label.setFont(font_(point_size=8))
        self.Filepath_label.setText(filename)
        self.Filepath_label.setStyleSheet("background-color: rgb(195, 200, 211);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "")
        self.Filepath_label.setObjectName("Filepath_label")

        self.extension_select = QtWidgets.QComboBox(self)
        self.extension_select.setGeometry(QtCore.QRect(280, 40, 90, 21))
        self.extension_select.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color:rgb(0, 0, 0);\n"
                                            "")
        self.extension_select.setEditable(True)
        self.extension_select.setObjectName("extension_select")
        self.extension_select.addItems(items.get_class_ext())
        self.extension_label = QtWidgets.QLabel(self)
        self.extension_label.setGeometry(QtCore.QRect(280, 20, 71, 21))
        self.extension_label.setFont(font_(point_size=10))
        self.extension_label.setText('Extensions')
        self.extension_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.extension_label.setObjectName("extension_label")

        self.editFrames = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFrames.sizePolicy().hasHeightForWidth())
        self.editFrames.setSizePolicy(sizePolicy)
        self.editFrames.setGeometry(QtCore.QRect(10, 10, 81, 71))
        self.editFrames.setStyleSheet("background-color: rgb(102, 111, 128);\n"
                                      "border:2px;\n"
                                      "border-radius:25px;")
        self.editFrames.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editFrames.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editFrames.setObjectName("editFrames")
        self.editFrames.hide()

        self.file_button = QtWidgets.QPushButton(self)
        self.file_button.setGeometry(QtCore.QRect(10, 10, 81, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_button.setIcon(icon)
        self.file_button.clicked.connect(self.button_edit_animation)

        self.edit_button = QtWidgets.QPushButton(self.editFrames)
        self.edit_button.setGeometry(QtCore.QRect(145, 0, 81, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon2)
        self.edit_button.clicked.connect(self.edit_file)

        self.delete_button = QtWidgets.QPushButton(self.editFrames)
        self.delete_button.setGeometry(QtCore.QRect(280, 0, 81, 71))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon3)
        self.delete_button.clicked.connect(self.delete_file)

        for buttons in [self.file_button, self.edit_button, self.delete_button]:
            buttons.setFont(font_(point_size=14))
            buttons.setStyleSheet("QPushButton{\n"
                                  "    background-color:rgb(102, 111, 128);\n"
                                  "    border:2px;\n"
                                  "    border-radius:25px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color: rgb(251, 109, 108);\n"
                                  "    color:rgb(102, 111, 128)\n"
                                  "}")
            buttons.setIconSize(QtCore.QSize(70, 70))
        if recent_class is not None:
            self.extension_select.setCurrentText(recent_class)

    def button_edit_animation(self):
        """Button Side animations"""
        width = 81
        self.animate = QtCore.QPropertyAnimation(self.editFrames, b'geometry')
        if self.editFrames.width() == width:
            self.editFrames.show()
            self.animate.setStartValue(
                QtCore.QRect(self.editFrames.x(), self.editFrames.y(), self.editFrames.width(),
                             self.editFrames.height()))
            self.animate.setEndValue(
                QtCore.QRect(self.editFrames.x(), self.editFrames.y(), 361, self.editFrames.height()))
            self.animate.start()

        else:
            self.animate.setStartValue(
                QtCore.QRect(self.editFrames.x(), self.editFrames.y(), self.editFrames.width(),
                             self.editFrames.height()))
            self.animate.setEndValue(
                QtCore.QRect(self.editFrames.x(), self.editFrames.y(), width, self.editFrames.height()))
            self.animate.start()

    def edit_file(self):
        """Edit the File in the button"""
        self.filename = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.filename) != 0:
            self.Filename_label.setText(self.filename.split("/")[-1:][0])
            self.Filepath_label.setText(self.filename)
        self.button_edit_animation()

    def delete_file(self):
        """Delete Itself"""
        self.setParent(None)


class ArchiveAid(QtWidgets.QMainWindow):
    """Main Menu of the ArchiveAid Architecture"""
    def __init__(self):
        """It's the constructor, loading the recent file, if its empty then it will prompt one to add your default"""
        super().__init__()
        self.setup(self)
        self.show()
        self.load_start()

    def setup(self, main):
        """The main Config for the Software"""
        main.setObjectName("ArchiveAid")
        main.setWindowModality(QtCore.Qt.WindowModal)
        main.resize(450, 600)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(size_policy)
        main.setMinimumSize(QtCore.QSize(450, 600))
        main.setMaximumSize(QtCore.QSize(450, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet("background-color: rgb(251, 109, 108);")
        main.setUnifiedTitleAndToolBarOnMac(True)
        main.setWindowTitle('ArchiveAid')

        self.central_widget = QtWidgets.QWidget(main)
        self.central_widget.setObjectName("central_widget")

        self.menu_button = QtWidgets.QPushButton(self.central_widget)
        self.menu_button.setGeometry(QtCore.QRect(10, 10, 51, 50))
        self.menu_button.setStyleSheet("QPushButton{\n"
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
        self.menu_button.setIcon(icon1)
        self.menu_button.setIconSize(QtCore.QSize(50, 50))
        self.menu_button.setCheckable(False)
        self.menu_button.setObjectName("MenuButton")
        self.menu_button.clicked.connect(self.option_frame_animation)

        self.title_frame = QtWidgets.QFrame(self.central_widget)
        self.title_frame.setGeometry(QtCore.QRect(70, 10, 371, 55))
        self.title_frame.setStyleSheet("#TitleFrame{\n"
                                      "    background-color: rgb(102, 111, 128);\n"
                                      "    border:2px;\n"
                                      "border-radius: 25px;\n"
                                      "\n"
                                      "}")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("TitleFrame")

        self.title_label = QtWidgets.QLabel(self.title_frame)
        self.title_label.setGeometry(QtCore.QRect(90, 7, 251, 41))
        self.title_label.setFont(font_(point_size=28))
        self.title_label.setStyleSheet("#title_label{\n"
                                       "    background-color: rgb(102, 111, 128);\n"
                                       "    \n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.title_label.setObjectName("title_label")
        self.title_label.setText("ARCHIVE/AID")

        self.logo_pixmap = QtWidgets.QLabel(self.title_frame)
        self.logo = QtGui.QPixmap("assets/logo.png")
        self.logo_pixmap.setGeometry(QtCore.QRect(20, 7, 51, 41))
        self.logo_pixmap.setStyleSheet("background-color: rgb(102, 111, 128);")
        self.logo_pixmap.setPixmap(self.logo)
        self.logo_pixmap.setScaledContents(True)
        self.logo_pixmap.setObjectName("Logo_pixmap")

        self.file_frame = QtWidgets.QFrame(self.central_widget)
        self.file_frame.setGeometry(QtCore.QRect(10, 70, 431, 521))
        self.file_frame.setStyleSheet("#FileFrame{\n"
                                     "    background-color: rgb(102, 111, 128);\n"
                                     "    border:2px;\n"
                                     "    border-radius: 20px;\n"
                                     "\n"
                                     "}")
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("FileFrame")

        self.scrollArea = QtWidgets.QScrollArea(self.file_frame)
        self.scrollArea.setGeometry(QtCore.QRect(5, 20, 411, 431))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(size_policy)
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

        self.OrganizeBtn = QtWidgets.QPushButton(self.file_frame)
        self.OrganizeBtn.setGeometry(QtCore.QRect(150, 460, 131, 51))
        self.OrganizeBtn.setFont(font_(point_size=14))
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
        self.OrganizeBtn.setText('ORGANIZE')

        self.add_btn = QtWidgets.QPushButton(self.file_frame)
        self.add_btn.setGeometry(QtCore.QRect(90, 460, 51, 51))
        self.add_btn.setFont(font_(point_size=14))
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

        self.Refresh_btn = QtWidgets.QPushButton(self.file_frame)
        self.Refresh_btn.setGeometry(QtCore.QRect(290, 460, 51, 51))
        self.Refresh_btn.setFont(font_(point_size=14))
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
        icon4.addPixmap(QtGui.QPixmap("assets/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_btn.setIcon(icon4)
        self.Refresh_btn.setIconSize(QtCore.QSize(40, 40))
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.Refresh_btn.clicked.connect(self.restore_past)

        self.OptionFrame = QtWidgets.QFrame(self.central_widget)
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
        self.back_button.clicked.connect(self.option_frame_animation)

        self.option_label = QtWidgets.QLabel(self.OptionFrame)
        self.option_label.setGeometry(QtCore.QRect(20, 15, 161, 41))
        self.option_label.setFont(font_(point_size=28))
        self.option_label.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.option_label.setObjectName("option_label")
        self.option_label.setText("OPTIONS")

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

        self.about_button = QtWidgets.QPushButton(self.OptionSelection)
        self.about_button.setGeometry(QtCore.QRect(10, 250, 210, 70))
        self.about_button.setText("ABOUT")
        self.about_button.clicked.connect(self.open_about)

        self.issue_report = QtWidgets.QPushButton(self.OptionSelection)
        self.issue_report.setGeometry(QtCore.QRect(10, 170, 210, 70))
        self.issue_report.setText("REPORT AN ISSUE")
        self.issue_report.clicked.connect(self.open_report_issue)

        self.delete_all = QtWidgets.QPushButton(self.OptionSelection)
        self.delete_all.setGeometry(QtCore.QRect(10, 90, 210, 70))
        self.delete_all.setText("DELETE ALL CURRENT FILES")
        self.delete_all.clicked.connect(self.delete_all_file)

        self.file_source_selection = QtWidgets.QPushButton(self.OptionSelection)
        self.file_source_selection.setGeometry(QtCore.QRect(10, 10, 210, 70))
        self.file_source_selection.clicked.connect(self.get_source)

        for button in [self.about_button, self.issue_report, self.delete_all,
                       self.file_source_selection]:
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(size_policy)
            button.setMinimumSize(QtCore.QSize(210, 70))
            button.setFont(font_())
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

        self.file_source_selection.setObjectName("file_source_selection")
        main.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(main)

    def load_start(self):
        """Loads all the recent saved configurations, follows recent.conf in the config file"""
        run_recent = setting.Recent()
        for i in run_recent.get_filepath():
            self.addButtonFrame(i[0], i[1])
        self.file_source_selection.setText(f"CURRENT FILE SOURCE: \n {run_recent.get_sourcepath()[0]}")

    def get_file(self):
        """gets the directory to put the organized files"""
        self.filename = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.filename) != 0:
            self.addButtonFrame(self.filename)

    def get_source(self):
        """get the source directory you want to organize"""
        self.source_file = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.source_file) != 0:
            self.file_source_selection.setText(f"CURRENT FILE SOURCE: \n {self.source_file}")

    def if_repeat_ext(self, extensions):
        """Checks out for the repeated categorized extensions"""
        for i in range(len(extensions)):
            for j in range(len(extensions)):
                if j == i:
                    continue
                if extensions[i] == extensions[j]:
                    return True
        return False

    def what_repeat_ext(self, extensions):
        """returns what is the repeated categorized extensions"""
        return list(set([i for i in extensions if extensions.count(i) > 1]))

    def addButtonFrame(self, filename, recent_class=None):
        """Adds a file button frame"""
        button = FileButton(filename, self.scrollAreaWidgetContents, recent_class)
        self.verticalLayout.addWidget(button)

    def del_buttons(self):
        """Deletes all the buttons you have done"""
        while self.verticalLayout.count() > 0:
            self.verticalLayout.itemAt(0).widget().setParent(None)

    def restore_past(self):
        """Restoring the buttons from the recent config"""
        run_recent = setting.Recent()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Rfreshing Files')
        msg.setText("THIS WILL REFRESH THIS CONFIG TO RECENT CONFIG SAVED")
        msg.setInformativeText("Do you wish to proceed?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            self.del_buttons()
            for i in run_recent.get_filepath():
                self.addButtonFrame(i[0], i[1])

    def organize_(self):
        """Organize the files form the source path file to designated directories (filtering)
           -> filters the config form raw extensions to categorized extensions
           -> pass through the organizing proper"""
        source = self.OptionSelection.children()[3].text().split('\n')[1]
        filepath = []
        file_cat = []
        file_path = []
        file_ext = []
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Confirmation')
        msg.setText("THIS WILL ORGANIZE YOUR FILES")
        msg.setInformativeText("Do you wish to proceed? (Proceeding also Save this config)")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
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
                self.display_critical_msg(mode='0rep', detail=self.what_repeat_ext(file_cat))
            if self.if_repeat_ext(file_ext):
                self.display_critical_msg(mode='1rep', detail=self.what_repeat_ext(file_ext))
            else:
                self.organize_files(src=source, dic_cat=dict(zip(file_cat, filepath)),
                                    dic_ext=dict(zip(file_ext, file_path)))
                save_config = setting.SaveRecent(source, filepath, file_cat, file_path, file_ext)
                save_config.save_config()

    def organize_files(self, src, dic_cat, dic_ext):
        """Organize the files form the source path file to designated directories (applying)
        -> Checks the files in the source file
        -> move them to the desired directory"""
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
                self.display_critical_msg(mode="0file", detail="The File Directory cannot be found")
        print(done)

    def option_frame_animation(self):
        """Force the animation of the Option Frame (Side panel Animation)"""
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

    def open_report_issue(self):
        """Redirects you to "Report an Issue" page in ArchiveAid's Repository"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Confirmation')
        msg.setText("YOU WILL BE REDIRECTED TO GITHUB")
        msg.setInformativeText("Do you wish to proceed?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            return webbrowser.open("https://github.com/KurtyMittens/ArchiveAid/issues/new")

    def open_about(self):
        """Redirects you to "README" page in ArchiveAid's Repository"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Confirmation')
        msg.setText("YOU WILL BE REDIRECTED TO GITHUB")
        msg.setInformativeText("Do you wish to proceed?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            return webbrowser.open("https://github.com/KurtyMittens/ArchiveAid/blob/main/README.md")

    def display_critical_msg(self, mode='', detail=""):
        """Displays a dialogue box and shows error"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Something is Wrong!")
        if mode == '0rep':
            msg.setText("err0rep: REPEATED CATEGORIZED EXTENSIONS")
            msg.setInformativeText(
                "Repetition of Categorized File-Extensions are not allowed! it may break or lose your files")
            msg.setDetailedText(f"{detail} categories are repeated multiple times...")
        if mode == '1rep':
            msg.setText("err1rep: REPEATED RAW EXTENSIONS")
            msg.setInformativeText(
                "Repetition of Raw File-Extensions are not allowed! it may break or lose your files")
            msg.setDetailedText(f"{detail} categories are repeated multiple times...")
        if mode == '1rep':
            msg.setText("err1rep: REPEATED RAW EXTENSIONS")
            msg.setInformativeText(
                "Repetition of Raw File-Extensions are not allowed! it may break or lose your files")
            msg.setDetailedText(f"{detail} categories are repeated multiple times...")
        if mode == '0file':
            msg.setText("err0file: FILE NOT FOUND")
            msg.setInformativeText("File is not found")
        retval = msg.exec_()

    def delete_all_file(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Confirmation')
        msg.setText("THIS WILL DELETE YOUR CURRENT CONFIGs")
        msg.setInformativeText("Do you wish to proceed?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            self.del_buttons()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    run = ArchiveAid()
    sys.exit(app.exec_())
